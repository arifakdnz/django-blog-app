from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name = "Yazar") #User tablosundan kullanıcı silindiği zaman buradan da sil 'on_delete'. varolan baika bir tabloyu göstermek istiyorsak Foreignkey kullanıyoruz.
    title = models.CharField(max_length=50, verbose_name = "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    article_image = models.FileField(blank = True, null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.title  

    class Meta:
        ordering = ['-created_date']   #En son eklenen makale ilk gösteriliyor.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Makale", related_name= "comments") #Her bir makalemizin birden fazla yorumu olabilir. Commentlerimizi makalelerimize bağlamaya yarıyor.Related name = makalelerimizin yorumlarını almak için bir isim veriyoruz. article.comments diyerek makalenin yorumlarına erişebiliyoruz. Article silindiği zaman yorumlarda silinmesi için on_delete kullandık.
    comment_author = models.CharField(max_length = 50, verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200, verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']  #En son eklenen yorum ilk gösteriliyor.
    