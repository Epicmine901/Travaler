from django.shortcuts import render

def packagesView(request):
    return render(request, 'packages.html')
