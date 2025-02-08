from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserLoginSerializer, UserRegistrationSerializer, SendVerificationEmailSerializer, ForgotPasswordSerializer, ResetPasswordSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from .utils import generate_email_verification_token, verify_email_verification_token

User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class LoginUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class SendVerificationEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SendVerificationEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()

            if not user:
                return Response({"error": "Bunday email mavjud emas."}, status=status.HTTP_404_NOT_FOUND)

            token = generate_email_verification_token(user.email)
            verification_url = f"http://localhost:8000/api/users/verify-email/?token={token}"

            send_mail(
                "Email Tasdiqlash",
                f"Salom {user.username}, emailingizni tasdiqlash uchun ushbu havolani bosing: {verification_url}",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return Response({"message": "Tasdiqlash emaili yuborildi."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyEmailView(APIView):
    def get(self, request):
        token = request.GET.get("token")
        email = verify_email_verification_token(token)

        if email:
            user = get_object_or_404(User, email=email)
            user.is_active = True
            user.save()
            return Response({"message": "Email muvaffaqiyatli tasdiqlandi."}, status=status.HTTP_200_OK)

        return Response({"error": "Noto‘g‘ri yoki muddati o‘tgan token."}, status=status.HTTP_400_BAD_REQUEST)
    
class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()

            if user:
                token = generate_email_verification_token(user.email)
                reset_url = f"http://localhost:8000/api/users/reset-password/?token={token}"

                send_mail(
                    "Parolni Tiklash",
                    f"Salom {user.username}, parolingizni tiklash uchun ushbu havolani bosing: {reset_url}",
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                )

            return Response({"message": "Agar email mavjud bo‘lsa, parolni tiklash havolasi yuborildi."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']
            email = verify_email_verification_token(token)

            if email:
                user = get_object_or_404(User, email=email)
                user.set_password(new_password)
                user.save()
                return Response({"message": "Parol muvaffaqiyatli tiklandi."}, status=status.HTTP_200_OK)

        return Response({"error": "Noto‘g‘ri yoki muddati o‘tgan token."}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user