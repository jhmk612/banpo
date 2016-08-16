from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=10)

    def save(self, commit=True):
        user=super(SignupForm, self).save(commit=False)
        user.first_name=self.cleaned_data['name']

        if commit:
            user.save()
        return user

    class Meta:
        model=User
        fields=['username', 'password1', 'password2', 'first_name']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디를 입력하세요.'
        self.fields['password1'].label = '비밀번호를 입력하세요.'
        self.fields['password2'].label = '비밀번호를 다시 한 번 입력하세요.'
        self.fields['first_name'].label = '이름을 적어주세요.'

    def clean_name(self):
        data=self.cleaned_data['first_name']
        if User.objects.filter(first_name=data).exists():
            raise forms.ValidationError('이미 회원가입이 완료되었습니다.')
        return data