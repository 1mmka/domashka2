from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import ClientViewSet,LoginClient
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('site',ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginClient.as_view(),name='login-view'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls