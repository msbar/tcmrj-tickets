from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from tcmrj_tickets.core.decorators import group_required
from django.utils.decorators import method_decorator
from tcmrj_tickets.tickets.forms import TicketForm, SolverForm
from tcmrj_tickets.tickets.models import Ticket, Solver
from tcmrj_tickets.tickets.mixins import OwnerTicketCreateMixin, TicketUpdateMixin, TicketListMixin
from django.urls import reverse_lazy
from tcmrj_tickets.core.mixins import MessageSuccessDeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


@method_decorator(login_required, name='dispatch')
class TicketCreateView(SuccessMessageMixin, OwnerTicketCreateMixin, CreateView):
    template_name = 'tickets/tickets_form.html'
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy('tickets:list')
    success_message = "Chamado criado com sucesso!"


decorators = [login_required, group_required('gestor', 'suporte')]
@method_decorator(decorators, name='dispatch')
class TicketUpdateView(SuccessMessageMixin, TicketUpdateMixin, UpdateView):
    template_name = 'tickets/tickets_form.html'
    model = Ticket
    success_url = reverse_lazy('tickets:list')
    success_message = "Chamado atualizado com sucesso!"
    
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
class TicketDeleteView(MessageSuccessDeleteView):
    template_name = 'tickets/tickets_delete.html'
    model = Ticket
    success_url = reverse_lazy('tickets:list')
    success_message = "Chamado excluído com sucesso!"

""" SOLVER VIEWS"""

decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SolverCreateView(SuccessMessageMixin, CreateView):
    template_name = 'solver/solver_form.html'
    model = Solver
    form_class = SolverForm
    success_url = reverse_lazy('tickets:solver_list')
    success_message = "Responsável criado com sucesso!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SolverUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'solver/solver_form.html'
    model = Solver
    form_class = SolverForm
    success_url = reverse_lazy('tickets:solver_list')
    success_message = "Responsável atualizado com sucesso!"

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
class SolverDeleteView(MessageSuccessDeleteView):
    template_name = 'solver/solver_delete.html'
    model = Solver
    success_url = reverse_lazy('tickets:solver_list')
    success_message = "Responsável excluído com sucesso!"