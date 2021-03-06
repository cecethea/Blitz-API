# Generated by Django 2.2.12 on 2020-07-23 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0035_auto_20200721_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomaticEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes_delta', models.BigIntegerField(verbose_name='Time delta in minutes')),
                ('time_base', models.CharField(choices=[('before_start', 'Before start'), ('after_end', 'After end')], max_length=253, verbose_name='Time base')),
                ('template_id', models.CharField(max_length=253, verbose_name='Template ID')),
                ('context', models.TextField(default='{}', max_length=253, verbose_name='Context')),
                ('retreat_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='automatic_emails', to='retirement.RetreatType')),
            ],
            options={
                'verbose_name': 'Automatic email',
                'verbose_name_plural': 'Automatic emails',
            },
        ),
    ]
