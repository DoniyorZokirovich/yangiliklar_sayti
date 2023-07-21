from django.shortcuts import render
from .models import Category, New, Contact, Comment, View
import requests

from .services import get_all_ctg, search_new


def valyuta():
    url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/'
    data ={

    }
    headers = {

    }
    response = requests.get(url,data=data,headers=headers)
    return response.json()

def catg():
    return Category.objects.all()

def index(re):
    news= New.objects.all().order_by('-date')
    sqlctgs = get_all_ctg()
    print("\n\n", sqlctgs, "\n\n")

    forighn_cate =Category.objects.get(name = 'Forighn')
    forighn_news = New.objects.filter(cate=forighn_cate)

    economy_cate = Category.objects.get(id = 5)
    economy_news =New.objects.filter(cate=economy_cate)

    maxalla_cate = Category.objects.get(name = 'Local')
    maxalla_news = New.objects.filter(cate=maxalla_cate)

    football_cate = Category.objects.get(name = 'Football')
    football_news = New.objects.filter(cate = football_cate)

    actnews = New.objects.all().order_by('-view')
    ctx = {
        'catg':sqlctgs,
        'big':news[0],
        'news':actnews[0:3],
        'pop_news':news[4:8],
        'pre_pop':news[8:12],
        'pre_big':news[12],
        'politica1':news[13:18],
        'politica2':news[18:23],
        'fresh_news':news[23:27],
        'fresh_news2':news[27:31],
        'posledniy':news[31:33],
        'jahon':forighn_news,
        'economy':economy_news[:3],
        'economy1':economy_news[3:6],
        'big_maxalla':maxalla_news[:2],
        'maxalla1':maxalla_news[2:6],
        'maxalla2':maxalla_news[6:10],
        'football':football_news[0:2],
        'val' : valyuta


    }
    return render(re,'index.html',ctx)


def view(re,pk):
    new=New.objects.filter(id=pk).first()

    if not re.user.is_anonymous:
        view = View.objects.get_or_create(user=re.user,new =new)

    if not new:
        return render(re, 'view.html', {
            'catg':catg(),
            'error':True,
            'val': valyuta
        })
    new.view =new.view + 1
    new.save()

    if re.POST:
        user = re.user
        izoh = re.POST.get('comment')

        cmt = Comment()
        cmt.user = user
        cmt.comment = izoh
        cmt.new = new
        cmt.save()


    comments = Comment.objects.filter(new=new,trash=False).order_by('-pk')

    ctx = {
        'catg': catg(),
        'new':new,
        'val': valyuta,
        'comments':comments,
        'len_comment':len(comments)
    }
    return render(re, 'view.html', ctx)


def cat(re,_id):
    try:
        cat = Category.objects.get(id=_id)
    except:
        ctx = {
            'error':True,
            'catg':catg(),
            'val': valyuta
        }
        return render(re, 'category.html', ctx)
    cat_news =New.objects.filter(cate=cat).order_by('-id')

    ctx = {
        'catg': catg(),
        'cat':cat,
        'cat_news':cat_news[1:],
        'val': valyuta

    }
    if len(cat_news) > 0:
        ctx['big'] = cat_news[0]
    return render(re, 'category.html', ctx)


def con(re):
    ctx = {
        'catg': catg(),
        'val': valyuta
    }


    if re.POST:
        ism = re.POST.get('ism')
        sms = re.POST.get('sms')
        tel = re.POST.get('tel')
        contact = Contact.objects.create(ism=ism, phone=tel,message=sms)
        ctx['contact'] = contact
    return render(re, 'contact.html', ctx)


def ser(re):
    savol = re.GET.get('q',None)
    news = search_new(savol)
    print(news)

    ctx = {
        'news':news, 'len':len(news),
        'savol':savol,
        'catg': catg(),'val' : valyuta
    }
    return render(re, 'search.html', ctx)
# Create your views here.
