# Generated by Django 4.0.4 on 2022-06-15 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_customer_alter_agency_options_alter_guide_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.customer'),
        ),
    ]