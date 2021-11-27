from rest_framework             import generics, viewsets
from rest_framework.generics    import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators  import action
from rest_framework.response    import Response

from .models                    import Tire
from .serializers               import TireSerializers

class TireViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class   = TireSerializers
    
    def register_tires(self, request):
        tire = Tire.objects.create(
            id = request.data[id],
            trimid = request.data[trimid]
        )
        return Response(self.get_serializer(tire).data, status=status.HTTP_201_CREATED)