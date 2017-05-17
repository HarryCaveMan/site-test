# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.
index=lambda request:  render_to_response('index.html')
portfolio = lambda request: render_to_response('portfolio.html')
resume = lambda request: render_to_response('resume.pdf')