from django.db import models
from stdimage import StdImageField

import core.models


class Base(models.Model):
    criado = models.DateTimeField("Criado_em", auto_now_add=True)
    modificado = models.DateTimeField("Modificado_em", auto_now=True)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICON_CHOICES = (
        ("lni-cog", "engrenagem"),
        ("lni-stats-up", "grágico"),
        ("lni-users", "usuários"),
        ("lni-layers", "design"),
        ("lni-mobile", "mobile"),
        ("lni-rocket", "foguete"),
    )

    name = models.CharField("Serviço", max_length=100)
    description = models.CharField("Descrição", max_length=300)
    icon = models.CharField("Icone", max_length=20, choices=ICON_CHOICES)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.name


class Cargo(Base):
    cargo = models.CharField("Cargo", max_length=100)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo


class Equipe(Base):
    nome = models.CharField("Nome", max_length=150)
    cargo = models.ForeignKey(
        "core.Cargo", verbose_name="Cargo", on_delete=models.CASCADE
    )
    biografia = models.CharField("Biografia", max_length=300)
    imagem_perfil = StdImageField(
        "Imagem",
        upload_to="equipe",
        variations={"thumb": {"width": 480, "height": 480, "crop": True}},
    )
    social_facebook = models.CharField("facebook", max_length=100, default="#")
    social_instagram = models.CharField("instagram", max_length=100, default="#")
    social_twitter = models.CharField("twitter", max_length=100, default="#")
    social_whatsapp = models.CharField("whatsapp", max_length=100, default="#")

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.nome