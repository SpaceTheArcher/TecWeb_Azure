# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 22:18
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ra', models.IntegerField(unique=True, verbose_name='RA')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique='True', verbose_name='E-mail')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('perfil', models.CharField(choices=[('A', 'Aluno'), ('P', 'Professor'), ('C', 'Coordenador')], max_length=1, verbose_name='Perfil')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=50, verbose_name='Assunto')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('mensagem', models.TextField(verbose_name='Mensagem')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horária')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo')),
                ('professor', models.CharField(max_length=20, verbose_name='Professor')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horária')),
                ('teoria', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Teoria')),
                ('pratica', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prática')),
                ('ementa', models.TextField(verbose_name='Ementa')),
                ('competencias', models.TextField(verbose_name='Competencias')),
                ('habilidades', models.TextField(verbose_name='Habilidades')),
                ('conteudo', models.TextField(verbose_name='Conteudo')),
                ('bibliografia_basica', models.TextField(verbose_name='Bibliografia Básica')),
                ('bibliografia_complementar', models.TextField(verbose_name='Bibliografia Complementar')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('parent_link', models.OneToOneField(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuario',),
        ),
    ]
