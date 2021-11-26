from rest_framework             import generics, viewsets
from rest_framework.generics    import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response    import Response

from .models                    import Tire
from .serializers               import TireSerializers

class TireViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class   = TireSerializers

    def create(self, request):
        # """
        # 유저별 타이어 정보 저장
        # POST /tires

        # data params
        # {id : 유저아이디, trimid : 타이어번호}
        # """
        print(request.data)
        tire = Tire.objects.create(
            id = request.data[id],
            trimid = request.data[trimid]
        )
        print(id)

        return Response(self.get_serializer(tire).data, status=status.HTTP_201_CREATED)

# class SearchTireView(RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class   = TireSerializer
