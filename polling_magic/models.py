from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Poll(models.Model):
    set = models.CharField(max_length=250, null=False, blank=False)
    image = CloudinaryField('image', null=False, blank=False)
    new_cards = models.IntegerField(default='0', null=False, blank=False)
    set_icon = CloudinaryField('image', null=False, blank=False)
    lore = models.TextField(null=False, blank=False)
    release_date = models.DateField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name=='set_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='set_dislikes', blank=True)
    slug = models.SlugField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.set

    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_dislikes(self):
        return self.dislikes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
