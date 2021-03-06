# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-09 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='用户名')),
                ('email', models.EmailField(max_length=255, verbose_name='邮箱')),
                ('url', models.URLField(blank=True, verbose_name='个人网站')),
                ('text', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comm_artc', to='blog.Article')),
            ],
        ),
    ]
