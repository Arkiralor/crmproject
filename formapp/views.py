from django.shortcuts import render
from rest_framework.views import APIView
from .models import Questionare
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionareSerializer
from django.db.models import Q

# Create your views here.

class QuestionareAll(APIView):

    def get(self, request):
        queryset = Questionare.objects.filter(Q(claimed_by = None) or Q(claimed_by = "")).all()
        serialized = QuestionareSerializer(queryset, many=True)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )

    def post(self, request):
        try:
            data = QuestionareSerializer(data=request.data)
        except Exception as err:
            return Response(
                {
                    "error": str(err)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if data.is_valid():
            data.save()
            return Response(
                data.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "error": str(data.errors)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class Claiming(APIView):
    def get(self, request):
        queryset = Questionare.objects.filter(claimed_by=request.user_id).all()
        serialized = QuestionareSerializer(queryset, many=True)

        return Response(
            serialized.data,
            status=status.HTTP_302_FOUND
        )





