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

    def __str__(self):
        return self.set
