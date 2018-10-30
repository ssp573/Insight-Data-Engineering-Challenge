import sys

#input:		list of tuples of data returned by read_data
#process: 	calculates the counts and total certified, percentage certified. Also sorts the list in decreasing order of number of certifieds and alphabetically for ties. 
#		Same function used to calculate top 10 states as well as occupations (inputs modified to achieve this)
#output: 	returns a sorted list of top 10 entries
def top_10(data):
	num_certified={}	#dictionary to count how many certified in each category
	certified=0		#counter for total number of certified
	for item in data:
		if item[0]=="CERTIFIED":
			if item[1] in num_certified:
				num_certified[item[1]]+=1
			else:
				num_certified[item[1]]=1
			certified+=1
	list_unsorted=[]	
	for key in num_certified:
		list_unsorted.append((key,num_certified[key],num_certified[key]/certified*100))		#creating unsorted list as required
	list_sorted = sorted(list_unsorted, key=lambda item: (-item[1], item[0]))			#sorting the list. using -item[1] to ensure descending order.
	return list_sorted[:10]
	

#input: 	top 10 entries received from the function top_10, type of output-(states or occupations)
#process:	creates the appropriate output file based on the type_out parameter. Creates the output string in semi-colon seperated format and stores it in the output file.
#output:	None
def print_top10(top_10,type_out):
	if type_out=="s":							#if the type of output is states, create top_10_states.txt
		string="TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n"
		outfile="top_10_states.txt"
	else:									#else create top_10_occupations.txt
		string="TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n"
		outfile="top_10_occupations.txt"
	for item in top_10:
		string+=item[0]+";"+str(item[1])+";"+str(round(item[2],1))+"%\n"	#building required line and adding to output string
	out_f=open("./output/"+outfile,'w')
	out_f.write(string[:-1])						#writing except last character to ignore the last \n
	out_f.close()


#input: 	filename to be processed
#process: 	creates a list of tuples for each line with only the relevant information, i.e: status, job name and state.
#		Also checks if any of the required fields is not available and exits if so.
#output: 	returns the list of tuples
def read_data(filename):
	with open(filename,"r") as input_file:
		data=[]
		string=input_file.read()
		if not string or string[0]=="\n":
			print("Empty file. Aborting.")		#abort program if file is empty
			exit()
		string_list=string.split("\n")
		#try catch blocks to see if any of the necessary fields are missing and if not, storing their indexes. 
		#Assuming the names of the relevant fields to be as given in the files uploaded on the drive. If that field name is not found, prompt the user for the current name of the field.
		#This is done to account for if the names of the fields are changed in the future.
		try:
			status_ind=string_list[0].split(";").index("CASE_STATUS")
		except:
			status_string=input("Assuming Status field to be named \"CASE_STATUS\" which was not found. If named differently, please mention here:")
			while True:			
				try:
					status_ind=string_list[0].split(";").index(status_string)
					break
				except:				
					status_string=input("Assuming Status field to be named \"CASE_STATUS\" which was not found. If named differently, please mention here:")
				
		try:
			name_ind=string_list[0].split(";").index("SOC_NAME")
		except:
			name_string=input("Assuming Occupation name field to be named \"SOC_NAME\" which was not found. If named differently, please mention here:")
			while True:
				try:			
					name_ind=string_list[0].split(";").index(name_string)
					break
				except:
					name_string=input("Assuming Occupation name field to be named \"SOC_NAME\" which was not found. If named differently, please mention here:")
		try:
			state_ind=string_list[0].split(";").index("WORKSITE_STATE")
		except:
			state_string=input("Assuming Work state field to be named \"WORKSITE_STATE\" which was not found. If named differently, please mention here:")
			while True:
				try:			
					state_ind=string_list[0].split(";").index(state_string)
					break
				except:				
					state_string=input("Assuming Work state field to be named \"WORKSITE_STATE\" which was not found. If named differently, please mention here:")
		
		for line in string_list[1:]:		#ignoring header, hence[1:]
			if line=="":
				continue		#ignoring empty lines
			line_split=line.split(";")
			data.append([line_split[status_ind],line_split[name_ind].replace("\"",""),line_split[state_ind]])
	return data


data=read_data('./input/'+sys.argv[1])
top_10s=top_10([[item[0],item[2]] for item in data])		#using only status and state fields for top 10 states
top_10o=top_10([item[:2] for item in data])			#using only status and occupation fields for top 10 occupations
print_top10(top_10s,"s")
print_top10(top_10o,"o")
print("Done Processing. Please check the output folder for the required files.")

