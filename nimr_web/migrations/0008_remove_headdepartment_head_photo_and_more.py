# Generated by Django 4.1 on 2023-01-05 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nimr_web", "0007_centremanagerphoto_headdepartment_sliderphoto_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="headdepartment",
            name="head_photo",
        ),
        migrations.RemoveField(
            model_name="headdepartment",
            name="head_photo_link",
        ),
        migrations.RemoveField(
            model_name="historicalheaddepartment",
            name="head_photo",
        ),
        migrations.RemoveField(
            model_name="historicalheaddepartment",
            name="head_photo_link",
        ),
        migrations.AlterField(
            model_name="headdepartment",
            name="head_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nimr_web.staffprofile"
            ),
        ),
        migrations.AlterField(
            model_name="historicalheaddepartment",
            name="head_name",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="nimr_web.staffprofile",
            ),
        ),
    ]
