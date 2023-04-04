from django.shortcuts import render
from .models import Job, Company, JobApplication , EmailSubscription
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest



def home(request):
    return render(request, 'index.html')

def job_list(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'job_listings.html', context)


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {
        'job': job,
    }
    return render(request, 'job_details.html', context)

def company_list(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'companies.html', context)


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company_detail.html', {'company': company})


def about(request):
    return render(request, 'about.html')


def job_search(request):
    jobs = Job.objects.all()
    
    # Get user input
    title = request.GET.get('title')
    location = request.GET.get('location')
    job_type = request.GET.get('job_type')
    job_category = request.GET.get('job_category')

    # Filter jobs based on user input
    if title:
        jobs = jobs.filter(Q(title__icontains=title))
    if location:
        jobs = jobs.filter(Q(location__icontains=location))
    if job_type:
        jobs = jobs.filter(Q(job_type=job_type))
    if job_category:
        jobs = jobs.filter(Q(job_category=job_category))
    
    # Render the search results
    return render(request, 'job_search.html', {'jobs': jobs})


def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        # retrieve form data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        resume = request.FILES['resume']
        cover = request.FILES['cover']
        skills = request.POST['skills']
        # create a new JobApplication instance
        job_application = JobApplication(job=job, name=name, email=email, phone=phone, resume=resume, cover=cover, skills=skills, application_status='new')
        
        # save the JobApplication instance to the database
        job_application.save()

        # Debugging: print the data to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Resume: {resume}")
        
        # render a thank you page
        return render(request, 'thank_you.html')
        
    # if the request method is GET, render the form
    context = {'job': job}
    return render(request, 'thank_you.html', context)

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        text = request.POST.get('text', 'Subscription request')
        if email:
            subscription = EmailSubscription.objects.create(email=email, text=text)
            # Send email to ORM here
            return render( request, 'thankyou_notifications.html')
    return HttpResponseBadRequest('Invalid request')