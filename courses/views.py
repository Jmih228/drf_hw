from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets, generics
from courses.serializers import CoursesSerializer, LessonSerializer, SubscriptionSerializer
from courses.models import Course, Lesson, Subscription
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsNotStaff, IsOwner
from courses.paginators import CoursesPaginator, LessonsPaginator


class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Course.objects.all()
    pagination_class = CoursesPaginator

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsNotStaff]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, ~IsNotStaff | IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, ~IsNotStaff | IsOwner]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated, ~IsNotStaff | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsNotStaff & IsOwner]
        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsNotStaff]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonsPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsNotStaff | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsNotStaff | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsNotStaff, IsOwner]


class SubscriptionAPIView(generics.GenericAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):

        user = self.request.user
        course_id = self.request.data['course']
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_id)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка оформлена'

        return HttpResponse(message)
