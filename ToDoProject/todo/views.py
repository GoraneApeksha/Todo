from django.shortcuts import render,redirect
from todo.models import task
# Create your views here.
def add(request):
    if(request.method=='POST'):
        heading__ = request.POST["heading"] #here heading is value of name attribute from html input tag
        detail__ = request.POST["detail"]
        date__ = request.POST["date"]
        print(heading__)
        print(detail__)
        print(date__)

        #creating sql query to insert data into the database
        #model_class.objects.create(coluumn_name = value)
        insert_data=task.objects.create(heading=heading__, detail=detail__, date=date__,is_deleted="n")

        #execute sql query
        insert_data.save()
        return redirect("/")
    return render(request,'todo/add.html')

#display all records
def index(request):
    content={}
    #content["data"]=task.objects.all()
    content["data"]=task.objects.filter(is_deleted="n")
    return render(request,'todo/index.html',content)

def delete(request,tid):
    record_to_be_deleted=task.objects.filter(id=tid)
    #record_to_be_deleted.delete()
    record_to_be_deleted.update(is_deleted="y")
    return redirect("/")

def update(request,tid):
    if(request.method=='POST'):
        heading__ = request.POST["heading"] #here heading is value of name attribute from html input tag
        detail__ = request.POST["detail"]
        date__ = request.POST["date"]
        record_to_be_update=task.objects.filter(id=tid)
        record_to_be_update.update(heading=heading__,detail=detail__,date=date__)
        return redirect('/')
    else:
        content={}
        content['data']=task.objects.get(id=tid)
        return render(request,'todo/update.html',content)
