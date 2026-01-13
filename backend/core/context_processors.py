# core/context_processors.py
from user.models import Website

def website_context(request):
    try:
        website = Website.objects.first()
        return {'website': website}
    except Website.DoesNotExist:
        return {'website': None}
