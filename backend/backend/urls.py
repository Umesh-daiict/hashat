from django.contrib import admin
from django.urls import path, include
from auth.views import CreateUserView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/register/',CreateUserView.as_view(),name="register_user"),
    path('api/v1/token/',TokenObtainPairView.as_view(),name="get_token"),
    path('api/v1/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api-auth',include('rest_framework.urls'))
]
