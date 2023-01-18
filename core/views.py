from django.views.generic import TemplateView
from .models import Equipe, Servico, Funcionalidade

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all().order_by("?").all()
        context["funcionarios"] = Equipe.objects.all()
        context["funcionalidades"] = Funcionalidade.objects.all()

        return context


class TesteView(TemplateView):
    template_name = "404.html"

