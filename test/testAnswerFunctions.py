root = "data"
exam = 1
studentNames = ["Shashank", "Lucas", "Eric", "Adam"]
qIds = 3
newTest(root, exam, studentNames, qIds)
str1 = "111111111111111111111"
str2 = "222222222222222222222"
str3 = "333333333333333333333"

updateAns(root, exam, studentNames[0], 0, str1)
updateAns(root, exam, studentNames[0], 0, str2)
updateAns(root, exam, studentNames[0], 0, str3)

print (getExam(root, 'exam1')).questions['0']
print (getExam(root, 'exam1')).questions['1']
print (getExam(root, 'exam1')).questions['2']
print (getExam(root, 'exam1')).start_time
print (getExam(root, 'exam1')).end_time

				
	









