from django.shortcuts import render,redirect
from .models import Product_movement,Product,Location

# Create your views here.

def index(request):
    return render(request, 'html/index.html')
def Product_movement_view(request):
    qs=list(Product_movement.objects.values())
    final=[]
    for i in qs:
        x=list(i.values())
        final.append(x)
    return render(request,'html/Product_movements.html',{'qs':final})


def Product_view(request):
    qs=list(Product.objects.values())
    print(qs)
    final=[]
    for i in qs:
        x=list(i.values())
        final.append(x)
    return render(request,'html/products.html',{'qs':final})

def Location_view(request):
    qs=list(Location.objects.values())
    print(qs)
    final=[]
    for i in qs:
        x=list(i.values())
        final.append(x)
    print(final)
    return render(request,'html/locations.html',{'qs':final})

def add_product_movement(request):
    if(request.method=='GET'):
        products=list(Product.objects.values())
        final1=[]
        final2=[]
        for i in products:
            x=list(i.values())
            final1.append(x)
        locations=list(Location.objects.values())
        for i in locations:
            x=list(i.values())
            final2.append(x)
            print(final1,final2)
        return render(request,'html/add_product_movement.html', {'products':final1,'locations':final2})
    else:
        x=request.POST.get('from')
        y=request.POST.get('to')
        from_l=Location.objects.get(location_id=int(x))
        to_l=Location.objects.get(location_id=int(y))
        print(from_l,to_l)
        product=request.POST.get('product')
        print(product)
        pr=Product.objects.get(product_name=product)
        quantity=int(request.POST.get('quantity'))
        new_object=Product_movement.objects.create(from_location=from_l.location_id,to_location=to_l.location_id,product=pr,quantity=quantity)
        new_object.save()
        loc_quantity= Location.objects.get(location_id=int(y))
        x=loc_quantity.product_balance+quantity
        loc_quantity.product_balance=x
        loc_quantity.save()
        return redirect('/view_product_movement/')

def add_product(request):
    if request.method=='GET':
        return render(request, 'html/add_products.html')
    else:
        name=request.POST['product_name']
        price=request.POST['product_price']
        new_object=Product.objects.create(product_id=Product.objects.all().count() + 1,product_name=name, product_price=price)
        new_object.save()
        return redirect('/view_products/')

def add_location(request):
    if request.method=='GET':
        return render(request, 'html/add_locations.html')
    else:
        name=request.POST.get('locationname')
        print(name)
        new_object=Location.objects.create(location_id=Location.objects.all().count() + 1,location_name=name)
        new_object.save()
        return redirect('/view_locations/')

