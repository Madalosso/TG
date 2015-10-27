from django.shortcuts import render
from django.http import HttpResponse
from experiment import tasks
# Create your views here.


def about(request):
	result = tasks.sleeptask.delay(10)
	result_one = tasks.sleeptask.delay(10)
	result_two = tasks.sleeptask.delay(10)
   	return HttpResponse(result.task_id)
   	