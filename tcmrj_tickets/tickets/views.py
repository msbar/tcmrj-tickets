from django.shortcuts import render


def ticket_create(request):
    
    return render(request, 'tickets/ticket_create.html')