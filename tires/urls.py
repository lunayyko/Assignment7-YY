from django.urls            import path, include

from rest_framework.routers import SimpleRouter

from .views                 import TireViewSet

app_name = 'tires'

router = SimpleRouter()

router.register('tires', TireViewSet, basename='tires')

urlpatterns = [
    path('', include((router.urls, 'tires'))),
]