from django.http import HttpResponse
from django.template import loader
import quizzy_app.answerFunctions as exam_lib
from django.conf import settings
import datetime
import calendar

def index(request):
    exam_data = exam_lib.getExam(settings.BASE_DIR + '/data',\
                                 request.GET['examID'])
    start_time = exam_data.start_time
    end_time = exam_data.end_time
    server_time = datetime.datetime.now()
    
    if server_time < start_time:
        displayed_start = start_time
        template = loader.get_template('quizzy_app/waitingpage.html')
        context = {
            'start_time':displayed_start,
            'exam_name':exam_data.ID
        }
         
    else:
        exam_object = exam_data
        template = loader.get_template('quizzy_app/index.html')
        context = {
            'exam':exam_object
        }
        
    return HttpResponse(template.render(context, request))