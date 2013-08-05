from django.shortcuts import render

def index(request):
    context = { 'top_tab': 'docs' }
    return render(request, 'index.html', context)

def about(request):
    context = { 'top_tab': 'about' }
    return render(request, 'about.html', context)

def users(request):
    context = { 'top_tab': 'docs', 'command': 'users' }
    return render(request, 'users.html', context)

def categories(request):
    context = { 'top_tab': 'docs', 'command': 'categories' }
    return render(request, 'categories.html', context)

def incomes(request):
    context = { 'top_tab': 'docs', 'command': 'incomes' }
    return render(request, 'incomes.html', context)

def outcomes(request):
    context = { 'top_tab': 'docs', 'command': 'outcomes' }
    return render(request, 'outcomes.html', context)
