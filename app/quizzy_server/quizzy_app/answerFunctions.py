import os
import json
import datetime
import logging

logger = logging.getLogger(__name__)

class Exam:
	def __init__(self, eID, cID, start, end, q, lang):
		self.ID = eID
		self.course = cID
		self.start_time = start
		self.end_time = end
		self.questions = q
		self.language = lang

def newTest(root, examId, studentNames, qIds):
    if not os.path.exists(root+'/'+'responses'+'/'+str(examId)):
        os.makedirs(root+'/'+'responses'+'/'+str(examId))
    
	for i in range(len(studentNames)):
		name = studentNames[i]
		if not os.path.exists(root+'/'+'responses'+'/'+str(examId)+'/'+name):
			os.makedirs(root+'/'+'responses'+'/'+str(examId)+'/'+name)
		for j in qIds:
			open(root+'/'+'responses'+'/'+str(examId)+'/'+name+'/'+j["id"], 'w')	
            
    return True

			
def updateAns(root, examId, name, question, answer):
    target = open(root+'/'+'responses'+'/'+str(examId)+'/'+name+'/'+str(question), 'w')
    target.truncate()
    target.write(answer)

def getExam(root, examId):
	e = open(root+'/'+'exams'+'/'+examId+'.json', 'r')
	whole = json.load(e)
	course = whole["course"]
	start = whole["startTime"]
	end = whole["endTime"]
	lang = whole["language"]
	start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
	end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
	allQs = whole["questions"]
	exam = Exam(examId, course, start, end, allQs, lang)
	return exam


class Course:
	def __init__(self, name, ID, rost):
		self.name = name
		self.ID = ID
		self.roster = rost

def getCourse(root, courseId):
	c = open(root+'/'+'courses'+'/'+courseId+'.json', 'r')
	whole = json.load(c)
	c = whole["course"]
	r = whole["roster"]
	course = Course(c, courseId, r)
	return course
	

def generateAnswersFolder(root, exam):
    return newTest(root, exam.ID, getCourse(root, exam.course).roster, exam.questions)

	










	




