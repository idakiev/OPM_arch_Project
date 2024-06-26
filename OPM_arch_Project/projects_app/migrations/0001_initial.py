# Generated by Django 4.0 on 2024-03-17 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts_app', '0003_alter_appuser_groups_alter_appuser_user_permissions'),
        ('clients_app', '0003_rename_company_client_alter_client_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('project_type', models.CharField(choices=[('SINGLE_HOUSE', 'Single House'), ('ROW_HOUSES', 'Row Houses'), ('MULTI_FAMILY_SMALL', 'Small Multi-Family building'), ('MULTI_FAMILY_MEDIUM', 'Medium Multi-Family building'), ('MULTI_FAMILY_BIG', 'Big Multi-Family building'), ('OFFICE_BUILDING', 'Office building'), ('PUBLIC_BUILDING', 'Public building'), ('RENOVATION', 'Renovation'), ('OTHER', 'Other')], max_length=19)),
                ('project_phase', models.CharField(choices=[('PRE_DESIGN', 'Pre-design'), ('DESIGN', 'Design'), ('PERMISSION', 'Permission'), ('EXECUTIVE', 'Executive'), ('OTHER', 'Other')], max_length=10)),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='municipality', chained_model_field='municipality', on_delete=django.db.models.deletion.DO_NOTHING, to='clients_app.city')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients_app.client')),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients_app.municipality')),
                ('project_manager', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts_app.appuser')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('base_project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='projects_app.baseproject')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed')], max_length=9, null=True)),
                ('progress', models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], max_length=11, null=True)),
                ('employees', models.ManyToManyField(blank=True, default=None, limit_choices_to={'is_staff': True}, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
