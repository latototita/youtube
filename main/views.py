from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from pytube import *

# defining function
def index(request):
    # checking whether request.method is post or not
    if request.method == 'POST':
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
        # downloads video
        stream.download()
        # returning HTML page
        return render(request, 'index.html')
    return render(request, 'index.html')