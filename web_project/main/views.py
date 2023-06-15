from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Post

def index(request):
    return render(request, 'main/index.html')

#게시판 페이지
def board(request):
    post_list = Post.objects.all()
    return render(request, 'main/post_list.html', {'post_list':post_list})

#상세페이지
def post_detail(request, postId):
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'main/post_detail.html', context)

#글쓰기 페이지 이동
def post_add(request):
    return render(request, 'main/post_add.html')

#글 추가 
def post_new(request):
    if request.method == 'POST':
        post=Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            date=timezone.now() )
        post.save()
        return HttpResponseRedirect(reverse('main:board'))

#글 수정 페이지 이동  
def post_edit(request, postId):
    post=Post.objects.get(id=postId)
    post = {"post":post}
    return render(request, 'main/post_edit.html',post)
    
def post_update(request, postId):
    post=Post.objects.get(id=postId)
    if request.method == 'POST':
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.date = timezone.now()
        post.save()
        return HttpResponseRedirect(reverse('main:board')) 

#글 삭제
def post_remove(request, postId):
    post = Post.objects.get(id=postId)
    post.delete()
    return HttpResponseRedirect(reverse('main:board'))
