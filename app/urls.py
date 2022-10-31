from xml.etree.ElementInclude import include
from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("items", views.ItemViewSet)

urlpatterns = [
    path('',include(router.urls)),
]