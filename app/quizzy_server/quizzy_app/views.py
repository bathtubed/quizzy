from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie

import quizzy_app.answerFunctions as exam_lib
from django.conf import settings
import datetime
import calendar

root = settings.BASE_DIR + '/data'

def get_exam(examID):
    return exam_lib.getExam(root, examID)

def get_user(cookie):
    return 'ebonyWilliams'

@ensure_csrf_cookie
def index(request):
    if request.method == 'GET':
        params = request.GET
    else:
        params = request.POST
    
    exam_data = get_exam(params["examID"])
    start_time = exam_data.start_time
    end_time = exam_data.end_time
    server_time = datetime.datetime.now()
    
    exam_lib.generateAnswersFolder(root, exam_data)
    
    if server_time < start_time or server_time > end_time:  # this cannot be submitted
        if request.method == 'POST':
            return HttpResponse("You cannot submit at this time", status=400);
        displayed_start = start_time
        template = loader.get_template('quizzy_app/waitingpage.html')
        context = {
            'start_time':displayed_start,
            'exam_name':exam_data.ID
        }
    
    elif request.method == 'POST':
        try:
            exam_lib.updateAns(root, params["examID"], get_user("abc"), params["questionID"], params["answer"])
        except:
            return HttpResponse("Couldn't save file at " + params["examID"] + '/' + get_user("abc") + '/' + params["questionID"] + " with " + params["answer"], status=500);
        
        return HttpResponse("Answer Saved", status=200)
    else:
        exam_object = exam_data
        template = loader.get_template('quizzy_app/index.html')
        context = {
            'exam':exam_object
        }
        
    return HttpResponse(template.render(context, request))
