from rest_framework import serializers
from ..models import Todo


class TodoSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ("id", "title", "details", "date")

    def get_date(self, obj):
        return obj.date.strftime("%Y-%m-%d %H:%M:%S")
