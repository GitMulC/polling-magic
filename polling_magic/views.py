from django.shortcuts import render
from django.views import generic
from .models import Poll


class PollList(generic.ListView):
    model = Poll
    # queryset = Poll.objects.filter(status=1).order_by('-release_date') Status needed?
    template_name = 'index.html'
    paginate_by = 6
