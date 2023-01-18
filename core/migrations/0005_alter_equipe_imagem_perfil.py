# Generated by Django 4.1.5 on 2023-01-18 14:00

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_equipe_imagem_perfil"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipe",
            name="imagem_perfil",
            field=stdimage.models.StdImageField(
                force_min_size=False,
                upload_to="equipe\\<function get_file_path at 0x0000020FF9C91510>",
                variations={"thumb": {"crop": True, "height": 480, "width": 480}},
                verbose_name="Imagem",
            ),
        ),
    ]
