from django.shortcuts import redirect, render
from django.contrib import auth
from .models import UserModel

# Create your views here.
def sign_up(request):
    if request.method=='GET':
        return render(request, 'users/sign_up.html')
    elif request.method == 'POST':
        UserModel.objects.create_user(
            username = request.POST.get('user_id'),
            password = request.POST.get('user_password'),
            cat_name = request.POST.get('cat_name'),
        )
        return render(request, 'users/success.html', {'msg' : '회원가입 성공입니다.'})


def success(request):
    return render(request, 'users/success.html')


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'users/sign_in.html')
    elif request.method == 'POST':
        username = request.POST.get('user_id','')
        password = request.POST.get('user_password','')
        me = auth.authenticate(request, username = username, password = password)
        if me:
            auth.login(request, me)
            return render(request, 'users/success.html', {'msg' : '로그인 성공입니다.'})
        else:
            return redirect('/user/sign_in')