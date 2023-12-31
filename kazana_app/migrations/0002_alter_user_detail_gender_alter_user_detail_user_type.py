# Generated by Django 4.2.2 on 2023-06-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kazana_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='male', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_type',
            field=models.CharField(blank=True, choices=[('', 'Select One'), ('company', 'Company'), ('user', 'User')], max_length=12, null=True),
        ),
    ]
