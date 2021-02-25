from django.shortcuts import render, HttpResponseRedirect, reverse
from bug_app.models import CustomUser, Ticket
from bug_app.forms import LoginForm, TicketForm
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
    return render(request, 'login.html', {
        'heading':'Login',
        'subheading':'Sorry, you need to be authenticated to do that. Please log in below.',
        'form': form
        })

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(reverse('login_view'))

@login_required
def ticket_view (request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets': tickets})

@login_required
def submit_view(request):
    context = {}
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_data = Ticket.objects.create(
                title = data['title'],
                description = data['description'],
                creator = request.user
            )
            return HttpResponseRedirect(reverse('ticket_details', args=[new_data.id]))
    
    form = TicketForm()
    context.update({
        'form': form,
        'heading': 'Submit a Ticket',
        'subheading': 'What\'s wrong? Something broken? Write it down!'
    })
    return render(request, 'submit.html', context)

@login_required
def user_details(request, user_id):
    user_obj = CustomUser.objects.get(id=user_id)
    tickets = Ticket.objects.filter(creator=user_obj)
    return render(request, 'user_detail.html', {
        'creator': user_obj,
        'tickets': tickets,
    })


@login_required
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})

@login_required
def ticket_edit(request, ticket_id):
    context = {}
    edit_item = Ticket.objects.get(id=ticket_id)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            edit_item.title = data['title']
            edit_item.description = data['description']
            edit_item.creator = request.user
            edit_item.save()
            return HttpResponseRedirect(reverse('ticket_details', args=[edit_item.id]))
    
    form = TicketForm(
        initial={'title': edit_item.title, 'description': edit_item.description, 'creator': edit_item.creator}
    )
    context.update({
        'form': form,
        'heading': 'Submit a Ticket',
        'subheading': 'What\'s wrong? Something broken? Write it down!'
    })
    return render(request, 'submit.html', context)

@login_required
def progress_status(request, status_id):
    edit_item = Ticket.objects.get(id=status_id)
    edit_item.status = 'In Progress'
    edit_item.assigned = request.user
    edit_item.save()
    return HttpResponseRedirect(reverse('ticket_details', args=[edit_item.id]))


@login_required
def completed_status(request, status_id):
    edit_item = Ticket.objects.get(id=status_id)
    edit_user = CustomUser.objects.get(username=request.user.username)
    edit_item.status = 'Completed'
    edit_item.completed = edit_user
    edit_item.assigned = None
    edit_item.save()
    return HttpResponseRedirect(reverse('ticket_details', args=[edit_item.id]))

@login_required
def invalid_status(request, status_id):
    edit_item = Ticket.objects.get(id=status_id)
    edit_item.status =  'invalid'
    edit_item.completed = None
    edit_item.assigned = None
    edit_item.save()
    return HttpResponseRedirect('/')
