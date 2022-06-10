from django.http import HttpRequest
from commons.middlewares.pagination import StandardResultsSetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from commons.exceptions import NotFoundException, ValidationException
from rest_framework.permissions import IsAuthenticated

class CreateVoucherAPIView(APIView):
    class CreateVoucherSerializer(serializers.Serializer):
        name = serializers.CharField()
        code = serializers.CharField()
        user_limit = serializers.IntegerField()
        max_redemption = serializers.IntegerField()
        valid_until = serializers.DateTimeField()
        promo_type = serializers.CharField()
        discount_value = serializers.IntegerField()
        minimum_order_amount = serializers.IntegerField()
        min_order_count = serializers.IntegerField()
        max_order_count = serializers.IntegerField()
        exclusive_to_user = serializers.BooleanField(default=True)
        active = serializers.BooleanField(default=True)
        claimable = serializers.BooleanField(default=True)

    def post(self, request: HttpRequest):
        data: dict = request.data
        serializer = CreateVoucherSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        voucher = create_voucher(**serializer.validated_data)
        return Response(CreateVoucherSerializer(voucher).data)

# class ListUserView(ListAPIView):
#     serializer_class = DetailsUserSerializer
#     pagination_class = StandardResultsSetPagination
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         data: dict = self.request.GET
#         queryset = User.objects.filter(username__icontains=data['username']).order_by('id')
#         return queryset

# class GetAndUpdateAndDeleteUserView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request: HttpRequest, user_id: int):
#         data = User.objects.filter(pk=user_id)
#         if not data.exists():
#             raise NotFoundException
#         serializer_data = DetailsUserSerializer(data.first())
#         return Response(serializer_data.data)

#     def put(self, request: HttpRequest, user_id: int):
#         data: dict = request.data
#         user = User.objects.filter(pk=user_id)
#         if not user.exists():
#             raise NotFoundException
#         serializer_data = DetailsUserSerializer(user.first(), data=data)
#         if serializer_data.is_valid():
#             serializer_data.save()
#             return Response(serializer_data.data)
#         else:
#             raise ValidationException(data=serializer_data.errors)

#     def delete(self, request: HttpRequest, user_id: int):
#         user = User.objects.filter(pk=user_id)
#         if not user.exists():
#             raise NotFoundException
#         serializer_data = DeleteUserSerializer(user.first(), data=request.data)
#         if serializer_data.is_valid():
#             serializer_data.save()
#             return Response({})
#         else:
#             raise ValidationException(data=serializer_data.errors)
