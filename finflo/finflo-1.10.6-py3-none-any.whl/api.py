from .models import Action, PartyType, SignList, States
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .transition import FinFlotransition
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView
)
from django.shortcuts import get_object_or_404
from django.conf import settings
from .serializer import  (
    StatesSerializer,
    TransitionManagerserializer,
    Actionseriaizer,
    partytypeserializer,
    signlistserialzier,
    workflowitemslistserializer,
    workeventslistserializer,
    Workitemserializer
)
from .models import (
    Action, 
    TransitionManager, 
    workevents, 
    workflowitems
)
from django.db.models import Q



####################################################
################      API       ####################
####################################################



# 1 . TRANSITION MAKING API


class TransitionApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        type = request.data.get("type")
        action = request.data.get("action")
        t_id = request.data.get("t_id")
        # extra datas for manual transitions
        source = request.data.get("source")
        interim = request.data.get("interim")
        target = request.data.get("target")

        if type and t_id  is not None:
            transitions = FinFlotransition(action = action.upper() , type = type.capitalize() , t_id = t_id , source = source , interim = interim ,target = target )
            return Response({"status" : "Transition success"},status = status.HTTP_200_OK)
        return Response({"status" : "Transition failure"},status = status.HTTP_204_NO_CONTENT)


    


#  2 . ALL WORK_MODEL LIST 


class DetailsListApiView(ListAPIView):
    queryset = TransitionManager.objects.all()
    serializer_class = TransitionManagerserializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        type = self.request.query_params.get('type',None)
        t_id = self.request.query_params.get('t_id',None)
        if t_id and type is not None :
            queryset = TransitionManager.objects.filter(Q(type__icontains = type ) | Q(t_id = int(t_id)))
        elif type is not None and t_id is None:
            queryset = TransitionManager.objects.filter(type__icontains = type)
        else:
            queryset = TransitionManager.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TransitionManagerserializer(queryset, many=True)
        return Response({"status": "success", "type" : settings.FINFLO['WORK_MODEL'] , "data": serializer.data}, status=status.HTTP_200_OK)



# 3 . WORFLOW API 

class WorkFlowitemsListApi(RetrieveUpdateAPIView):
    queryset = workflowitems.objects.all()
    serializer_class = Workitemserializer
    permission_classes = [IsAuthenticated]


    def retrieve(self, request, pk=None):
        queryset = workflowitems.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = Workitemserializer(user)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



# WORKEVENTS API 


class WorkEventsListApi(RetrieveUpdateAPIView):
    queryset = workevents.objects.all()
    serializer_class = workeventslistserializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = workevents.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = workeventslistserializer(user)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



# ACTION CREATE AND LIST API 


class ActionListApi(ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = Actionseriaizer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Action.objects.all()
        serializer = Actionseriaizer(queryset, many=True)
        return Response({"status": "success" , "data": serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = Actionseriaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors},status=status.HTTP_204_NO_CONTENT)


# STATES API 


class statesListCreateApi():
    queryset = States.objects.all()
    serializer_class = StatesSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = States.objects.all()
        serializer = StatesSerializer(queryset, many=True)
        return Response({"status": "success" , "data": serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = StatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors},status=status.HTTP_204_NO_CONTENT)




# PARTY TYPE API 

class PartyTypeListCreateApi():
    queryset = PartyType.objects.all()
    serializer_class = partytypeserializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = PartyType.objects.all()
        serializer = partytypeserializer(queryset, many=True)
        return Response({"status": "success" , "data": serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = partytypeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors},status=status.HTTP_204_NO_CONTENT)



# SIGN LIST API 


class SignListListCreateApi():
    queryset = SignList.objects.all()
    serializer_class = signlistserialzier
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = SignList.objects.all()
        serializer = signlistserialzier(queryset, many=True)
        return Response({"status": "success" , "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = signlistserialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors},status=status.HTTP_204_NO_CONTENT)