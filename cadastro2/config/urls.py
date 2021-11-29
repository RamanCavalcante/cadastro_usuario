
from django.contrib import admin
from django.urls import path, include

from registration.views import UsersViewSet, XLSXViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'User', UsersViewSet)

xlsxRouter = routers.DefaultRouter()
xlsxRouter.register(r'Export',XLSXViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(xlsxRouter.urls)),
    path('',include(router.urls))
    
]
