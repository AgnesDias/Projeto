# Generated by Django 2.2.3 on 2019-08-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('genero', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')], max_length=255, verbose_name='Genero')),
                ('cpf', models.IntegerField(max_length=11, verbose_name='CPF')),
                ('telefone', models.IntegerField(max_length=11, verbose_name='Telefone Fixo')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('senha', models.CharField(max_length=8, verbose_name='Senha')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('email_comercial', models.EmailField(max_length=255, verbose_name='E-mail Comercial')),
                ('cep', models.CharField(max_length=9, verbose_name='endereco')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=6, verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('municipio', models.CharField(max_length=50, verbose_name='Município')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('senha', models.CharField(max_length=8, verbose_name='Senha')),
            ],
        ),
    ]
