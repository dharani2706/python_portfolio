from django.contrib import admin

from .models import Certification, ContactMessage, Education, Project, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "proficiency", "display_order")
    list_editable = ("proficiency", "display_order")
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "display_order", "created_at")
    list_editable = ("featured", "display_order")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "technologies")
    list_filter = ("featured",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "start_year", "end_year", "display_order")
    list_editable = ("display_order",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "issue_date", "display_order")
    list_editable = ("display_order",)
    search_fields = ("name", "organization")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    list_editable = ("is_read",)
