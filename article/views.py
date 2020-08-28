from django.shortcuts import redirect, render, HttpResponse, get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment
from django.contrib.auth.decorators import login_required #djangonun içinde gelen decorator. Giriş yapmadan sayfaların gösterilmemesini sağlıyor.

# Create your views here.

def index(request):   
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


@login_required(login_url="user:login") #Eğer giriş yapmadıysak login sayfasına yönlendir.
def dashboard(request): 
    articles = Article.objects.filter(author = request.user)                      #Kullanıcının makalelerini dashboard da gösterme
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html",context)


@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None , request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit = False)  #ModelForm dan oluştuğu için formumuz kaydetmesi artık böyle. Save işlemini form.save yapmasın diye commit = False yazdık. Kendimiz yapmak istiyoruz.
        article.author = request.user #Yazar adının atamasını yapıyoruz.
        article.save() #Kendimiz elle kaydediyoruz
        messages.success(request,"Makale Başarıyla Oluşturuldu...")
        return redirect("article:dashboard")
     
    return render(request,"addarticle.html",{"form":form})


def detail(request,id):
    #article = Article.objects.filter(id = id).first() #first demezsek bize liste objesi dönüyor. first diyerek bize ilk elemanı yolluyor.
    article = get_object_or_404(Article, id = id) #istenilen sorgu çalıştırılacak. eğer article yoksa 404 hatası döndürecek.
    comments = article.comments.all()
    
    
    return render(request,"detail.html",{"article" : article,"comments": comments})


@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article, id = id) #Öyle bir article yoksa 404 hatası verir

    form = ArticleForm(request.POST or None, request.FILES or None, instance = article) #instance objesi ile article bilgileri içine gelecek. Bundan emin değilim tekrar bak. Evet instance objesi ile formun içeriği alınıyor.
    if form.is_valid():
        article = form.save(commit = False)  #ModelForm dan oluştuğu için formumuz kaydetmesi artık böyle. Save işlemini form.save yapmasın diye commit = False yazdık. Kendimiz yapmak istiyoruz.
        article.author = request.user #Yazar adının atamasını yapıyoruz.
        article.save() #Kendimiz elle kaydediyoruz
        messages.success(request,"Makale Başarıyla Güncellendi...")
        return redirect("article:dashboard")
  
    return render(request,"update.html", {"form" : form}) # form is valid değilse veya GET request ise burası çalışır. Oluşturduğumuz form gönderilir.


@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi...")
    
    return redirect("article:dashboard") #Article uygulaması altındaki dashboard'a git


def showArticles(request):
    articles = Article.objects.all()   
    return render(request,"articles.html",{"articles" : articles})

def addComment(request,id):
    article = get_object_or_404(Article, id = id)

    if request.method == "POST": #post işlemi gerçekleşince form bilgisinden author ve content bilgilerini alıyoruz. 
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article

        newComment.save()
        
    return redirect(reverse("article:detail", kwargs={"id": id}))

    