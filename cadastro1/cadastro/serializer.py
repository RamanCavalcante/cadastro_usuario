from django.db import models
from rest_framework import serializers
from cadastro.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'login', 'senha','data_nascimento']