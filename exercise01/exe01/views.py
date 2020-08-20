from django.shortcuts import render
from exe01.forms import UserProfileInfoForm, UserForm
from exe01.models import UserProfileInfo
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# funzioni per il processo login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from exe01.funzioni import raddoppio, import_file, normaliz_path



# Create your views here.


def index(request):
    return render(request, 'index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required(login_url='/exe01/login/')
def special(request):
    return HttpResponse('You are logged in, Nice!')


def registration(request):

    registered = False


    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            # Do Something

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
            print(registered)

        else:
            print(user_form.errors,profile_form.errors )

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'folder01/registration.html', {'user_form': user_form, 'profile_form' : profile_form, 'registered' : registered} )



def users_ls(request):

    myhelp_dict = {}
    #users_list = User.objects.order_by('user_id')
    users_list = User.objects.values()
    users_list = [entry for entry in users_list]
    for items in users_list:
        for item in items:
            print(item, ': ', items[item] )

    myhelp_dict['users_list'] = users_list
    return render(request, 'folder01/users.html', context = myhelp_dict )


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)


        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password {}'.format(username,password))
            return HttpResponse("invalid login detail supplied!")
    else:
        return render(request, 'folder01/login.html', {})

"""
def apps(request):

    num = raddoppio(5)

    return render(request, 'folder01/apps.html', {'num' : num, 'test' : settings.MEDIA_DIR })


"""
def apps(request):

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        file_ex = import_file(normaliz_path(uploaded_file_url))
        return render(request, 'folder01/apps.html', {
            'uploaded_file_url': uploaded_file_url, 'file_ex' : file_ex
        })



    return render(request, 'folder01/apps.html', {})
