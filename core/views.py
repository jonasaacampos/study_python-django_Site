from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Equipe, Servico, Funcionalidade
from .forms import ContatoForm

class IndexView(FormView):
    template_name = "index.html"
    form_class = ContatoForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all().order_by("?").all()
        context["funcionarios"] = Equipe.objects.all()
        context["funcionalidades"] = Funcionalidade.objects.all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "email enviado com sucesso")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "erro ao enviar o email")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class TesteView(FormView):
    template_name = "404.html"

