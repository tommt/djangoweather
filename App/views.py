from django.shortcuts import render
#  this is views file


def home(request):
    context = {
    }
    return render(request,'home.html', context)


def about(request):
    return render(request, 'about.html', {})