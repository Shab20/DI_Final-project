from django import forms
from .models import JobApplication

class JobApplicationForm(forms.Form):
    APPLICATION_STATUS_CHOICES = (
        ('new', 'New'),
        ('under_review', 'Under review'),
        ('rejected', 'Rejected'),
        ('shortlisted', 'Shortlisted'),
        ('hired', 'Hired'),
    )

    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    resume = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), required=True)
    cover_letter = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), required=True)
    application_status = forms.ChoiceField(choices=APPLICATION_STATUS_CHOICES, required=True)

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume.content_type not in ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
            raise forms.ValidationError("File type not supported.")
        return resume
