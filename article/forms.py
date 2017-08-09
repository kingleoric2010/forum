#from django import forms
from django.forms import ModelForm
from article.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']


'''
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=10000)
'''
