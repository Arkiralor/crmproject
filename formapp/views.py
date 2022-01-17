from django.shortcuts import render
from rest_framework.views import APIView
from .models import Questionare, Agent, User
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionareSerializer, QuestionareSerializerAll
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.

class QuestionareAll(APIView):

    def get(self, request):
        queryset = Questionare.objects.filter(
            Q(claimed_by = None) 
            or Q(claimed_by = "")
            ).all()
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
        agent = Agent.objects.filter(user = request.user).first()
        try:
            lead = Questionare.objects.filter((Q(claimed_by = None) or Q(claimed_by = agent)) and Q(id = id)).first()
            lead_serialized = QuestionareSerializerAll(lead)
        except Questionare.DoesNotExist:
            return Response(
                {
                    "error": "Lead already claimed."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
                lead_serialized.data,
                status=status.HTTP_202_ACCEPTED
            )
       
    def post(self, request, id:int):
        agent = Agent.objects.filter(user = request.user).first()
        try:
            # lead = Questionare.objects.filter(Q(claimed_by = None) or Q(claimed_by = "") or Q(claimed_by = agent)).get(pk=id)
            # lead = Questionare.objects.filter(Q(id = id) or Q(claimed_by = agent)).first()
            # lead = Questionare.objects.filter(Q(claimed_by = None)and Q(id = id)).first()
            lead = Questionare.objects.get(pk=id)
        except Questionare.DoesNotExist:
            return Response(
                {
                    "error": "Lead already claimed."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not lead.claimed_by:
            # agent = Agent.objects.filter(user = request.user).first()
            lead.claimed_by = agent
            lead.save()
            serialized = QuestionareSerializerAll(lead)

            return Response(
                serialized.data,
                status=status.HTTP_202_ACCEPTED
            )
        elif lead.claimed_by != agent:
            return Response(
                {
                    "error": "Lead already claimed."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        elif lead.claimed_by == agent:
            return Response(
                {
                    "error": "You have already claimed this."
                },
                status=status.HTTP_400_BAD_REQUEST
            )





