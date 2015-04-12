import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class Page(models.Model):
    title = models.CharField(max_length=200)
    content =  models.TextField()
    pub_date = models.DateTimeField("Date published", auto_now_add = True)
    choices = (
        ('CH', 'Character'),
        ('FA', 'Faction'),
        ('EV', 'Event'),
        ('TC', 'Technology'),
        ('LC', 'Location'),
        ('MS', 'Miscellaneous'),
    )
    category = models.CharField(max_length=2,
                                      choices=choices,
                                      default='MS')

    def full_title(self):
        return self.title.replace("_"," ")

    def __str__(self):
        return self.full_title()[:99] + ": " + self.get_category_display() + ": " + self.content[:99]
    
    @classmethod
    def get_history(cls, path):
        return cls.objects.filter(title__iexact=path).distinct().order_by('-pub_date')
    
    @classmethod
    def get_latest(cls, path):
        return cls.objects.filter(title__iexact=path).distinct().latest('pub_date')

    @classmethod
    def get_by_id(cls, path, ver):
        return cls.objects.filter(title__iexact=path).distinct().get(id=ver)


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['category', 'content']

    
##
##def ver_check(v, path):
##    p = None
##    if v:
##        if v.isdigit():
##            p = Page.by_id(int(v), path)
##
##        if not p:
##            return None
##    else:
##        p = Page.by_path(path).get()
##    return p
