from django.contrib.auth.decorators import login_required
from tcmrj_tickets.core.decorators import group_required
from django.utils.decorators import method_decorator
from tcmrj_tickets.tickets.forms import TicketForm, SolverForm
from tcmrj_tickets.tickets.models import Ticket, Solver
from tcmrj_tickets.tickets.mixins import OwnerTicketCreateMixin, TicketUpdateMixin, TicketListMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


@method_decorator(login_required, name='dispatch')
class TicketCreateView(OwnerTicketCreateMixin, CreateView):
    template_name = 'tickets/tickets_form.html'
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy('tickets:list')


decorators = [login_required, group_required('gestor', 'suporte')]
@method_decorator(decorators, name='dispatch')
class TicketUpdateView(TicketUpdateMixin, UpdateView):
    template_name = 'tickets/tickets_form.html'
    model = Ticket
    success_url = reverse_lazy('tickets:list')

    
@method_decorator(login_required, name='dispatch')
class TicketListView(TicketListMixin, ListView):
    template_name = 'tickets/tickets_list.html'
    model = Ticket
    paginate_by = 100

    
@method_decorator(login_required, name='dispatch')
class TicketDatailView(DetailView):
    template_name = 'tickets/tickets_detail.html'
    model = Ticket
    

decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class TicketDeleteView(DeleteView):
    template_name = 'tickets/tickets_delete.html'
    model = Ticket
    success_url = reverse_lazy('tickets:list')

""" SOLVER VIEWS"""

decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SolverCreateView(CreateView):
    template_name = 'solver/solver_form.html'
    model = Solver
    form_class = SolverForm
    success_url = reverse_lazy('tickets:solver_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SolverUpdateView(UpdateView):
    template_name = 'solver/solver_form.html'
    model = Solver
    form_class = SolverForm
    success_url = reverse_lazy('tickets:solver_list')
    

decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SolverListView(ListView):
    template_name = 'solver/solver_list.html'
    model = Solver
    paginate_by = 10


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SolverDatailView(DetailView):
    template_name = 'solver/solver_detail.html'
    model = Solver


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SolverDeleteView(DeleteView):
    template_name = 'solver/solver_delete.html'
    model = Solver
    success_url = reverse_lazy('tickets:solver_list')