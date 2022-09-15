# This Django app is build for automation using python, build by Abhijith KR 

from django.shortcuts import redirect, render

# importing django login athentications
from django.contrib.auth import authenticate, login, logout

from accounts.models import User_Account

from django.contrib.auth.models import User

# Create your views here.


def signup(request):

    # user already logged in section (case 1)
    if request.user.is_authenticated: 
        print(request.user,'User already logged in')
        return render(request,'admin/dashboard.html')

    else:
        # Registration section (case 2)
        if request.method == 'POST':
            email = request.POST.get('email')
            pswd1 = request.POST.get('pswd1')
            pswd2 = request.POST.get('pswd2')
    
            # print(email)
            # print(pswd1)
            # print(pswd2)

            if(email== '' or pswd1=='' or pswd2==''):
                print('No value')
                context={'static_mail':email,'error_msg':'Please enter valid info...'}
                return render(request,'accounts/signup.html',context)

            elif(len(pswd1)<6):
                print('Password length too short.')
                context={'static_mail':email,'error_msg':'Password length is too short. Require a minimum password length of 6–10 characters.'}
                return render(request,'accounts/signup.html',context)

            elif(not pswd1==pswd2):
                print('Password Missmatch')
                context={'static_mail':email,'error_msg':"Those passwords didn't match. Try again."}
                return render(request,'accounts/signup.html',context)

            elif User.objects.filter(username=email).exists():
                print('User already exist View')
                context={'static_mail':email,'error_msg':'Email already exist...'}
                return render(request,'accounts/signup.html',context)

            else:
                User_db=User.objects.create_user(
                        username=email,
                        password=pswd1,
                    )
                # user_obj.set_password(password)

                User_Account.objects.create(
                    user_id=User_db,
                    email=email,
                )

                print('Sucessfully registered')
                return render(request,'accounts/login.html',{'success_msg': 'Successfully registered, Please login','static_mail':email})
                    
        return render(request,'accounts/signup.html')




def login_page(request):
    # user already logged in section (case 1)
    if request.user.is_authenticated: 
        print(request.user,'User already logged in')

        return render(request,'admin/dashboard.html')
    
    else:
        # Login section (case 2)
        if request.method == 'POST':
            email = request.POST.get('email')
            pswd = request.POST.get('pswd')

            # print(email)
            # print(pswd)


            if(email== '' or pswd==''):
                print('No value')
                context={'static_mail':email,'error_msg':'Please enter valid info...'}
                return render(request,'accounts/login.html',context)

            else:
                user =authenticate(request, username=email, password=pswd) # check the user is valid
                print(user)

                if user is not None:
                    login(request, user) #login is hold uservalue(request&user), and added to django_section database
                    print(type(user),user)
                    print('User Login succesfull')

                    return render(request,'admin/dashboard.html')   

                else:
                    print(user,'user')
                    print('login failed')
                    context={'static_mail':email,'error_msg':'Invalid Email and Password'}
                    return render(request,'accounts/login.html',context)

        return render(request,'accounts/login.html')


def logout_page(request):
    logout(request)
    return redirect('/')