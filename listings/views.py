from django.shortcuts import render,get_object_or_404
from .models import Listing
from .models import Chef
from django.utils import timezone
from django.core.paginator import Paginator

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
    return render(request,"pages/search.html",locals())
