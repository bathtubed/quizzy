import os
import json
import datetime

class Exam:
	def __init__(self, ID, start, end, q):
		self.ID = ID
		self.start_time = start
		self.end_time = end
		self.questions = q		

def newTest(root, examId, studentNames, qIds):
	if not os.path.exists(root+'/'+'responses'+'/'+str(examId)):
		os.makedirs(root+'/'+'responses'+'/'+str(examId))
	for i in range(len(studentNames)):
		name = studentNames[i]
		if not os.path.exists(root+'/'+'responses'+'/'+str(examId)+'/'+name):
			os.makedirs(root+'/'+'responses'+'/'+str(examId)+'/'+name)
		for j in range(qIds):
			open(root+'/'+'responses'+'/'+str(examId)+'/'+name+'/'+str(j), 'w')	
			
def updateAns(root, examId, name, question, answer):
	target = open(root+'/'+'responses'+'/'+str(examId)+'/'+name+'/'+str(question), 'w')
	target.truncate()
	target.write(answer)

def getExam(root, examId):
	e = open(root+'/'+'exams'+'/'+examId+'.json', 'r')
	whole = json.load(e)
	start = whole["startTime"]
	end = whole["endTime"]
	start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
	end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
	allQs = whole["questions"]
	d = {}
	for i in range(len(allQs)):
		d[allQs[i]['id']] = allQs[i]["data"]
		
	exam = Exam(examId, start, end, d)
	return exam
			

	










	




