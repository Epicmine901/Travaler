from django.shortcuts import render
from users.models import User
def IndexView(request):
    context = {
        'users': User
    }
    return render(request,'index.html',context)
# Create your views here.
