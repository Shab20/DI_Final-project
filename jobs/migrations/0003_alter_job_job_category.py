# Generated by Django 4.1.7 on 2023-03-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_review_company_delete_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_category',
            field=models.CharField(choices=[('accounting', 'Accounting'), ('administrative', 'Administrative'), ('customer-service', 'Customer Service'), ('engineering', 'Engineering'), ('finance', 'Finance'), ('human-resources', 'Human Resources'), ('information-technology', 'Information Technology'), ('marketing', 'Marketing'), ('sales', 'Sales'), ('healthcare', 'Health Care')], max_length=50),
        ),
    ]
