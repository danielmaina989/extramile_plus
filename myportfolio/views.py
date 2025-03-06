from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myportfolio/index.html')

def about(request):
    return render(request, 'myportfolio/about.html')

def portfolio(request):
    return render(request, 'myportfolio/portfolio.html')

def contact(request):
    return render(request, 'myportfolio/contact.html')
