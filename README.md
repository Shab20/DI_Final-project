# DI_Final-project

This is a job portal application developed using Django and MySQL. The application allows job seekers to create a profile, search and apply for jobs, and receive notifications about new job openings. Employers can create an account, post job openings, and manage job applications.

Getting Started
To run this application on your local machine, follow these steps:

1. Clone the repository to your local machine.

git clone https://github.com/your-username/job-portal.git

2. Install the required packages by running the following command:

pip install -r requirements.txt

3. Create a MySQL database and update the settings.py file with the database credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'job_portal',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4. Run database migrations by running the following command:

python manage.py migrate

5. Create a superuser to access the admin panel.

python manage.py createsuperuser

6. Start the development server by running the following command:

python manage.py runserver

Features

Job Seekers:
Job seekers can create a profile, search and apply for jobs, and receive notifications about new job openings.
Job seekers can upload their resumes and cover letters and manage their job applications.
Job seekers can save job listings and receive email notifications when a job listing matching their search criteria is posted.

Employers:
Employers can create an account, post job openings, and manage job applications.
Employers can search resumes and cover letters uploaded by job seekers and contact them directly.
Employers can receive email notifications when a job seeker applies for their job listing.

Admin:
The admin panel allows administrators to manage job listings, job applications, job seekers, and employers.
The admin panel provides detailed analytics about the job portal's usage and performance.

Technologies Used
- Django
- MySQL
- HTML/CSS/JavaScript
- Bootstrap
- Python
