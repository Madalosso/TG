from django.shortcuts import render
from django.http import HttpResponse
from tasks import add
# Create your views here.


def about(request):
	result = add.delay(10,1)
	print result.task_id
	result_one = add.delay(10,2)
	result_two = add.delay(10,3)
   	return HttpResponse(result.task_id)
   	
