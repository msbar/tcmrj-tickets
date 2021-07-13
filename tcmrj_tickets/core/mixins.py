from django.views.generic.edit import DeleteView
from django.contrib import messages


class ViewCreatedByMixin(object):
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class MessageSuccessDeleteView(DeleteView):
    def delete(self, request, *args, **kwargs):
            messages.success(self.request, self.success_message)
            return super(MessageSuccessDeleteView, self).delete(request, *args, **kwargs)