from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
# from django.views.generic.edit import CreateView
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
            'commented': False,
            'comment_form': CommentForm()
        }
        return render(request, template, context,)

# class PollView(View):

    # def view_poll(request, id):
    #     poll = get_object_or_404(Poll, id=id)
    #     comments = Comment.objects.filter(post=poll, approved=True)
    #     template = 'poll.html'
    #     context = {
    #         'poll': poll,
    #         'comments': comments,
    #         'commented': True,
    #         'comment_form': CommentForm()
    #     }

    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         comment_form.instance.email = request.user.email
    #         comment_form.instance.name = request.user.username
    #         comment = comment_form.save(commit=False)
    #         comment.poll = poll
    #         comment.save()
    #     else:
    #         comment_form = CommentForm()

    #     return render(request, template, context,)



# class AddCommentView(CreateView):
#    model = Comment
#    # form_class = Form
#    template = 'add_comment.html'
#     fields = '__all__'

def home(request):
    return render(request, 'templates/index')

class PollLike(View):
    def post(self, request, slug):
        poll = get_object_or_404(Poll, slug=slug)

        if poll.likes.filter(id-request.user.id).exists():
            poll.likes.remove(request.user)
        else:
            poll.likes.add(request.user)

        return HttpResponseRedirect(reverse('view_poll'))
