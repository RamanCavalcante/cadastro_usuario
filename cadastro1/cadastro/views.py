from django.db.models import query
from rest_framework import serializers, viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from cadastro.models import Usuario
from cadastro.serializer import UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class MyExampleViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    renderer_classes = (XLSXRenderer,)
    filename = 'my_export.xlsx'