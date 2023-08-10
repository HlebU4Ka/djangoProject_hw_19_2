from django.shortcuts import render


def home_page(request):
    return render(request, 'catalog/home_page.html')


def info_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        massage = request.POST.get('message')
        print(name, phone, massage)
    return render(request, 'catalog/info_contact_page.html')
