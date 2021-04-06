from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiView = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives most control',
            'mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiView': an_apiView})
