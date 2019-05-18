from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

#crete the posts list from the published manager we made.
def post_list(request):
	#posts = Post.published.all()
	object_list = Post.published.all()
	paginator = Paginator(object_list, 3) # 3 posts in each page.
	# Get to get page number
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)

	except PageNotAnInteger:
		#if page not integer deliver the first page
		posts = paginator.page(1)

	except EmptyPage:
		# if page is out of range deliver last page
		posts = paginator.page(paginator.num_pages)

	return render(request, 'blog/post/list.html', {'page' : page, 'posts' : posts})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, status = 'published', publish__year=year, publish__month=month, publish__day=day)

	return render(request, 'blog/post/detail.html', {'post' : post})  