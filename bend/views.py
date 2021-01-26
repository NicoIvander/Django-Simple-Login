from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'titleID': 'WELCOME BACK',
        'titleEN': 'Login page',
        'piclog': 'login.png',
        'picg': 'Google.png',
        'picl': 'LinkedIN.png',
        'picf': 'Facebook.png',
        'css': 'style.css',
        'navigasi': [
            ['/register', 'Register']
        ]
    }
    return render(request, 'index.html', context)