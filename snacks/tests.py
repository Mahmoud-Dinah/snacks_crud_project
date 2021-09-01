from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

class snack_test(TestCase):
    def adduser(self):
        self.user = get_user_model().objects.create_user(
            username="purchaser test", email="test@email.com", password="test"
        )

        self.snack = Snack.objects.create(
            title="title test", description="description test", purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "title test")



    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "title test")
        self.assertEqual(f"{self.snack.purchaser}", "purchaser test")
        self.assertEqual(f"{self.snack.description}", "description test")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "title test")
        self.assertTemplateUsed(response, "snack_list.html")


    def test_snack_create(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "create test",
                "description": "create test",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "create test")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "test Updated title","description":"test description update","reviewer":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))