from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Poll, Comment


class PollList(generic.ListView):
    model = Poll
    # queryset = Poll.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


def view_poll(request, id):
    poll = get_object_or_404(Poll, id=id)
    comments = Comment.objects.filter(post=poll, approved=True)
    template = 'poll.html'
    context = {
        'poll': poll,
        'comments': comments,
    }
    return render(request, template, context)
