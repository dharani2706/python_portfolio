from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage, Project


class PortfolioViewsTests(TestCase):
    def setUp(self):
        Project.objects.create(
            title="Demo API",
            slug="demo-api",
            description="A small REST API built with Django.",
            technologies="Python, Django, REST APIs",
            github_url="https://github.com/example/demo-api",
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Demo API")

    def test_contact_form_saves_message(self):
        response = self.client.post(
            reverse("home"),
            {
                "name": "Alex Kumar",
                "email": "alex@example.com",
                "subject": "Project inquiry",
                "message": "I would like to discuss a Django project.",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_form_rejects_short_message(self):
        response = self.client.post(
            reverse("home"),
            {
                "name": "A",
                "email": "not-an-email",
                "subject": "Hi",
                "message": "Too short",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_resume_download(self):
        response = self.client.get(reverse("download_resume"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")
