# Generated by Django 2.2.7 on 2019-12-15 00:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UmkaPage', '0005_ajouter_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='datePhoto',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de parution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='nomPhoto',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='dateArticle',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de parution'),
        ),
    ]