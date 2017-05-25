# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.http import HttpResponse

from .models import Post
from .forms import PostForm


def post_create(request):
    form = PostForm(request.POST or None)
    #we did the above because post forms has built in validation errors
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        
    #BELOW IS A BAD PRACTICE BECAUSE WE DON'T VALIDATE THE DATA
    # if request.method == "POST":
    #     print request.POST.get("title")
    #     print request.POST.get("content")
    #     title = request.POST.get("title")
    #     Post.objects.create(title=title)
    context={
        "form" : form,
    }

    return render(request, "post_form.html",context)

def post_detail(request,id = None):
    # instance = Post.obj(id=1)
    instance = get_object_or_404(Post , id=id)
    context = {
        "title" : instance.title,
        "instance" : instance
    }
    return render(request, "post_details.html", context)

def post_list(request): #retrive
    # if request.user.is_authenticated():
    #     context = {
    #         "title":"My User List"
    #     }
    # else:
    #     context = {
    #         "title" : "List"
    #     }
    querySet = Post.objects.all()
    context = {
        "title" : "List",
        "object_list" : querySet
    }
    return render(request,"index.html",context)
    # return HttpResponse("<h1>List</h1>")

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
