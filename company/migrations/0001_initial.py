# Generated by Django 4.1.7 on 2023-03-26 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='company_logos/')),
                ('website', models.URLField()),
                ('location', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=20)),
                ('industry', models.CharField(choices=[('accounting', 'Accounting'), ('advertising', 'Advertising'), ('agriculture', 'Agriculture'), ('automotive', 'Automotive'), ('banking', 'Banking'), ('construction', 'Construction'), ('education', 'Education'), ('entertainment', 'Entertainment'), ('finance', 'Finance'), ('healthcare', 'Healthcare'), ('hospitality', 'Hospitality'), ('insurance', 'Insurance'), ('manufacturing', 'Manufacturing'), ('media', 'Media'), ('real-estate', 'Real Estate'), ('retail', 'Retail'), ('technology', 'Technology'), ('telecommunications', 'Telecommunications'), ('transportation', 'Transportation')], max_length=20)),
            ],
        ),
    ]