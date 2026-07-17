from django.contrib.auth.models import User
from django.test import TestCase

from .models import Hotel


class HotelModelTests(TestCase):

    def test_hotel_str(self):
        user = User.objects.create_user('tester')
        hotel = Hotel.objects.create(
            author=user,
            title='Smart Hotel',
            text='A nice place in Bishkek.',
            price=100,
            amount=5,
        )
        self.assertEqual(str(hotel), 'Smart Hotel')
