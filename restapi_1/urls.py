from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include,path
from movies.views import MovieViewSet,ActionViewSet,ComedyViewSet,ArtisticViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('movies',MovieViewSet)
router.register('action',ActionViewSet)
router.register('artistic',ArtisticViewset)
router.register('comedy',ComedyViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)