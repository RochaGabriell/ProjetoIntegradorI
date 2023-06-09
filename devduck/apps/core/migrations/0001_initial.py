# Generated by Django 4.2.1 on 2023-06-21 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=255, verbose_name='Descrição')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Aprovado')),
                ('is_rejected', models.BooleanField(blank=True, null=True, verbose_name='Rejeitado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_permissions', to=settings.AUTH_USER_MODEL, verbose_name='Aprovado por')),
                ('requesting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_permissions', to=settings.AUTH_USER_MODEL, verbose_name='Usuário solicitante')),
            ],
            options={
                'verbose_name': 'Solicitação de permissão',
                'verbose_name_plural': 'Solicitações de permissão',
            },
        ),
    ]
