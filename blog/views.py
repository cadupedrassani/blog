from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post, Comentario
from django.utils import timezone

def post_list(request):
    posts_publicados = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    comentarios = Comentario.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'post_list.html', {'posts' : posts_publicados, 'comentarios' : comentarios})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comentarios = Comentario.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post' : post, 'comentarios': comentarios})
