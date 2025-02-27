from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            return HttpResponse(user.is_staff)

            if user.is_staff == True:
                login(request, user)
                if next == 'None':
                    return redirect('mypage_app:mypage')
                else:
                    return redirect(to=next)
    else:
        form = LoginForm()
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }

    return render(request, 'login_app/login.html', param)
    
def logout_view(request):
    logout(request)

    return redirect('home_app:homepage')
