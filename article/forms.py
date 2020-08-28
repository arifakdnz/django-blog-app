from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):   #Model Form ile oluşturmak çok kolay.
    class Meta:
        model = Article
        fields = ["title","content","article_image"]  #Title ve content den iki input alanı




