from django.shortcuts import render
from django.views import View

# Create your views here.

class App2(View):
    def get(self,request):
        return render(request,"app2/index.html")