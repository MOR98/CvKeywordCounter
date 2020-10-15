import textract
#import textract library
text = textract.process("Path\\YourCV.docx")
#load CV.docx
punctuation = ["!","%","*","(",")","=","{","}","[","]","'\'","|",",",".","/","?","'",";",":","~"]
#punctuation to remove
skillsets = [["python","c++","java","c#","ruby"," c ","verilog","hdl"], ["teamwork","leadership","communication","management","project management","analytical thinking"],["aws","vivado","matlab","simulink","vitis","git","perforce","jira","linux","microsoft office"],["mini-lab","signal generator","oscilloscope","soldering"]]
#list of skillsets, feel free to add or remove as per job 
text = str(text)
text = text.lower()
dummy = text
text = ""
for char in dummy :
	if(char not in punctuation):
		text = text + char 
#standardise data set by removing punctuation and lowering all characters

for skillset in skillsets:
	c = 0
	total = len(skillset)
	#used to check amount uised
	print("|=======================================")
	for skill in skillset:
		count = text.count(skill)
		#count skills in CV
		if(count>0):
			c = c+1
		print("| ",skill, ":",count)

	print("|---------------------------------------")
	print("|  Total:",c, "/",total, "(",(100*(c/total)),"%)")
	#print appropriate summary
print("|=======================================")
