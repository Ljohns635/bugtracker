from django.shortcuts import render, HttpResponseRedirect, reverse
from bug_app.models import CustomUser, Ticket
from bug_app.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect(request.GET.get('next', reverse('ticket_page')))
            else:
                messages.error(request, "Invalid username or password.")

    form = LoginForm()
    return render(request, 'login.html', {'heading':'Login','form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(reverse('login_view'))

@login_required
def ticket_view (request):
    return render(request, 'tickets.html', {'heading': 'This is the ticket page'})
