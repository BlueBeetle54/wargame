# Generated by Django 3.0.5 on 2020-08-03 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prob', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='probAcessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.GenericIPAddressField(null=True, protocol='IPv4')),
                ('userAgent', models.CharField(max_length=500)),
                ('onTime', models.DateTimeField(auto_now_add=True)),
                ('acessProb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prob.prob')),
                ('acessUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='loginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.GenericIPAddressField(null=True, protocol='IPv4')),
                ('userAgent', models.CharField(max_length=500)),
                ('onTime', models.DateTimeField(auto_now_add=True)),
                ('loginUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='downloadLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.GenericIPAddressField(null=True, protocol='IPv4')),
                ('userAgent', models.CharField(max_length=500)),
                ('onTime', models.DateTimeField(auto_now_add=True)),
                ('downloadProb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prob.prob')),
                ('downloadUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='authLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.GenericIPAddressField(null=True, protocol='IPv4')),
                ('userAgent', models.CharField(max_length=500)),
                ('is_solved', models.BooleanField(default=False)),
                ('onTime', models.DateTimeField(auto_now_add=True)),
                ('authProb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prob.prob')),
                ('authUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]