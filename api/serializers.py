from .models import classroom, Std, Teacher ,division
from rest_framework import serializers

class teacherserializer(serializers.ModelSerializer):
    # test_teacher = stdserializer(read_only=True, many=True)
    class Meta: 
        model = Teacher
        fields = '__all__'
        # exclude=["id"]
        depth = 2

class stdserializer(serializers.ModelSerializer):
    class Meta: 
        model = Std
        fields = '__all__'

        # depth=1

class   classroomserializer(serializers.ModelSerializer):
    # data = stdserializer(read_only=True, many=True)
    class Meta:
        model = classroom
        fields = '__all__'
        # depth=1

class divserializer(serializers.ModelSerializer):
    class Meta:
        model = division
        fields = '__all__'
    