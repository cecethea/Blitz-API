# Generated by Django 2.2.12 on 2020-07-23 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0036_automaticemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomaticEmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Sent date')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='automatic_email_logs', to='retirement.AutomaticEmail')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='automatic_email_logs', to='retirement.Reservation')),
            ],
            options={
                'verbose_name': 'Automatic email log',
                'verbose_name_plural': 'Automatic email logs',
            },
        ),
    ]