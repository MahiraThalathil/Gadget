from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request,c_slug=None):
    # c_slug=None
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(catag,slug=c_slug)
        prodt=products.objects.filter(catagory=c_page,available=True)
    else:
        prodt=products.objects.filter(available=True)
    cat=catag.objects.all() 
    paginator=Paginator(prodt,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'pr':prodt,'ct':cat,'pg':pro})


def prodDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(slug=product_slug)
        # prod=request.session.flush()                                       
        cat=catag.objects.get(slug=c_slug)

    except products.DoesNotExist:
        prod=None
    return render(request,'item.html',{'pr':prod})


def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query)|Q(brand__contains=query))

    return render(request,'search.html',{'qr':query,'pr':prod})