from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post, Comentario
from django.utils import timezone
from .forms import formComentario, formPost

def post_list(request):
    posts_publicados = Post.objects.order_by('data_publicacao')
    return render(request, 'post_list.html', {'posts' : posts_publicados})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comentarios = Comentario.objects.filter(post=post)
    form = formComentario()

    if request.method == 'POST':
        form = formComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.data = timezone.now()
            comentario.post = Post.objects.get(id=pk)
            comentario.save()
            return redirect(post_detail, pk=pk)
        else:
            post = Post.objects.get(id=pk)
            comentarios = Comentario.objects.filter(post=post).order_by('data_publicacao')
            form = formComentario()

    return render(request, 'post_detail.html', {'post' : post, 'comentarios' : comentarios, 'form' : form})

def new_post(request):
    form = formPost()

    if request.method == 'POST':
        form = formPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_criacao = timezone.now()
            post.save()
            return redirect(post_list)

    return render(request, 'new_post.html', {'form': form})