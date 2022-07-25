from re import X
from .models import Std, Teacher, classroom, division
from .serializers import classroomserializer,stdserializer,teacherserializer,divserializer
from rest_framework import viewsets

# Create your views here.

class classroomModelViewSet(viewsets.ModelViewSet):
    # import pdb; pdb.set_trace()
    queryset = classroom.objects.all()
    # for i in queryset:
        # import pdb; pdb.set_trace()
        # print(i.std.standard,"###############")
        # print(i.div_id,"###############")

    serializer_class = classroomserializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = classroomserializer

class stdViewSet(viewsets.ModelViewSet):
    queryset = Std.objects.all()
    serializer_class = stdserializer

class divViewSet(viewsets.ModelViewSet):
    queryset = division.objects.all()
    serializer_class = divserializer

class getStudentsByStd_is_monitor(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = classroomserializer
    
    def get_queryset(self):
        std = self.request.GET.get('std')
        is_moniter = self.request.GET.get('is_moniter') 
        
        if is_moniter == "true":
            is_moniter=True
            self.queryset = self.queryset.filter(is_monitor=is_moniter)
        if is_moniter == "false":
            is_moniter=False
            self.queryset = self.queryset.filter(is_monitor=is_moniter)

        if std:
            return self.queryset.filter(std_id=int(std))

        return self.queryset

class getStudentsBydivision(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = classroomserializer

    def get_queryset(self):
        div = self.request.GET.get('div')
        if div:
            return self.queryset.filter(div = div)
        return self.queryset

class getStudentsByis_monitor(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = classroomserializer 

    def get_queryset(self):
        is_monitor = self.request.GET.get('is_monitor')
        self.queryset = self.queryset.filter(is_monitor=is_monitor)
        return self.queryset

class teacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = teacherserializer

class getStudentsBydiv_is_monitor(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = classroomserializer
    
    def get_queryset(self):
        div = self.request.GET.get('div')
        is_moniter = self.request.GET.get('is_moniter') 
        if is_moniter == "true":
            is_moniter=True
            self.queryset = self.queryset.filter(is_monitor=is_moniter)
        if is_moniter == "false":
            is_moniter=False
            self.queryset = self.queryset.filter(is_monitor=is_moniter)

        if div:
            return self.queryset.filter(div_id=div)
        return self.queryset

class getdivByteacher(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = classroomserializer

    def get_queryset(self):
        t_id = self.request.GET.get('t_id')
        if t_id:
            # data1 = self.queryset.filter(div = t_id)      
            data2 = self.queryset.filter(div__teacher=t_id)     
            print(data2)
        return  data2



class getdivByteacher_name(viewsets.ModelViewSet):  
    y = []
    queryset = classroom.objects.all()
    serializer_class = classroomserializer

    def get_queryset(self):
        

        teacher_name = self.request.GET.get('teacher_name')
        if teacher_name:
            x = []
            data1 = self.queryset.filter(div__= teacher_name)      
            data2 = self.queryset.filter(div__teacher=teacher_name)  
            x.append(data2)
            print(data1)
                # return  x
            return data1


class getStudentsByTeacher_is_monitor(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = classroomserializer
    
    def get_queryset(self):
        teacher_name = self.request.GET.get('teacher_name')
        is_moniter = self.request.GET.get('is_moniter') 

        if is_moniter == "true":
            is_moniter=True
            self.queryset = self.queryset.filter(is_monitor=is_moniter)
        if is_moniter == "false":
            is_moniter=False
            self.queryset = self.queryset.filter(is_monitor=is_moniter)

        
        if teacher_name:
                # data1 = self.queryset.filter(div = t_id)      
            return self.queryset.filter(div__teacher__tname=teacher_name)  

        return self.queryset
