from django import forms
from pet.models import BaseInfo, DetailInfo


class BaseInfoForm(forms.ModelForm):
    class Meta:
        model = BaseInfo  # 사용할 모델
        fields = ['name', 'species']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'name': '이름',
            'species': '종류',
        }


class DetailInfoForm(forms.ModelForm):
    class Meta:
        model = DetailInfo
        fields = ['content']
        labels = {
            'content': '상세 정보 입력',
        }