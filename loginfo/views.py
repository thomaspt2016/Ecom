from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from loginfo.forms import SignupForm
from django.contrib import messages
from django.core.mail import send_mail
from loginfo.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from shop.models import category,Product


class SignupView(View):
    def get(self, request):
        print("Inside Signup")
        form_instance=SignupForm()
        return render(request,'login/signup.html',{'form':form_instance})
    
    def post(self, request):
        print("Inside post")
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            print("form is valid")
            user=form_instance.save(commit=False)
            user.is_active=False
            user.save()
            user.generate_otp()
            send_mail(
                'OTP Test',
                user.otp,
                'thomaspt2016@example.com',
                [user.email],
                fail_silently=False,
                )
            return redirect('loginfo:verifyotp')
        else:
            print("form is not valid")
            return render(request, 'login/signup.html', {'form': form_instance})
        

class OtpVerificationView(View):
    def post(self,request):
        otp = request.POST.get('otp')
        try:
            u=CustomUser.objects.get(otp=otp)
            u.is_active=True
            u.is_verified=True
            u.otp=None
            u.save()
            return redirect('loginfo:signin')
        except:
            print("Invalid otp")
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('loginfo:verifyotp  ')

    def get(self,request):
        return render(request,'login/verify.html')
    
class SigninView(View):
    def post(self, request):
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        print(name, pwd)
        user = authenticate(username=name, password=pwd)
        if user:
            login(request, user)
            u = request.user
            if user.is_superuser:
                cate = category.objects.all()
                pro = Product.objects.all()
                return render(request, 'admin/adminhome.html', {'cat': cate, 'pro': pro})
            else:
                return redirect('shop:category')
        else:
            print("Invalid user credentials")
            return HttpResponse("Invalid username or password")

    def get(self, request):
        return render(request, 'login/signin.html')
    

class SignoutView(View):
    def get(self, request):
        logout(request)
        return redirect('shop:category')

class SuperAdminView(View):
    def get(self, request):
        u =request.user
        cate = category.objects.all()
        pro = Product.objects.all()
        return render(request, 'admin/adminhome.html', {'cat': cate, 'pro': pro})


