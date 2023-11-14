from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_form, Update_profile
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


def doctor_list(request):
    doctor = User.objects.all()

    return render(request, 'user/app.html', {'doctor':doctor})



def doctor_detail(request, slug):
    doctor = Profile.objects.get(slug=slug)
    return render(request, 'user/detail.html', {'doc_detail':doctor})


def user_login(request):
    if request.method == 'POST':
        form = Login_form
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request , user)
            return redirect('accounts:doctor_list')
    else:
        form = Login_form()
    return render(request, 'user/login.html', {
        'form': form
    })

@login_required()
def my_profile(request):
    return render(request, 'user/myprofile.html')


def update_profile(request):
    user_form = Update_profile(instance=request.user)

    if request.method == "POST":
        user_form = Update_profile(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
    return render(request, 'user/update.html', {
        'user_form':user_form
    })