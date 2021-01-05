from django.shortcuts import render, HttpResponse

from .models import DagFile
# Create your views here.
def index(request):
    dag = DagFile.objects.all()[0]
    print(dag.to_code())
    for task in dag.tasks.all():
        print(task.name)
        try:
            print(task.dummytask)
        except Exception as e:
            print(e)
        try:
            print(task.s3togooglecloudstoragetask)
        except Exception as e:
            print(e)
    return HttpResponse('Hello')