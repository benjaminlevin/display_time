# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import get_current_timezone
from django.utils import timezone
from datetime import datetime

def index(request):
    date = datetime.now().strftime('%b %d, %Y')
    time = datetime.now().strftime('%-I:%M %p')
    context = { 
    	'datetime' : [
  			{'date' : date},
  			{'time' : time}
  		]
  	}
    #how to set time zone to local for end user and fixed for db?
    print ("*"*50)
    print get_current_timezone()
    print datetime.now().strftime('%-I:%M %p')
    print ("*"*50)
    return render(request, "time1/index.html", context)
