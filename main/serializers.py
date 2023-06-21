from rest_framework import serializers

from main import models


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newsletter
        fields = "__all__"
