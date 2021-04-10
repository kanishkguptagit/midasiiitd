from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
# Create your views here.

def register(request):
    if (request.method == 'POST'):
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1==password2):
            if(User.objects.filter(username = username).exists()):
                messages.info(request,'Username Already exist')
                return redirect('register')

            elif(User.objects.filter(email = email).exists()):
                messages.info(request,'Username Already exist')
                return redirect('register')

            else:                
                user = User.objects.create_user(username=username, email=email, password = password1, first_name = firstName, last_name = lastName )
                user.save()
                print('user created')

        else:
            print('Password not matching')
            messages.info(request,'Username Already exist')
            return redirect('register')

        return redirect('/accounts/login')      
        
    else:
        return render(request, 'register1.html')


def login(request):
    if(request.method == 'POST'):
        user_entered = request.POST['username']
        password_entered = request.POST['password']
        
        user = auth.authenticate(username = user_entered, password = password_entered)

        if(user is not None):            
            auth.login(request,user)           
            return render(request,'dashboard.html')
        else:
            messages.info(request,'invalid credential')
            return redirect ('/accounts/login')
    else:
        return render(request, 'login1.html')