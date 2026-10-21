from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.

class Harry_Potter(View):
    def get(self, request):
        data={
            "Title":"Harry Potter",
            "Price": 1000,
            "Author": "J K Rowling",
            "Published_year":1997
        }
        return JsonResponse(data)

class Gullivers_Travels(View):
    def get(self, request):
        data={
            "Title":"Gulliver's Travels",
            "Price": 950,
            "Author": "Jonathan Swift",
            "Published_year":1726
        }
        return JsonResponse(data)

class Pride_and_Prejudice(View):
    def get(self, request):
        data={
            "Title":"Pride and Prejudice",
            "Price": 800,
            "Author": "Jane Austin",
            "Published_year":1813
        }
        return JsonResponse(data)

class The_Alchemist(View):
    def get(self, request):
        data={
            "Title":"The Alchemist",
            "Price": 650,
            "Author": "Paulo Coelho",
            "Published_year":1988
        }
        return JsonResponse(data)

class Frankenstein(View):
    def get(self, request):
        data={
            "Title":"Frankenstein ",
            "Price": 550,
            "Author": "Mary Shelley",
            "Published_year":1818
        }
        return JsonResponse(data)