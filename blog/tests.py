from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class PostModelTests(TestCase):

    def test_post_str(self):
        user = User.objects.create_user('tester')
        post = Post.objects.create(author=user, title='Hello', text='World')
        self.assertEqual(str(post), 'Hello')
