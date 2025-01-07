from django.shortcuts import render
def servicesView(request):
    return render(request, 'services.html')
