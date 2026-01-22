# python
from django.contrib.auth import get_user_model

class EmailAuthBackend:
    """
    Authenticate using an email address.
    Add 'account.authentication.EmailAuthBackend' to AUTHENTICATION_BACKENDS.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        email = kwargs.get('email') or username
        if not email or not password:
            return None
        email = email.strip().lower()
        user = User.objects.filter(email__iexact=email).first()
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
