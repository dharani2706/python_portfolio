from django.core.management.base import BaseCommand

from portfolio.models import Certification, Education, Project, Skill


class Command(BaseCommand):
    help = "Load sample portfolio content so the site is not empty."

    def handle(self, *args, **options):
        skills = [
            {
                "name": "Python",
                "description": "Core language for backend logic, scripting, and data work.",
                "icon_class": "bi-filetype-py",
                "proficiency": 90,
                "display_order": 1,
            },
            {
                "name": "Django",
                "description": "Building secure, maintainable web applications.",
                "icon_class": "bi-globe2",
                "proficiency": 88,
                "display_order": 2,
            },
            {
                "name": "HTML",
                "description": "Semantic page structure for accessible websites.",
                "icon_class": "bi-filetype-html",
                "proficiency": 85,
                "display_order": 3,
            },
            {
                "name": "CSS",
                "description": "Responsive layouts, theming, and visual polish.",
                "icon_class": "bi-filetype-css",
                "proficiency": 82,
                "display_order": 4,
            },
            {
                "name": "JavaScript",
                "description": "Interactive UI behavior and form enhancements.",
                "icon_class": "bi-filetype-js",
                "proficiency": 75,
                "display_order": 5,
            },
            {
                "name": "SQL",
                "description": "Querying and modeling relational data.",
                "icon_class": "bi-table",
                "proficiency": 80,
                "display_order": 6,
            },
            {
                "name": "Git & GitHub",
                "description": "Version control, collaboration, and code review.",
                "icon_class": "bi-git",
                "proficiency": 85,
                "display_order": 7,
            },
            {
                "name": "PostgreSQL",
                "description": "Production database design and administration basics.",
                "icon_class": "bi-database",
                "proficiency": 78,
                "display_order": 8,
            },
            {
                "name": "REST APIs",
                "description": "Designing and consuming JSON APIs.",
                "icon_class": "bi-diagram-3",
                "proficiency": 80,
                "display_order": 9,
            },
        ]

        for skill in skills:
            Skill.objects.update_or_create(name=skill["name"], defaults=skill)

        projects = [
            {
                "title": "TaskFlow API",
                "slug": "taskflow-api",
                "description": (
                    "A Django REST API for personal task management with user "
                    "authentication, filtering, and PostgreSQL storage."
                ),
                "technologies": "Python, Django, REST APIs, PostgreSQL",
                "github_url": "https://github.com/",
                "live_url": "",
                "display_order": 1,
            },
            {
                "title": "Campus Events Portal",
                "slug": "campus-events-portal",
                "description": (
                    "A full-stack Django site where students can browse events, "
                    "register attendance, and manage listings from the admin."
                ),
                "technologies": "Django, HTML, CSS, JavaScript, SQLite",
                "github_url": "https://github.com/",
                "live_url": "",
                "display_order": 2,
            },
            {
                "title": "Portfolio CMS",
                "slug": "portfolio-cms",
                "description": (
                    "This website: a production-ready Django portfolio with "
                    "dynamic projects, certifications, and a contact inbox."
                ),
                "technologies": "Django, Bootstrap, WhiteNoise, Gunicorn",
                "github_url": "https://github.com/",
                "live_url": "",
                "display_order": 3,
            },
        ]

        for project in projects:
            Project.objects.update_or_create(slug=project["slug"], defaults=project)

        education_items = [
            {
                "school": "Your University Name",
                "degree": "Bachelor of Technology",
                "field_of_study": "Computer Science and Engineering",
                "start_year": "2021",
                "end_year": "2025",
                "description": (
                    "Coursework in data structures, databases, web development, "
                    "and software engineering. Built multiple Python projects."
                ),
                "display_order": 1,
            },
            {
                "school": "Online / Self-paced",
                "degree": "Django Web Development",
                "field_of_study": "Backend Engineering",
                "start_year": "2024",
                "end_year": "Present",
                "description": (
                    "Focused on Django apps, REST APIs, PostgreSQL, Git, and "
                    "deploying Python web applications."
                ),
                "display_order": 2,
            },
        ]

        for item in education_items:
            Education.objects.update_or_create(
                school=item["school"],
                degree=item["degree"],
                defaults=item,
            )

        certifications = [
            {
                "name": "Python for Everybody",
                "organization": "University of Michigan / Coursera",
                "issue_date": "2024-06-01",
                "credential_url": "https://www.coursera.org/",
                "display_order": 1,
            },
            {
                "name": "Django Web Framework",
                "organization": "Meta / Coursera",
                "issue_date": "2025-01-15",
                "credential_url": "https://www.coursera.org/",
                "display_order": 2,
            },
            {
                "name": "Git and GitHub",
                "organization": "Google",
                "issue_date": "2024-11-10",
                "credential_url": "https://www.coursera.org/",
                "display_order": 3,
            },
        ]

        for cert in certifications:
            Certification.objects.update_or_create(
                name=cert["name"],
                organization=cert["organization"],
                defaults=cert,
            )

        self.stdout.write(self.style.SUCCESS("Sample portfolio content is ready."))
