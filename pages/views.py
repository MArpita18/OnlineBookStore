from django.shortcuts import render, HttpResponse

def index(request):
    #return HttpResponse("<h1>Hello Arpita</h1>")
    return render(request, 'pages/index.html')

def aboutus(request):
     #name="Arpita"
     student = {1: "arpita", 2: "ankita", 3: "abhipsa", 4: "ansita" }
     results = { 
          1 : {"name" : "Arpita", "cgpa" :[9.2,9.3,9.4,9.1]},
          2 : {"name" : "Jane", "cgpa" :[9.4,9.3,9.2,9.1]},
          3 : {"name" : "Sam", "cgpa" :[9.8,9.7,9.4,9.6]},
          4 : {"name" : "Sara", "cgpa" :[9.4,9.7,9.3,9.6]},
          5 : {"name" : "Will", "cgpa" :[9.2,9.3,9.4,9.1]}
         
     }
     context = {
          "name" : "Arpita",
          "age" : 19,
          "num1" : 12,
          "num2" : 10,
          "nums" : [1,2,3,4,5,10,2,],
          "students" : student,
          "results" : results,
     }
     return render(request, 'pages/about.html',context)
