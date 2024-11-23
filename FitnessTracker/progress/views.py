from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ProgressPageView(TemplateView):
    template_name = 'progress/progress.html'


class LogProgressView(TemplateView):
    template_name = 'progress/log-progress.html'


class LogHistoryView(TemplateView):
    template_name = 'progress/log-history.html'
