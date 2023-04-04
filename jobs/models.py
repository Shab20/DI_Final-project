from django.db import models
from company.models import Company

# Job Model:
class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    )
    JOB_CATEGORY_CHOICES = (
        ('accounting', 'Accounting'),
        ('administrative', 'Administrative'),
        ('customer-service', 'Customer Service'),
        ('engineering', 'Engineering'),
        ('finance', 'Finance'),
        ('human-resources', 'Human Resources'),
        ('information-technology', 'Information Technology'),
        ('marketing', 'Marketing'),
        ('sales', 'Sales'),
        ('healthcare', 'Health Care'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    job_category = models.CharField(max_length=50, choices=JOB_CATEGORY_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    requirements = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.title


# Application Model: This model would represent a job application submitted by a user. Some example fields you could include in this model are:
class JobApplication(models.Model):
    APPLICATION_STATUS_CHOICES = (
        ('new', 'New'),
        ('under_review', 'Under review'),
        ('rejected', 'Rejected'),
        ('shortlisted', 'Shortlisted'),
        ('hired', 'Hired'),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover = models.FileField(upload_to='cover/', null=True)
    skills = models.CharField(max_length=255, null=True)
    application_status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES)

    def __str__(self):
        return f"{self.name} applied for {self.job.title}"

# Skill Model: This model would represent a skill that a job requires or a user possesses. Some example fields you could include in this model are:
class Skill(models.Model):
    SKILL_CATEGORY_CHOICES = (
        ('technical', 'Technical'),
        ('soft', 'Soft'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=SKILL_CATEGORY_CHOICES)

    def __str__(self):
        return self.name

# Location Model: This model would represent a geographic location. Some example fields you could include in this model are:
class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

# Review Model: This model would represent a review of a company or a job. Some example fields you could include in this model are:
class Review(models.Model):
    reviewer_name = models.CharField(max_length=255)
    reviewer_email = models.EmailField()
    reviewer_rating = models.IntegerField()
    review_content = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.reviewer_name} reviewed {self.company or self.job}"
    
class EmailSubscription(models.Model):
    text = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
