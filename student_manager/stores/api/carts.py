from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from student_manager.stores.services import create_cart, update_cart
from student_manager.stores.selectors import get_store_by_id, get_cart_by_id
from student_manager.stores.models import Cart
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from student_manager.users.selectors import get_user_by_id

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("id", "owner", "ordering_for", "store", "created_at")

class CreateCartAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    class InputSerializer(serializers.Serializer):
        store_id = serializers.IntegerField()
        owner_id = serializers.IntegerField()
        ordering_for_id = serializers.IntegerField()

    def post(self, request):
        data: dict = request.data
        owner = request.user
        store = get_store_by_id(pk=data["store_id"])
        serializer = self.InputSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        cart = create_cart(owner=owner, store=store, ordering_for_id=data["ordering_for_id"])
        response = OutputSerializer(cart).data
        return Response(response)

class UpdateCartAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    class InputSerializer(serializers.Serializer):
        ordering_for = serializers.CharField()
        owner = serializers.CharField()

    def put(self, request, id: int):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_date = serializer.validated_data
        cart = get_cart_by_id(pk=id)
        data = update_cart(
            cart=cart, 
            owner=request.user, 
            ordering_for=get_user_by_id(pk=validated_date["ordering_for"])
        )
        response = OutputSerializer(data).data
        return Response(response)
