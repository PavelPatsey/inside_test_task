from django.core.management.base import BaseCommand

from ...models import Message, User

OBJECTS_NUMBER = 15


class Command(BaseCommand):
    help = "Fill the database with test data"

    def handle(self, *args, **kwargs):

        test_user = User.objects.create_user(username="test_user", password="test_password")

        objects_number = OBJECTS_NUMBER
        objects = (
            Message(
                name=test_user,
                message="test message text %s" % i,
            )
            for i in range(objects_number)
        )
        Message.objects.bulk_create(list(objects))
