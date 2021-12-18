from django.test import TestCase
from mainapp.models import Post
import datetime, pytz


class PostModelTest(TestCase):
    def setUp(self):
        self.content = "Test string"
        self.date = datetime.datetime.now(pytz.timezone("Europe/Istanbul"))
        self.post_object = Post.objects.create(content=self.content)

    def test_content_value(self):
        self.assertEqual(self.post_object.content, self.content)

    def test_date_created(self):
        strftime_input = "%d %m %Y %H %M"  # don't need to check seconds

        """ I could code that test case better. Explanation:
        "Django stores datetime information in UTC in the database." (https://docs.djangoproject.com/en/4.0/topics/i18n/timezones/)
        And the self.date should use same timezone with object.date_created in order make an accurate comparison
        so, you can just get self.date as UTC right? (line 11)
        Yes, I think it is simple as that
        But I converted these times to "Europe/Istanbul" timezone because this app displays Istanbul timezone
        also I wanted to practise timezone convert proccess :)
        """

        print("\nIn database:       " + str(self.post_object.date_created))
        print(
            "Istanbul timezone: "
            + str(
                self.post_object.date_created.astimezone(
                    pytz.timezone("Europe/Istanbul")
                )
            )
        )

        self.assertEqual(
            self.post_object.date_created.astimezone(
                pytz.timezone("Europe/Istanbul")
            ).strftime(strftime_input),
            self.date.strftime(strftime_input),
        )

    def test_initial_like_count(self):
        self.assertEqual(self.post_object.like_count, 0)
