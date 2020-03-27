from blog.models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


# post_new는 폼으로 연결해주는 함수이다.
def post_new(request):
    # 만들어놓았던 폼 양식을 가죠오기 위해서는
    # 변수 = 폼양식() 를 써야한다. ()가 우측에 붙음에 주의.
    # 현재 코두는 Postform() 양식을 따라 만들것임을 보여준다.
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog/post_detail.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)      
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})