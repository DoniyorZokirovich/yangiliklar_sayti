
from django.shortcuts import render,redirect
from sayt.models import User
from django.contrib.auth import login as log_in, logout as log_out,authenticate



def login(requests):
    if not requests.user.is_anonymous:
        return  redirect('index')

    if requests.POST:
        username = requests.POST.get('username')
        pas = requests.POST.get('pass')

        user = User.object.filter(username = username).first()
        if not user:
            ctx = {
                'error': 'Bunaqa username topilmadi'
            }
            return render(requests, 'auth/login.html', ctx)

        if not user.check_password(pas):
            ctx ={
                'error':'Parol xato'
            }
            return render(requests, 'auth/login.html', ctx)

        log_in(requests, user)
        return redirect('index')




    return render(requests, 'auth/login.html', {})

def logout(requests, conf=None):
    if requests.user.is_anonymous:
        return redirect('login')
    if conf:
        log_out(requests)
        return redirect('login')
    return render(requests, 'auth/logout.html')


def regis(re):
    if not re.user.is_anonymous:
        return redirect('index')

    if re.POST:
        if  'oferta' not in re.POST:
            return render(re, 'auth/regis.html', {"error": "oferta qabul qilinmagan"})

        username = re.POST.get('username')
        user = User.object.filter(username=username).first()

        if user:
            return render(re, 'auth/regis.html', {"error": 'BUnaqa username bor'})
        if not username.islower() or len(username.split())>1:
            return render(re, 'auth/regis.html', {'error':'xato username'})
        pas = re.POST.get('pass')
        pas_conf = re.POST.get('pass_conf')

        if pas != pas_conf:
            return render(re, 'auth/regis.html', {'error':'Parollar mos emas'})

        name = re.POST.get('name')
        phone = re.POST.get('phone')
        user = User.object.create_user(username=username,password=pas, name= name, phone =phone)
        log_in(re,user)
        authenticate(re)
        return redirect('index')


    return render(re, 'auth/regis.html', {})