from django.shortcuts import render
from django.http import FileResponse
from django.http import StreamingHttpResponse

# Create your views here.
def index(request):
    print('我是index')
    return render(request,'firstapp/index.html')


def fanapp(request):
    print('我是fanapp')
    file = open('E:\python\django\myboke\myboke\崔玉林个人简历1.doc', 'rb')
    response = StreamingHttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="cui.doc"'
    return response
