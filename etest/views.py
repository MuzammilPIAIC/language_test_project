from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from .forms import *

# Create your views here.

def home(request):

    context={}
    return render(request, 'etest/home.html',context)

def resgister(request):

    if request.method == "POST":
        form = UserRegisteration(request.POST)
        if form.is_valid():
            try:
                data = form.save()
            except Exception as e:
                errors = [str(e)]
                context = {'form':form,'errors':errors}
                return render(request, 'etest/registeration.html',context)

            user_data = AppUser.objects.get(pk = data.pk)
            user = authenticate(request, username=user_data.user, password=user_data.password)
            if user is not None:
                print('user Logined.....')
                login(request, user)
            return redirect('test')
        
        

    user_form = UserRegisteration()
    context = {'form':user_form}
    return render(request, 'etest/registeration.html',context)

# @login_required(login_url='/')
def test(request):
    context = {}
    return render(request, 'etest/testpage.html', context)


def logout_button(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


def audio_file(request):

    if request.method == "POST":
        form = AudioForm(request.POST,request.FILES)
        user = AppUser.objects.get(id = 1)
        file = request.FILES['audio']
        create_at = datetime.today()

        try:
            new_data = AudioData()
            new_data.user = user
            new_data.audio_file = file
            new_data.create_at = create_at
            new_data.save()

            data = {
                'status' : 200,
                'message':'the file has been uploaded!!',
                'data' : []
            }
            return JsonResponse(data)
        except Exception as e:
            data = {
                'status' : 404,
                'message':f'Got error while uploading file!!! \n {str(e )}',
                'data' : []
            }
            return JsonResponse(data)

        # if form.is_valid():
        #     form.save()
        #     data = {
        #         'status' : 200,
        #         'message':'the file has been uploaded!!',
        #         'data' : []
        #     }
        #     return JsonResponse(data)
        # else:
        #     data = {
        #         'status' : 404,
        #         'message':f'Got error while uploading file!!! \n {form.errors}',
        #         'data' : []
        #     }
        #     return JsonResponse(data)


