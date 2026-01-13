from user.models import *
from user.forms import *
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.conf import settings
from datetime import datetime, timedelta
import json

def admin_required(user):
    return user.is_authenticated and user.is_staff

# Old template-based view removed - using API endpoint instead

@require_http_methods(["GET", "OPTIONS"])
def api_homepage(request):
    """API endpoint to return homepage data as JSON"""
    # CORS is now handled by django-cors-headers middleware
    
    try:
        hero = HeroInfo.objects.first()
        website = Website.objects.first()
        educations = EducationAndTraining.objects.all().order_by('-id')
        skill_categories = SkillCategory.objects.all()
        projects = MyProject.objects.all().order_by('-id')
        footer = Footer.objects.first()
        social_icons = SocialIcon.objects.all()
        
        # Serialize hero data
        hero_data = None
        if hero:
            hero_data = {
                'title': hero.title,
                'availability': hero.get_availability_display(),
                'full_name': hero.full_name,
                'short_intro': hero.short_intro,
                'company_name': hero.company_name,
                'hireme_link': hero.hireme_link or '',
                'download_cv_button': hero.download_cv_button or '',
                'long_biography': hero.long_biography,
            }
        
        # Serialize website data
        website_data = None
        if website:
            website_data = {
                'name': website.name,
                'favicon': website.favicon.url if website.favicon else None,
                'profile_picture': website.profile_picture.url if website.profile_picture else None,
            }
        
        # Serialize educations
        educations_data = []
        for edu in educations:
            educations_data.append({
                'training_type': edu.get_training_type_display(),
                'institution_name': edu.institution_name,
                'subject': edu.subject,
                'cgpa': str(edu.cgpa) if edu.cgpa else None,
                'year': edu.year,
            })
        
        # Serialize skill categories with skills
        skill_categories_data = []
        for category in skill_categories:
            skills = category.skills.all()
            skills_data = []
            for skill in skills:
                skills_data.append({
                    'name': skill.name,
                    'icon': skill.icon.url if skill.icon else None,
                })
            skill_categories_data.append({
                'name': category.name,
                'skills': skills_data,
            })
        
        # Serialize projects
        projects_data = []
        for project in projects:
            projects_data.append({
                'name': project.name,
                'difficulty_level': project.get_difficulty_level_display(),
                'project_type': project.project_type,
                'logo': project.logo.url if project.logo else None,
                'status': project.get_status_display(),
                'project_link': project.project_link or '',
                'start_date': project.start_date.strftime('%Y-%m-%d') if project.start_date else None,
            })
        
        # Serialize footer
        footer_data = None
        if footer:
            footer_data = {
                'title': footer.title,
                'small_talk': footer.small_talk,
                'hire_me_link': footer.hire_me_link,
                'copyright_text': footer.copyright_text,
            }
        
        # Serialize social icons
        social_icons_data = []
        for icon in social_icons:
            social_icons_data.append({
                'icon': icon.icon.url if icon.icon else None,
                'icon_link': icon.icon_link,
            })
        
        response = JsonResponse({
            'hero': hero_data,
            'website': website_data,
            'educations': educations_data,
            'skill_categories': skill_categories_data,
            'projects': projects_data,
            'footer': footer_data,
            'social_icons': social_icons_data,
        })
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Old template-based contact view removed - frontend handles contact form

# Contact Form API
@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def api_contact_submit(request):
    """API endpoint to handle contact form submission"""
    # CORS is now handled by django-cors-headers middleware
    
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        # Validation
        if not name or not email or not message:
            return JsonResponse({'error': 'All fields are required'}, status=400)
        
        # Save to database
        submission = ContactSubmission.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # Send email via Mailjet
        mailjet_settings = MailjetSettings.load()
        if mailjet_settings.api_key and mailjet_settings.api_secret:
            try:
                from mailjet_rest import Client
                
                mailjet = Client(auth=(mailjet_settings.api_key, mailjet_settings.api_secret), version='v3.1')
                
                # Format message with line breaks
                formatted_message = message.replace(chr(10), "<br>")
                formatted_message_text = message
                
                # Beautiful HTML template for admin notification (Frontend UI Style)
                admin_html_template = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #F0F0F0;
        }}
        .container {{
            background: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #DFF7EC;
        }}
        .header h1 {{
            color: #059855;
            margin: 0;
            font-size: 28px;
            font-weight: 700;
        }}
        .header p {{
            color: #6D6D6D;
            margin: 10px 0 0 0;
            font-size: 14px;
        }}
        .info-section {{
            background-color: #DFF7EC;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }}
        .info-row {{
            display: flex;
            margin-bottom: 15px;
            align-items: flex-start;
            padding: 10px 0;
            border-bottom: 1px solid rgba(5, 152, 85, 0.1);
        }}
        .info-row:last-child {{
            margin-bottom: 0;
            border-bottom: none;
        }}
        .info-label {{
            font-weight: 600;
            color: #059855;
            min-width: 100px;
            font-size: 14px;
        }}
        .info-value {{
            color: #333;
            flex: 1;
            font-size: 14px;
        }}
        .info-value a {{
            color: #059855;
            text-decoration: none;
            font-weight: 600;
        }}
        .info-value a:hover {{
            text-decoration: underline;
        }}
        .message-section {{
            background-color: #F7F7F7;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }}
        .message-section h3 {{
            color: #059855;
            margin: 0 0 15px 0;
            font-size: 18px;
            font-weight: 700;
        }}
        .message-box {{
            background: #ffffff;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 20px;
            margin-top: 10px;
        }}
        .message-box p {{
            margin: 0;
            color: #333;
            line-height: 1.8;
            white-space: pre-wrap;
        }}
        .button-container {{
            text-align: center;
            margin: 30px 0;
        }}
        .button {{
            display: inline-block;
            background: #000000;
            color: #ffffff;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease-in-out;
        }}
        .button:hover {{
            background: #059855;
            transform: scale(1.05);
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 2px solid #DFF7EC;
            color: #6D6D6D;
            font-size: 12px;
        }}
        .status-badge {{
            display: inline-block;
            background-color: #DFF7EC;
            color: #059855;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: 600;
            font-size: 14px;
            margin-left: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📧 New Contact Form Submission</h1>
            <p>You have received a new message from your portfolio website</p>
        </div>
        
        <div class="info-section">
            <div class="info-row">
                <span class="info-label">👤 Name:</span>
                <span class="info-value"><strong>{name}</strong></span>
            </div>
            <div class="info-row">
                <span class="info-label">📧 Email:</span>
                <span class="info-value"><a href="mailto:{email}">{email}</a></span>
            </div>
            <div class="info-row">
                <span class="info-label">📅 Date:</span>
                <span class="info-value">{submission.submitted_at.strftime("%B %d, %Y at %I:%M %p")}</span>
            </div>
        </div>
        
        <div class="message-section">
            <h3>💬 Message:</h3>
            <div class="message-box">
                <p>{formatted_message}</p>
            </div>
        </div>
        
        <div class="button-container">
            <a href="https://admin.shaznuz.com/contact-submissions/" class="button">View in Admin Panel</a>
        </div>
        
        <div class="footer">
            <p>This is an automated notification from your portfolio contact form.</p>
        </div>
    </div>
</body>
</html>
                '''
                
                # Beautiful HTML template for sender confirmation
                sender_html_template = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            border-radius: 12px;
            padding: 2px;
            margin-bottom: 20px;
        }}
        .content {{
            background: #ffffff;
            border-radius: 10px;
            padding: 30px;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #f0f0f0;
        }}
        .header h1 {{
            color: #11998e;
            margin: 0;
            font-size: 28px;
            font-weight: 700;
        }}
        .header p {{
            color: #666;
            margin: 10px 0 0 0;
            font-size: 14px;
        }}
        .success-box {{
            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
            border-left: 4px solid #28a745;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            text-align: center;
        }}
        .success-box h2 {{
            color: #155724;
            margin: 0 0 10px 0;
            font-size: 22px;
        }}
        .success-box p {{
            color: #155724;
            margin: 0;
            font-size: 14px;
        }}
        .message-preview {{
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        .message-preview h3 {{
            color: #11998e;
            margin: 0 0 15px 0;
            font-size: 16px;
            font-weight: 600;
        }}
        .message-preview p {{
            margin: 0;
            color: #495057;
            line-height: 1.8;
            white-space: pre-wrap;
        }}
        .info-box {{
            background: #f8f9fa;
            border-left: 4px solid #11998e;
            padding: 15px;
            margin: 20px 0;
            border-radius: 8px;
        }}
        .info-box p {{
            margin: 5px 0;
            color: #666;
            font-size: 14px;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 2px solid #f0f0f0;
            color: #999;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
            <div class="header">
                <h1>✅ Message Received!</h1>
                <p>Thank you for contacting us</p>
            </div>
            
            <div class="success-box">
                <h2>🎉 Your message has been sent successfully!</h2>
                <p>We have received your message and will get back to you soon.</p>
            </div>
            
            <div class="message-preview">
                <h3>📝 Your Message:</h3>
                <p>{formatted_message}</p>
            </div>
            
            <div class="info-box">
                <p><strong>📅 Submitted:</strong> {submission.submitted_at.strftime("%B %d, %Y at %I:%M %p")}</p>
                <p><strong>📧 From:</strong> {email}</p>
            </div>
            
            <div class="footer">
                <p>This is an automated confirmation email. Please do not reply to this message.</p>
                <p>If you have any questions, feel free to contact us again.</p>
            </div>
        </div>
    </div>
</body>
</html>
                '''
                
                # Prepare email messages - Only one email to admin, one to sender
                messages = []
                
                # Email to admin (only notification)
                messages.append({
                    'From': {
                        'Email': mailjet_settings.sender_email,
                        'Name': mailjet_settings.sender_name
                    },
                    'To': [{
                        'Email': mailjet_settings.admin_email,
                        'Name': 'Admin'
                    }],
                    'Subject': f'📧 New Contact Form Submission from {name}',
                    'TextPart': f'''New contact form submission received:

Name: {name}
Email: {email}
Date: {submission.submitted_at.strftime("%Y-%m-%d %H:%M:%S")}

Message:
{formatted_message_text}

---
View all submissions in admin panel: https://admin.shaznuz.com/contact-submissions/
                    ''',
                    'HTMLPart': admin_html_template
                })
                
                # Confirmation email to sender (separate call to avoid confusion)
                sender_email_data = {
                    'Messages': [{
                        'From': {
                            'Email': mailjet_settings.sender_email,
                            'Name': mailjet_settings.sender_name
                        },
                        'To': [{
                            'Email': email,
                            'Name': name
                        }],
                        'Subject': f'✅ Thank you for contacting us, {name}!',
                        'TextPart': f'''Thank you for contacting us!

Your message has been received successfully. We will get back to you soon.

Your Message:
{formatted_message_text}

Submitted: {submission.submitted_at.strftime("%B %d, %Y at %I:%M %p")}

This is an automated confirmation email. Please do not reply to this message.
                        ''',
                        'HTMLPart': sender_html_template
                    }]
                }
                
                # Send admin notification email
                email_data = {
                    'Messages': messages
                }
                
                result = mailjet.send.create(data=email_data)
                if result.status_code == 200:
                    submission.save()
                    # Send confirmation email to sender separately
                    try:
                        mailjet.send.create(data=sender_email_data)
                    except Exception as e:
                        print(f"Error sending confirmation email: {str(e)}")
                else:
                    # Log error but don't fail the submission
                    print(f"Mailjet error: {result.status_code}")
            except Exception as e:
                # Log error but don't fail the submission
                print(f"Error sending email: {str(e)}")
        
        return JsonResponse({
            'success': True,
            'message': 'Your message has been sent successfully!'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Dashboard
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def dashboard(request):
    # Get counts for statistics
    hero_count = HeroInfo.objects.count()
    education_count = EducationAndTraining.objects.count()
    project_count = MyProject.objects.count()
    skill_category_count = SkillCategory.objects.count()
    footer_count = Footer.objects.count()
    social_icon_count = SocialIcon.objects.count()
    
    context = {
        'hero_count': hero_count,
        'education_count': education_count,
        'project_count': project_count,
        'skill_category_count': skill_category_count,
        'footer_count': footer_count,
        'social_icon_count': social_icon_count,
    }
    return render(request, 'dashboard.html', context)

# HeroInfo CRUD
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def hero_list(request):
    heroes = HeroInfo.objects.all()
    return render(request, 'hero_list.html', {'heroes': heroes})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def hero_create(request):
    website, _ = Website.objects.get_or_create(pk=1)
    if request.method == 'POST':
        form = HeroInfoForm(request.POST)
        website_form = WebsiteForm(request.POST, request.FILES, instance=website)
        if form.is_valid() and website_form.is_valid():
            form.save()
            website_form.save()
            messages.success(request, 'Hero info created successfully!')
            return redirect('hero_list')
    else:
        form = HeroInfoForm()
        website_form = WebsiteForm(instance=website)
    return render(request, 'hero_form.html', {'form': form, 'website_form': website_form, 'title': 'Create Hero Info', 'website': website})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def hero_update(request, pk):
    hero = get_object_or_404(HeroInfo, pk=pk)
    website, _ = Website.objects.get_or_create(pk=1)
    if request.method == 'POST':
        form = HeroInfoForm(request.POST, instance=hero)
        website_form = WebsiteForm(request.POST, request.FILES, instance=website)
        if form.is_valid() and website_form.is_valid():
            form.save()
            website_form.save()
            messages.success(request, 'Hero info updated successfully!')
            return redirect('hero_list')
    else:
        form = HeroInfoForm(instance=hero)
        website_form = WebsiteForm(instance=website)
    return render(request, 'hero_form.html', {'form': form, 'website_form': website_form, 'title': 'Update Hero Info', 'hero': hero, 'website': website})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def hero_delete(request, pk):
    hero = get_object_or_404(HeroInfo, pk=pk)
    if request.method == 'POST':
        hero.delete()
        messages.success(request, 'Hero info deleted successfully!')
        return redirect('hero_list')
    return render(request, 'hero_confirm_delete.html', {'hero': hero})

# EducationAndTraining CRUD
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def education_list(request):
    educations = EducationAndTraining.objects.all().order_by('-year')
    return render(request, 'education_list.html', {'educations': educations})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def education_create(request):
    if request.method == 'POST':
        form = EducationAndTrainingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education record created successfully!')
            return redirect('education_list')
    else:
        form = EducationAndTrainingForm()
    return render(request, 'education_form.html', {'form': form, 'title': 'Create Education'})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def education_update(request, pk):
    education = get_object_or_404(EducationAndTraining, pk=pk)
    if request.method == 'POST':
        form = EducationAndTrainingForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education record updated successfully!')
            return redirect('education_list')
    else:
        form = EducationAndTrainingForm(instance=education)
    return render(request, 'education_form.html', {'form': form, 'title': 'Update Education', 'education': education})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def education_delete(request, pk):
    education = get_object_or_404(EducationAndTraining, pk=pk)
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education record deleted successfully!')
        return redirect('education_list')
    return render(request, 'education_confirm_delete.html', {'education': education})

# MyProject CRUD
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def project_list(request):
    projects = MyProject.objects.all().order_by('-start_date')
    return render(request, 'project_list.html', {'projects': projects})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def project_create(request):
    if request.method == 'POST':
        form = MyProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_list')
    else:
        form = MyProjectForm()
    return render(request, 'project_form.html', {'form': form, 'title': 'Create Project'})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def project_update(request, pk):
    project = get_object_or_404(MyProject, pk=pk)
    if request.method == 'POST':
        form = MyProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_list')
    else:
        form = MyProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form, 'title': 'Update Project', 'project': project})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def project_delete(request, pk):
    project = get_object_or_404(MyProject, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('project_list')
    return render(request, 'project_confirm_delete.html', {'project': project})

# SkillCategory CRUD
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def skill_category_list(request):
    categories = SkillCategory.objects.all()
    return render(request, 'skill_category_list.html', {'categories': categories})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def skill_category_create(request):
    if request.method == 'POST':
        form = SkillCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill category created successfully!')
            return redirect('skill_category_list')
    else:
        form = SkillCategoryForm()
    return render(request, 'skill_category_form.html', {'form': form, 'title': 'Create Skill Category'})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def skill_category_update(request, pk):
    category = get_object_or_404(SkillCategory, pk=pk)
    if request.method == 'POST':
        form = SkillCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill category updated successfully!')
            return redirect('skill_category_list')
    else:
        form = SkillCategoryForm(instance=category)
    return render(request, 'skill_category_form.html', {'form': form, 'title': 'Update Skill Category', 'category': category})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def skill_category_delete(request, pk):
    category = get_object_or_404(SkillCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Skill category deleted successfully!')
        return redirect('skill_category_list')
    return render(request, 'skill_category_confirm_delete.html', {'category': category})

# MySkill CRUD
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def skill_list(request, category_id):
    category = get_object_or_404(SkillCategory, pk=category_id)
    skills = MySkill.objects.filter(category=category)
    return render(request, 'skill_list.html', {'skills': skills, 'category': category})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def skill_create(request, category_id):
    category = get_object_or_404(SkillCategory, pk=category_id)
    if request.method == 'POST':
        form = MySkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.category = category
            skill.save()
            messages.success(request, 'Skill created successfully!')
            return redirect('skill_list', category_id=category_id)
    else:
        form = MySkillForm()
    return render(request, 'skill_form.html', {'form': form, 'title': 'Create Skill', 'category': category})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def skill_update(request, category_id, pk):
    category = get_object_or_404(SkillCategory, pk=category_id)
    skill = get_object_or_404(MySkill, pk=pk, category=category)
    if request.method == 'POST':
        form = MySkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('skill_list', category_id=category_id)
    else:
        form = MySkillForm(instance=skill)
    return render(request, 'skill_form.html', {'form': form, 'title': 'Update Skill', 'category': category, 'skill': skill})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def skill_delete(request, category_id, pk):
    category = get_object_or_404(SkillCategory, pk=category_id)
    skill = get_object_or_404(MySkill, pk=pk, category=category)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('skill_list', category_id=category_id)
    return render(request, 'skill_confirm_delete.html', {'skill': skill, 'category': category})

# Footer CRUD
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def footer_list(request):
    footers = Footer.objects.all()
    return render(request, 'footer_list.html', {'footers': footers})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def footer_create(request):
    if request.method == 'POST':
        form = FooterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Footer created successfully!')
            return redirect('footer_list')
    else:
        form = FooterForm()
    return render(request, 'footer_form.html', {'form': form, 'title': 'Create Footer'})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def footer_update(request, pk):
    footer = get_object_or_404(Footer, pk=pk)
    if request.method == 'POST':
        form = FooterForm(request.POST, instance=footer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Footer updated successfully!')
            return redirect('footer_list')
    else:
        form = FooterForm(instance=footer)
    return render(request, 'footer_form.html', {'form': form, 'title': 'Update Footer', 'footer': footer})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def footer_delete(request, pk):
    footer = get_object_or_404(Footer, pk=pk)
    if request.method == 'POST':
        footer.delete()
        messages.success(request, 'Footer deleted successfully!')
        return redirect('footer_list')
    return render(request, 'footer_confirm_delete.html', {'footer': footer})

# SocialIcon CRUD
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def social_icon_list(request):
    icons = SocialIcon.objects.all()
    return render(request, 'social_icon_list.html', {'icons': icons})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def social_icon_create(request):
    if request.method == 'POST':
        form = SocialIconForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social icon created successfully!')
            return redirect('social_icon_list')
    else:
        form = SocialIconForm()
    return render(request, 'social_icon_form.html', {'form': form, 'title': 'Create Social Icon'})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def social_icon_update(request, pk):
    icon = get_object_or_404(SocialIcon, pk=pk)
    if request.method == 'POST':
        form = SocialIconForm(request.POST, request.FILES, instance=icon)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social icon updated successfully!')
            return redirect('social_icon_list')
    else:
        form = SocialIconForm(instance=icon)
    return render(request, 'social_icon_form.html', {'form': form, 'title': 'Update Social Icon', 'icon': icon})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def social_icon_delete(request, pk):
    icon = get_object_or_404(SocialIcon, pk=pk)
    if request.method == 'POST':
        icon.delete()
        messages.success(request, 'Social icon deleted successfully!')
        return redirect('social_icon_list')
    return render(request, 'social_icon_confirm_delete.html', {'icon': icon})

# Contact Submissions CRUD
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def contact_submission_list(request):
    filter_type = request.GET.get('filter', 'all')
    today = timezone.now().date()
    week_start = today - timedelta(days=today.weekday())
    
    if filter_type == 'today':
        submissions = ContactSubmission.objects.filter(submitted_at__date=today)
    elif filter_type == 'week':
        submissions = ContactSubmission.objects.filter(submitted_at__date__gte=week_start)
    elif filter_type == 'unread':
        submissions = ContactSubmission.objects.filter(is_read=False)
    else:
        submissions = ContactSubmission.objects.all()
    
    # Statistics
    total_count = ContactSubmission.objects.count()
    today_count = ContactSubmission.objects.filter(submitted_at__date=today).count()
    week_count = ContactSubmission.objects.filter(submitted_at__date__gte=week_start).count()
    unread_count = ContactSubmission.objects.filter(is_read=False).count()
    
    context = {
        'submissions': submissions,
        'filter_type': filter_type,
        'total_count': total_count,
        'today_count': today_count,
        'week_count': week_count,
        'unread_count': unread_count,
    }
    return render(request, 'contact_submission_list.html', context)

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def contact_submission_detail(request, pk):
    submission = get_object_or_404(ContactSubmission, pk=pk)
    if not submission.is_read:
        submission.is_read = True
        submission.save()
    return render(request, 'contact_submission_detail.html', {'submission': submission})

@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def contact_submission_delete(request, pk):
    submission = get_object_or_404(ContactSubmission, pk=pk)
    if request.method == 'POST':
        submission.delete()
        messages.success(request, 'Submission deleted successfully!')
        return redirect('contact_submission_list')
    return render(request, 'contact_submission_confirm_delete.html', {'submission': submission})

# Mailjet Settings
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def mailjet_settings(request):
    settings = MailjetSettings.load()
    if request.method == 'POST':
        form = MailjetSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mailjet settings updated successfully!')
            return redirect('mailjet_settings')
    else:
        form = MailjetSettingsForm(instance=settings)
    return render(request, 'mailjet_settings.html', {'form': form, 'settings': settings})

# Website Settings
@login_required(login_url='/admin/login/')
@user_passes_test(admin_required, login_url='/admin/login/')
def website_settings(request):
    website, created = Website.objects.get_or_create(pk=1)
    if request.method == 'POST':
        form = WebsiteForm(request.POST, request.FILES, instance=website)
        if form.is_valid():
            form.save()
            messages.success(request, 'Website settings updated successfully!')
            return redirect('website_settings')
    else:
        form = WebsiteForm(instance=website)
    return render(request, 'website_settings.html', {'form': form, 'website': website})