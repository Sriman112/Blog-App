from django.shortcuts import render
from .models import blogpost
from .forms import blogform
from django.http import HttpResponseRedirect
from datetime import datetime

def display(request):
    form=blogpost.objects.all()
    return render(request,'htmlfiles/display.html',context={'form':form})


def insert(request):
    form = blogform()
    if request.method=="POST":
        form=blogform(request.POST)
        
        if form.is_valid():
            post=form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
            return HttpResponseRedirect('/display')
    return render(request,'htmlfiles/insert.html',context={'form':form})




