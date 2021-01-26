from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titleID': 'WELCOME',
        'titleEN': 'Register page',
        'navigasi': [
            ['/register', 'Register']
        ]
    }
    return render(request, 'index.html', context)