from django import forms
from .models import Post


# ModelForm 을 상속받는 PostModelForm 클래서 정의
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', )


def min_length_5_validator(value):
    if len(value) < 5:
        # ValidationError 예외 강제 발생
        raise forms.ValidationError('text는 5글자 이상 입력해야 합니다.')


class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, validators=[min_length_5_validator])
