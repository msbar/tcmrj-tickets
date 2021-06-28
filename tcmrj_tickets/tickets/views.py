from tcmrj_tickets.tickets.forms import TicketForm, SolverForm
from tcmrj_tickets.tickets.models import Category, Ticket, Solver
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


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
    success_url = reverse_lazy('tickets:list')
    
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
    success_url = reverse_lazy('tickets:list')

""" SOLVER VIEWS"""

class SolverCreateView(CreateView):
    template_name = 'solver/solver_form.html'
    model = Solver
    form_class = SolverForm
    success_url = reverse_lazy('tickets:solver_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class SolverUpdateView(UpdateView):
    template_name = 'solver/solver_form.html'
    model = Solver
    form_class = SolverForm
    success_url = reverse_lazy('tickets:solver_list')
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Solver, id=pk)    


class SolverListView(ListView):
    template_name = 'solver/solver_list.html'
    model = Solver
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SolverDatailView(DetailView):
    template_name = 'solver/solver_detail.html'
    model = Solver
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Solver, id=pk)

class SolverDeleteView(DeleteView):
    template_name = 'solver/solver_delete.html'
    model = Solver
    success_url = reverse_lazy('tickets:solver_list')