from django.conf import settings


def site_profile(request):
    return {
        "site_name": settings.SITE_NAME,
        "site_title": settings.SITE_TITLE,
        "site_email": settings.SITE_EMAIL,
        "site_github": settings.SITE_GITHUB,
        "site_linkedin": settings.SITE_LINKEDIN,
        "site_location": settings.SITE_LOCATION,
    }
