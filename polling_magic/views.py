from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Poll, Comment
from .forms import CommentForm


class PollList(generic.ListView):
    model = Poll
    template_name = 'index.html'
    paginate_by = 6


def view_poll(request, id):
    poll = get_object_or_404(Poll, id=id)
    comments = Comment.objects.filter(post=poll, approved=True)
    template = 'poll.html'
    context = {
        'poll': poll,
        'comments': comments,
        'comment_form': CommentForm()

    }

    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.poll = poll
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template, context)


# class AddCommentView(CreateView):
#     model = Comment
#     # form_class = Form
#     template = 'add_comment.html'
#     fields = '__all__'


def home(request):
    return render(request, 'templates/index')
