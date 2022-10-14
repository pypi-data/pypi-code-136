import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ControlHub.settings.local")
django.setup()


def create_user(LOGON_NAME):

    from django.contrib.auth import get_user_model
    User = get_user_model()
    params = {
        'role': 1,
    }
    user_obj = User.objects.create_user(username=LOGON_NAME, password='111222333', **params)
    print(user_obj)


if __name__ == '__main__':
    import sys
    print(sys.argv[1])
    LOGON_NAME = sys.argv[1]
    # create_user(LOGON_NAME)