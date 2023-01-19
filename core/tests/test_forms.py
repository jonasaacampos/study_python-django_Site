from django.test import TestCase
from model_mommy import mommy

from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = "Jonas Campos"
        self.email = "jonascampos@email.com"
        self.assunto = "Teste unitário"
        self.mensagem = "Mensgem aqui..."

        self.dados = {
            "nome": self.nome,
            "email": self.email,
            "assunto": self.assunto,
            "mensagem": self.mensagem,
        }

        # o mesmo que ContatoForm(request.POST)
        self.form = ContatoForm(data=self.dados)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)


