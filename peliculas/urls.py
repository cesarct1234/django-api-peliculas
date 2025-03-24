from rest_framework.routers import DefaultRouter
from .views import PeliculaViewSet, GeneroViewSet

router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet)
router.register(r'generos', GeneroViewSet)

urlpatterns = router.urls


