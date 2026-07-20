from django.shortcuts import render
from listings.models import Listing

# Create your views here
def index(request):
    listings = Listing.objects.order_by("-list_date")
    context={"listings":listings}
    print(listings[0].photo_main)
    print(listings[0].photo_main.url)
    return render(request,"pages/index.html",context)

def about(request):
    return render(request,"pages/about.html")