from cmd import IDENTCHARS
from rest_framework.views import APIView
from .models import Std, Teacher, classroom, division
from .serializers import classroomserializer,stdserializer,teacherserializer,divserializer
from rest_framework import viewsets
from rest_framework.response import Response
import json
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



class getdivStudentByteacher_id(viewsets.ModelViewSet):  
    
    pass
    # queryset = classroom.objects.all()
    # serializer_class = classroomserializer

    # def get_queryset(self):

    #     a = self.request.GET.get('a')
    #     div_data = division.objects.filter(teacher_id= a)
        
    #     if a:
    #         dictionary = {}
    #         for i in div_data:
    #             x = []
    #             y = []
    #             y.append(i)
    #             stu_data = self.queryset.filter(div_id__div= i)
    #             for j in stu_data:
    #                 x.append(j)
    #             # return stu_data
    #             # dictionary.add('div_data', y)
    #             dict = {
    #                 'div_data': y  ,'student':{'stu_data': x}
    #             }
                # print(dict)
            # print(dictionary,"##################")    
            # return Response([dict])

        # if a:
        
        #     # from id 
        #     # data = self.queryset.filter(div_id__teacher_id=a)
            
        #     #from name
        #     data = self.queryset.filter(div_id__teacher_id__tname=a)
        #     return data



    # def list(self, request, *args, **kwargs):
    #     a = self.request.GET.get('a')
        # div_data = division.objects.filter(teacher_id= a)
        # print(div_data)
        # if a:
        #     dictionary = {}
        #     x = []
        #     y = []
        #     for i in div_data:
                
        #         i.__dict__.pop("_state")
        #         y.append(i.__dict__)
        #         print("##",y)
        #         stu_data = classroom.objects.filter(div_id__div= i)
        #         print(stu_data)
        #         for j in stu_data:
        #             j.__dict__.pop("_state")
        #             x.append(j.__dict__)
        # import pdb; pdb.set_trace()

        # data = {}
        
        # div_data = division.objects.filter(teacher_id= a)
        # for i in div_data:
        #     # print(i)
        #     i.__dict__.pop("_state")
            
        #     stu_data = classroom.objects.filter(div_id__div= i)
        #     # print(stu_data)
        #     # count = 0
        #     for j in stu_data:
        #         # print("jjjjjjjjjjjjjjjjjjjjj",j)
                
        #         j.__dict__.pop("_state")
        #         if data:
                    
        #             if len(data['division']) == 0: 
        #                 data["division"] = [i.__dict__]
        #             else:
        #                 d = data["division"]
        #                 # print([i.__dict__][0]["id"],"[i.__dict__]     ")

        #                 if [i.__dict__][0]["id"] != [i.__dict__][0]["id"]:
        #                     data["division"] = data["division"]+[i.__dict__] 
        #                     print(data["division"]+[i.__dict__] ,"")
                            
        #                 else:
        #                     data["division"] = data["division"]
        #                     # print("#@#@#",data["division"][0]["student"]+[j.__dict__])
        #                 data["division"][0]["student"] = data["division"][0]["student"]+[j.__dict__]
        #         else:
        #             data["division"] = [i.__dict__]
        #             data["division"][0]["student"] = [j.__dict__]
        #     print(data)
            # count += 1
            # print(count,"counttt")

        # print(self,"self")
        # print(request, "request")
        # print(args, "args")
        # print(kwargs, "kwargs")
        # dict = {
        #             'div_data': y ,'student':{'stu_data': x}
        #         }
        # response = super(getdivStudentByteacher_id, self).list(request, *args, **kwargs)
        # # response.data = {result.pop('name'): result for result in response.data}
        # response.data=data
        # return response


class getTeacher(APIView):
    def get(self, request,*args, **kwargs):
        # id = self.request.GET.get('id')
        # emp = classroom.objects.filter(id = id)
        emp = classroom.objects.all()

        students = []
        data = {}

        for em in emp:
            teacher = str(em.std.teacher.tname)
            standard = str(em.std.standard)
            div = str(em.div)

            if teacher not in data:     
                data[teacher] = {}

            if standard not in data[teacher]:
                data[teacher][standard] = {}

            if div not in  data[teacher][standard]:
                data[teacher][standard][div] = {}

            if "students" not in data[teacher][standard][div]:
                data[teacher][standard][div]['students'] = []

            students = data[teacher][standard][div]['students']
            student_detail = {
                                "id":em.id, 
                                "name":em.name,
                                "roll no":em.roll_no, 
                                "email":em.email       }

            students.append(student_detail)
        return Response(data)


class getTeacher2(APIView):
    queryset = Teacher.objects.all()
    serializer_class = teacherserializer
    def get(self, request,*args, **kwargs):

        emp = classroom.objects.all()
        students = []
        data = {}

        id = self.request.GET.get('id')
        if id:
            da = self.queryset.filter(id = id)
            print(da, "!!!")
            






    # def get_queryset(self):
    #     t_id = self.request.GET.get('t_id')
    #     if t_id:
    #         # data1 = self.queryset.filter(div = t_id)      
    #         data2 = self.queryset.filter(div__teacher=t_id)     
    #         print(data2)
    #     return  data2

        t = Teacher.objects.filter(id=id)
        # print(t,"teacher ")
        

        s = Std.objects.all()
        d = division.objects.all()

        teacher = str(t)
        standard = str(s)
        div = str(d)

        for em in emp:
            # teacher = str(em.std.teacher.tname)
            # standard = str(em.std.standard)
            # div = str(em.div)

            if teacher not in data:     
                data[teacher] = {}

            if standard not in data[teacher]:
                data[teacher][standard] = {}

            if div not in  data[teacher][standard]:
                data[teacher][standard][div] = {}

            if "students" not in data[teacher][standard][div]:
                data[teacher][standard][div]['students'] = []

            students = data[teacher][standard][div]['students']
            student_detail = {
                                "id":em.id, 
                                "name":em.name,
                                "roll no":em.roll_no, 
                                "email":em.email       }

            students.append(student_detail)
        return Response(data)



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
