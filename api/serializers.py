from rest_framework import serializers
from base.models import QueryAPIModel

class QueryAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryAPIModel
        fields = '__all__'