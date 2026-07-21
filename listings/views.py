from django.shortcuts import render
from .models import Listing
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def listings(request):
    # print(request.path)
    listings = Listing.objects.filter(is_published=True)
    paginator =  Paginator(listings,3)
    page_number = request.GET.get("page")
    paged_listings =  paginator.get_page(page_number)
    current_time = timezone.localtime().time()
    content={
        "listings":paged_listings,
        "current_time":current_time
    }
    return render(request,"pages/listings.html",content)

def listing(request):
    return render(request,"pages/listing.html",locals())

def search(request):
    return render(request,"pages/search.html",locals())
