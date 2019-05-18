from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

#add custom manager not objects
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')


		
class   Post(models.Model):
	"""docstring for post"""
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	#this for SEO-friendly URLs for the blog posts
	slug = models.SlugField(max_length=250, unique_for_date='publish')

	author = models.ForeignKey(User, on_delete='CASCADE', related_name='blog_posts')

	body = models.TextField()

	publish = models.DateTimeField(default=timezone.now)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')

	objects = models.Manager() #the defult manager.

	published = PublishedManager() #our custom manager.

	class Meta:
		# negative sign for descending order????
		ordering = ('-publish',)

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])


	def __str__(self):
		return self.title
