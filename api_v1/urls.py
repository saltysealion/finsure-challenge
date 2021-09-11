from rest_framework.routers import DefaultRouter
from .views import LenderViewSet

router = DefaultRouter()
router.register(r'lenders', LenderViewSet, basename='lender')
urlpatterns = router.urls