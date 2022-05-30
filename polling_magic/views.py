from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
# from django.views.generic.edit import CreateView
from .models import Poll, Comment
from .forms import CommentForm


def home(request):
    return render(request, 'templates/index')


class PollList(generic.ListView):
    model = Poll
    template_name = 'index.html'
    paginate_by = 6


def view_poll(request, id):
    poll = get_object_or_404(Poll, id=id)
    comments = Comment.objects.filter(post=poll, approved=True)
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment_form.instance.body = request.POST.get("body")
            comment_form.instance.approved = True
            comment_form.instance.post = poll
            comment_form.instance.save()
            messages.success(request, "Comment Added")
        else:
            messages.error(request, "Error: Please Try Again.")
    comment_form = CommentForm()
    template = 'poll.html'
    context = {
        'poll': poll,
        'comments': comments,
        'commented': False,
        'comment_form': comment_form
    }
    return render(request, template, context)


def edit_comment(request, p_id, c_id):
    poll = get_object_or_404(Poll, id=p_id)
    comment = get_object_or_404(Comment, id=c_id)
    comment_form = CommentForm(request.POST or None, instance=comment)
    if comment_form.is_valid():
        comment_form.instance.name = request.user.username
        comment_form.instance.body = request.POST.get("body")
        comment_form.instance.approved = True
        comment_form.instance.post = poll
        comment_form.instance.save()
        messages.success(request, "Comment Updated")
    else:
        messages.error(request, "Error: Please Try Again.")
    return redirect("view_poll", p_id)


def delete_comment(request, p_id, c_id):
    poll = get_object_or_404(Poll, id=p_id)
    comment = get_object_or_404(Comment, id=c_id)
    comment.delete()
    return redirect("view_poll", p_id)

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


# class PollLike(View):
#     def post(self, request, slug):
#         poll = get_object_or_404(Poll, slug=slug)

#         if poll.likes.filter(id-request.user.id).exists():
#             poll.likes.remove(request.user)
#         else:
#             poll.likes.add(request.user)

#         return HttpResponseRedirect(reverse('view_poll'))


def poll_like(request, id):
    poll = get_object_or_404(Poll, id=id)
    if poll.likes.filter(id=request.user.id).exists():
        poll.likes.remove(request.user)
    else:
        poll.likes.add(request.user)
    return redirect("view_poll", id)


def poll_dislike(request, id):
    poll = get_object_or_404(Poll, id=id)
    if poll.dislikes.filter(id=request.user.id).exists():
        poll.dislikes.remove(request.user)
    else:
        poll.dislikes.add(request.user)
    return redirect("view_poll", id)
