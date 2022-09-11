from django.shortcuts import render,redirect

from jinja2 import Environment, FileSystemLoader
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from rest_framework.response import Response
from empapp.models import EmployDetails
import json


class Home(View):
    global env
    env = Environment(
                loader=FileSystemLoader("home/")
            )

    def get(self,request):
        try:
           
            template = env.get_template('template/index.html')
            return HttpResponse(template.render())

        except Exception as e:
            return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
            return HttpResponse(return_msg)
            
    def add_details(request):
        try:
           
            template = env.get_template('template/adddetails.html')
            return HttpResponse(template.render())

        except Exception as e:
            return_msg=json.dumps({"success":False,"msg":"Error: {}".format(e)})
            return HttpResponse(return_msg)

