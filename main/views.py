from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
#from .forms import *
# Create your views here.
def index(request):

    List=Scholarship.objects.all()
    i = request.GET.get('i')
    if i:
        y=Scholarship.objects.get(id=i)
        request.session['job']=y.school
        form=Formone()
        context={'form':form}
        return render(request,'first.html',context)

    context={'List':List}
    return render(request,'index.html',context)
def secondpage(request):
    
    if request.method == 'POST':
        form = Formone(request.POST)
        if form.is_valid():
            age=form.cleaned_data['age']
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            request.session['age']=age
            request.session['name']=name
            request.session['email']=email
            form=Formstwo()
            context={'form':form}
            return render(request,'second.html',context)

def thirdpage(request):
    
    if request.method == 'POST':
        form = Formstwo(request.POST)
        if form.is_valid():
            date_of_birth=form.cleaned_data['date_of_birth']
            nationality=form.cleaned_data['nationality']
            request.session['date_of_birth']=str(date_of_birth)
            request.session['nationality']=nationality
            form=Formthree()
            context={'form':form}
            return render(request,'third.html',context)

def forthpage(request):
    
    if request.method == 'POST':
        form = Formthree(request.POST)
        if form.is_valid():
            file=form.cleaned_data['file']
            number_of_children_in_the_family=form.cleaned_data['number_of_children_in_the_family']
            last_level_of_studying=form.cleaned_data['last_level_of_studying']
            number_of_family_members=form.cleaned_data['number_of_family_members']
            Family_total_income_level=form.cleaned_data['Family_total_income_level']
            request.session['number_of_children_in_the_family']=number_of_children_in_the_family
            Family_total_income_level=Income.objects.get(name=Family_total_income_level)
            request.session['Family_total_income_level']=str(Family_total_income_level)
            last_level_of_studying=Level.objects.get(name=last_level_of_studying)
            request.session['last_level_of_studying']=str(last_level_of_studying)
            request.session['file']=file
            request.session['number_of_family_members']=number_of_family_members
            form=Formfour()
            context={'form':form}
            return render(request,'forth.html',context)
    
def lastpage(request):
    if request.method == 'POST':
        form = Formfour(request.POST)
        if form.is_valid():
            letter_to_manager=form.cleaned_data['letter_to_manager']
            request.session['letter_to_manager']=letter_to_manager
            return redirect('last')
        context={'form':form}
        return render(request,'first.html',context)
def last(request):
    messages.success(request, 'Application Submited Successfully.Wait Until You are Contacted Through Email.')
    return redirect('index')