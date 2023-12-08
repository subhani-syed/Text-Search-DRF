from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from api import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload/',views.upload_paragraph,name='upload'),
    path('search/',views.search_text,name='search'),
]
