from .serializers import RegisterSerializer, LoginSerilaizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg' : 'User created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({'msg' : 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serialaizer = LoginSerilaizer(data = data)
            if serialaizer.is_valid():
                print(serialaizer.data)
                response = serialaizer.get_jwt_token(serialaizer.data)
                return Response(response, status=status.HTTP_200_OK)
            return Response (serialaizer.errors, status=status.HTTP_401_UNAUTHORIZED)

        except:
            return Response ({'msg' : 'user invalid'}, status=status.HTTP_400_BAD_REQUEST)

    

