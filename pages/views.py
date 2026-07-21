from django.shortcuts import render
from listings.models import Listing
from django.utils import timezone


# Create your views here
def index(request):

    # print(listings[0].photo_main)
    # print(listings[0].photo_main.url)

    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    current_time=timezone.localtime().time()
    top3_rated = Listing.objects.order_by("-rating").filter(is_published=True)[:3]

    context={
        "listings":listings,
        "current_time":current_time,
        "top3_rated":top3_rated
    }
    
    return render(request,"pages/index.html",context)

def about(request):
    return render(request,"pages/about.html")