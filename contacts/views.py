from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        chef_email = request.POST['chef_email']
        message = request.POST['message']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        phone = request.POST['phone']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted= Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already booked this resturant")
                return redirect('listings:listing',listing_id=listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, name= name,email = email,
                        chef_email=chef_email, message=message,phone=phone, user_id=user_id)
        contact.save()
        # send email
        # send_mail(
        #     "Reservation Request",
        #     "There has been a reservation request for "+listing,
        #     'a942408856@gmail.com',
        #     [chef_email],
        #     fail_silently=False
        # )


        messages.success(request,'Your request has been submitted, resturant will get back to you soon')

    return redirect('listings:listing',listing_id=listing_id)

def edit_contact(request,contact_id):
    contact = get_object_or_404(Contact,pk=contact_id)
    if request.method =="POST":
        form = ContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = ContactForm(instance=contact)


    context={
        "form":form
    }
    return render(request,"contacts/edit_contact.html",context)


def delete_contact(request,contact_id):
    contact = get_object_or_404(Contact,pk=contact_id)
    contact.delete()
    return redirect("accounts:dashboard")


