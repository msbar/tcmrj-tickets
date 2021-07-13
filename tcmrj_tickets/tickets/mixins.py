from tcmrj_tickets.tickets.forms import TicketForm, TicketManagerForm, TicketBasicForm
from tcmrj_tickets.tickets.models import Ticket


# decide qual formulário será apresentado para o gestor e para o suporte
class TicketUpdateMixin(object):
    def get_form_class(self):
        if self.request.user.groups.filter(name__in=['gestor']).exists():
            return TicketManagerForm
        return TicketBasicForm

# Retorna lista de ticket completa para gestor e suporte e apenas os próprios tickets para o padrao
class TicketListMixin(object):
    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['padrao']).exists():
            return Ticket.objects.filter(created_by=self.request.user)
        else:
            return Ticket.objects.all()