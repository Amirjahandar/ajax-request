from .models  import Comment
from django.shortcuts import render
import json




def index(request):
    if request.method == 'POST':
        jsondata = json.loads(request.body)
        newcomment =  Comment()
        newcomment.username = jsondata.get('username')
        newcomment.comment = jsondata.get('comment')

        newcomment.like = jsondata.get('like')
        newcomment.save()

        return render(request, 'home.html')

    else:
        return render(request, 'home.html')




# def index(request):
#     if request.method == 'POST':
#         newcom = Comment()
#         newcom.username = request.POST['txtusername']
#         newcom.comment = request.POST['txtcomment']
#         newcom.like = False
#         newcom.save()

#         msg = {'msg': 'confrimed!!'}
#         return render(request, 'home.html', msg )

#     else:
#         return render(request, 'home.html')