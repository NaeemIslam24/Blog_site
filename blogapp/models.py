from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    objects = None
    STATUS_CHOICE = (('draft','Draft'),('published','Published'),)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICE, default='draft')

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse("blogapp:single_post",
         args=[self.id,self.slug])
    

    def __str__(self):
        return self.title



