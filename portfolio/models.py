from django.core.validators import EmailValidator, URLValidator
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=180, blank=True)
    icon_class = models.CharField(
        max_length=80,
        blank=True,
        help_text="Bootstrap Icons class, for example: bi-filetype-py",
    )
    proficiency = models.PositiveSmallIntegerField(
        default=80,
        help_text="Skill level from 0 to 100.",
    )
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, max_length=140)
    description = models.TextField()
    technologies = models.CharField(
        max_length=255,
        help_text="Comma-separated list, for example: Django, PostgreSQL, Bootstrap",
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    featured = models.BooleanField(default=True)
    display_order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title

    def technology_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]


class Education(models.Model):
    school = models.CharField(max_length=160)
    degree = models.CharField(max_length=160)
    field_of_study = models.CharField(max_length=160, blank=True)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20, default="Present")
    description = models.TextField(blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-start_year"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} — {self.school}"


class Certification(models.Model):
    name = models.CharField(max_length=180)
    organization = models.CharField(max_length=160)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True, validators=[URLValidator()])
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-issue_date"]

    def __str__(self):
        return f"{self.name} ({self.organization})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(validators=[EmailValidator()])
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} from {self.name}"
