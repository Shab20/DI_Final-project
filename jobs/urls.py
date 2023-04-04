from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('home', views.home, name='home'),
    path('joblist/', views.job_list, name='joblist'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('companies/', views.company_list, name='companies'),
    path('companydetail/<int:pk>/', views.company_detail, name='companydetail'),
    path('about', views.about, name="about"),
    path('<int:job_id>/apply/', views.apply_job, name='apply'),
    path('job_search/', views.job_search, name='job_search'),
    path('subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]
