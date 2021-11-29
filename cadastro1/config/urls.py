from django.contrib import admin
from django.urls import path, include
from cadastro.views import UsuariosViewSet, MyExampleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)

xlsxRouter = routers.DefaultRouter()
xlsxRouter.register(r'Export',MyExampleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(xlsxRouter.urls)),
    path('',include(router.urls))
    
]
