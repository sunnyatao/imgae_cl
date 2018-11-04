from django.shortcuts import render
from django.shortcuts import HttpResponse
from tf_model_call.classifier import do_classify

# Create your templates here.
def index(request):
    return HttpResponse('OK')

def call_model(request):
    human_string, score = '12', 0.29 #do_classify()
    return HttpResponse('call_model successfull: %s-(%.5f)'%(human_string, score), )

import os
import json
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def upload(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    elif request.method == "POST":
        print('go in to post method...')
        obj = request.FILES.get('img_file')
        path_dir = os.path.join('static', 'upload')
        if not os.path.exists(path_dir):
            print('create path: ' + path_dir)
            os.makedirs(path_dir)

        file_path = os.path.join(path_dir, obj.name)
        print('file_path:   ' + file_path)

        f = open(file_path, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()

        human_string, score = do_classify(file_path)
        ret={'human_string':human_string,'score':str(score)}
        return HttpResponse(json.dumps(ret))