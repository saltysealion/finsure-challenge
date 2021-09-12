from django.urls.conf import path
from rest_framework.routers import DefaultRouter
from .views import LenderViewSet, LenderImportAPIView, LenderExportAPIView

urlpatterns = [
    path(
        'lenders/import/', LenderImportAPIView.as_view(), name='lender-import'
    ),
    path(
        'lenders/export/', LenderExportAPIView.as_view(), name='lender-export'
    ),
]

router = DefaultRouter()
router.register(r'lenders', LenderViewSet, basename='lender')
urlpatterns += router.urls
