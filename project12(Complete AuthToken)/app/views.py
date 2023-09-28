from django.shortcuts import render
from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes

from app.serializers import SigninSerializers, SignupSerializers

from django.contrib.auth import authenticate, login, logout

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated

from datetime import timedelta  # Import timedelta

class Signup(APIView):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        data = request.data
        serializers = SignupSerializers(data=data)
        print(data)
        if serializers.is_valid():

            serializers.save()
            return Response({"Message": "Account Created"})
        return Response({"Message": "Not Created"}, status=status.HTTP_406_NOT_ACCEPTABLE)



class Signin(APIView):
    def get(self, request):
        return render(request, "signin.html")

    def post(self, request):
        data = request.data
        serializer = SigninSerializers(data=data)
        user = authenticate(username=data['username'], password=data["password"])

        if user is None:
            return Response({"Message": "Invalid Credentials", "is_valid": False})

        if serializer.is_valid():
            # Delete the old token cookie if it exists
            if 'authtoken' in request.COOKIES:
                response = Response({"MESSAGE": "Login successfully", "is_valid": True})
                response.delete_cookie('authtoken')
            else:
                response = Response({"MESSAGE": "Login successfully", "is_valid": True})

            # Create and set a new token
            token, created = Token.objects.get_or_create(user=user)
            token_seconds_to_expire = 86400
            token.expires = token.created + timedelta(seconds=token_seconds_to_expire)
            response.set_cookie("authtoken", token.key, max_age=token_seconds_to_expire)
            token.save()


            login(request, user)
            return response
        else:
            return Response({"MESSAGE": "Invalid input data", "is_valid": False})

class Home(APIView):
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def get(self,request):
        if request.user.is_authenticated:
            auth_token = request.COOKIES.get('authtoken')
            if auth_token:
                # Now you have the auth token in 'auth_token', you can use it as needed
                print("Auth Token:", auth_token)
                print("hey ", request.user)
                return render(request, "home.html")
            else:
                print("Auth token not found")
                print(request.user)
                return redirect("/signin")
        return Response("Not Authenticated", status=status.HTTP_406_NOT_ACCEPTABLE)

class Logout(APIView):
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def get(self,request):

        Token.objects.filter(user=request.user).delete()
        response = render(request, "logout.html")
        response.delete_cookie('authtoken')
        logout(request)
        return response
