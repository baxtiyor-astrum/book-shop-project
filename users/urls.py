from django.urls import path
from .views import RegisterUserView, LoginUserView, SendVerificationEmailView, VerifyEmailView, ForgotPasswordView, ResetPasswordView, UserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view()),
    path('send-verification-email/', SendVerificationEmailView.as_view()),
    path('verify-email/', VerifyEmailView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
    path('profile/', UserProfileView.as_view()),
]
