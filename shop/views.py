from django.shortcuts import render
from .models import product,Order
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def index(request):
    #search code
    product_object=product.objects.all()
    item_name=request.GET.get('item_name')
    if(item_name!="" and item_name is not None):
        product_object=product_object.filter(title__icontains=item_name)
    #paginatorcode
    Paginator1 =Paginator(product_object,4)
    page=request.GET.get('page')
    product_object=Paginator1.get_page(page)
    return render(request,'shop/index.html',{'product_object':product_object})
def detail(request,id):
    product_object1=product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object1':product_object1})
def checkout(request):
    if request.method=="POST":
        items=request.POST.get('items','')
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address',"")
        city=request.POST.get('city',"")
        state=request.POST.get('state',"")
        zipcode=request.POST.get('zipcode',"")
        total=request.POST.get('total',"")
        order1= Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order1.save()
    return render(request,'shop/checkout.html')