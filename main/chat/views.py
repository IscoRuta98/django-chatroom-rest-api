from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, ChatMessageSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.db.models import Q

from .models import User, ChatMessage


@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def user_login(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")

        user = None
        if "@" in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == "POST":
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response(
                {"message": "Successfully logged out."}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["POST"])
@authentication_classes([TokenAuthentication])  # Add TokenAuthentication
@permission_classes([IsAuthenticated])
def send_chat_message(request):
    if request.method == "POST":
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_chat_history(request, receiver_username):
    if request.method == "GET":
        user = request.user
        try:
            receiver = User.objects.get(username=receiver_username)
        except ObjectDoesNotExist:
            return Response(
                {"error": f"User with username '{receiver_username}' not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Retrieve chat history between the authenticated user and the specified receiver
        chat_history = ChatMessage.objects.filter(
            (Q(sender=user, receiver=receiver) | Q(sender=receiver, receiver=user))
        ).order_by("timestamp")

        serializer = ChatMessageSerializer(chat_history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
