from django.views.generic.edit import DeleteView
from django.contrib import messages

class MessageSuccessDeleteView(DeleteView):

    def delete(self, request, *args, **kwargs):
            messages.success(self.request, self.success_message)
            return super(MessageSuccessDeleteView, self).delete(request, *args, **kwargs)