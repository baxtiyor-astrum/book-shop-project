from itsdangerous import URLSafeTimedSerializer
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY

def generate_email_verification_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt="email-confirmation")

def verify_email_verification_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(token, salt="email-confirmation", max_age=expiration)
        return email
    except:
        return None
