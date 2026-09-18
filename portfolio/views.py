from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from .forms import ContactForm
from .models import Certification, Education, Project, Skill


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for reaching out. I will get back to you soon.",
            )
            return redirect(f"{reverse('home')}#contact")
        messages.error(request, "Please correct the errors in the contact form.")
    else:
        form = ContactForm()

    context = {
        "form": form,
        "skills": Skill.objects.all(),
        "projects": Project.objects.filter(featured=True),
        "education": Education.objects.all(),
        "certifications": Certification.objects.all(),
    }
    return render(request, "portfolio/home.html", context)


@require_GET
def download_resume(request):
    resume_path = Path(settings.BASE_DIR) / "static" / "files" / settings.RESUME_FILENAME
    if not resume_path.exists():
        raise Http404("Resume file is not available yet.")
    return FileResponse(
        resume_path.open("rb"),
        as_attachment=True,
        filename=f"{settings.SITE_NAME.replace(' ', '_')}_Resume.pdf",
    )
