# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from hw1.models import User

from django.shortcuts import render


# Create your views here.

def index(request):
    dt = datetime.now()
    return render(request, 'index.html', locals())


def userquery(request):
    userlist = User.objects.all()

    return render(request, 'userquery.html', locals())


def userdetail(request):
    return render(request, 'userdetail.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        status = ''
        message = ''
        if not "username" in request.session:

            user = User.objects.filter(Username__exact=username).filter(Password__exact=password)
            if user[0]:
                print(user[0].Password + 'logged')
                request.session['username'] = username
                message = 'Welcome ' + username
                status = 'login'
        else:
            if 'username' in request.session:
                if request.session['username'] == username:
                    message = request.session['username'] + ' already logged'
                    status = 'login'
        print(username + " " + status + " " + message)
        return render(request, 'index.html', locals())

    pass
    return render(request, 'login.html')


def logout(request):
    status = 'login'
    if 'username' in request.session:
        message = request.session['username'] + ' logged out OuOb'
        del request.session['username']
    return render(request, 'index.html', locals())


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        sex = request.POST['sex']
        detail = request.POST['detail']
        if username != "" and sex != "" and detail != "":
            user = User(Username=username, Password=password, Sex=sex, Detail=detail)
            user.save()
            pass

    return render(request, 'register.html', locals())
