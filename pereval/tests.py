from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Coords, Users, Images

class PerevalAddedTests(APITestCase):
    def setUp(self):

        self.url_post = reverse('submit_data')
        self.user = Users.objects.create(name='Василий', mid_name='Петрович', last_name='Пупкин', phone='+79805554433',
                                         email='test1@testmail.com')
        self.coord = Coords.objects.create( latitude=42.1012, longitude=5.6056, height=1450)
        self.img = Images.objects.create(img="https://disk.yandex.ru/i/eOV_srOt3ZPh7Q", title='Гора')
        self.valid_payload = {
            "status": "new",
            "beauty_title": "test beautytitle",
            "title": "test title",
            "other_titles": "test other title",
            "connect": "Куда то там примыкает",
            "user": self.user.pk,
            "coords": self.coord.pk,
            "images": [self.img.pk],
            "winter": "test 1A",
            "spring": "test 2B",
            "summer": "test 3A",
            "autumn": "test 2A"
        }

    def test_create_pereval_added_with_valid_payload(self):
        data = self.valid_payload
        response = self.client.post(self.url_post, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

