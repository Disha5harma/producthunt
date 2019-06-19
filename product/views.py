from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
def home(request):
    product = Product.objects
    return render(request,'product/home.html',{'project':product})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image'] and request.POST['url']:
            product = Product()
            product.title= request.POST['title']
            product.body = request.POST['body']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            if request.POST['url'].startswith('https://') or request.POST['url'].startswith('http://') :
                product.url= request.POST['url']
            else:
                product.url= 'https://' + request.POST['url'] 

            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/product/'+ str(product.id))
        else:
            return render(request,'product/create.html',{'error':'Fill up the details'})
            
    else:
        return render(request,'product/create.html')

def detail(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request,'product/detail.html',{'product':product})
@login_required
def upvote(request,product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total+=1
        product.save()
        return redirect('/product/'+ str(product.id))
    
