from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Event
from django.db.models import DateTimeField

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm

from .forms import RegisterForm, Eventform

def home(request):
    #owned_events = foundUser.isOwnerOf()
    #vendor_events = foundUser.isVendorOf()
    #guest_events = foundUser.isGuestOf()
    return render(request, 'home.html')

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})

def change_password(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')

            if redirect_to:
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {'form': form, 'next': redirect_to})

def owner(request):
    return render(request, 'RSVP_WEB/owner.html')

def vendor(request):
    return render(request, 'RSVP_WEB/vendor.html')

def guest(request):
    return render(request, 'RSVP_WEB/guest.html')

def create_event(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == "POST":
        new_event_form = Eventform(request.POST)
        if new_event_form.is_valid():
            new_event_form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/owner_page')
                messages.error(request,"Invalid, please check date format.")
        #    return redirect(create_success)
        #print(new_event_form.errors)
        #messages.error(request,"Invalid, please check date format.")
        #return redirect('create_event')
    else:
        new_event_form = Eventform()
    return render(request,'RSVP_WEB/create_event.html',{'form':new_event_form, 'next': redirect_to})            
            
def create_success(request):
    return render(request,'RSVP_WEB/create_success.html')
    
#def vendor(request):
#        return redirect('vendor_event')
    
#def vendor_event(request):
#        return HttpResponse("empty")
    
# Create your views here.

