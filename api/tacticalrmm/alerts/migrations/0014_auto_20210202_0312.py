# Generated by Django 3.1.4 on 2021-02-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20210123_0149'),
        ('agents', '0027_agent_overdue_dashboard_alert'),
        ('alerts', '0013_auto_20210202_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerttemplate',
            name='excluded_agents',
            field=models.ManyToManyField(blank=True, related_name='alert_exclusions', to='agents.Agent'),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='excluded_clients',
            field=models.ManyToManyField(blank=True, related_name='alert_exclusions', to='clients.Client'),
        ),
        migrations.AlterField(
            model_name='alerttemplate',
            name='excluded_sites',
            field=models.ManyToManyField(blank=True, related_name='alert_exclusions', to='clients.Site'),
        ),
    ]
