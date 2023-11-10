from django.urls import path
from chat.views import (
    register_user,
    user_login,
    user_logout,
    send_chat_message,
    get_chat_history,
)

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("send-message/", send_chat_message, name="send_message"),
    path(
        "get-chat-history/<str:receiver_username>/",
        get_chat_history,
        name="get_chat_history",
    ),
]
