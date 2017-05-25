# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # return "/posts/%s/" %(self.id)
        return reverse("detail" , kwargs={"id" :self.id})
        #above is the 4th version of url mapper which is very very dynamic

    """     #<!-- href=/posts/{{obj.id}}-->
        #<!-- href="{% url 'detail' id=obj.id %}"-->
    """
    #can use both of the above in the index.html to redirect to corresponding details page in href attribute