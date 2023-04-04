from django.db import models

class Company(models.Model):
    COMPANY_INDUSTRY_CHOICES = (
        ('accounting', 'Accounting'),
        ('advertising', 'Advertising'),
        ('agriculture', 'Agriculture'),
        ('automotive', 'Automotive'),
        ('banking', 'Banking'),
        ('construction', 'Construction'),
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('hospitality', 'Hospitality'),
        ('insurance', 'Insurance'),
        ('manufacturing', 'Manufacturing'),
        ('media', 'Media'),
        ('real-estate', 'Real Estate'),
        ('retail', 'Retail'),
        ('technology', 'Technology'),
        ('telecommunications', 'Telecommunications'),
        ('transportation', 'Transportation'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/')
    website = models.URLField()
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    industry = models.CharField(max_length=20, choices=COMPANY_INDUSTRY_CHOICES)

    def __str__(self):
        return self.name
