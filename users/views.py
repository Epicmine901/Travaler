from django.shortcuts import render
from .forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.views import View
class Register(View):
    template_name = 'Registration/register.html'
    def get(self,request):
        context = {
            'form': UserCreationForm()
        }
        return render(request,self.template_name,context)
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
        context = {
            'form' : form
        }
        return render(request,self.template_name,context)
