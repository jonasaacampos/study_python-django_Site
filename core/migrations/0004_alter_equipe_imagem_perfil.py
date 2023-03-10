# Generated by Django 4.1.5 on 2023-01-18 13:58

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_equipe_biografia_alter_equipe_imagem_perfil_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipe",
            name="imagem_perfil",
            field=stdimage.models.StdImageField(
                force_min_size=False,
                upload_to="equipe\\<function get_file_path at 0x00000184CB751510>",
                variations={"thumb": {"crop": True, "height": 480, "width": 480}},
                verbose_name="Imagem",
            ),
        ),
    ]
