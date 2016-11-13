import os

def newTest(root, examId, studentNames, qIds):
	if not os.path.exists(root+'/'+str(examId)):
		os.makedirs(root+'/'+str(examId))
	for i in range(len(studentNames)):
		name = studentNames[i]
		if not os.path.exists(root+'/'+str(examId)+'/'+name):
			os.makedirs(root+'/'+str(examId)+'/'+name)
		for j in range(qIds):
			open(root+'/'+str(examId)+'/'+name+'/'+str(j), 'w')	
			
def updateAns(root, examId, name, question, answer):
	target = open(root+'/'+str(examId)+'/'+name+'/'+str(question), 'w')
	target.truncate()
	target.write(answer)







