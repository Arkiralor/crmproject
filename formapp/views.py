from django.shortcuts import render
from rest_framework.views import APIView
from .models import Questionare
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionareSerializer, QuestionareSerializerAll
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

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

class AssignAgentView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        lead = Questionare.objects.filter(Q(claimed_by = None) or Q(claimed_by = "")).get(pk=id)

        if not lead.claimed_by:
            lead.claimed_by = request.user.id
            serialized = QuestionareSerializerAll(lead)
            lead.save()

            return Response(
                serialized.data,
                status=status.HTTP_202_ACCEPTED
            )
    def put(self, request, id):
        pass





