from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('main')
    else:
        return redirect('/user/sign_in')

def main(request):
    return render(request, 'post_test/main.html')