from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import CreateUserView, ManagerUserView


app_name = "users"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("me/", ManagerUserView.as_view(), name="manage_user"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
