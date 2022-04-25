from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort=request.GET.get("sort", None)
    phones=Phone.objects.all()
    if sort=='name':
        phones=phones.order_by('name')
    if sort=='min_price':
        phones=phones.order_by('price')
    if sort=='max_price':
        phones=phones.order_by('-price')
    template = 'catalog.html'
    context = {'phones':phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(slug)
    context = {'phone': Phone.objects.get(slug__contains=slug)}
    return render(request, template, context)
