from django.db import models
from django.contrib.auth.models import User


class BaseInfo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_baseInfo')
    name = models.CharField(max_length=200)
    species = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_baseInfo')  # 추천인 추가

    def __str__(self):
        return self.name


class DetailInfo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_detailInfo')
    baseInfo = models.ForeignKey(BaseInfo, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_detailInfo')

# Create your models here.
