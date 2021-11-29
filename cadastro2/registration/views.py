from django.db.models import query
from rest_framework import serializers, viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer

from rest_framework import serializers, viewsets
from registration.models import User
from registration.serializer import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class XLSXViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (XLSXRenderer,)
    filename = 'export2.xlsx'
