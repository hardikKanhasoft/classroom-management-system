from .models import Std, Teacher, classroom, division
from .serializers import classroomserializer,stdserializer,teacherserializer,divserializer
from rest_framework import viewsets
from rest_framework.response import Response
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



class getdivByteacher_id(viewsets.ModelViewSet):  
    queryset = classroom.objects.all()
    serializer_class = classroomserializer

    def get_queryset(self):
        a = self.request.GET.get('a')
        div_data = division.objects.filter(teacher_id= a)
        print(div_data)       

        for i in div_data:
            # x = []
            print(i,"== i")
            stu_data = self.queryset.filter(div_id__div= i)

            print(stu_data)

            Dict = {
                'division': 
            }

            # x.append(Dict)
            # print(x)
        # for i in a:
        #     print(i)
        # return a
        

        # if a:
        
        #     # from id 
        #     # data = self.queryset.filter(div_id__teacher_id=a)
            
        #     #from name
        #     data = self.queryset.filter(div_id__teacher_id__tname=a)
        #     return data


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
