from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Message
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def index(request):
    latest_message = Message.objects.order_by('-pub_date')[:5]
    template = loader.get_template('comments/index.html')
    context = {
    'latest_message': latest_message,
}
    return HttpResponse(template.render(context, request))

@login_required
def postcomment (request):
    myauthor= request.POST.get("author_text")
    mytitle = request.POST.get("title_text")
    mymessage = request.POST.get("message_text")
    newMsg = Message.objects.create(author_text=myauthor,title_text=mytitle,message_text=mymessage)
    newMsg.save()
    return redirect("/comments")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/comments/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
