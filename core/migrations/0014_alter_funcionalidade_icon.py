# Generated by Django 4.1.5 on 2023-01-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_alter_funcionalidade_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionalidade",
            name="icon",
            field=models.CharField(
                choices=[
                    ("fa-solid fa-feather", "pena"),
                    ("fa-solid fa-bug", "bug"),
                    ("fa-solid fa-fish", "peixe"),
                    ("fa-solid fa-earth-americas", "planeta"),
                    ("fa-solid fa-handshake", "aperto de mãos"),
                    ("fa-solid fa-users", "usuários"),
                    ("fa-solid fa-thumbs-up", "curtir"),
                    ("fa-solid fa-paper-plane", "avião de papel"),
                ],
                max_length=30,
                verbose_name="Ícone",
            ),
        ),
    ]
