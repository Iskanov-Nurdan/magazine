from rest_framework import viewsets
from apps.contact.models import Contact
from apps.contact.serializers import ContactSerializer

class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
