from django.db import models
from django.utils import timezone
from django import forms


# title 필드의 length가 2보다 작으면 검증오류를 발생시키는 함수 선언
def min_length_2_validator(value):
    if len(value) < 2:
        # ValidationError 예외 강제 발생
        raise forms.ValidationError('title은 2글자 이상 입력해야 합니다.')


class Comment(models.Model):
    # 참조하는 Post 객체
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE,
                             related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text + '(' + str(self.id) + ')'


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, validators=[min_length_2_validator])
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

    # Post가 참조하는 Comment 중에서 승인된 Comment만 Filtering
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    # published_data 필드에 현재 날짜를 저장하는 메서드
    def publish_date(self):
        self.published_date = timezone.now()
        self.save()
