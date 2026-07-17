from datetime import date, timedelta

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Booking, Hotel, Review


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

    def test_availability_one_room_type(self):
        user = User.objects.create_user('tester')
        hotel = Hotel.objects.create(
            author=user,
            title='Smart Hotel',
            text='A nice place in Bishkek.',
            price=100,
            amount=2,
        )
        today = date.today() + timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        day_after = tomorrow + timedelta(days=1)

        self.assertTrue(hotel.is_available(today, tomorrow))

        Booking.objects.create(
            hotel=hotel,
            guest_name='Guest 1',
            email='guest1@example.com',
            check_in=today,
            check_out=tomorrow,
            guests=1,
        )
        self.assertTrue(hotel.is_available(today, tomorrow))

        Booking.objects.create(
            hotel=hotel,
            guest_name='Guest 2',
            email='guest2@example.com',
            check_in=today,
            check_out=tomorrow,
            guests=1,
        )
        self.assertFalse(hotel.is_available(today, tomorrow))

    def test_overlapping_bookings_within_limit(self):
        user = User.objects.create_user('tester')
        hotel = Hotel.objects.create(
            author=user,
            title='Smart Hotel',
            text='A nice place in Bishkek.',
            price=100,
            amount=2,
        )
        today = date.today() + timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        day_after = tomorrow + timedelta(days=1)

        Booking.objects.create(
            hotel=hotel,
            guest_name='Guest 1',
            email='guest1@example.com',
            check_in=today,
            check_out=tomorrow,
            guests=1,
        )
        Booking.objects.create(
            hotel=hotel,
            guest_name='Guest 2',
            email='guest2@example.com',
            check_in=today,
            check_out=tomorrow,
            guests=1,
        )

        self.assertFalse(hotel.is_available(today, tomorrow))
        self.assertTrue(hotel.is_available(tomorrow, day_after))

    def test_booking_str(self):
        user = User.objects.create_user('tester')
        hotel = Hotel.objects.create(
            author=user,
            title='Smart Hotel',
            text='A nice place in Bishkek.',
            price=100,
            amount=5,
        )
        today = date.today() + timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        booking = Booking.objects.create(
            hotel=hotel,
            guest_name='Guest',
            email='guest@example.com',
            check_in=today,
            check_out=tomorrow,
            guests=1,
        )
        self.assertIn('Guest', str(booking))
        self.assertIn('Smart Hotel', str(booking))

    def test_hotel_capacity_and_rating(self):
        user = User.objects.create_user('tester')
        hotel = Hotel.objects.create(
            author=user,
            title='Smart Hotel',
            text='A nice place in Bishkek.',
            price=100,
            amount=2,
            capacity=4,
        )
        self.assertEqual(hotel.capacity, 4)

        Review.objects.create(hotel=hotel, user=user, rating=4, text='Great!')
        Review.objects.create(hotel=hotel, user=User.objects.create_user('other'), rating=2, text='Okay')
        self.assertEqual(hotel.review_count, 2)
        self.assertEqual(hotel.average_rating, 3)
