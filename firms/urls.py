from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(r'entity', views.EntityViewSet, basename="entities")
router.register(r'', views.FirmsViewSet, basename="firms")

urlpatterns = router.urls