from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework import generics, permissions

from .serializers import UserRegisterSerializer, UserProfileListSerializer
from .models import MyUser


class UserRegisterView(APIView):

    @swagger_auto_schema(request_body=UserRegisterSerializer())
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(status.HTTP_400_BAD_REQUEST)


class UserProfileListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(responses={200: UserProfileListSerializer()})
    def get(self, request):

        user_object = MyUser.objects.filter(id=request.user.id).first()

        serializer_class = UserProfileListSerializer(user_object)

        return Response(serializer_class.data)

