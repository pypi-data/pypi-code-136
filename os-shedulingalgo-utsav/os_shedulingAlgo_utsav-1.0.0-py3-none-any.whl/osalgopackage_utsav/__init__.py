

class BestShedulingAlgo:

	main_processes=[]
	fcfs_processes=[]
	sjf_processes=[]
	priority_processes=[]
	rr_processes=[]

	AVG_WT_FCFS=0.000
	AVG_WT_SJF=0.000
	AVG_WT_PRIORITY=0.000
	AVG_WT_RR=0.000

	constant_dicts={
		"ST":0,
		"TQ":3,
		"WT":0,
		"REM":0
		}

	def __init__(self,size):
		self.size=size
		print(f"{size} length size is initialized")

	def __taking_input(self):
		print('Enter input in this manner --> processName AT BT P')
		for i in range(0,self.size):
			name=input('Enter process name: ')
			at=input('Enter AT(Arrival Time): ')
			bt=input('Enter BT(Burst Time): ')
			p=input('Enter P(Priority): ')
			inpt={
				"name":name,
				"AT":int(at),
				"BT":int(bt),
				"P":int(p)
			}

			self.main_processes.append({**inpt,**self.constant_dicts})
			self.fcfs_processes.append({**inpt,**self.constant_dicts})
			self.sjf_processes.append({**inpt,**self.constant_dicts})
			self.priority_processes.append({**inpt,**self.constant_dicts})
			self.rr_processes.append({**inpt,**self.constant_dicts})


	def __FCFS(self):
		g=0
		avg=0.000
		for i in self.fcfs_processes:
			i['ST']=g
			g=g+i['BT']
			i['WT']=i['ST']-i['AT']
			avg=avg+i['WT']
		self.AVG_WT_FCFS=avg/self.size

	def __SJF(self):
		sort_sjf=sorted(self.sjf_processes,key=lambda x:x['BT'])
		g=0
		avg=0.000
		for i in sort_sjf:
			i['ST']=g
			g=g+i['BT']
			i['WT']=i['ST']-i['AT']
			avg=avg+i['WT']
		self.AVG_WT_SJF=avg/self.size

	def __PRIORITY(self):
		sort_priority=sorted(self.priority_processes,key=lambda x:x['P'],reverse=True)
		g=0
		avg=0.000
		for i in sort_priority:
			i['ST']=g
			g=g+i['BT']
			i['WT']=i['ST']-i['AT']
			avg=avg+i['WT']
		print(avg)
		self.AVG_WT_PRIORITY=avg/self.size

	def __ROUND_ROBIN(self):
		g=0
		avg=0.000
		sum_wt=1
		while sum_wt:
			sum_wt=0
			for i in self.rr_processes:
				if(i['BT']<i['TQ'] and i['BT']):
					i['REM']=i['BT']
					i['WT']=i['WT']+(g-i['AT'])
					g=g+i['REM']
					i['BT']=0

				elif i['BT']>0:
					i['REM']=i['BT']-i['TQ']
					i['BT']=i['REM']
					i['WT']=i['WT']+(g-i['AT'])
					g=g+i['TQ']
					i['AT']=g	

				sum_wt=sum_wt+i['BT']

		for i in self.rr_processes:
			avg=avg+i['WT']
		print(avg)
		self.AVG_WT_RR=avg/self.size

	def RunAndCompare(self):
		self.__taking_input()
		self.__FCFS()
		self.__SJF()
		self.__PRIORITY()
		self.__ROUND_ROBIN()
		print("Unchanged inputed process.........")
		for i in self.main_processes:
			print(i)
		print()

		print("changed process for FCFS.........")
		for i in self.fcfs_processes:
			print(i)
		print()

		print("changed process for SJF.........")
		for i in self.sjf_processes:
			print(i)
		print()

		print("changed process for PRIORITY.........")
		for i in self.priority_processes:
			print(i)
		print()

		print("changed process for ROUND_ROBIN.........")
		for i in self.rr_processes:
			print(i)
		print()

		res={
			"FCFS":self.AVG_WT_FCFS,
			"SJF":self.AVG_WT_SJF,
			"PRIORITY":self.AVG_WT_PRIORITY,
			"ROUND_ROBIN":self.AVG_WT_RR,
		}
		print()
		print("AVERAGE WAITING TIMES....")
		print(res)
		print()
		minimum=min([self.AVG_WT_FCFS,self.AVG_WT_SJF,self.AVG_WT_PRIORITY,self.AVG_WT_RR])
		key_list = list(res.keys())
		val_list = list(res.values())
		print("Best Algorithm For this set of processes is--->",minimum,f"[{key_list[val_list.index(minimum)]}]")




