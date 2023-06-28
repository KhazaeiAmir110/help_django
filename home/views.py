from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question
from .serializers import PersonSerializer, QuestionSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .permissons import IsOwnerOrReadOnly, IsOwnerOrReadOnlyDelete


class Home(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    def get(self, request):
        question = Question.objects.all()
        ser_data = QuestionSerializer(instance=question, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class QuestionCreatViews(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = QuestionSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateViews(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        # به طور خودکار بررسی نمیکند permissins که ما ساخته ایم باید به او بگوییم که بررسی کند.
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteViews(APIView):
    permission_classes = [IsOwnerOrReadOnlyDelete, ]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'massage': 'questions delete'}, status=status.HTTP_200_OK)
