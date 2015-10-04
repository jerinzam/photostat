# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-04 12:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docType', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=60, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('pageNoRange', models.CharField(blank=True, max_length=100, null=True)),
                ('display_doc', models.FileField(blank=True, upload_to='display_docs')),
                ('display', models.BooleanField(default=True)),
                ('is_public', models.BooleanField(default=False)),
                ('is_user_private', models.BooleanField(default=False)),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('uploadedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('edition', models.IntegerField(blank=True, null=True)),
                ('author_names', models.TextField(blank=True, null=True)),
                ('course', models.ManyToManyField(blank=True, to='printo_app.Course')),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printo_app.DocType')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docCount', models.IntegerField(default=0)),
                ('employee', models.ManyToManyField(blank=True, null=True, related_name='org_employee', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='org_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopName', models.CharField(max_length=100)),
                ('orderCount', models.IntegerField(default=0)),
                ('createdOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop_employee', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_owner', to='printo_app.Organization')),
                ('services', models.ManyToManyField(blank=True, to='printo_app.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='documents')),
                ('userType', models.IntegerField(choices=[(1, 'owner'), (2, 'employee'), (3, 'Private person')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_owner', to='printo_app.Organization'),
        ),
        migrations.AddField(
            model_name='document',
            name='private_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='printo_app.Publisher'),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(blank=True, to='printo_app.Tag'),
        ),
        migrations.AddField(
            model_name='document',
            name='topic',
            field=models.ManyToManyField(blank=True, to='printo_app.Topic'),
        ),
        migrations.AddField(
            model_name='document',
            name='university',
            field=models.ManyToManyField(blank=True, to='printo_app.University'),
        ),
        migrations.AddField(
            model_name='college',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='printo_app.University'),
        ),
        migrations.AddField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printo_app.Course'),
        ),
    ]