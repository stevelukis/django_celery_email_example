from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from main import models, serializers
from main.tasks import send_newsletter


class NewsletterView(viewsets.ModelViewSet):
    queryset = models.Newsletter.objects.all()
    serializer_class = serializers.NewsletterSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Sending newsletter
        send_newsletter.delay(serializer.validated_data.get("subject"), serializer.validated_data.get("body"))

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
