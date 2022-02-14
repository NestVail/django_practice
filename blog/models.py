from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ------ Migration Test ------
    # test = models.TextField()

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # Model Class 에 정의된 __str__ 함수를 재정의
    def __str__(self):
        return self.title + '(' + str(self.id) + ')'

    # published_data 필드에 현재 날짜를 저장하는 메서드
    def publish_date(self):
        self.published_date = timezone.now()
        self.save()
