from django.test import TestCase as BaseTestCase
from django.test.client import Client as BaseClient, RequestFactory
from django.contrib.auth.models import User

from nexgen.models import Video


class TestCase(BaseTestCase):

    '''
    @classmethod
    def setUpClass(cls):
        cls.request = RequestFactory()
        cls.client = BaseClient()

        # Editor
        cls.editor, dc = User.objects.get_or_create(
            username='editor',
            email='editor@test.com'
        )
        cls.editor.set_password("password")
        cls.editor.save()

        # Post
        obj, dc = Post.objects.get_or_create(
            title='Post',
            content='aaaa <div style="page-break-after: always;"></div>bbb',
            owner=cls.editor, state='published',
        )
        obj.sites = [1]
        obj.save()
        cls.post = obj
    '''

    def test_aaa(self):
        self.failUnless(1 == 1)
