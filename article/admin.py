from django.contrib import admin

from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"] #Başlığa ve oluşturulma tarihine basıldığında makaleye gidilir.
    
    search_fields = ["title"] #Başlıklara göre arama yapmak için arama çubuğu çıkıyot.

    list_filter = ["created_date"] #Oluşturulma tarihine göre makaleleri filtreleme özelliği çıktı.



    class Meta:
        model = Article


 