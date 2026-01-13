from django.urls import path
from . import views

urlpatterns = [ 
    path('api/homepage/', views.api_homepage, name='api_homepage'),
    
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # HeroInfo CRUD
    path('hero/', views.hero_list, name='hero_list'),
    path('hero/create/', views.hero_create, name='hero_create'),
    path('hero/<int:pk>/update/', views.hero_update, name='hero_update'),
    path('hero/<int:pk>/delete/', views.hero_delete, name='hero_delete'),
    
    # EducationAndTraining CRUD
    path('education/', views.education_list, name='education_list'),
    path('education/create/', views.education_create, name='education_create'),
    path('education/<int:pk>/update/', views.education_update, name='education_update'),
    path('education/<int:pk>/delete/', views.education_delete, name='education_delete'),
    
    # MyProject CRUD
    path('project/', views.project_list, name='project_list'),
    path('project/create/', views.project_create, name='project_create'),
    path('project/<int:pk>/update/', views.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # SkillCategory CRUD
    path('skill-category/', views.skill_category_list, name='skill_category_list'),
    path('skill-category/create/', views.skill_category_create, name='skill_category_create'),
    path('skill-category/<int:pk>/update/', views.skill_category_update, name='skill_category_update'),
    path('skill-category/<int:pk>/delete/', views.skill_category_delete, name='skill_category_delete'),
    
    # MySkill CRUD
    path('skill-category/<int:category_id>/skills/', views.skill_list, name='skill_list'),
    path('skill-category/<int:category_id>/skills/create/', views.skill_create, name='skill_create'),
    path('skill-category/<int:category_id>/skills/<int:pk>/update/', views.skill_update, name='skill_update'),
    path('skill-category/<int:category_id>/skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    
    # Footer CRUD
    path('footer/', views.footer_list, name='footer_list'),
    path('footer/create/', views.footer_create, name='footer_create'),
    path('footer/<int:pk>/update/', views.footer_update, name='footer_update'),
    path('footer/<int:pk>/delete/', views.footer_delete, name='footer_delete'),
    
    # SocialIcon CRUD
    path('social-icon/', views.social_icon_list, name='social_icon_list'),
    path('social-icon/create/', views.social_icon_create, name='social_icon_create'),
    path('social-icon/<int:pk>/update/', views.social_icon_update, name='social_icon_update'),
    path('social-icon/<int:pk>/delete/', views.social_icon_delete, name='social_icon_delete'),
    
    # Contact Submissions
    path('contact-submissions/', views.contact_submission_list, name='contact_submission_list'),
    path('contact-submissions/<int:pk>/', views.contact_submission_detail, name='contact_submission_detail'),
    path('contact-submissions/<int:pk>/delete/', views.contact_submission_delete, name='contact_submission_delete'),
    
    # Mailjet Settings
    path('mailjet-settings/', views.mailjet_settings, name='mailjet_settings'),
    
    # Website Settings
    path('website-settings/', views.website_settings, name='website_settings'),
    
    # API Endpoints
    path('api/contact/', views.api_contact_submit, name='api_contact_submit'),
]