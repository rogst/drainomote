from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.


def post_login(request):
    if request.method == "POST":
        username = request.POST['form_username']
        password = request.POST['form_password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                if request.GET['next']:
                    return redirect(request.GET['next'])
            else:
                messages.add_message(request,
                                     messages.ERROR,
                                     'Account has been disabled.')
                # Return a 'disabled account' error message
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Authentication failed.')
            # Return an 'invalid login' error message.

    return render(request, "accounts/login.html")


def do_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
