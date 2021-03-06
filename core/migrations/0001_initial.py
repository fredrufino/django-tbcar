# Generated by Django 3.2.12 on 2022-03-16 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(blank=True, max_length=100, null=True, verbose_name='endereço')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cidade')),
                ('cep', models.CharField(blank=True, max_length=20, null=True, verbose_name='CEP')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_clientes', verbose_name='Foto')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Fabricantes',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30, verbose_name='Modelo')),
                ('ano', models.IntegerField(blank=True, default=2022, null=True, verbose_name='Ano')),
                ('cor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cor')),
                ('placa', models.CharField(max_length=50, verbose_name='Placa')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_veiculos', verbose_name='Foto')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente', verbose_name='Cliente')),
                ('id_fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fabricante', verbose_name='Fabricante')),
            ],
            options={
                'verbose_name_plural': 'Veículos',
            },
        ),
    ]
