from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.

class Kochi_Public_Library(View):
    def get(self, request):
        data={
            "Library_name":"Kochi Public Library",
            "Location":"Cochin" ,
            "Email": "admin@kochilibrary.com",
            "Contact_Number":"8987456523",
            "Contact_Person_Name":"Muralikrishnan"
        }
        return JsonResponse(data)


class Kollam_Public_Library(View):
    def get(self, request):
        data = {
            "Library_name": "Kollam Public Library",
            "Location": "Kollam",
            "Email": "admin@Kollamlibrary.com",
            "Contact_Number": "8987456544",
            "Contact_Person_Name": "Alfiya"
        }
        return JsonResponse(data)


class Kottayam_Public_Library(View):
    def get(self, request):
        data = {
            "Library_name": "Kottayam Public Library",
            "Location": "Kottayam",
            "Email": "admin@Kottayamlibrary.com",
            "Contact_Number": "8987459923",
            "Contact_Person_Name": "Jaithri"
        }
        return JsonResponse(data)


class Kannur_Public_Library(View):
    def get(self, request):
        data = {
            "Library_name": "Kannur Public Library",
            "Location": "Kannur",
            "Email": "admin@Kannurlibrary.com",
            "Contact_Number": "6287456523",
            "Contact_Person_Name": "Vishnu"
        }
        return JsonResponse(data)


class Thrissur_Public_Library(View):
    def get(self, request):
        data = {
            "Library_name": "Thrissur Public Library",
            "Location": "Thrissur",
            "Email": "admin@Thrissurlibrary.com",
            "Contact_Number": "8887456523",
            "Contact_Person_Name": "Esha"
        }
        return JsonResponse(data)

