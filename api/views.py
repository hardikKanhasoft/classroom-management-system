from datetime import datetime
from itertools import count
from rest_framework.views import APIView
from .models import Std, Teacher, classroom, division, CustomUser, Agenda
from .serializers import Agendaserializer, classroomserializer, stdserializer, teacherserializer, divserializer, CustomUserserializer
from rest_framework import viewsets
from rest_framework.response import Response
from mailjet_rest import Client

from api import serializers

class classroomModelViewSet(viewsets.ModelViewSet):
    queryset = classroom.objects.all()

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
            is_moniter = True
            self.queryset = self.queryset.filter(is_monitor=is_moniter)
        if is_moniter == "false":
            is_moniter = False
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
            return self.queryset.filter(div=div)
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
            is_moniter = True
            self.queryset = self.queryset.filter(is_monitor=is_moniter)
        if is_moniter == "false":
            is_moniter = False
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
        return data2

class getTeacher1(APIView):
    def get(self, request, *args, **kwargs):
        id = self.request.GET.get('id')
        # emp = classroom.objects.filter(id = id)
        emp = classroom.objects.all()

        students = []
        data = {}
        print(data)

        for em in emp:
            teacher = str(em.std.teacher.tname)
            standard = str(em.std.standard)
            div = str(em.div)

            if teacher not in data:
                data[teacher] = {}

            if standard not in data[teacher]:
                data[teacher][standard] = {}

            if div not in data[teacher][standard]:
                data[teacher][standard][div] = {}

            if "students" not in data[teacher][standard][div]:
                data[teacher][standard][div]['students'] = []

            students = data[teacher][standard][div]['students']
            student_detail = {
                "id": em.id,
                "name": em.name,
                "roll no": em.roll_no,
                "email": em.email}

            students.append(student_detail)
        return Response(data)

class getTeacher(APIView):
    def get(self, request, *args, **kwargs):

        teacher_data = Teacher.objects.all()
        # standard_data = Std.objects.all()
        # student_data = classroom.objects.all()

        data = {}
        # get teacher
        teacher = []
        for i in teacher_data:
            teacher_details = {
                "id": i.id,
                "name": i.tname
            }
            # get standard
            std = []
            standard_data = Std.objects.filter(id = i.id)
            for j in standard_data:
               
            # if i.id == j.teacher.id:
                standard_details = {
                    "id": j.id,
                    "standard": j.standard
                }
                std.append(standard_details)
                # get student
                stu = []
                student_data = classroom.objects.filter(id = j.id)
                for k in student_data:     
                    # if j.id == k.std.id:
                    student_details = {
                        "id": k.id,
                        "roll_no": k.roll_no,
                        "name": k.name,
                        "email": k.email,
                        "is_monitor": k.is_monitor,
                    }
                    stu.append(student_details)

                standard_details["students"] = stu

            teacher_details["standards"] = std
            teacher.append(teacher_details)

        data['teacher'] = teacher
        return Response(data)

class getStudentsByTeacher_is_monitor(viewsets.ModelViewSet):
    queryset = classroom.objects.all()
    serializer_class = classroomserializer

    def get_queryset(self):
        teacher_name = self.request.GET.get('teacher_name')
        is_moniter = self.request.GET.get('is_moniter')

        if is_moniter == "true":
            is_moniter = True
            self.queryset = self.queryset.filter(is_monitor=is_moniter)
        if is_moniter == "false":
            is_moniter = False
            self.queryset = self.queryset.filter(is_monitor=is_moniter)

        if teacher_name:
            # data1 = self.queryset.filter(div = t_id)
            return self.queryset.filter(div__teacher__tname=teacher_name)
        return self.queryset

# class Register(APIView):
#     def post(self, request,*args, **kwargs):
#         try:
#             name = request.data.get('name')
#             email = request.data.get('email')
#             password = request.data.get('password')
#             is_active = request.data.get('is_active')
#             type = request.data.get('type')
#             save_user = CustomUser(username=name, email=email, password=password, is_active=is_active, type=type)
#             save_user.save()
#             return HttpResponse ("data created")
#         except IntegrityError as e:
#             return HttpResponse ("email or username already exists")

class Register(APIView):

    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        serializer_obj = CustomUserserializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()

            latest_id = CustomUser.objects.latest('username').id
            # for email send
            api_key = '70a530a1f41ccfbfd0f94bf810962a81'
            api_secret = '0f57730f537cee90c8587cc25bdec296'
            mailjet = Client(auth=(api_key, api_secret), version='v3.1')
            data = {
                'Messages': [
                    {
                        "From": {

                            "Email": "hardikjethava.kanhasoft@gmail.com",
                            "Name": "test123"
                        },
                        "To": [
                            {
                                "Email": "test123.kanhasoft@gmail.com",
                                "Name": "hardikjethava"
                            }
                        ],
                        "Subject": "Greetings from Mailjet.",
                        "TextPart": "hello",
                        "HTMLPart": "http://127.0.0.1:8000/set_password/?id="f"{latest_id}",
                        "CustomID": "AppGettingStartedTest"
                    }
                ]
            }
            result = mailjet.send.create(data=data)
            # print(result.status_code)
            # print(result.json())
            # print("http://127.0.0.1:8000/set_password/?id="f"{latest_id}")

            return Response({"msg": 'Data Created and mail sent successfully'})
        else:
            return Response({"msg": serializer_obj.errors})

class GetUser(APIView):

    def get(self, request):
        id = self.request.GET.get("id")
        try:
            if id is not None:
                try:
                    user = CustomUser.objects.get(id=id)
                    serializer = CustomUserserializer(user)
                    # link
                    #
                except CustomUser.DoesNotExist:
                    return Response({"msg": 'User Does Not Exis'})
            return Response(serializer.data)
        except:
            user = CustomUser.objects.all()
            serializer = CustomUserserializer(user, many=True)
            return Response(serializer.data)

class SetPassword(APIView):
    def patch(self, request):
        id = self.request.GET.get("id")
        user = CustomUser.objects.get(id=id)
        serializer = CustomUserserializer(
            user, data=request.data, partial=True)
        a = request.data['password']
        b = request.data['confirm password']
        if a != b:
            return Response({'msg': "confirm password don't match with password"})
        else:
            if serializer.is_valid():
                serializer.save()

                return Response({"msg": 'Success'})
            return Response({"msg": 'Not Success'})

class Mail(APIView):
    def post(self, request):
        # subject = 'welcome to Kanhasoft'
        # message = 'Hi "hardik", thank you for registering'
        # email_from = 'test123.kanhasoft@gmail.com'
        # recipient_list = ['hardikjethava.kanhasoft@gmail.com', ]
        # send_mail( subject, message, email_from, recipient_list)

        # server = smtplib.SMTP('smtp.example.com', 25)
        # server.connect("smtp.example.com",587)
        # server.ehlo()
        # server.starttls()
        # server.ehlo()
        # server.sendmail(email_from, recipient_list, message)
        # server.quit()
        # import pdb; pdb.set_trace()

        api_key = '70a530a1f41ccfbfd0f94bf810962a81'
        api_secret = '0f57730f537cee90c8587cc25bdec296'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
            'Messages': [
                {
                    "From": {

                        "Email": "hardikjethava.kanhasoft@gmail.com",
                        "Name": "test123"
                    },
                    "To": [
                        {
                            "Email": "test123.kanhasoft@gmail.com",
                            "Name": "hardikjethava"
                        }
                    ],
                    "Subject": "Greetings from Mailjet.",
                    "TextPart": "hello",
                    "HTMLPart": "http://127.0.0.1:8000/set_password/?id=",
                    "CustomID": "AppGettingStartedTest"
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())
        return Response({"msg": 'Success'})

class Agendas(APIView):
    def post(self, request):
        serializer_obj = Agendaserializer(data = request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()

            #difference between time
            start = serializer_obj.data['start_time']
            end = serializer_obj.data['end_time']
            start_data = datetime.strptime(start,"%Y-%m-%dT%H:%M:%SZ")
            end_data = datetime.strptime(end,"%Y-%m-%dT%H:%M:%SZ")
            diff = end_data - start_data
            
            #how much taskas
            data = serializer_obj.data['agenda'].split(",") 
            len_data = (len(data))     

            #task time
            task_time = diff/len_data     
            
            #calculating time
            seconds = task_time.total_seconds()            
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60

            time = f"{'hours',hours}:{'minutes',minutes}:{'seconds',seconds}"
           
            print(220//3600,"floor")
            print(3600//3600,"floor2")

            dictionary = {}
            list_data= []
            for i in data:
                print(task_time,"to",i)
                d = {
                    "agenda":i,
                    "time":time
                }
                list_data.append(d)
            dictionary['list'] = list_data
            return Response(dictionary)
        else :
            return Response({'msg':serializer_obj.errors})
        

