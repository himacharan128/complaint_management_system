import os
filename='file1'
filename2='file2'
def read(filename):
	f=open(filename,"r")
	print('*'*80)
	print('======================= > COMPLAINTS REGISTERED SO FAR < ===========================')
	print('*'*80)
	print(f.read())
	f.close()
def append(data2,stu,roll):
	f=open(filename,"a")
	i=0
	i+=1    
	f.write('@_' +str(roll) +'\n'+'roll number  : '+roll+'\n'+'student name : '+stu+'\n'+'complaint    : '+data2 +'\n')
	f.write('*'*80+'\n')
	f.close()
	print('#'*80)
	print(' '*20+'COMPLAINT REGISTERED SUCCESSFULLY!')
	print('#'*80)
def solve(role):
	while True:
		find_roll=input('enter roll number of the complaint you want to resolve : ')
		remark=input('enter remark or solution for the query                 : ')
		if role==2:
			data4='\n------->COMPLAINT RESOLVED BY CR !'
		elif role==3:
			data4='\n------->COMPLAINT RESOLVED BY PRINCIPAL !'
		line_number = find_query(find_roll,filename)
		if line_number==None:
			print('no complaint fount with entered roll number details \nPLEASE ENTER VALID DETAILS')
			continue

		with open(filename) as f:
			data_search=f.readlines()
		f=open(filename,"w")
		for idx, line in enumerate(data_search):
	 		if idx ==line_number-1:
	 			f.write(line+data4+'\n'+'Remark       :'+remark+'\n\n')
	 		else :
	 			f.write(line)
		break
def find_query(find_roll,filename):
	with open(filename) as f:
		data_search=f.readlines()
	line_count=0
	for line in data_search:
		line_count+=1
		if ('@_'+find_roll) in line:
			return line_count
def forward_query(forward_roll,remark):
	if  os.path.isfile("./"+filename):
		let=int(forward_roll)
		data_forward=''
		with open(filename) as f:
			data_search=f.readlines()
		line_count=0
		for line in data_search:
			line_count+=1
			if line_count  in (let,let+1,let+2,let+3,let+4):
				data_forward=data_forward+line
				if line_count==let:
					data_forward=data_forward+'Remark by CR : '+remark+'\n'
		f=open(filename2,'a')
		f.write(data_forward)
		f.close()
	else:
		data=''
		f=open(filename,"w")
		f.write(data + "\n")
		f.close()
		forward_query(forward_roll)	
while True:
	if  os.path.isfile("./"+filename):
		print('\n'+'+'*80)
		print('\n\t\t\t    1---> student\n\t\t\t    2---> cr\n\t\t\t    3---> principal')
		user_type=int(input('\nselect user type : '))
		if user_type==1:
			print('-'*80)
			print('\t\tFILL THE FOLLOWING DETAILS TO REGISTER A COMPLAINT ')
			print('-'*80)
			stud_name=input('enter your name      : ')
			stud_id=input('enter your id no     : ')
			stud_comp=input('enter your complaint : ')

			append(stud_comp,stud_name,stud_id)

		elif user_type==2:
			read(filename)
			cr_select=input('\n\n\t\t\t\t1---> solve\n\t\t\t\t2---> forward\n\t\t\t\t3---> exit\nselect an option : ')
			if cr_select=='1':
				solve(user_type)
				print(' \n')
				print('#'*80)
				print(' '*20+'COMPLAINT RESOLVED SUCCESSFULLY!')
				print('#'*80)
			elif cr_select=='2':
				find_roll=input('enter roll number of the complaint you want to forward : ')
				remark=input('enter remark for forwading this to higher authorities  : ')
				forward_roll=find_query(find_roll,filename)
				if forward_roll==None:
					print('no complaint fount with entered roll number details \nPLEASE ENTER VALID DETAILS')
					continue
				forward_query(forward_roll,remark)
				print('#'*80)
				print(' '*20+'COMPLAINT FORWARDED SUCCESSFULLY!')
				print('#'*80)
			elif cr_select=='3':
				print()
			else:
				print('you have selected wrong option\nPLEASE TRY AGAIN!')
				continue
		elif user_type==3:
			high_select=input(' '*20+'1--->check all queries\n'+' '*20+'2--->check forwarded queries\nselect an option : ')
			if high_select=='1':
				read(filename)
				x=input('DO YOU WANT TO SOLVE ANY QUERY(yes/no) : ')
				if x== 'yes':
					solve(user_type)
					print('#'*80)
					print(' '*20+'COMPLAINT RESOLVED SUCCESSFULLY!')
					print('#'*80)
			elif high_select=='2':
				read(filename2)
				x=input('DO YOU WANT TO SOLVE ANY QUERY(yes/no) : ')
				if x== 'yes':
					roll_file2=input('enter roll number of the complaint you want to solve : ')
					remark_file2=input('enter remark                                        : ')
					position=find_query(roll_file2,filename2)
					if position==None:
						print('no complaint fount with entered roll number details \nPLEASE ENTER VALID DETAILS')
						continue
					data4='\n------->COMPLAINT RESOLVED !'
					with open(filename2) as f:
						data_search=f.readlines()
					f=open(filename2,"w")
					for idx, line in enumerate(data_search):
	 					if idx ==position-1:
	 						f.write(line+data4+'\n'+'Remark       :'+remark_file2+'\n\n')
	 					else :
	 						f.write(line)
					print('\n\n'+'#'*80)
					print(' '*20+'COMPLAINT RESOLVED SUCCESSFULLY!')
					print('#'*80)

			else:
				print('you have selected wrong option\nPLEASE TRY AGAIN!')
				continue				

		else:
			print('@@@@@@@ YOU HAVE ENTERED INCORRECT user type @@@@@@@\n       Please try again!')
			continue
	else:
		data=''
		f=open(filename,"w")
		f.write(data + "\n")
		f.close()
		continue
	print()
	op=input('\t\t\t\t0---->  END\n\t\t\t\t1---->  RESTART\nselect an option : ')
	print()
	if op=='0':
		exit(0)
