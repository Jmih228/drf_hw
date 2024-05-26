from rest_framework import serializers
from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', read_only=True, many=True)

    class Meta:
        model = Course
        fields = ('title', 'description', 'lessons_count', 'lessons')

    def get_lessons_count(self, instance):
        return len(Lesson.objects.filter(id=instance.id))
