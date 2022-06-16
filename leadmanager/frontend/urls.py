from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from . import views


# tells django to search for URL patterns 
# responsible for mapping the routes and paths in your project 
urlpatterns = [
    path('', views.index),
    path('accounts/', include("django.contrib.auth.urls")),  # new
    path('admin', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]