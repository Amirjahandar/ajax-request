from .models  import Comment
from django.shortcuts import render
import json




def index(request):
    if request.method == 'post':
        jsondata = json.loads(request.body)
        newcomment =  Comment()
        newcomment.username = jsondata.get('username')
        newcomment.comment = jsondata.get('comment')
        newcomment.like = False
        newcomment.save()

        return render(request, 'home.html')

    else:
        return render(request, 'home.html')
