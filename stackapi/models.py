from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=300)
    vote_count = models.IntegerField(default=0)
    views = models.CharField(max_length=50)
    tags = models.CharField(max_length=250)
    time = models.CharField(max_length=250, default='')
    asked_by = models.CharField(max_length=250, default='')


    def __str__(self):
        return f"{self.question}"
