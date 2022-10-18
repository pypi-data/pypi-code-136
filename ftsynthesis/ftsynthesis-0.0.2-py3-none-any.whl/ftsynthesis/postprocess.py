
from collections import OrderedDict
from icecream import ic
import error
import globalVariable as g
import re

parser = re.compile("[\{a-zA-Z0-9_.*/\->\+}]+")


def change_cnot_order_time_ordered(system_code):
	"""
		time ordered form 의 시스템 코드를 기준으로 commutable cnot 순서 교환하여 회로 depth 축소
	"""

	window = list()
	list_commutable = {}
	list_anti_commutable = {}

	new_system_code = []


	for time_idx, list_instructions in system_code.items():
		ic(time_idx, list_instructions)

		for gate_id, inst in enumerate(list_instructions):
			token = parser.findall(inst)
			if not len(token): continue

			ic(token)
			# 새로 들어온 게이트가 cnot 일 경우, 기존에 window 에 포함된 cnot 들과 관계 비교 확인 필요
			if token[0] in [g.str_gate_cnot]:
				ctrl, trgt = map(int, token[1:])

				# 현재 window 가 empty 이면, 무조건 window 에 삽입
				if not len(window):
					window.append({"ctrl": ctrl, "trgt": trgt, "gate": token[0], "gate_id": gate_id, "time_id": time_idx})
					
				# window 가 empty 가 아니면, window 에 포함된 cnot 게이트 들과 비교 필요
				else:
					flag_overlap = False
					ic(window, reversed(window))

					for item in reversed(window):
						# window 상에 포함된 cnot 과 완전 중복이면, cancel out
						if (item["ctrl"] == ctrl) and (item["trgt"] == trgt):
							ic("완전 중복")
							ic("before window")
							window.remove(item)
							ic("after window")
							break

						# ctrl 큐빗과 중복 : 
						# 1. window 에 추가
						# 2. trgt 큐빗에 1-큐빗 게이트가 인가되면 window 에 포함된 cnot 들 사이에 commute 가능함
						elif item["ctrl"] == ctrl:
							ic("ctrl 공유")
							element = {"ctrl": ctrl, "trgt": trgt, "gate": token[0], "gate_id": gate_id, "time_id": time_idx}
							ic("before window")
							window.append(element)
							ic("after window")
							ic("list commutable : ")
							list_commutable[trgt] = (item, element, "ctrl")
							ic("list anti commutable : ")
							list_anti_commutable[ctrl] = (item, element)
							flag_overlap = True
							break

						# trgt 큐빗과 중복
						# 1. window 에 추가
						# 2. 후행 cnot 의 ctrl 큐빗에 1-큐빗 게이트가 인가되면, window 에 포함된 cnot 들 사이에 commute 가능함
						elif item["trgt"] == trgt:
							element = {"ctrl": ctrl, "trgt": trgt, "gate": token[0], "gate_id": gate_id, "time_id": time_idx}
							ic("trgt 공유")
							ic("before window : ")
							window.append(element)
							ic("after window : ")

							ic("list commutable : ")
							list_commutable[ctrl] = (item, element, "trgt")
							ic("list anti commutable : ")
							list_anti_commutable[trgt] = (item, element)
							flag_overlap = True
							break

						# ctrl 또는 trgt 큐빗 공유 없이 두 개의 cnot 이 반대 큐빗에 중복이 있으면 -> commutable 하지 않음
						# 선행 cnot 제외하고, new_system_code 에 추가함
						# 후행 cnot 은 window 에 추가함
						elif (item["ctrl"] == trgt) or (item["trgt"] == ctrl):
							ic("큐빗 반대로 일부 공유")
							ic("before window : ")
							window.remove(item)
							ic("after window : ")
							new_system_code.append(item)
							ic(new_system_code)
							break

							# element = {"ctrl": ctrl, "trgt": trgt, "gate": token[0], "gate_id": gate_id, "time_id": time_idx}
							# window.append(element)
							# flag_overlap = True

					# 큐빗 overlap이 없으면, 새로운 cnot 을 window 에 추가함
					if not flag_overlap:
						window.append({"ctrl": ctrl, "trgt": trgt, "gate": token[0], "gate_id": gate_id, "time_id": time_idx})


			# window 상에 포함된 cnot 과 큐빗 중복되는 swap, cz 게이트가 들어오면 cnot 을 window 에서 제거하고, swap/cz 도 시스템 코드로..
			elif token[0] in [g.str_gate_swap, g.str_gate_cz]:
				ctrl, trgt = map(int, token[1:])
				flag_overlap = False
				
				ic(window, reversed(window))
				# window 상의 게이트와 큐빗 중복되면, window 상의 게이트
				for item in reversed(window):
					if (item["ctrl"] in [ctrl, trgt]) or (item["trgt"] in [ctrl, trgt]):
						ic("큐빗 일부 공유 ")
						ic("before window ")
						window.remove(item)
						ic("after window ")

						new_system_code.append([item["gate"], str(item["ctrl"]), str(item["trgt"])])
						new_system_code.append(token)

						ic(new_system_code)

						flag_overlap = True
						break

				# 중복이 없으면 그냥 시스템 코드로... (cnot 이 아니므로.. window 에는 삽입 x)
				if not flag_overlap:
					new_system_code.append(token)


			# barrier 이면, window 에 포함된 것 모두 삭제, new system code 로..
			elif token[0] in [g.str_barrier, g.str_barrier_all]:
				ic(window)
				for item in window:
					new_system_code.append([item["gate"], str(item["ctrl"]), str(item["trgt"])])
				
				# window 는 empty	
				window = []
				# barrier 명령은 new_system_code 로..
				new_system_code.append(token)
				ic(new_system_code)

			# 1-큐빗 게이트이면...
			else:
				# 게이트 특성에 따라 대상 큐빗 결정
				if token[0] in [g.str_gate_rz, g.str_gate_rx, g.str_gate_ry]: qubit = int(token[2])
				elif token[0] in [g.str_gate_u]: qubit = int(token[4])
				else: qubit = int(token[1])

				# measz 이면, token 상에서 -> 삭제
				if token[0] in [g.str_gate_measz]: token.remove("->")

				ic(qubit, list_commutable, list_anti_commutable)

				# 만약, 1-큐빗 게이트가 인가된 qubit 이 앞서 점검한 교환 가능 큐빗에 해당되면...
				# 실제로 교환할 것인지 결정할 필요가 있음
				if qubit in list_commutable:
					# 실제로 교환할 것인지 확인..
					# 조건 찾기
					# 선행 cnot, 후행 cnot, 그리고 공유하는 큐빗
					preceding, succeding, shared_qubit = list_commutable[qubit][:]
					
					ic(preceding, succeding, time_idx, preceding.get("time_id"), succeding.get("time_id"), preceding.get("trgt"), succeding.get("trgt"))
					ic(shared_qubit)

					# 선행 cnot 의 time idx 와 후행 cnot 의 time idx
					time_i = preceding.get("time_id")
					time_j = succeding.get("time_id")

					# 선행 cnot 의 ctrl 큐빗, trgt 큐빗
					preceding_cnot_ctrl = preceding.get("ctrl")
					preceding_cnot_trgt = preceding.get("trgt")
					
					# 후행 cnot 의 ctrl / trgt 큐빗
					succeding_cnot_ctrl = succeding.get("ctrl")
					succeding_cnot_trgt = succeding.get("trgt")

					# time_i 명령중 succeding_cnot_trgt 에 동작하는 1-qubit 게이트 존재 여부
					# time_j 명령중 preceding_cnot_trgt 에 동작하는 1-qubit 게이트 존재 여부
					# 둘다 존재하지 않으면 swap, 아니면 do not swap

					# time_i 스텝에.. 조작되는 큐빗 목록
					list_qubits = []

					for inst in system_code[time_i]:
						inst_token = parser.findall(inst)
						if inst_token[0] in [g.str_gate_cnot]: 
							# cnot 이면, preceding cnot 과 중복되면 skip, 아니면 list_qubits 에 추가
							if inst_token[1:] == [preceding_cnot_ctrl, preceding_cnot_trgt]: 
								continue
							else:
								list_qubits.extend(list(map(int, inst_token[1:])))

						if inst_token[0] in [g.str_gate_rz, g.str_gate_rx, g.str_gate_ry]:
							list_qubits.extend(list(map(int, inst_token[1])))

						else:
							list_qubits.extend(list(map(int, inst_token[1:])))

					ic(list_qubits, "at {}-th time".format(time_i))

					# 공유하는 큐빗이 ctrl 이면, 
					# 후행 cnot 의 trgt 큐빗에 1-큐빗 게이트가 time_i 에 인가되지 않거나 또는 
					# 선행 cnot 의 trgt 큐빗에 1-큐빗 게이트가 time_j 에 인가되지 않으면
					if shared_qubit == "ctrl":
						if succeding_cnot_trgt not in list_qubits: flag_condition_A = True
						else: flag_condition_A = False
					elif shared_qubit == "trgt":
						if succeding_cnot_ctrl not in list_qubits: flag_condition_A = True
						else: flag_condition_A = False	
					
					# time_j 스텝에...
					list_qubits = []
					for inst in system_code[time_j]:
						inst_token = parser.findall(inst)
						if inst_token[0] in [g.str_gate_cnot]: 
							if inst_token[1:] == [succeding_cnot_ctrl, succeding_cnot_trgt]:
								continue
							else:
								list_qubits.extend(list(map(int, inst_token[1:])))

						if inst_token[0] in [g.str_gate_rz, g.str_gate_rx, g.str_gate_ry]:
							list_qubits.extend(list(map(int, inst_token[1])))

						else:
							list_qubits.extend(list(map(int, inst_token[1:])))

					ic(list_qubits, "at {}-th time".format(time_j))

					if shared_qubit == "ctrl":
						if preceding_cnot_trgt not in list_qubits: flag_condition_B = True
						else: flag_condition_B = False
					elif shared_qubit == "trgt":
						if preceding_cnot_ctrl not in list_qubits: flag_condition_B = True
						else: flag_condition_B = False

					ic(flag_condition_A, flag_condition_B)

					if flag_condition_A and flag_condition_B:
						ic("step 5")
						ic(window)
						ic(preceding, preceding in window)
						ic(succeding, succeding in window)

						window.remove(preceding)
						window.remove(succeding)

						new_system_code.append([succeding["gate"], str(succeding["ctrl"]), str(succeding["trgt"])])
						new_system_code.append(token)
						
						new_system_code.append([preceding["gate"], str(preceding["ctrl"]), str(preceding["trgt"])])

						if shared_qubit == "ctrl":
							del list_commutable[qubit]
							ic(list_anti_commutable, succeding)
							del list_anti_commutable[succeding["ctrl"]]
						
						else:
							del list_commutable[qubit]
							ic(list_anti_commutable, succeding)
							del list_anti_commutable[succeding["trgt"]]
						# 동일한 value 를 list_anti_commutable 에서 삭제해야 함
					
					else:
						ic("step 6")
						ic(preceding)
						ic(succeding)
						ic(window)
						window.remove(preceding)
						window.remove(succeding)
						ic(window)

						ic(new_system_code)
						new_system_code.append([preceding["gate"], str(preceding["ctrl"]), str(preceding["trgt"])])
						new_system_code.append([succeding["gate"], str(succeding["ctrl"]), str(succeding["trgt"])])
						new_system_code.append(token)
						ic(new_system_code)

						if shared_qubit == "ctrl":
							del list_commutable[qubit]
							del list_anti_commutable[succeding["ctrl"]]
							# 동일한 value 를 list_commutable 에서 삭제해야 함
						else:
							del list_commutable[qubit]
							del list_anti_commutable[succeding["trgt"]]
							# 동일한 value 를 list_commutable 에서 삭제해야 함
				
				# 
				elif qubit in list_anti_commutable:
					preceding, succeding = list_commutable[qubit][:]
					ic("step 7")
					window.remove(preceding)
					window.remove(succeding)
					new_system_code.append([preceding["gate"], str(preceding["ctrl"]), str(preceding["trgt"])])
					new_system_code.append([succeding["gate"], str(succeding["ctrl"]), str(succeding["trgt"])])
					new_system_code.append(token)

					del list_anti_commutable[qubit]
					del list_commutable[succeding["trgt"]]
					# 동일한 value 를 list_commutable 에서 삭제하자.
					
				else:
					flag_overlap = False
					for item in reversed(window):
						if qubit in [item["ctrl"], item["trgt"]]:
							flag_overlap = True
							if token[0] in [g.str_gate_z]:
								ic("step 8")
								ic(item)
								ic(window)
								window.remove(item)
								ic(window)
								ic(new_system_code)
								new_system_code.append([item["gate"], str(item["ctrl"]), str(item["trgt"])])
								new_system_code.append(token)
								ic(new_system_code)

							else:
								ic("step 9")
								ic(item)
								ic(window)
								window.remove(item)
								ic(window)
								ic(new_system_code)
								new_system_code.append([item["gate"], str(item["ctrl"]), str(item["trgt"])])
								new_system_code.append(token)
								ic(new_system_code)

							break

					if not flag_overlap:
						new_system_code.append(token)
	
		ic(new_system_code)
	return new_system_code


def change_cnot_order(system_code):
	'''
		시스템 코드상에서 commutable cnot 의 순서를 교환하여, 회로 depth 축소
	'''

	window = list()
	list_commutable = {}
	list_anti_commutable = {}

	new_system_code = []

	for gate_id, inst in enumerate(system_code):
		ic("new gate : {}".format(inst))
		
		if inst[0] in [g.str_gate_cnot]:
			ctrl, trgt = inst[1:]

			if not len(window):
				ic("insert cnot {} into window ".format(inst))
				window.append({"ctrl": ctrl, "trgt": trgt, "gate": inst[0], "id": gate_id})

			else:
				flag_overlap = False
				for item in reversed(window):
					if (item["ctrl"] == ctrl) and (item["trgt"] == trgt):
						# 두 개의 cnot 이 중복됨 --> cancel both out
						# new system code 에도 포함시키지 않음
						ic("remove cnot {} in window due to redundancy".format(item))
						window.remove(item)
						flag_overlap = True

					elif item["ctrl"] == ctrl:
						# ctrl 공유 cnot
						element = {"ctrl": ctrl, "trgt": trgt, "gate": inst[0], "id": gate_id}
						ic("new cnot shares the control qubit {} with a cnot {} in window ".format(ctrl, item))
						window.append(element)
						list_commutable[trgt] = (item, element)
						list_anti_commutable[ctrl] = (item, element)
						ic(list_commutable, list_anti_commutable)
						flag_overlap = True

					elif item["trgt"] == trgt:
						# trgt 공유 cnot
						element = {"ctrl": ctrl, "trgt": trgt, "gate": inst[0], "id": gate_id}
						ic("new cnot shares the target qubit {} with a cnot {} in window".format(trgt, item))
						window.append(element)
						list_commutable[ctrl] = (item, element)
						list_anti_commutable[trgt] = (item, element)
						ic(list_commutable, list_anti_commutable)
						flag_overlap = True

					elif (item["ctrl"] == trgt) or (item["trgt"] == ctrl):
						# 
						window.remove(item)
						new_system_code.append(item)
						ic("new cnot works in the opposite direction with a cnot {} in window".format(item))
						element = {"ctrl": ctrl, "trgt": trgt, "gate": inst[0], "id": gate_id}
						window.apend(element)
						flag_overlap = True

				# 신규 cnot 이 기존 window 에 포함된 cnot 과 큐빗 중복 없으면, 
				# 기존 window 포함 cnot 을 그대로 유지하면서 신규 cnot 을 window 에 포함시킴
				if not flag_overlap:
					ic("new cnot does not share any working qubits in the cnots in window")
					window.append({"ctrl": ctrl, "trgt": trgt, "gate": inst[0], "id": gate_id})
					
		elif inst[0] in [g.str_gate_swap, g.str_gate_cz]:
			# cnot 과 동일 하게 처리함 : 다만, swap 및 cz 은 window 에 저장하지 않음
			ctrl, trgt = inst[1:]

			flag_overlap = False
			for item in reversed(window):
				# swap/cz 가 window 상의 cnot 과 동작하는 큐빗에 중복이 있으면, 
				# 기존 cnot 을 window 에서 제거 -> new_system code 로, swap/cz 역시 new_system_code 로..
				if (item["ctrl"] in [ctrl, trgt]) or (item["trgt"] in [ctrl, trgt]):
					ic("new gate {} shares the qubits for a cnot in window".format(inst))
					ic("therefore, a cnot {} is deleted from window ".format(item))
					window.remove(item)

					new_system_code.append([item["gate"], item["ctrl"], item["trgt"]])
					new_system_code.append(inst)
					flag_overlap = True
			
			# 중복이 없으면, swap/cz 만 new_system_code 로
			if not flag_overlap:
				new_system_code.append(inst)

		elif inst[0] in [g.str_barrier, g.str_barrier_all]:
			for item in window:
				window.remove(item)
				new_system_code.append([item["gate"], item["ctrl"], item["trgt"]])
			
			new_system_code.append(inst)

		else:
			# barrier 경우
			if inst[0] in [g.str_gate_rz]: qubit = inst[2]
			else: qubit = inst[1]
				
			# 1-qubit gate 경우, 어느 큐빗에 동작하는지가 중요함
			# commutable 가능 큐빗에 동작하면, 교환함
			if qubit in list_commutable: 
				ic("new gate {} shares the qubit {} that permits the cnot changes".format(inst, qubit))
				preceding, succeding = list_commutable[qubit][:]
				window.remove(preceding)
				window.remove(succeding)

				new_system_code.append([succeding["gate"], succeding["ctrl"], succeding["trgt"]])
				new_system_code.append([preceding["gate"], preceding["ctrl"], preceding["trgt"]])
				
				list_commutable.delete(qubit)
				list_anti_commutable.delete(qubit)
				ic("교환 발생: ", preceding, succeding, inst)

			# anti-commutable 큐빗에 동작하면, 교환하지 못함
			# new_system_code 에 기존 system_code 순서 그대로...
			elif qubit in list_anti_commutable:
				ic("new gate {} shares the qubit {} that does not permit the cnot changes".format(inst, qubit))
				preceding, succeding = list_anti_commutable[qubit][:]
				window.remove(preceding)
				window.remove(succeding)

				new_system_code.append([preceding["gate"], preceding["ctrl"], preceding["trgt"]])
				new_system_code.append([succeding["gate"], succeding["ctrl"], succeding["trgt"]])
				list_commutable.delete(qubit)
				list_anti_commutable.delete(qubit)
				ic("교환 불가: ", preceding, succeding, inst)
				
			# window 에 포함된 하나의 cnot 과 관련이 있거나 없거나...
			else:	
				flag_overlap = False
				for item in reversed(window):
					if qubit in [item["ctrl"], item["trgt"]]:
						flag_overlap = True

						# 1-qubit 게이트가 Z 이면...
						# cnot 과 commutable 해서, 위치 이동 가능....  
						# 일단은 다른 1-큐빗 게이트와 동일하게...
						if inst[0] in [g.str_gate_z]:
							window.remove(item)
							new_system_code.append([item["gate"], item["ctrl"], item["trgt"]])
							new_system_code.append(inst)
						# 
						else:
							ic("new gate {} shares the qubit {} where cnot {} in window act".format(inst, qubit, item))
							window.remove(item)
							ic(item)
							new_system_code.append([item["gate"], item["ctrl"], item["trgt"]])
							new_system_code.append(inst)

				# 1-q 게이트가 window 상의 cnot 과 관련이 없으면, new_system_code 로 바로..
				if not flag_overlap:
					ic("new 1-qubit gate {} does not share any qubit where cnot in window".format(inst))
					new_system_code.append(inst)

		ic(window)
		ic(new_system_code)

	ic("변경 : ", new_system_code)
	
	return new_system_code
