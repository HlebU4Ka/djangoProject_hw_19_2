from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def info_page(request):
    return render(request, 'info_contact_page.html')
