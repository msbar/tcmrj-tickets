from django.contrib.auth.decorators import login_required
from tcmrj_tickets.core.decorators import group_required
from django.utils.decorators import method_decorator
from tcmrj_tickets.tickets.forms import TicketForm, SolverForm
from tcmrj_tickets.tickets.models import Ticket, Solver
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


@method_decorator(login_required, name='dispatch')
class TicketCreateView(CreateView):
    template_name = 'tickets/tickets_form.html'
    model = Ticket
    form_class = TicketForm
    # success_url = reverse_lazy('ticket_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor', 'suporte'), name='dispatch')
class TicketUpdateView(UpdateView):
    template_name = 'tickets/tickets_form.html'
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy('tickets:list')
    

@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor', 'suporte'), name='dispatch')
class TicketListView(ListView):
    template_name = 'tickets/tickets_list.html'
    model = Ticket
    paginate_by = 100


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor', 'suporte'), name='dispatch')
class TicketDatailView(DetailView):
    template_name = 'tickets/tickets_detail.html'
    model = Ticket
    

@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor'), name='dispatch')
class TicketDeleteView(DeleteView):
    template_name = 'tickets/tickets_delete.html'
    model = Ticket
    success_url = reverse_lazy('tickets:list')

""" SOLVER VIEWS"""

@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor'), name='dispatch')
class SolverCreateView(CreateView):
    template_name = 'solver/solver_form.html'
    model = Solver
    form_class = SolverForm
    success_url = reverse_lazy('tickets:solver_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor'), name='dispatch')
class SolverUpdateView(UpdateView):
    template_name = 'solver/solver_form.html'
    model = Solver
    form_class = SolverForm
    success_url = reverse_lazy('tickets:solver_list')
    

@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor'), name='dispatch')
class SolverListView(ListView):
    template_name = 'solver/solver_list.html'
    model = Solver
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor'), name='dispatch')
class SolverDatailView(DetailView):
    template_name = 'solver/solver_detail.html'
    model = Solver


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor'), name='dispatch')
class SolverDeleteView(DeleteView):
    template_name = 'solver/solver_delete.html'
    model = Solver
    success_url = reverse_lazy('tickets:solver_list')