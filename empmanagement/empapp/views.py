from django.shortcuts import render,redirect
from django.contrib import messages
from jinja2 import Environment, PackageLoader, FileSystemLoader
from django.http import HttpResponseRedirect, HttpResponse
# from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from django.db import connection
import json


class Employee(View):
    global env
    env = Environment(
                loader=FileSystemLoader("empapp/")
            )
    """
    List all snippets, or create a new snippet.
    """

    def post(self,request):
        try:
            reqdata=request.POST
            cursor=connection.cursor()
            readquery="""SELECT * from empapp_EmployDetails WHERE "employe_id" = '{}'""".format(str(reqdata['employe_id']))
            c=cursor.execute(readquery)
            records = c.fetchall()
            if not records:
                reqdata['task_in_progress']
                data=(reqdata['employe_name'],reqdata['employe_id'],reqdata['department'],reqdata['salary'],reqdata['manager'],reqdata['task'],reqdata['task_in_progress'],reqdata['id_proof'])
                query="""INSERT INTO empapp_EmployDetails
                                    (employe_name, employe_id, department, salary, manager, task, task_in_progress, id_proof) 
                                    VALUES {};""".format(data)
                cursor.execute(query)
                return_msg=json.dumps({"success":True,"msg":"data Added successfully"})
                messages.success(request, "return_msg")
                return redirect("/employ/")
            else:
                return_msg=json.dumps({"success":True,"msg":"Employe ID already exist"})
                return HttpResponse(return_msg)

        except Exception as e:
            return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
            return HttpResponse(return_msg)
        


    # def post(self,request):
    #     try:
    #         reqdata=json.loads(request.body)
    #         print(reqdata)
    #         cursor=connection.cursor()
    #         readquery="""SELECT * from empapp_EmployDetails WHERE "employe_id" = '{}'""".format(str(reqdata['employe_id']))
    #         c=cursor.execute(readquery)
    #         records = c.fetchall()
    #         print(records)
    #         if not records:
    #             data=(str(reqdata['employe_name']),str(reqdata['employe_id']),str(reqdata['department']),reqdata['salary'],str(reqdata['manager']))
    #             print(data)
    #             query="""INSERT INTO empapp_EmployDetails
    #                                 (employe_name, employe_id, department, salary, manager) 
    #                                 VALUES {};""".format(data)
    #             cursor.execute(query)

    #             # query="""INSERT INTO empapp_EmployDetails
    #             #                     (employe_name, employe_id, department, salary, manager) 
    #             #                     VALUES {};""".format(("Vivek Sharma", "comp1", "Backend", 100, "qwerty"))
    #             # cursor.execute(query)
    #             return_msg=json.dumps({"success":True,"msg":"data Added successfully"})
    #             return HttpResponse(return_msg)
    #         else:
    #             return_msg=json.dumps({"success":True,"msg":"Employe ID already exist"})
    #             return HttpResponse(return_msg)

    #     except Exception as e:
    #         return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
    #         return HttpResponse(return_msg)
        
    
    
    def get(self,request):
        try:
            cursor=connection.cursor()
            readquery="""SELECT * from empapp_EmployDetails"""
            c=cursor.execute(readquery)
            records = c.fetchall()
            all_recordlist=[]
            for i in records:
                all_recordlist.append({
                    # "employe_name":i["employe_name"],
                    # "employe_id":i["employe_id"],
                    # "department":i["department"],
                    # "salary":i["salary"],
                    # "manager":i["manager"]
                    "employe_name":i[1],
                    "employe_id":i[2],
                    "department":i[3],
                    "salary":i[4],
                    "manager":i[5],
                    "task":i[6],
                    "task_in_progress":i[7],
                    "id_proof":i[8]
                    })

            jinja_var = {
                'data': all_recordlist
            }

            template = env.get_template('template/main.html')
            return HttpResponse(template.render(jinja_var))

        except Exception as e:
            return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
            return HttpResponse(return_msg)
            

    def delete(self,request):
        try:
            cursor=connection.cursor()
            emp_ids=str(request.build_absolute_uri())
            if emp_ids:
                emp=emp_ids.split("employ_id=")[-1]
                if "&" in emp:
                    emp_id=emp.split("&")[0]
                else:
                    emp_id=emp

                delquery="""DELETE from empapp_EmployDetails where employe_id = {}""".format(str(emp_id))
                cursor.execute(delquery)
                
            return_msg=json.dumps({"success":True,"msg":"data Added successfully"})
            return HttpResponse(return_msg)
        except Exception as e:
            return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
            return HttpResponse(return_msg)
            

    def view_one(request):
        try:
            cursor=connection.cursor()
            readquery="""SELECT * from empapp_EmployDetails WHERE "employe_id" = '{}'""".format(str(request.GET["employ_id"]))
            c=cursor.execute(readquery)
            records = c.fetchall()
            all_recordlist=[]
            for i in records:
                all_recordlist.append({
                    # "employe_name":i["employe_name"],
                    # "employe_id":i["employe_id"],
                    # "department":i["department"],
                    # "salary":i["salary"],
                    # "manager":i["manager"]
                    "employe_name":i[1],
                    "employe_id":i[2],
                    "department":i[3],
                    "salary":i[4],
                    "manager":i[5],
                    "task":i[6],
                    "task_in_progress":i[7]
                    })
            

            jinja_var = {
                'data': all_recordlist
            }
            template = env.get_template('template/edit.html')
            return HttpResponse(template.render(jinja_var))

        except Exception as e:
            return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
            return HttpResponse(return_msg)

    def employ_update(request):
        try:
            cursor=connection.cursor()
            readquery="""Update empapp_EmployDetails set (employe_name, department, salary, manager, task, task_in_progress)  = {} WHERE employe_id = '{}' """.format((request.POST['employe_name'],request.POST['department'],request.POST['salary'],request.POST['manager'],request.POST['task'],request.POST['task_in_progress']),request.POST['employe_id'])
            cursor.execute(readquery)
            # return HttpResponse("hii")
            # template = env.get_template('template/main.html')
            # return HttpResponse(template.render())
            return redirect("/employ/")

        except Exception as e:
            return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
            return HttpResponse(return_msg)

        
    def delete_one(request):
        try:
            cursor=connection.cursor()
            delquery="""DELETE from empapp_EmployDetails where employe_id = '{}'""".format(str(request.GET['employ_id']))
            cursor.execute(delquery)
            return redirect("/employ/")
        except Exception as e:
            return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
            return HttpResponse(return_msg)
















# from django.views import View

# # from .forms import MyForm

# class MyFormView(View):
#     # # form_class = MyForm
#     # initial = {'key': 'value'}
#     # template_name = 'form_template.html'

#     # def get(self, request, *args, **kwargs):
#     #     # form = self.form_class(initial=self.initial)
#     #     # return render(request, self.template_name, {'form': form})

#     # def post(self, request, *args, **kwargs):
#     #     form = self.form_class(request.POST)
#     #     if form.is_valid():
#     #         # <process form cleaned data>
#     #         return HttpResponseRedirect('/success/')

#     #     return render(request, self.template_name, {'form': form})

