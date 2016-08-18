from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Message
from django.template import loader


def index(request):
    latest_message = Message.objects.order_by('-pub_date')[:5]
    template = loader.get_template('comments/index.html')
    context = {
    'latest_message': latest_message,
}
    return HttpResponse(template.render(context, request))

def postcomment (request):
    myauthor= request.POST.get("author_text")
    mytitle = request.POST.get("title_text")
    mymessage = request.POST.get("message_text")
    newMsg = Message.objects.create(author_text=myauthor,title_text=mytitle,message_text=mymessage)
    newMsg.save()
    return redirect("/comments")


