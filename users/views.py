from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import update_session_auth_hash
from .permissions import UserViewSetPermissions
#from workspaces.models import WorkSpaceInvite
from . import serializers
from django.contrib.auth.models import User

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        login_serializer= serializers.LoginSerializer(
            data= request.data
        )
        login_serializer.is_valid(raise_exception=True)
        user= authenticate(request, **login_serializer.data)
        print(user)
        if user is None:
            response= Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
            return response
        
        if not user.is_active:
            response = Response(
                {"detail": "Account disabled"}, status=status.HTTP_401_UNAUTHORIZED
            )
            response.set_cookie('loggedIn', 'false', httponly=True)
            return response
        
        login(request, user)
        response = Response(status=status.HTTP_200_OK)
        response.set_cookie('loggedIn', 'true', httponly=True)
        return response
    

class SignupView(APIView):
    permission_classes= (permissions.AllowAny, )

    def post(self, request):
        # Initialize serializer first
        serializer = serializers.UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the user
        user = serializer.save()
        # Log the user in
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        # Set response with cookie
        response = Response(status=status.HTTP_201_CREATED)
        response.set_cookie('loggedIn', 'true', httponly=True)

        return response
    

    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = (UserViewSetPermissions,)
    queryset = User.objects.all().select_related("profile")

    def list(self, request, *args, **kwargs):
        # dont list all users
        raise Http404
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial",False)
        instance= self.get_object()
        serializer = serializers.UserSerializer(
            instance=instance,data=request.data,partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)


    @action(methods=("GET",), detail=False, url_path="me")
    def get_current_user_data(self, request):
        return Response(self.get_serializer(request.user).data)


class ChangePasswordView(APIView):
    permission_classes= (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = serializers.ChangePasswordSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        user= self.request.user
        if user.check_password(serializer.validated_data.get('current_password')):
            if serializer.validated_data.get('new_password') == serializer.validated_data.get('confirm_new_password'):
                user.set_password(serializer.validated_data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({'detail': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({"detail":"Password and confirm password didn't match"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Incorrect password.'}, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(views.APIView):
    def post(self, request):
        logout(request)


        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('loggedIn')
        return response