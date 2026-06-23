# usuarios/views.py

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # validar que ambos campos vengan llenos
        # y que el password y el username sean correcto
        if not username or not password:
            return Response(
                {'error': 'Por favor ingrese un usuasrio y contraseña válidos'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Autenticamos contra la base de datos

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            if usuario.is_active:
                return Response({
                    'mensaje': 'Inicio de sesión exitoso',
                    'usuario': {
                        'id': usuario.id,
                        'username': usuario.username,
                        'first_name': usuario.first_name,
                        'last_name': usuario.last_name,
                        'rol': usuario.rol
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'error': 'El usuario no está activo'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(
                {'error': 'El usuario o la contraseña son incorrectos'},
                status=status.HTTP_401_UNAUTHORIZED
            )
