from rest_framework import generics
from investments_app.models import Investment
from .serializers import InvestmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class InvestmentListCreateView(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDetailView(generics.RetrieveAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


@api_view(['POST', 'PUT', 'DELETE'])
def manage_investment(request, pk=None):    
    if request.method == 'POST':
        # Create operation
        serializer = InvestmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT']:
        # Update operation
        try:
            investment = Investment.objects.get(pk=pk)
        except Investment.DoesNotExist:
            return Response({'error': 'Investment not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvestmentSerializer(investment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete operation
        try:
            investment = Investment.objects.get(pk=pk)
        except Investment.DoesNotExist:
            return Response({'error': 'Investment not found'}, status=status.HTTP_404_NOT_FOUND)

        investment.delete()
        return Response({'message': 'Investment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)