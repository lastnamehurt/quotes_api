import json

from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework import serializers
from rest_framework import viewsets

# Serializers define the API representation.
from quotes.mailer import send_quote_confirmation
from quotes.models import Quote

"""
Move the Serializer and ViewSet to it's own module once we have more than one!
"""

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


# ViewSets define the view behavior.
class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    authentication_classes = []  # disables authentication
    permission_classes = []  # disables permission

    def create(self, request):
        print(json.dumps(request.data))
        send_quote_confirmation(**request.data)

        # create quote
        Quote.objects.create(
            **request.data
        )
        return super().create(request)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'quotes', QuoteViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
