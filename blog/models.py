from django.db import models
from django.utils import timezone


class Post(models.Model):
    이용자 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    제목 = models.CharField(max_length=200)
    내용 = models.TextField()
    제작일 = models.DateTimeField(
            default=timezone.now)
    유포일 = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
