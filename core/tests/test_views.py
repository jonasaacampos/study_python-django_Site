from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.dados = {
            "nome": "Jonas Campos",
            "email": "jonascampos@email.com",
            "assunto": "Teste unitário",
            "mensagem": "Mensgem aqui...",
        }

        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy("index"), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            "nome": "Nome",
            "mensagem": "??",
        }
        request = self.cliente.post(reverse_lazy("index"), data=dados)
        self.assertEquals(request.status_code, 200)
