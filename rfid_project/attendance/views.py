from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Log
from django.shortcuts import redirect
import datetime
global stat
stat = ''
# Create your views here.
global selected
selected = None

def index1(request):
    logf = []
    logs = Log.objects.all()
    for log in logs:
        if str(log.date) == str(datetime.datetime.now())[:10]:
            logf.append(log)
    logf.reverse()
    dataset = {'log':logf}
    return render(request,'attendance/attendance.html',dataset)

def index(request):
    return render(request, 'attendance/index.html')

def process(request):
    card = request.GET.get('card_id', 'kuch nahi mila')
    users = User.objects.all()
    for user in users:
        if user.card_id == int(card):
            ans = attend(user)
            return HttpResponse(ans)
    new_user = User(card_id=int(card))
    new_user.save()
    return HttpResponse('registered successfully')

def attend(user):
    if user.name == None:
        statu = 'profile to save krle bhai'
        return statu
    logs = Log.objects.all()
    for log in logs:
        if log.card_id == int(user.card_id):
            if str(log.date) == str(datetime.datetime.now())[:10]:
                if log.time_out == None:
                    log.time_out = datetime.datetime.now()
                    log.save()
                    statu = 'logout'
                    return statu
                else:
                    statu = 'nikal ja bhai ab'
                    return statu
    new_log = Log(ida=user.id,card_id=user.card_id,name=user.name,phone=user.phone,date=datetime.datetime.now(),time_in=datetime.datetime.now(),status='')
    new_log.save()
    statu='login'
    return statu

def details1(request):
    users = User.objects.all()
    us = []
    for user in users:
        us.append(user)
    us.reverse()
    userset = {'users': us}
    return render(request,'attendance/userdetails.html',userset)

def details(request):

    return render(request, 'attendance/details.html')


def manage1(request):
    users = User.objects.all()
    us=[]
    for user in users:
        us.append(user)
    us.reverse()
    global stat
    userset = {'users': us}
    stat = ''
    return render(request, 'attendance/allusers.html',userset)

def manage(request):
    global stat
    status = {'cardstatus' : stat}
    return render(request, 'attendance/manage.html',status)

def card(request):
    users = User.objects.all()
    global stat
    global selected
    if request.method == 'POST':
        if request.POST.get("sel"):
            ids = request.POST.get('idsearch', 'kuch nahi mila')
            for user in users:
                if user.id == int(ids):
                    stat = 'Card is Selected'
                    selected = user
                    break
                else:
                    stat = 'Card not found'
            return redirect('/manage')
        else:
            ids = request.POST.get('idsearch')
            for user in users:
                if user.id == int(ids):
                    user.delete()
                    stat = 'Deleted Successfully'
                    break
                else:
                    stat = 'Card not found'
            return redirect('/manage')


def edit(request):
    i=0
    users = User.objects.all()
    global selected
    global stat
    if selected == None:
        stat = 'No Card was Selected'
        return redirect('/manage')
    else:
        name = request.POST.get('name')
        dob = request.POST.get('date')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        new = [name,phone,dob,email,gender,address]
        for user in users:
            if user.card_id == selected.card_id:
                old = [user.name,user.phone,user.dob,user.email,user.sex,user.address]
                for item in new:
                    if item == '' or item is None:
                        new[i] = old[i]
                    i=i+1
                user.name = new[0]
                user.phone = new[1]
                user.dob = new[2]
                user.email = new[3]
                user.sex = new[4]
                user.address = new[5]
                user.save()
                stat = 'Profile Updated'
        selected = None
        return redirect('/manage')

def search(request):
    sel_user=''
    users = User.objects.all()
    logs = Log.objects.all()
    path = request.get_full_path()
    id = request.POST.get('search')
    if (id):
        logf = []
        for user in users:
            if str(user.id) == str(id):
                sel_user = user
        for log in logs:
            if str(log.date)[5:7] == str(datetime.datetime.now())[5:7] and str(log.ida) == str(id):
                logf.append(log)
        logf.reverse()
        dataset = {'use': sel_user,'log': logf}
        return render (request,'attendance/search.html',dataset)
    else:
        return redirect(request.META['HTTP_REFERER'])

