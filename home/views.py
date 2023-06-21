from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class Home(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionView(APIView):
    def get(self, request):
        question = Question.objects.all()
        ser_data = QuestionSerializer(instance=question, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = QuestionSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        # partial : برای این است که ما فقط بخواهیم یکی از موار سوال را تغییر دهیم نه تمام موارد آن را
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'massage': 'questions delete'}, status=status.HTTP_200_OK)
