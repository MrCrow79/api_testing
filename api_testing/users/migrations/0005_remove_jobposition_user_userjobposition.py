# Generated by Django 5.0.3 on 2024-04-18 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_password_jobposition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobposition',
            name='user',
        ),
        migrations.CreateModel(
            name='UserJobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.jobposition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
