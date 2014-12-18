from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    #user = models.ForeignKey(User)
    sector = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    senti = models.IntegerField() #average sentiment value of comments
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    description = models.TextField()
    #user = models.ForeignKey(User)
    story = models.ForeignKey(Story)
    senti = models.IntegerField() #sentiment value
    is_anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Watch(models.Model):
    story = models.ForeignKey(Story)
    #user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)