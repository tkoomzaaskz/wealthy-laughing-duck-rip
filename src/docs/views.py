from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
    context = { 'top_tab': 'docs' }
    return render(request, 'index.html', context)

def about(request):
    context = { 'top_tab': 'about' }
    return render(request, 'about.html', context)

def users(request):
    context = {
        'top_tab': 'docs',
        'command': 'users',
        'url': reverse('api_dispatch_list', kwargs={'resource_name': 'user', 'api_name': 'v1'})
    }
    return render(request, 'users.html', context)

def categories(request):
    context = {
        'top_tab': 'docs',
        'command': 'categories',
        'url': reverse('api_dispatch_list', kwargs={'resource_name': 'category', 'api_name': 'v1'})
    }
    return render(request, 'categories.html', context)

def incomes(request):
    context = { 'top_tab': 'docs', 'command': 'incomes' }
    return render(request, 'incomes.html', context)

def outcomes(request):
    context = { 'top_tab': 'docs', 'command': 'outcomes' }
    return render(request, 'outcomes.html', context)
