from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    following = models.ManyToManyField("self", symmetrical=False, related_name="follower")

    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Post(models.Model):
    post = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.post
