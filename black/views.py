from django.shortcuts import render, redirect
from .models import People, Like, Post, Comment
from .forms import PostForm, CommentForm, LikeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
# Create your views here.
def index(request):
    people_list=People.objects.all()
    return render(request, 'black/index.html', {'people_list':people_list})

def post(request, pk):
    instance=People.objects.get(pk=pk)
    if request.method=='POST':
        p=PostForm(request.POST, request.FILES)
        if p.is_valid():
            new_post=p.save(commit=False)
            new_post.writer=request.user
            new_post.person=instance
            new_post.save()

            return redirect('black:post_detail', person_pk=instance.pk, post_pk=new_post.pk)
    else:
        p=PostForm()

    return render(request, 'black/post.html', {'form':p})

def post_detail(request, person_pk, post_pk):
    instance=People.objects.get(pk=person_pk)
    post=Post.objects.get(pk=post_pk)
    comments=Comment.objects.filter(post=post_pk)
    likes=Like.objects.filter(post=post_pk)
    num_likes=Like.objects.filter(post=post_pk).count()
    avg=Like.objects.filter(post=post_pk).aggregate(Avg('rating')).values()
    likes_avg=list(avg)[0]


    if request.method=='POST':
        if request.POST['form_type'] == u'like':
            l=LikeForm(request.POST,)

            if l.is_valid():
                new_like=l.save(commit=False)
                new_like.writer=request.user
                new_like.post=post
                new_like.save()

                return redirect('black:post_detail', person_pk=instance.pk, post_pk=post.pk)



        else:
            c=CommentForm(request.POST,)

            if c.is_valid():
                new_comment=c.save(commit=False)
                new_comment.writer=request.user
                new_comment.post=post
                new_comment.save()

                return redirect('black:post_detail', person_pk=instance.pk, post_pk=post.pk)

    else:
        l=LikeForm()
        c=CommentForm()

    context={'post':post, 'comments':comments, 'likes':likes, 'num_likes':num_likes, 'commentform': c, 'likeform': l, 'avg':likes_avg}
    return render(request, 'black/post_detail.html', context)


def post_list(request, pk):
    instance=People.objects.get(pk=pk)
    post_list=Post.objects.filter(person=pk)
    return render(request, 'black/post_list.html', {'person': instance ,'post_list':post_list})