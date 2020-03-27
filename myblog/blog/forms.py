'''
Created on 2020. 3. 25.

@author: seongkeun
'''

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    # 폼의 상세정보 설정ㅇ을 위해 class PostForm 내부에
    # class Meta를 다시 만들어야함. Meta에 정의한 정보대로
    # 폼이생성됨.
    
    class Meta:
        model = Post
        fields = ('title', 'text',)