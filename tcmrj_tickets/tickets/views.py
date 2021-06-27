from tcmrj_tickets.tickets.forms import TicketForm
from tcmrj_tickets.tickets.models import Category, SubCategory, Ticket
from django.shortcuts import render, get_object_or_404
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
    form_class = TicketForm
    success_url = 'list'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TicketUpdateView(UpdateView):
    template_name = 'tickets/tickets_form.html'
    ticket = None
    form_class = TicketForm
    success_url = 'list'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Ticket, id=pk)
    '''
    def dispatch(self, request, pk):
        self.ticket = get_object_or_404(Ticket, id=pk)
        return super().dispatch(request, pk)
    
    def get(self, request, *args, **kwargs):
        return self.render_to_response({'ticket': self.ticket,
                                        'form': TicketForm})
    
    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form(data=request.POST)
        if form.is_valid():
            form.save()
            return
        return self.render_to_response({'ticket': self.ticket,
                                        'form': TicketForm})
    '''    


class TicketListView(ListView):
    template_name = 'tickets/tickets_list.html'


class TicketDatailView(DetailView):
    template_name = 'tickets/tickets_datail.html'


class TicketDeleteView(DeleteView):
    template_name = 'tickets/tickets_delete.html'