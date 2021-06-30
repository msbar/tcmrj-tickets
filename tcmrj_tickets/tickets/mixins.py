from tcmrj_tickets.tickets.forms import TicketForm, TicketBasicForm
from tcmrj_tickets.tickets.models import Ticket

# define o ticket owner com request user
class OwnerTicketCreateMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# decide qual formulário será apresentado para o gestor e para o suporte
class TicketUpdateMixin(object):
    def get_form_class(self):
        if self.request.user.groups in ['gestor']:
            return TicketForm
        return TicketBasicForm

# Retorna lista de ticket completa para gestor e suporte e apenas os próprios tickets para o padrao
class TicketListMixin(object):
    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['padrao']).exists():
            return Ticket.objects.filter(owner=self.request.user)
        else:
            return Ticket.objects.all()