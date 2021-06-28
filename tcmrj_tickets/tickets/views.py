from tcmrj_tickets.tickets.forms import TicketForm
from tcmrj_tickets.tickets.models import Category, SubCategory, Ticket
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
import json
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def get_subcategory(request):
    id = request.GET.get('id','')
    #result = list(SubCategory.objects.filter(
    #    category_id=int(id)).values('id', 'name'))
    result = ['computador','memória','mouse']
    return HttpResponse(json.dumps(result), content_type="application/json")


class TicketCreateView(CreateView):
    template_name = 'tickets/tickets_form.html'
    model = Ticket
    form_class = TicketForm
    # success_url = reverse_lazy('ticket_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TicketUpdateView(UpdateView):
    template_name = 'tickets/tickets_form.html'
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy('ticket:list')
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Ticket, id=pk)    


class TicketListView(ListView):
    template_name = 'tickets/tickets_list.html'
    model = Ticket
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TicketDatailView(DetailView):
    template_name = 'tickets/tickets_detail.html'
    model = Ticket
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Ticket, id=pk)

class TicketDeleteView(DeleteView):
    template_name = 'tickets/tickets_delete.html'
    model = Ticket
    success_url = reverse_lazy('ticket:list')