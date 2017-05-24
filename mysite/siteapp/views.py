# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render,render_to_response,HttpResponse

# Create your views here.
index=lambda request:  render_to_response('index.html')

portfolio = lambda request: render_to_response('portfolio.html')

def resume(request): 
    with open('siteapp/templates/resume.pdf', 'r') as pdf:
 	    out=HttpResponse(pdf.read(), content_type='application/pdf')
 	    out['Content-Disposition'] = 'filename=HJoseph_Resume.pdf'
 	    return out
    pdf.closed
