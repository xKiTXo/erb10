from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.utils import timezone
from django.core.paginator import Paginator
from .choices import category_choices,district_choices,price_range_choices,open_now_choices
from django.db.models import Q

# Create your views here.
def listings(request):
    # print(request.path)
    listings = Listing.objects.order_by('list_date').filter(is_published=True)
    paginator =  Paginator(listings,3)
    page_number = request.GET.get("page")
    paged_listings =  paginator.get_page(page_number)
    current_time = timezone.localtime().time()
    content={
        "listings":paged_listings,
        "current_time":current_time
    }
    return render(request,"pages/listings.html",content)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    current_time = timezone.localtime().time()
    context = {
        "listing":listing,
        "current_time":current_time,
    }
    return render(request,"pages/listing.html",context)

def search(request):
    current_time = timezone.localtime().time()
    listings = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings= listings.filter(Q(description__icontains=keywords)
                                      |Q(title__icontains=keywords)
                                      |Q(cuisine_choices__icontains=keywords))
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            listings = listings.filter(district__iexact=district)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            listings = listings.filter(cuisine_choices__iexact=category)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            if price =='Budget':
                listings=listings.filter(price__lte=200)
            if price =='Mid':
                listings=listings.filter(price__gt=200).filter(price__lte=400)
            if price =='Premium':
                listings=listings.filter(price__gt=400)
            
    if 'open' in request.GET:
        open = request.GET['open']
        if open:
            if open =="Yes":
                listings = listings.filter(opening_hours__gte=current_time)

    paginator =  Paginator(listings,3)
    page_number = request.GET.get("page")
    paged_listings =  paginator.get_page(page_number)

    context = {
        "category_choices":category_choices,
        "district_choices":district_choices,
        "price_range_choices":price_range_choices,
        "open_now_choices":open_now_choices,
        "listings":paged_listings,
        "current_time":current_time,
        "values":request.GET
    }
    return render(request,"pages/search.html",context)
