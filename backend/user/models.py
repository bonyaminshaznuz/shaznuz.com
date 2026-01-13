from django.db import models
from django.core.validators import FileExtensionValidator

class Website(models.Model):
    name = models.CharField(max_length=100)
    favicon = models.FileField(upload_to='static/icon/', null=True, blank=True,help_text='Upload an SVG file')
    profile_picture = models.ImageField(upload_to='static/image/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class HeroInfo(models.Model):
    AVAILABILITY_CHOICES = [
        ('available', 'Available Now'),
        ('on_holiday', 'On Holiday'),
    ]

    title = models.CharField(max_length=100)  
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='available', 
    )
    full_name = models.CharField(max_length=200) 
    short_intro = models.TextField(max_length=500)  
    company_name = models.CharField(max_length=200) 
    hireme_link = models.URLField(max_length=500,null=True, blank=True)  
    download_cv_button = models.URLField(max_length=500,null=True, blank=True)  
    long_biography = models.TextField() 

    def __str__(self):
        return self.full_name


class EducationAndTraining(models.Model):
    TRAINING_TYPES = [
        ('trining', 'Trining'),
        ('diploma', 'Diploma'),
        ('certificate', 'Certificate'),
        ('ssc', 'Ssc'),
        ('hsc', 'Hsc'),
        ('bsc', 'Bsc'),
    ]
    
    training_type = models.CharField(max_length=50, choices=TRAINING_TYPES)
    institution_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    year = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.training_type} at {self.institution_name} ({self.year})"

class SkillCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class MySkill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='static/icon/', help_text='Upload an SVG file')

    def __str__(self):
        return self.name


class MyProject(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    name = models.CharField(max_length=255)
    difficulty_level = models.CharField(
        max_length=6,
        choices=DIFFICULTY_CHOICES,
        default='medium'
    )
    project_type = models.CharField(max_length=100) 
    logo = models.ImageField(upload_to='static/image/', null=True, blank=True)
    status = models.CharField(max_length=11,choices=STATUS_CHOICES,default='in_progress')
    project_link = models.URLField(max_length=200, null=True, blank=True)
    start_date = models.DateField()
    
    def __str__(self):
        return self.name

class Footer(models.Model):
    title = models.CharField(max_length=255)
    small_talk = models.TextField()
    hire_me_link = models.URLField(max_length=200)
    copyright_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class SocialIcon(models.Model):
    icon = models.FileField(upload_to='static/icon/', validators=[FileExtensionValidator(allowed_extensions=['svg'])])
    icon_link = models.URLField()

    def __str__(self):
        return self.icon_link

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'
    
    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

class MailjetSettings(models.Model):
    api_key = models.CharField(max_length=255, help_text='Mailjet API Key')
    api_secret = models.CharField(max_length=255, help_text='Mailjet API Secret')
    admin_email = models.EmailField(help_text='Admin email to receive contact form submissions')
    sender_email = models.EmailField(help_text='Sender email address')
    sender_name = models.CharField(max_length=100, default='Portfolio Contact Form', help_text='Sender name')
    
    class Meta:
        verbose_name = 'Mailjet Settings'
        verbose_name_plural = 'Mailjet Settings'
    
    def __str__(self):
        return 'Mailjet Settings'
    
    def save(self, *args, **kwargs):
        # Only allow one instance
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj