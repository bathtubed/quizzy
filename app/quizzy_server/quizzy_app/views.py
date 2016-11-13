from django.http import HttpResponse
from django.template import loader
import quizzy_app.answerFunctions as exam_lib
from django.conf import settings
import datetime
import calendar

root = settings.BASE_DIR + '/data'

def get_exam(examID):
    return exam_lib.getExam(root, examID)

def get_user(cookie):
    return 'eric'

def index(request):
    if request.method == 'GET':
        params = request.GET
    else:
        params = request.POST
    
    exam_data = get_exam(params["examID"])
    start_time = exam_data.start_time
    end_time = exam_data.end_time
    server_time = datetime.datetime.now()
    
    generateAnswersFolder(exam_data);
    
    if server_time < start_time:
        if request.method == 'POST':
            return HttpResponse("You cannot submit at this time", status_code=400);
        displayed_start = start_time
        template = loader.get_template('quizzy_app/waitingpage.html')
        context = {
            'start_time':displayed_start,
            'exam_name':exam_data.ID
        }
    
    elif request.method == 'POST':
        try:
            updateAns(root, params["examID"], get_user(request.COOKIES['sess_id']), params["questionID"], params["answer"])
        except:
            return HttpResponse("Couldn't save file", status_code=500);
        
        return HttpResponse("Answer Saved", status_code=200)
    else:
        exam_object = exam_data
        template = loader.get_template('quizzy_app/index.html')
        context = {
            'exam':exam_object
        }
        
    return HttpResponse(template.render(context, request))
