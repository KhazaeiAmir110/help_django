from django.test import TestCase
from apps.home.models import Writer


class TestWriterModel(TestCase):
    def test_model_str(self):
        writer = Writer.objects.create(first_name='amir', last_name='amiri', email='amir@gmail.com',
                                       country='Iran')
        self.assertEqual(str(writer), 'amir amiri')
