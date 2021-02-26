from accounts.views import CustomerViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
urlpatterns = router.urls