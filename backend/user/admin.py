from django.contrib import admin
from .models import *

class EducationAndTrainingAdmin(admin.ModelAdmin):
    list_display = ('training_type', 'institution_name', 'subject', 'year')
    list_filter = ('training_type', 'year')
    search_fields = ('institution_name', 'subject')

admin.site.register(EducationAndTraining, EducationAndTrainingAdmin)
admin.site.register(SkillCategory)
admin.site.register(MySkill)
admin.site.register(MyProject)

class WebsiteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Website.objects.exists():
            return False 
        return True  

admin.site.register(Website, WebsiteAdmin)
admin.site.register(HeroInfo,WebsiteAdmin)
admin.site.register(Footer)
admin.site.register(SocialIcon)
admin.site.register(ContactSubmission)
admin.site.register(MailjetSettings)