from django.shortcuts import render
from category.models import Category

from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True)[0:15]

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)



def contact(request):
    return render(request, 'contact.html')



def about(request):
    return render(request, 'about.html')