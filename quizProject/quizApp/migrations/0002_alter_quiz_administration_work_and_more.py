# Generated by Django 4.2.2 on 2023-06-27 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='administration_work',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='computer_work',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user_email',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user_name',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user_nick',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user_surname',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user_visit',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='why_filial',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='why_we',
            field=models.TextField(null=True),
        ),
    ]
