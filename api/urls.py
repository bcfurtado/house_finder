from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter(trailing_slash=False)
router.register(r'houses', views.HouseViewSet, 'Houses')

urlpatterns = router.urls
