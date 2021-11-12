from django.conf import settings
from dajngo.shortcuts import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter


from src.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

app_name = "api"
urlpatterns = [path('',include('api.urls')),]

urlpatterns += router.urls
