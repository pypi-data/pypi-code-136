
import collections
import re
import copy
from pprint import pprint
from icecream import ic
import error
import globalVariable as g
import itertools
from math import *


get_bigger = lambda a, b: a if a>b else b


def cancel_redundancy(syscode):
	"""
		function to cancel out the redundant quantum gates in time order

		args:
			syscode in list
	"""

	table = collections.defaultdict(list)

	for idx, inst in enumerate(syscode):
		# 2-qubit gate : typeA (control, target 큐빗 명시가 중요한 게이트)
		if inst[0] in [g.str_gate_cnot, g.str_gate_cz]:
			if len(table[inst[1]]) and len(table[inst[2]]):
				# 새로운 명령과 이전 명령 비교
				last_instA = table[inst[1]][-1]
				last_instB = table[inst[2]][-1]

				conditionA = (last_instA["gate"] == inst[0]) and (last_instA["qubits"] == inst[1:])
				conditionB = (last_instB["gate"] == inst[0]) and (last_instB["qubits"] == inst[1:])

				# 동일하면
				if conditionA and conditionB:
					table[inst[1]].pop()
					table[inst[2]].pop()

				# 다르면
				else:
					table[inst[1]].append({"gate": inst[0], "qubits": inst[1:], "idx": idx})
					table[inst[2]].append({"gate": inst[0], "qubits": inst[1:], "idx": idx})

			else:
				table[inst[1]].append({"gate": inst[0], "qubits": inst[1:], "idx": idx})
				table[inst[2]].append({"gate": inst[0], "qubits": inst[1:], "idx": idx})

		# 2-qubit gate : typeB (control, target 큐빗 명시가 필요없는 게이트)
		elif inst[0] in [g.str_gate_swap]:
			if len(table[inst[1]]) and len(table[inst[2]]):
				# 새로운 명령과 이전 명령 비교
				last_instA = table[inst[1]][-1]
				last_instB = table[inst[2]][-1]

				conditionA = (last_instA["gate"] == inst[0]) and (set(last_instA["qubits"]) == set(inst[1:]))
				conditionB = (last_instB["gate"] == inst[0]) and (set(last_instB["qubits"]) == set(inst[1:]))

				# 동일하면
				if conditionA and conditionB:
					table[inst[1]].pop()
					table[inst[2]].pop()

				# 다르면
				else:
					table[inst[1]].append({"gate": inst[0], "qubits": inst[1:], "idx": idx})
					table[inst[2]].append({"gate": inst[0], "qubits": inst[1:], "idx": idx})

			else:
				table[inst[1]].append({"gate": inst[0], "qubits": inst[1:], "idx": idx})
				table[inst[2]].append({"gate": inst[0], "qubits": inst[1:], "idx": idx})

		# barrier-All
		elif inst[0] in [g.str_barrier_all]:
			for qubit in table.keys():
				table[qubit].append({"gate": g.str_barrier_all, "idx": idx})

		# selective barrier : 
		elif inst[0] in [g.str_barrier]:
			list_qubits = inst[1]
			for qubit in list_qubits:
				table[qubit].append({"gate": g.str_barrier, "qubits": list_qubits, "idx": idx})

		# 1-qubit gate
		elif inst[0] in [g.str_gate_rz]:
			if len(table[inst[2]]):
				last_inst = table[inst[2]][-1]

				# Rz 게이트가 연속되면, angle 확인 후, 앞선 게이트의 angle 값을 변경
				if (last_inst["gate"] == inst[0]) and (last_inst["qubits"] == inst[2:]):
					new_angle = float(eval(last_inst["angle"])) + float(eval(inst[1]))
					table[inst[2]][-1]["angle"] = str(new_angle)

				else:
					table[inst[2]].append({"gate": inst[0], "qubits": [inst[2]], "idx": idx, "angle": inst[1]})
			else:
				table[inst[2]].append({"gate": inst[0], "qubits": [inst[2]], "idx": idx, "angle": inst[1]})
		
		elif inst[0] in [g.str_gate_u]:
			if len(table[inst[2]]):
				last_inst = table[inst[2]][-1]
				if last_inst["gate"] == inst[0] and last_inst["qubits"] == inst[2:]:
					new_angle = {}
					for axis in ["x", "z", "y"]:
						new_angle[axis] = float(eval(last_inst["angle"][axis])) + float(eval(inst[1][axis]))
					table[inst[2]][-1]["angle"] = new_angle
				else:
					table[inst[2]].append({"gate": inst[0], "qubits": [inst[2]], "angle": inst[1], "idx": idx})	
			else:
				table[inst[2]].append({"gate": inst[0], "qubits": [inst[2]], "angle": inst[1], "idx": idx})

		else:
			# 새로운 명령과 이전 명령 비교
			if len(table[inst[1]]):
				last_inst = table[inst[1]][-1]

				# 동일하면
				if (last_inst["gate"] == inst[0]) and (last_inst["qubits"] == inst[1:]):
					table[inst[1]].pop()

				# 다르면
				else:
					table[inst[1]].append({"gate": inst[0], "qubits": [inst[1]], "idx": idx})	

			else:
				table[inst[1]].append({"gate": inst[0], "qubits": [inst[1]], "idx": idx})

	temp_syscode = {}
	for v_list in list(table.values()):
		for v in v_list:
			temp_syscode[v["idx"]] = v
	
	sorted_index = sorted(temp_syscode.keys())

	post_processed_syscode = []
	for k in sorted_index:
		v = temp_syscode[k]
		if v["gate"] in [g.str_gate_cnot, g.str_gate_cz, g.str_gate_swap]:
			post_processed_syscode.append([v["gate"], v["qubits"][0], v["qubits"][1]])
		
		elif v["gate"] in [g.str_gate_measz, g.str_gate_measx]:
			post_processed_syscode.append([v["gate"], v["qubits"][0], v["qubits"][0]])
		
		elif v["gate"] in [g.str_gate_rz, g.str_gate_u]:
			post_processed_syscode.append([v["gate"], v["angle"], v["qubits"][0]])

		# barrier-all
		elif v["gate"] == g.str_barrier_all:
			post_processed_syscode.append([v["gate"]])
			
		# selective barrier
		elif v["gate"] == g.str_barrier:
			post_processed_syscode.append([v["gate"], v["qubits"]])

		else:
			post_processed_syscode.append([v["gate"], v["qubits"][0]])

	return post_processed_syscode	


def transform_time_ordered_syscode(syscode, qubit_mapping):
	
	inverse_qubit_mapping = {v: k for k, v in qubit_mapping.items()}

	collections_qubits = collections.defaultdict(lambda: collections.defaultdict(bool))

	list_working_qubits = []
	circuit_index = 0

	collections_circuits = collections.defaultdict(object)
	circuit = collections.defaultdict(list)
	qubit_time_index = collections.defaultdict(int)

	for inst in syscode:
		if inst[0] in [g.str_gate_cnot, g.str_gate_cz, g.str_gate_swap]:
			ctrl, trgt = inst[1:]
			ctrl_name = inverse_qubit_mapping[ctrl]
			trgt_name = inverse_qubit_mapping[trgt]

			time_index = get_bigger(qubit_time_index[ctrl_name], qubit_time_index[trgt_name])
			circuit[time_index].append(inst)

			qubit_time_index[ctrl_name] = qubit_time_index[trgt_name] = time_index + 1

			if inst[0] == g.str_gate_swap:
				inverse_qubit_mapping[ctrl], inverse_qubit_mapping[trgt] =\
					inverse_qubit_mapping[trgt], inverse_qubit_mapping[ctrl]

		elif inst[0] in [g.str_gate_prepz, g.str_gate_prepx]:
			qubit_index = inst[1]
			qubit_name = inverse_qubit_mapping[qubit_index]

			qubit_type = qubit_name
			while qubit_type[-1].isdigit(): qubit_type = qubit_type[:-1]
			collections_qubits[qubit_type][qubit_name] = True

			circuit[qubit_time_index[qubit_name]].append(inst)
			qubit_time_index[qubit_name]+=1

		elif inst[0] in [g.str_gate_measz, g.str_gate_measx]:
			qubit_index = inst[1]
			qubit_name = inverse_qubit_mapping[qubit_index]

			qubit_type = qubit_name
			while qubit_type[-1].isdigit(): qubit_type = qubit_type[:-1]
			collections_qubits[qubit_type][qubit_name] = False

			circuit[qubit_time_index[qubit_name]].append(inst)
			qubit_time_index[qubit_name] += 1

			if not any(collections_qubits[qubit_type].values()): 
				collections_circuits[circuit_index] = circuit
				for qubit in qubit_time_index.keys(): qubit_time_index[qubit] = 0

				circuit = collections.defaultdict(list)
				circuit_index+=1
		else:
			qubit_index = inst[1]
			qubit_name = inverse_qubit_mapping[qubit_index]

			circuit[qubit_time_index[qubit_name]].append(inst)
			qubit_time_index[qubit_name]+=1

	inverse_qubit_mapping = {v: k for k, v in qubit_mapping.items()}
	for circuit_idx, circuit in collections_circuits.items():
		print(circuit_idx)
		for time_idx, instructions in circuit.items():
			for inst in instructions:
				if inst[0] in [g.str_gate_swap, g.str_gate_cnot]:
					print(inst, inst[0], inverse_qubit_mapping[inst[1]], inverse_qubit_mapping[inst[2]])

					if inst[0] == g.str_gate_swap:
						inverse_qubit_mapping[inst[1]], inverse_qubit_mapping[inst[2]] =\
							inverse_qubit_mapping[inst[2]], inverse_qubit_mapping[inst[1]]
				else:
					print(inst, inst[0], inverse_qubit_mapping[inst[1]])
		print("\n")

	pprint(collections_circuits)



# def transform_ordered_syscode_barrier(syscode, qubit_mapping, **kwargs):
# 	"""
# 		A function to transform system code listed in a plain list to time ordered system code in dictionary format.
# 		Besides, the whole circuit is decomposed into several partial sub-circuits also time ordered.
# 	"""

# 	if "postprocessing" in kwargs and kwargs["postprocessing"]:
# 		number_qubits = len(qubit_mapping.keys())
# 		syscode = process_syscode(syscode, number_qubits)
	
# 	if "barrier" in kwargs: 
# 		group_barrier_qubits = kwargs["barrier"]
# 	else:
# 		group_barrier_qubits = []

# 	syscode_whole_circuit = collections.defaultdict(lambda: collections.defaultdict(list))
# 	syscode_subcircuit = collections.defaultdict(list)

# 	status_barrier_qubits = {}
# 	for qubit_group in range(len(group_barrier_qubits)):
# 		status_barrier_qubits[qubit_group] = {qubit: False for qubit in group_barrier_qubits[qubit_group]}

# 	# barrier qubit 의 현재 상태 : False after Preparation, True after Measurement
# 	# status_barrier_qubits = {{k: False for k in group_barrier_qubits[qubit_type]} for qubit_type in range(len(group_barrier_qubits))}

# 	# sub_circuit 을 whole circuit 으로 추가하는 flag
# 	# status_barrier_qubit[type] 내 모든 큐빗이 True 가 되면, flip the status: False -> True
# 	flag_insert_to_whole_circuit = {k: False for k in range(len(group_barrier_qubits))}

# 	table_qubit_mapping = copy.deepcopy(qubit_mapping)
# 	table_inverse_mapping = {v: k for k, v in table_qubit_mapping.items()}

# 	time_index = collections.defaultdict(int)
# 	last_time_measurement = collections.defaultdict(int)

# 	arxiv_time_index = collections.defaultdict(lambda: collections.defaultdict(int))
# 	# global_time_index = collections.defaultdict(int)

# 	sub_circuit_index = 0
# 	parser = re.compile("[\{a-zA-Z0-9_.*/\->\+}]+")

# 	for inst in syscode:
# 		if inst[0] in ["CNOT", "CZ", "cx", "SWAP"]:
# 			ctrl, trgt = inst[1:]
# 			applying_index = max(time_index[ctrl], time_index[trgt])
# 			# 
# 			time_index[ctrl] = time_index[trgt] = applying_index+1

# 			# global_applying_index = max(global_time_index[ctrl], global_time_index[trgt])
# 			# global_time_index[ctrl] = global_time_index[trgt] = global_applying_index+1

# 			list_command = "{} {},{}".format(inst[0], ctrl, trgt)
# 			# list_command = "{} {},{} [{}]".format(inst[0], ctrl, trgt, global_time_index[ctrl]-1)
# 			# list_command = "{} {},{} [{}, {}]".format(inst[0], table_inverse_mapping[ctrl], table_inverse_mapping[trgt], global_time_index[ctrl]-1, global_time_index[trgt]-1)

# 			if inst[0] in ["SWAP"]:
# 				table_inverse_mapping[ctrl], table_inverse_mapping[trgt] =\
# 					table_inverse_mapping[trgt], table_inverse_mapping[ctrl]
# 				table_qubit_mapping.update({v: k for k, v in table_inverse_mapping.items()})

# 		else:
# 			if inst[0] in ["Rz", "Rx", "Ry", "P"]:
# 				angle, qubit = inst[1:]
# 				list_command = "{}({}) {}".format(inst[0], angle, qubit)
# 				# list_command = "{}({}) {} [{}]".format(inst[0], angle, qubit, global_time_index[qubit])
# 				# list_command = "{}({}) {} [{}]".format(inst[0], angle, table_inverse_mapping[qubit], global_time_index[qubit])

# 			elif inst[0] in ["U"]:
# 				angle_x, angle_y, angle_z, qubit = inst[1:]
# 				list_command = "{}({},{},{}) {}".format(inst[0], angle_x, angle_y, angle_z, qubit)
# 				# list_command = "{}({},{},{}) {} [{}]".format(inst[0], angle_x, angle_y, angle_z, qubit, global_time_index[qubit])
# 				# list_command = "{}({},{},{}) {} [{}]".format(inst[0], angle_x, angle_y, angle_z, table_inverse_mapping[qubit], global_time_index[qubit])

# 			elif inst[0] in ["PrepZ", "PrepX"]:
# 				qubit = inst[1]
# 				qubit_name = table_inverse_mapping[qubit]
# 				list_command = "{} {}".format(inst[0], qubit)
# 				# list_command = "{} {} [{}]".format(inst[0], qubit, global_time_index[qubit])
# 				# list_command = "{} {} [{}]".format(inst[0], qubit_name, global_time_index[qubit])

# 			elif inst[0] in ["MeasZ", "MeasX"]:
# 				qubit, cbit, *arguments = inst[1:]
# 				qubit_name = table_inverse_mapping[qubit]

# 				list_str_command = [inst[0], str(qubit), "->", str(cbit)]
# 				# list_str_command = [inst[0], qubit_name, str(cbit)]

# 				if len(arguments):
# 					sub_args_command = []
# 					for value in arguments:
# 						if value.isdigit():
# 							sub_args_command.append("expected={}".format(str(value)))
# 						else:
# 							sub_args_command.append("role={}".format(value))
# 					str_args = ",".join(sub_args_command)
# 					str_args = "(" + str_args + ")"
# 					list_str_command.append(str_args)

# 				# list_str_command.append(str(global_time_index[qubit]))
# 				list_command = " ".join(list_str_command)

# 				# 큐빗 측정 후, 관련 상태 변수를 False -> True 로 변환
# 				for qubit_group, qubit_list in enumerate(group_barrier_qubits):
# 					if qubit_name in qubit_list:
# 						status_barrier_qubits[qubit_group][qubit_name] = True
# 						if last_time_measurement[qubit_group] < time_index[qubit]:
# 							last_time_measurement[qubit_group] = time_index[qubit]

# 						if all(status_barrier_qubits[qubit_group].values()):
# 							flag_insert_to_whole_circuit[qubit_group] = True

# 					# data 큐빗들은 시간 순서상, ancilla 큐빗의 verification 이후에 동작 가능함
# 					# 따라서, data 큐빗의 시간 index 는 verification 큐빗의 시간대로 설정 가능함
# 							for k, v in table_qubit_mapping.items():
# 								if "data" in k:
# 									time_index[v] = time_index[qubit]
# 									# global_time_index[v] = global_time_index[qubit]
# 			else:
# 				qubit = inst[1]
# 				list_command = "{} {}".format(inst[0], qubit)
# 				# list_command = "{} {} [{}]".format(inst[0], qubit, global_time_index[qubit])
# 				# list_command = "{} {} [{}]".format(inst[0], table_inverse_mapping[qubit], global_time_index[qubit])

# 			applying_index = time_index[qubit]
# 			time_index[qubit] += 1
# 			# global_time_index[qubit] += 1

# 		syscode_subcircuit[applying_index].append(list_command)
		
# 		for qubit_group, status in flag_insert_to_whole_circuit.items():
# 			## method 1
# 			if status:
# 				syscode_whole_circuit[sub_circuit_index] = syscode_subcircuit
# 				arxiv_time_index[sub_circuit_index] = copy.deepcopy(time_index)

# 				time_index.update({qubit: 0 for qubit in time_index.keys()})
# 				syscode_subcircuit = collections.defaultdict(list)

# 				# 전체 시스템 코드에 추가 후, 관련 상태 변수를 True -> False 로 변환
# 				flag_insert_to_whole_circuit[qubit_group] = False

# 				# 전체 시스템 코드에 추가 후, 큐빗의 상태를 나타내는 값도 False 로 변경
# 				status_barrier_qubits[qubit_group].update({qubit: False 
# 					for qubit in status_barrier_qubits[qubit_group].keys()})

# 				sub_circuit_index+=1
			
# 			# # method 2
# 			# if status:
# 			# 	total_subcircuit_depth = max(syscode_subcircuit.keys())
								
# 			# 	# ic(total_subcircuit_depth, applying_index, last_time_measurement[qubit_group])
# 			# 	last_measurement_applied_time = last_time_measurement[qubit_group]
# 			# 	if last_measurement_applied_time == total_subcircuit_depth:
# 			# 		syscode_whole_circuit[sub_circuit_index] = syscode_subcircuit
# 			# 		arxiv_time_index[sub_circuit_index] = copy.deepcopy(time_index)

# 			# 		time_index.update({qubit: 0 for qubit in time_index.keys()})
# 			# 		# syscode_subcircuit 도 초기화
# 			# 		syscode_subcircuit = collections.defaultdict(list)

# 			# 	elif last_measurement_applied_time < total_subcircuit_depth:
# 			# 		temp_syscode = collections.defaultdict(list)
# 			# 		reference_time_index = last_measurement_applied_time+1
# 			# 		for idx in range(reference_time_index, total_subcircuit_depth+1):
# 			# 			temp_syscode[idx - reference_time_index] = syscode_subcircuit[idx]
# 			# 			del syscode_subcircuit[idx]
					
# 			# 		syscode_whole_circuit[sub_circuit_index] = syscode_subcircuit
# 			# 		arxiv_time_index[sub_circuit_index] = copy.deepcopy(time_index)

# 			# 		syscode_subcircuit = temp_syscode

# 			# 		time_index.update({qubit: 0 for qubit in time_index.keys()})
# 			# 		for tid, instructions in temp_syscode.items():
# 			# 			for inst in instructions:
# 			# 				token = parser.findall(inst)
# 			# 				if token[0] in ["SWAP", "CNOT", "CZ"]:
# 			# 					ctrl, trgt = token[1:]
# 			# 					time_index[ctrl] = time_index[trgt] = max(time_index[ctrl], time_index[trgt]) + 1
# 			# 				else:
# 			# 					if token[0] in ["Rz", "Rx", "Ry", "P"]: 
# 			# 						angle, qubit = token[1:]
# 			# 					elif token[0] in ["U"]:
# 			# 						angle_x, angle_y, angle_z, qubit = token[1:]
# 			# 					elif token[0] in ["PrepZ", "PrepX"]:
# 			# 						qubit = token[1]
# 			# 					elif token[0] in ["MeasZ", "MeasX"]:
# 			# 						qubit, cbit, *arguments = token[1:]
# 			# 					else:
# 			# 						qubit = token[1]
							
# 			# 					time_index[qubit]+=1

# 			# 	# 전체 시스템 코드에 추가 후, 관련 상태 변수를 True -> False 로 변환
# 			# 	flag_insert_to_whole_circuit[qubit_group] = False

# 			# 	# 전체 시스템 코드에 추가 후, 큐빗의 상태를 나타내는 값도 False 로 변경
# 			# 	status_barrier_qubits[qubit_group].update({qubit: False 
# 			# 		for qubit in status_barrier_qubits[qubit_group].keys()})

# 			# 	last_time_measurement[qubit_group] = 0
# 			# 	# time index 초기화
# 			# 	sub_circuit_index+=1
				
# 	# pprint(arxiv_time_index)

# 	# 시스템 코드에 대해서 관련 처리 후, whole circuit 에 추가되지 못하고, subcircuit 에 남아 있는 내용이 있다면,
# 	# 이들을 추가로 whole circuit 에 추가함
# 	if len(syscode_subcircuit):
# 		syscode_whole_circuit[sub_circuit_index] = syscode_subcircuit

# 	return syscode_whole_circuit	


# def transform_ordered_syscode_with_barrier(syscode, qubit_mapping, **kwargs):
# 	# ancilla 큐빗의 PrepZ - MeasZ 단위로 block 화

# 	collection_blocks = collections.defaultdict(lambda: collections.defaultdict(list))

# 	time_index_per_qubit = collections.defaultdict(int)
# 	block_index_per_qubit = collections.defaultdict(int)

# 	table_qubit_mapping = copy.deepcopy(qubit_mapping)
# 	table_inverse_mapping = {v: k for k, v in table_qubit_mapping.items()}

# 	# list of ancilla qubits: activated or inactivated
# 	group_ancilla_qubits = collections.defaultdict(lambda: collections.defaultdict())

# 	for inst in syscode:
# 		if inst[0] in [g.str_gate_cnot, g.str_gate_cz, g.str_gate_swap]:
# 			ctrl, trgt = inst[1:]

# 			if block_index_per_qubit[ctrl] == block_index_per_qubit[trgt]:
# 				applying_block_index = block_index_per_qubit[ctrl]
# 				applying_time_index = get_bigger(time_index_per_qubit[ctrl], time_index_per_qubit[trgt])

# 			elif block_index_per_qubit[ctrl] > block_index_per_qubit[trgt]:
# 				applying_block_index = block_index_per_qubit[ctrl]
# 				applying_time_index = time_index_per_qubit[ctrl]

# 			else:
# 				applying_block_index = block_index_per_qubit[trgt]
# 				applying_time_index = time_index_per_qubit[trgt]

# 			# str_command = "{} {},{}".format(inst[0], ctrl, trgt)
# 			str_command = "{} {},{}".format(inst[0], table_inverse_mapping[ctrl], table_inverse_mapping[trgt])
# 			collection_blocks[applying_block_index][applying_time_index].append(str_command)

# 			time_index_per_qubit[ctrl] = time_index_per_qubit[trgt] = applying_time_index+1
# 			block_index_per_qubit[ctrl] = block_index_per_qubit[trgt] = applying_block_index

# 			if inst[0] == g.str_gate_swap:
# 				table_inverse_mapping[ctrl], table_inverse_mapping[trgt] =\
# 					table_inverse_mapping[trgt], table_inverse_mapping[ctrl]
# 				table_qubit_mapping.update({v: k for k, v in table_inverse_mapping.items()})


# 		elif inst[0] in [g.str_barrier, g.str_barrier_all]:
# 			if inst[0] == g.str_barrier: target_qubits = inst[1:]
# 			else:
# 				target_qubits = list(table_qubit_mapping.values())

# 			# barrier 만나면, 다음 block 으로 이동
# 			for qubit in target_qubits:
# 				block_index_per_qubit[qubit] += 1
# 				time_index_per_qubit[qubit] = 0

# 		else:
# 			# preparation 만나면, group_qub
# 			if inst[0] in [g.str_gate_prepz, g.str_gate_prepx]:
# 				qubit = inst[1]

# 				qubit_name = table_inverse_mapping[qubit]

# 				while qubit_name[-1].isdigit(): qubit_name = qubit_name[:-1]


# 				group_ancilla_qubits[qubit_name][table_inverse_mapping[qubit]] = True

# 				# str_command = "{} {}".format(inst[0], qubit)
# 				str_command = "{} {}".format(inst[0], table_inverse_mapping[qubit])

# 				applying_block_index = block_index_per_qubit[qubit]
# 				applying_time_index = time_index_per_qubit[qubit]

# 				collection_blocks[applying_block_index][applying_time_index].append(str_command)

# 				time_index_per_qubit[qubit] = applying_time_index + 1


# 			elif inst[0] in [g.str_gate_h]:
# 				qubit = inst[1]
# 				str_command = "{} {}".format(inst[0], table_inverse_mapping[qubit])
# 				applying_block_index = block_index_per_qubit[qubit]
# 				applying_time_index = time_index_per_qubit[qubit]

# 				collection_blocks[applying_block_index][applying_time_index].append(str_command)
# 				time_index_per_qubit[qubit] = applying_time_index+1

# 			elif inst[0] in [g.str_gate_measz, g.str_gate_measx]:
# 				qubit, cbit, *arguments = inst[1:]
# 				qubit_name = table_inverse_mapping[qubit]

# 				# list_str_command = [inst[0], str(qubit), "->", str(cbit)]
# 				list_str_command = [inst[0], qubit_name, "->", str(cbit)]

# 				if len(arguments):
# 					sub_args_command = []
# 					for value in arguments:
# 						if value.isdigit():
# 							sub_args_command.append("expected={}".format(str(value)))
# 						else:
# 							sub_args_command.append("role={}".format(value))

# 					str_args = ",".join(sub_args_command)
# 					str_args = "(" + str_args + ")"
# 					list_str_command.append(str_args)

# 					str_command = " ".join(list_str_command)

# 				applying_block_index = block_index_per_qubit[qubit]
# 				applying_time_index = time_index_per_qubit[qubit]

# 				collection_blocks[applying_block_index][applying_time_index].append(str_command)

# 				while qubit_name[-1].isdigit(): qubit_name = qubit_name[:-1]
# 				group_ancilla_qubits[qubit_name][table_inverse_mapping[qubit]] = False

# 				# 모두가 false 이면... block 완성
# 				# 해당 큐빗에 대한 block index 1 increment
# 				if not any(group_ancilla_qubits[qubit_name].values()):
# 					for qubit in group_ancilla_qubits[qubit_name]:
# 						block_index_per_qubit[table_qubit_mapping[qubit]] += 1
# 						time_index_per_qubit[table_qubit_mapping[qubit]] = 0
# 				else:
# 					time_index_per_qubit[qubit] = applying_time_index + 1

# 			else:
# 				raise error.Error("wrong instruction: {}".format(inst))

# 	return collection_blocks

	

# def transform_ordered_syscode_barrier3(syscode, qubit_mapping, **kwargs):
# 	"""
# 		A function to transform system code listed in a plain list to time ordered system code in dictionary format.
# 		Besides, the whole circuit is decomposed into several partial sub-circuits also time ordered.
# 	"""

# 	if "postprocessing" in kwargs and kwargs["postprocessing"]:
# 		number_qubits = len(qubit_mapping.keys())
# 		syscode = process_syscode(syscode, number_qubits)
	
# 	if "barrier" in kwargs: 
# 		group_barrier_qubits = kwargs["barrier"]
# 	else:
# 		group_barrier_qubits = []

# 	syscode_whole_circuit = collections.defaultdict(lambda: collections.defaultdict(list))
# 	syscode_subcircuit = collections.defaultdict(list)

# 	# barrier qubit 의 현재 상태 : False after Preparation, True after Measurement
# 	status_barrier_qubits = {}
# 	for qubit_group in range(len(group_barrier_qubits)):
# 		status_barrier_qubits[qubit_group] = {qubit: False for qubit in group_barrier_qubits[qubit_group]}

# 	# sub_circuit 을 whole circuit 으로 추가하는 flag
# 	# status_barrier_qubit[type] 내 모든 큐빗이 True 가 되면, flip the status: False -> True
# 	flag_insert_to_whole_circuit = {k: False for k in range(len(group_barrier_qubits))}

# 	table_qubit_mapping = copy.deepcopy(qubit_mapping)
# 	table_inverse_mapping = {v: k for k, v in table_qubit_mapping.items()}

# 	time_index = collections.defaultdict(int)
# 	last_time_measurement = collections.defaultdict(int)
# 	measurement_role = collections.defaultdict(str)

# 	arxiv_time_index = collections.defaultdict(lambda: collections.defaultdict(int))

# 	sub_circuit_index = 0
# 	parser = re.compile("[\{a-zA-Z0-9_.*/\->\+}]+")

# 	for inst in syscode:
# 		if inst[0] in ["CNOT", "CZ", "cx", "SWAP"]:
# 			ctrl, trgt = inst[1:]
# 			applying_index = max(time_index[ctrl], time_index[trgt])
# 			# 
# 			time_index[ctrl] = time_index[trgt] = applying_index+1
# 			list_command = "{} {},{}".format(inst[0], ctrl, trgt)

# 			if inst[0] in ["SWAP"]:
# 				table_inverse_mapping[ctrl], table_inverse_mapping[trgt] =\
# 					table_inverse_mapping[trgt], table_inverse_mapping[ctrl]
# 				table_qubit_mapping.update({v: k for k, v in table_inverse_mapping.items()})

# 		else:
# 			if inst[0] in ["Rz", "Rx", "Ry", "P"]:
# 				angle, qubit = inst[1:]
# 				list_command = "{}({}) {}".format(inst[0], angle, qubit)

# 			elif inst[0] in ["U"]:
# 				angle_x, angle_y, angle_z, qubit = inst[1:]
# 				list_command = "{}({},{},{}) {}".format(inst[0], angle_x, angle_y, angle_z, qubit)

# 			elif inst[0] in ["PrepZ", "PrepX"]:
# 				qubit = inst[1]
# 				qubit_name = table_inverse_mapping[qubit]
# 				list_command = "{} {}".format(inst[0], qubit)

# 			elif inst[0] in ["MeasZ", "MeasX"]:
# 				qubit, cbit, *arguments = inst[1:]
# 				qubit_name = table_inverse_mapping[qubit]

# 				list_str_command = [inst[0], str(qubit), "->", str(cbit)]
				
# 				if len(arguments):
# 					sub_args_command = []
# 					for value in arguments:
# 						if value.isdigit():
# 							sub_args_command.append("expected={}".format(str(value)))
# 						else:
# 							sub_args_command.append("role={}".format(value))
# 							measurement_role[sub_circuit_index] = value

# 					str_args = ",".join(sub_args_command)
# 					str_args = "(" + str_args + ")"
# 					list_str_command.append(str_args)

# 				list_command = " ".join(list_str_command)

# 				# 큐빗 측정 후, 관련 상태 변수를 False -> True 로 변환
# 				for qubit_group, qubit_list in enumerate(group_barrier_qubits):
# 					if qubit_name in qubit_list:
# 						status_barrier_qubits[qubit_group][qubit_name] = True

# 						if last_time_measurement[qubit_group] < time_index[qubit]:
# 							last_time_measurement[qubit_group] = time_index[qubit]

# 						if all(status_barrier_qubits[qubit_group].values()):
# 							flag_insert_to_whole_circuit[qubit_group] = True

# 					# data 큐빗들은 시간 순서상, ancilla 큐빗의 verification 이후에 동작 가능함
# 					# 따라서, data 큐빗의 시간 index 는 verification 큐빗의 시간대로 설정 가능함
# 							if measurement_role[sub_circuit_index] == "ancilla_verification":
# 								for k, v in table_qubit_mapping.items():
# 									if "data" in k or "syndrome" in k:
# 										time_index[v] = time_index[qubit] + 1

# 			elif inst[0] in [g.str_barrier, g.str_barrier_all]:
# 				list_command = "{}".format(inst[0])
# 			else:
# 				qubit = inst[1]
# 				list_command = "{} {}".format(inst[0], qubit)

# 			applying_index = time_index[qubit]
# 			time_index[qubit] += 1

# 		# 이번 명령이 앞선 파티션에 추가 가능한지 확인하는 파트
# 		flag_insert_previous_circuit = False

# 		# 이번 circuit block 이 1 이상이면 (0번째 block 은 앞으로 당길 수 없음)
# 		if sub_circuit_index:
# 			# 앞선 circuit block index
# 			previous_circuit_index = sub_circuit_index-1
# 			# 앞선 circuit block 의 circuit depth
# 			depth_previous_circuit_index = max(syscode_whole_circuit[previous_circuit_index].keys())
# 			# 이번 알고리즘 명령이 2-큐빗 게이트이면
# 			if inst[0] in ["SWAP", "CNOT"]:
# 				# 큐빗 정보 확인
# 				tokens = list_command.split(" ")
# 				ctrl, trgt = map(int, tokens[1].split(",")[:])
# 				# ic(list_command, ctrl, table_inverse_mapping[ctrl], trgt, table_inverse_mapping[trgt])
				
# 				# 이 경우에 앞선 회로로 당겨질 수 있는 경우는 대상이 되는 두 큐빗에 인가되는 명령이 처음 등장한 상황 (각각 time_index=1)일 때
# 				if time_index.get(ctrl) == 1 and time_index.get(trgt) == 1:
# 					# 두 큐빗에 대해서 앞선 회로에 삽입 가능한 time index 확인
# 					max_time_index = max(arxiv_time_index[previous_circuit_index][ctrl], arxiv_time_index[previous_circuit_index][trgt], depth_previous_circuit_index)
# 					# 회로 삽입 가능 index 가 앞선 회로의 circuit depth 보다 작거나 같으면 --> 삽입 가능
# 					if max_time_index <= depth_previous_circuit_index:
# 						# 앞선 회로의 기능이 ancilla verification 일 경우에, 두 큐빗 각각이 data type 이 아니어야 삽입 가능
# 						if measurement_role[previous_circuit_index] == "ancilla_verification":
# 							if "data" not in table_inverse_mapping[ctrl] and "data" not in table_inverse_mapping[trgt]:
# 								flag_insert_previous_circuit = True

# 							# ic(ctrl, table_inverse_mapping[ctrl], trgt, table_inverse_mapping[trgt], flag_insert_previous_circuit)
							

# 			# 1-큐빗 게이트이면
# 			else:
# 				# ic(list_command, qubit, table_inverse_mapping[qubit], time_index[qubit], arxiv_time_index[previous_circuit_index][qubit], depth_previous_circuit_index)
# 				# 이 경우 앞선 회로로 당겨질 수 있는 경우는 대상이 되는 큐빗이 이번에 처음 등장한 경우일 때 (time_index=1) 일 때
# 				if time_index.get(qubit) == 1:
# 					# 회로 삽입 가능 index 가 앞선 회로의 circuit depth 보다 작거나 같으면 -> 삽입 가능
# 					if arxiv_time_index[previous_circuit_index][qubit] <= depth_previous_circuit_index:
# 						# 앞선 회로의 기능이 ancilla verification 일 경우, 해당 큐빗의 type 이 data 가 아니면 앞선 회로에 삽입 가능
# 						if measurement_role[previous_circuit_index] == "ancilla_verification":
# 							if "data" not in table_inverse_mapping[qubit]:
# 								flag_insert_previous_circuit = True

# 		# 앞선 회로에 삽입 하기 위한 과정
# 		if flag_insert_previous_circuit:
# 			# 두 큐빗 게이트이면
# 			if inst[0] in ["SWAP", "CNOT"]:
# 				# 앞선 회로에 삽입 가능 지점 확인 : 
# 				tokens = list_command.split(" ")
# 				ctrl, trgt = map(int, tokens[1].split(",")[:])

# 				max_time_index = max(arxiv_time_index[previous_circuit_index][ctrl], arxiv_time_index[previous_circuit_index][trgt])
# 				# 앞선 회로에 지정된 지점에 명령 삽입
# 				syscode_whole_circuit[previous_circuit_index][max_time_index].insert(0, list_command)
# 				arxiv_time_index[previous_circuit_index][ctrl] = arxiv_time_index[previous_circuit_index][trgt] = max_time_index+1
# 				del time_index[ctrl]
# 				del time_index[trgt]

# 			# 1-큐빗 게이트이면
# 			else:
# 				# 지정된 시점: arxiv_time_index[previous_circuit_index][qubit]
# 				syscode_whole_circuit[previous_circuit_index][arxiv_time_index[previous_circuit_index][qubit]].insert(0, list_command)
# 				arxiv_time_index[previous_circuit_index][qubit] += 1
# 				del time_index[qubit]

# 		# 앞선 회로에 삽입 할 수 없으면
# 		else:
# 			# 회로에 명령을 삽입할 때, 기왕이면 Measurement 는 리스트 중 마지막에
# 			# 다른 unitary 게이트는 리스트 중 앞부분에 삽입
# 			if inst[0] in ["MeasX", "MeasZ"]:
# 				syscode_subcircuit[applying_index].append(list_command)
# 			else:
# 				syscode_subcircuit[applying_index].insert(0, list_command)
			
# 			# 회로에 삽입 한 후, partitioning 가능 여부 확인
# 			for qubit_group, status in flag_insert_to_whole_circuit.items():
				
# 				# # # method 1: 회로 파티셔닝
# 				# if status:
# 				# 	# 현재까지 collect 한 component 를 sub_circuit_index 로 삽입
# 				# 	syscode_whole_circuit[sub_circuit_index] = syscode_subcircuit
# 				# 	# 
# 				# 	# time index 를 arxiv 에 저장 후, 다음 component 작업을 위해서 초기화
# 				# 	arxiv_time_index[sub_circuit_index] = copy.deepcopy(time_index)
# 				# 	time_index.update({qubit: 0 for qubit in time_index.keys()})
					
# 				# 	# 다음 회로 component 구성을 위해 데이터 초기화
# 				# 	syscode_subcircuit = collections.defaultdict(list)

# 				# 	# 전체 시스템 코드에 추가 후, 관련 상태 변수를 True -> False 로 변환
# 				# 	flag_insert_to_whole_circuit[qubit_group] = False

# 				# 	# 전체 시스템 코드에 추가 후, 큐빗의 상태를 나타내는 값도 False 로 변경
# 				# 	status_barrier_qubits[qubit_group].update({qubit: False 
# 				# 		for qubit in status_barrier_qubits[qubit_group].keys()})

# 				# 	# increment the sub_circuit_index 
# 				# 	sub_circuit_index+=1
				
# 				# method 2
# 				if status:
# 					# 현재 component circuit depth
# 					total_subcircuit_depth = max(syscode_subcircuit.keys())
# 					# 현재 component circuit 에서 마지막 measurement 의 time index
# 					last_measurement_applied_time = last_time_measurement[qubit_group]
					
# 					# 마지막 측정 time index 가 현재 component circuit depth 와 동일하면
# 					if last_measurement_applied_time == total_subcircuit_depth:
# 						syscode_whole_circuit[sub_circuit_index] = syscode_subcircuit
# 						arxiv_time_index[sub_circuit_index] = copy.deepcopy(time_index)

# 						time_index.update({qubit: 0 for qubit in time_index.keys()})
# 						# syscode_subcircuit 도 초기화
# 						syscode_subcircuit = collections.defaultdict(list)

# 					# 마지막 측정 time index 가 현재 component circuit의 depth 보다 작으면
# 					elif last_measurement_applied_time < total_subcircuit_depth:
# 						# 마지막 측정 time index 초과분에 대해서 잘라내서 다음 component 로 넘기기 위한 데이터 설정 (temp_syscode)
# 						temp_syscode = collections.defaultdict(list)
# 						# 초과분 지정 기준: 마지막 측정 time index + 1
# 						reference_time_index = last_measurement_applied_time+1
# 						# 초과분에 대해서 syscode_subcircuit 의 내용을 temp_syscode 로 넘기고, syscode_subcircuit 에서는 삭제
# 						for idx in range(reference_time_index, total_subcircuit_depth+1):
# 							temp_syscode[idx - reference_time_index] = syscode_subcircuit[idx]
# 							del syscode_subcircuit[idx]
						
# 						# 마지막 측정 이후 초과분을 제거하고 난 syscode_sybcircuit 을 전체 회로에 삽입
# 						syscode_whole_circuit[sub_circuit_index] = syscode_subcircuit

# 						for t_idx, instructions in temp_syscode.items():
# 							for inst in instructions:
# 								tokens = inst.split(" ")
# 								if tokens[0] in ["CNOT", "SWAP"]:
# 									ctrl, trgt = map(int, tokens[1].split(","))
# 									time_index[ctrl] -= 1
# 									time_index[trgt] -= 1
# 								else:
# 									argument = int(tokens[1])
# 									time_index[argument] -= 1

# 						# time_index 에서 상기에서 초과분에 해당하는 내역 삭제하고, arxiv 에 저장
# 						arxiv_time_index[sub_circuit_index] = copy.deepcopy(time_index)

# 						# 초과분 (temp_syscode) 를 그 다음 component 회로로 지정
# 						syscode_subcircuit = temp_syscode
# 						# 초과분에 속한 component 회로 (temp_syscode) 에 속한 명령들을 기준으로 time_index 설정 
# 						time_index.update({qubit: 0 for qubit in time_index.keys()})
# 						for tid, instructions in temp_syscode.items():
# 							for inst in instructions:
# 								token = parser.findall(inst)
# 								if token[0] in ["SWAP", "CNOT", "CZ"]:
# 									ctrl, trgt = token[1:]
# 									time_index[ctrl] = time_index[trgt] = max(time_index[ctrl], time_index[trgt]) + 1
# 								else:
# 									if token[0] in ["Rz", "Rx", "Ry", "P"]: angle, qubit = token[1:]
# 									elif token[0] in ["U"]: angle_x, angle_y, angle_z, qubit = token[1:]
# 									elif token[0] in ["PrepZ", "PrepX"]: qubit = token[1]
# 									elif token[0] in ["MeasZ", "MeasX"]: qubit, cbit, *arguments = token[1:]
# 									else: qubit = token[1]
								
# 									time_index[qubit]+=1

# 					# 전체 시스템 코드에 추가 후, 관련 상태 변수를 True -> False 로 변환
# 					flag_insert_to_whole_circuit[qubit_group] = False

# 					# 전체 시스템 코드에 추가 후, 큐빗의 상태를 나타내는 값도 False 로 변경
# 					status_barrier_qubits[qubit_group].update({qubit: False 
# 						for qubit in status_barrier_qubits[qubit_group].keys()})

# 					last_time_measurement[qubit_group] = 0
# 					# time index 초기화
# 					sub_circuit_index+=1
					
# 	# 시스템 코드에 대해서 관련 처리 후, whole circuit 에 추가되지 못하고, subcircuit 에 남아 있는 내용이 있다면,
# 	# 이들을 추가로 whole circuit 에 추가함
# 	if len(syscode_subcircuit):
# 		syscode_whole_circuit[sub_circuit_index] = syscode_subcircuit

# 	return syscode_whole_circuit	



# def transform_ordered_syscode_barrier2(syscode, number_qubits, qubit_mapping, **kwargs):
# 	"""
# 		function to transform system code listed in plain list to time ordered system code in dictionary format
# 	"""

# 	if "postprocessing" in kwargs and kwargs["postprocessing"]:
# 		syscode = process_syscode(syscode, number_qubits)

# 	if "barrier" in kwargs:
# 		barrier_qubits = kwargs["barrier"]
# 	else:
# 		barrier_qubits = []

# 	time_index = collections.defaultdict(int)
# 	ordered_syscode = collections.defaultdict(list)
	
# 	status_barrier_qubits = {k: False for k in barrier_qubits}
	
# 	table_qubit_mapping = copy.deepcopy(qubit_mapping)
# 	table_inverse_mapping = {v: k for k, v in table_qubit_mapping.items()}

# 	for inst in syscode:
# 		if inst[0] in ["CNOT", "cnot", "CZ", "cz", "cx", "SWAP", "swap"]:
# 			ctrl, trgt = inst[1:]

# 			applying_index = max(time_index[ctrl], time_index[trgt])
# 			time_index[ctrl] = time_index[trgt] = applying_index+1
# 			list_command = "{} {},{}".format(inst[0], ctrl, trgt)
# 			# list_command = "{} {},{}".format(inst[0], table_inverse_mapping[ctrl], table_inverse_mapping[trgt])

# 			if inst[0] in ["SWAP", "swap"]:
# 				table_inverse_mapping[ctrl], table_inverse_mapping[trgt] =\
# 					table_inverse_mapping[trgt], table_inverse_mapping[ctrl]
			
# 				table_qubit_mapping.update({v: k for k, v in table_inverse_mapping.items()})

# 		else: 
# 			if inst[0] in ["Rz", "rz", "Rx", "rx", "Ry", "ry", "P"]:
# 				angle, qubit = inst[1:]
# 				list_command = "{}({}) {}".format(inst[0], angle, qubit)
# 				# list_command = "{}({}) {}".format(inst[0], angle, table_inverse_mapping[qubit])
			
# 			elif inst[0] in ["U"]:
# 				angle_x, angle_y, angle_z, qubit = inst[1:]
# 				list_command = "{}({},{},{}) {}".format(inst[0], angle_x, angle_y, angle_z, qubit)
# 				# list_command = "{}({},{},{}) {}".format(inst[0], angle_x, angle_y, angle_z, table_inverse_mapping[qubit])

# 			elif inst[0] in ["MeasZ", "MeasX", "measz", "measx"]:
# 				qubit, cbit, *arguments = inst[1:]
# 				list_str_command = [inst[0], str(qubit), str(cbit)]
# 				# list_str_command = [inst[0], table_inverse_mapping[qubit], str(cbit)]
				
# 				if len(arguments):
# 					sub_args_command = []
# 					for value in arguments:
# 						if value.isdigit():
# 							sub_args_command.append("expected={}".format(str(value)))
# 						else:
# 							sub_args_command.append("role={}".format(value))
# 					str_args = ",".join(sub_args_command)
# 					str_args = "(" + str_args + ")"
# 					list_str_command.append(str_args)

# 				list_command = " ".join(list_str_command)
				
# 				qubit_name = table_inverse_mapping[qubit]
# 				if qubit_name in barrier_qubits:
# 					status_barrier_qubits[qubit_name] = True

# 				if all(status_barrier_qubits.values()): 
# 					# data 큐빗들은 시간 순서상, ancilla 큐빗의 verification 이후에 동작 가능함
# 					# 따라서, data 큐빗의 시간 index 는 verification 큐빗의 시간대로 설정 가능함
# 					for k, v in table_qubit_mapping.items():
# 						if "data" in k:
# 							time_index[v] = time_index[qubit]

# 			elif inst[0] in ["PrepZ"]:
# 				qubit = inst[1]
# 				qubit_name = table_inverse_mapping[qubit]

# 				if qubit_name in barrier_qubits:
# 					status_barrier_qubits[qubit_name] = False

# 				list_command = "{} {}".format(inst[0], qubit)
# 				# list_command = "{} {}".format(inst[0], qubit_name)

# 			else:
# 				qubit = inst[1]
# 				list_command = "{} {}".format(inst[0], qubit)
# 				# list_command = "{} {}".format(inst[0], table_inverse_mapping[qubit])
				
# 			applying_index = time_index[qubit]
# 			time_index[qubit] += 1

# 		ordered_syscode[applying_index].append(list_command)

# 	return ordered_syscode



def transform_ordered_syscode(syscode, number_qubits, **kwargs):
	'''
		개별 게이트의 circuit index를 분석하고, 시간순으로 정리된 회로를 생성 리턴하는 함
	'''

	if "postprocessing" in kwargs and kwargs["postprocessing"]:
		# system code 후 처리: 동일한 게이트가 연속해서 추가된 경우, 서로 cancel 시킴
		syscode = process_syscode(syscode, number_qubits)
	
	time_index = collections.defaultdict(int)
	ordered_syscode = collections.defaultdict(list)
	
	for inst in syscode:
		flag_barrier = False
		
		# ic(inst)
		if inst[0] in [g.str_gate_cnot, g.str_gate_cz, g.str_gate_swap]:
			ctrl, trgt = inst[1:]

			applying_index = max(time_index[ctrl], time_index[trgt])
			time_index[ctrl] = time_index[trgt] = applying_index+1
			list_command = "{} {},{}".format(inst[0], ctrl, trgt)
		
		elif inst[0] in ["Qubit", "Cbit"]: continue
			
		else: 
			if inst[0] in [g.str_gate_rz, g.str_gate_rx, g.str_gate_ry, g.str_gate_phase]:
				angle, qubit = inst[1:]
				list_command = "{}({}) {}".format(inst[0], angle, qubit)
				applying_index = time_index[qubit]
				time_index[qubit] += 1
			
			elif inst[0] in [g.str_gate_u]:
				*angle, qubit = inst[1:]
				list_command = "{}({},{},{}) {}".format(inst[0], angle[0], angle[1], angle[2], qubit)
				applying_index = time_index[qubit]
				time_index[qubit] += 1
			
			elif inst[0] in [g.str_gate_measz, g.str_gate_measx]:
				qubit, cbit, *arguments = inst[1:]
				list_str_command = [inst[0], str(qubit), "->", str(cbit)]
				
				if len(arguments):
					sub_args_command = []
					# for value in arguments:
					# 	if isinstance(value, int):
					# 		sub_args_command.append("expected={}".format(str(value)))
					# 	# if value.isdigit():
					# 	# 	sub_args_command.append("expected={}".format(str(value)))
					# 	else:
					# 		sub_args_command.append("role={}".format(value))

					str_args = ",".join(sub_args_command)
					str_args = "(" + str_args + ")"
					list_str_command.append(str_args)

				list_command = " ".join(list_str_command)

				applying_index = time_index[qubit]
				time_index[qubit] += 1
			

			elif inst[0] in ["Qubit"]:
				if len(inst[1:]) == 2:
					qubit, size = inst[1:]
					list_command = "{} {} {}".format(inst[0], qubit, size)
				else:
					qubit = inst[1]
					list_command = "{} {}".format(inst[0], qubit)

			
			elif inst[0] == g.str_barrier_all:
				flag_barrier = True
				list_command = g.str_barrier_all
				applying_index = max(list(time_index.values()))

				for qubit in time_index.keys():
					time_index[qubit] = applying_index

			elif inst[0] == g.str_barrier:
				flag_barrier = True
				list_command = "{} {}".format(g.str_barrier, inst[1])
				applying_index = max(time_index[qubit] for qubit in inst[1])

				for qubit in inst[1]: time_index[qubit] = applying_index

			else:
				qubit = inst[1]
				list_command = "{} {}".format(inst[0], qubit)
				applying_index = time_index[qubit]
				time_index[qubit] += 1
				
			
		if flag_barrier: applying_index -= 1

		ordered_syscode[applying_index].append(list_command)

	return ordered_syscode



def extract_list_qubits(syscode):
	list_qubits = []
	parser = re.compile("[\{a-zA-Z0-9_.*/\->\+}]+")

	if type(syscode) in [collections.defaultdict, dict]:
		for time_index, list_instrunctions in syscode.items():
			for instruction in list_instrunctions:
				token = parser.findall(instruction)
				if not len(token): continue

				if token[0] in ["CNOT", "cx", "cz"]: list_qubits.extend(map(int, token[1:3]))
				else:
					if token[0] in ["Rz", "rz", "Rx", "rx", "Ry", "ry", "P"]:
						angle, qubit = token[1:]
						list_qubits.append(int(qubit))
					
					elif token[0] in ["U"]:
						_, _, _, qubit = token[1:]
						list_qubits.append(int(qubit))
					
					elif token[0] not in ["Cbit"]:
						list_qubits.append(int(token[1]))

	return set(list_qubits)




def transform_to_openqasm(qasm, **kwargs):
	if "number_qubits" in kwargs:
		number_qubits = kwargs["number_qubits"]

	list_converted_code = []
	list_converted_code.append(["OPENQASM 2.0"])
	list_converted_code.append(["include \"qelib1.inc\""])

	list_converted_code.append(["qreg", "{}".format(number_qubits)])
	list_converted_code.append(["creg", "{}".format(number_qubits)])

	flag_measurement_appear = False

	for inst in qasm:
		if inst[0] in ["PrepZ"]: 
			list_converted_code.append(["reset", "{}".format(inst[1])])

		elif inst[0] in ["X", "Z", "Y", "I", "H", "SX", "S"]:
			list_converted_code.append(["{}".format(inst[0].lower()), "{}".format(inst[1])])

		elif inst[0] in ["CNOT", "cx"]:
			list_converted_code.append(["cx", "{}".format(inst[1]), "{}".format(inst[2])])

		elif inst[0] in ["MeasZ"]:
			list_converted_code.append(["measure", "{}".format(inst[1]), "{}".format(inst[3])])

		elif inst[0] in ["Rx", "Rz", "Ry", "P"]:
			list_converted_code.append(["{}".format(inst[0].lower()), "{}".format(inst[1]), "{}".format(inst[2])])

		elif inst[0] in ["U"]:
			inst[0] = inst[0].lower()
			list_converted_code.append(inst)

	return list_converted_code


def preanalyze_qasm(qasm):
	'''
		commutable cnot swap 함수
		args: qasm in list data structure
	'''
	import re
	p = re.compile("[\{a-zA-Z0-9_.*\->\}]+")

	idx = 0

	# list_qasm -> idx: qasm instruction
	list_qasm = {}

	# monitoring_CNOT -> [{"control": ..., "target": ..., "idx": idx}, {..}]
	list_monitoring_CNOT = []

	# qubit -> qubit : [{"qubit": .., "cnots": [.. ]}]
	list_monitoring_qubit = []

	list_memory_declaration = []
	# with open(file_qasm, "r") as infile:
	
	for command in qasm:
		# 일단 순서대로 list에 저장
		list_qasm[idx] = command

		if command[0] in ["Qubit", "Cbit"]: 
			idx += 1
			continue

		# 게이트 타입에 따라 연산 작업
		# case 1: CNOT
		if command[0] == "CNOT":
			ctrl, trgt = command[1:]
			if ctrl == trgt:
				raise error.Error("For CNOT, ctrl qubit and trgt qubit are the same. {}".format(command))

			# 새로운 CNOT의 ctrl, trgt 큐빗이 기존 CNOT에 물려 있는지 확인
			# check 1: ctrl 만 공유되는 상황 
			# check 2: ctrl 과 trgt 가 공유되는 상황
			# check 3: check 1과 2는 아니지만, 어떻게는 큐빗 공유는 이루어지는 상황
			# check 4: 새로운 cnot 과 앞선 cnot 들이 완전히 독립적인 상황

			flag_checking = {k: False for k in range(3)}
			flag_new = True
			for cnot in list_monitoring_CNOT:
				if ctrl == cnot["control"]:
					if trgt == cnot["target"]:
						print("기존 CNOT: {}, 신규 CNOT : {}".format(cnot, (ctrl, trgt)))
						print("중복 발생")
						list_monitoring_CNOT.remove(cnot)
						# list_monitoring_CNOT.append({"control": ctrl, "target": trgt, "id": idx})
						flag_new = False
					
					else:
						print("기존 CNOT: {}, 신규 CNOT : {}".format(cnot, (ctrl, trgt)))
						print("교환 대상")
						list_monitoring_CNOT.append({"control": ctrl, "target": trgt, "id": idx})
						list_monitoring_qubit.append({"qubit": trgt, 
													  "cnot_list": [cnot, {"control": ctrl, "target": trgt, "id": idx}]})
						flag_new = False

				else:
					if ctrl == cnot["target"] or trgt in list(cnot.values()):
						print("기존 CNOT: {}, 신규 CNOT : {}".format(cnot, (ctrl, trgt)))
						print("기존 CNOT 제거 & 신규 CNOT 추가")
						list_monitoring_CNOT.remove(cnot)
						list_monitoring_CNOT.append({"control": ctrl, "target": trgt, "id": idx})
						flag_new = False
				break

			if flag_new:
				print("독립적인 CNOT 게이트")
				list_monitoring_CNOT.append({"control": ctrl, "target": trgt, "id": idx})

			print("list of monitoring cnot: ")
			pprint(list_monitoring_CNOT)

		# case 2: one-qubit gate
		else:
			# case 2-1: rotational gate with arguments: angle and qubit
			if command[0] in ["Rz", "rz"]: qubit = command[2]
			# case 2-2: the other one-qubit gate with argument: qubit
			else: qubit = command[1]

			if not len(list_monitoring_qubit):
				for cnot in list_monitoring_CNOT:
					if cnot["control"] == qubit or cnot["target"] == qubit:
						list_monitoring_CNOT.remove(cnot)

			pprint(list_monitoring_qubit)
			for q in list_monitoring_qubit:
				# check 1: 공통 control 큐빗에 one-qubit 게이트가 인가된 경우
				if (q["cnot_list"][0]["control"] == qubit) and (q["cnot_list"][1]["control"] == qubit):
					print("case 1-1.. ")
					former, latter = q["cnot_list"][:]
					list_monitoring_CNOT.remove(former)
					list_monitoring_CNOT.remove(latter)
					list_monitoring_qubit.remove(q)

				# # check 2: 첫번째 cnot의 타겟 큐빗에 one-qubit 게이트가 인가된 경우
				# if q["cnot_list"][0]["target"] == qubit:
				# 	pprint(q["cnot_list"])
				# 	former, latter = q["cnot_list"][:]
				# 	list_monitoring_CNOT.remove(former)
				# 	list_monitoring_qubit.remove(q)
				# check 3
				if q["qubit"] == qubit:
					print("교환하자... {}".format(q["cnot_list"]))
					print("교환 이전: ")
					pprint(list_qasm)
					former, latter = q["cnot_list"][:]
					list_qasm[former["id"]] = ["CNOT", latter["control"], latter["target"]]
					list_qasm[latter["id"]] = ["CNOT", former["control"], former["target"]]
					
					print("교환 결과: ")
					pprint(list_qasm)
					# list_monitoring_CNOT.remove(former)
					list_monitoring_CNOT.remove(latter)
					list_monitoring_qubit.remove(q)

					print("monitoring cnot: ")
					pprint(list_monitoring_CNOT)
					print("monitoring qubit: ")
					pprint(list_monitoring_qubit)

		idx += 1

	return list(list_qasm.values())


def preanalyze_qasm_file(file_qasm):
	'''
		commutable cnot swap 함수
		args: qasm in file
	'''

	import re
	p = re.compile("[\{a-zA-Z0-9_.*\->\}]+")

	idx = 0

	# list_qasm -> idx: qasm instruction
	list_qasm = {}

	# monitoring_CNOT -> [{"control": ..., "target": ..., "idx": idx}, {..}]
	list_monitoring_CNOT = []

	# qubit -> qubit : [{"qubit": .., "cnots": [.. ]}]
	list_monitoring_qubit = []

	list_memory_declaration = []
	with open(file_qasm, "r") as infile:
		for line in infile:
			tokens = p.findall(line)
			# print(tokens)
			if not len(tokens):  continue

			# 일단 순서대로 list에 저장
			list_qasm[idx] = tokens

			if tokens[0] in ["Qubit", "Cbit"]: 
				idx += 1
				continue

			# 게이트 타입에 따라 연산 작업
			# case 1: CNOT
			if tokens[0] == "CNOT":
				ctrl, trgt = tokens[1:]
				if ctrl == trgt:
					raise error.Error("For CNOT, ctrl qubit and trgt qubit are the same. {}".format(tokens))
				# 새로운 CNOT의 ctrl, trgt 큐빗이 기존 CNOT에 물려 있는지 확인
				# check 1: ctrl 만 공유되는 상황 
				# check 2: ctrl 과 trgt 가 공유되는 상황
				# check 3: check 1과 2는 아니지만, 어떻게는 큐빗 공유는 이루어지는 상황
				# check 4: 새로운 cnot 과 앞선 cnot 들이 완전히 독립적인 상황

				flag_checking = {k: False for k in range(3)}
				flag_new = True
				for cnot in list_monitoring_CNOT:
					if ctrl == cnot["control"]:
						if trgt == cnot["target"]:
							print("기존 CNOT: {}, 신규 CNOT : {}".format(cnot, (ctrl, trgt)))
							print("중복 발생")
							list_monitoring_CNOT.remove(cnot)
							# list_monitoring_CNOT.append({"control": ctrl, "target": trgt, "id": idx})
							flag_new = False
						
						else:
							print("기존 CNOT: {}, 신규 CNOT : {}".format(cnot, (ctrl, trgt)))
							print("교환 대상")
							list_monitoring_CNOT.append({"control": ctrl, "target": trgt, "id": idx})
							list_monitoring_qubit.append({"qubit": trgt, 
														  "cnot_list": [cnot, {"control": ctrl, "target": trgt, "id": idx}]})
							flag_new = False

					else:
						if ctrl == cnot["target"] or trgt in list(cnot.values()):
							print("기존 CNOT: {}, 신규 CNOT : {}".format(cnot, (ctrl, trgt)))
							print("기존 CNOT 제거 & 신규 CNOT 추가")
							list_monitoring_CNOT.remove(cnot)
							list_monitoring_CNOT.append({"control": ctrl, "target": trgt, "id": idx})
							flag_new = False
					break

				if flag_new:
					print("독립적인 CNOT 게이트")
					list_monitoring_CNOT.append({"control": ctrl, "target": trgt, "id": idx})

				print("list of monitoring cnot: ")
				pprint(list_monitoring_CNOT)

			# case 2: one-qubit gate
			else:
				# case 2-1: rotational gate with arguments: angle and qubit
				if tokens[0] in ["Rz", "rz"]: qubit = tokens[2]
				# case 2-2: the other one-qubit gate with argument: qubit
				else: qubit = tokens[1]

				if not len(list_monitoring_qubit):
					for cnot in list_monitoring_CNOT:
						if cnot["control"] == qubit or cnot["target"] == qubit:
							list_monitoring_CNOT.remove(cnot)

				for q in list_monitoring_qubit:
					# check 1: 공통 control 큐빗에 one-qubit 게이트가 인가된 경우
					if (q["cnot_list"][0]["control"] == qubit) and (q["cnot_list"][1]["control"] == qubit):
						print("case 1-1.. ")
						former, latter = q["cnot_list"][:]
						list_monitoring_CNOT.remove(former)
						list_monitoring_CNOT.remove(latter)
						list_monitoring_qubit.remove(q)

					# # check 2: 첫번째 cnot의 타겟 큐빗에 one-qubit 게이트가 인가된 경우
					# if q["cnot_list"][0]["target"] == qubit:
					# 	pprint(q["cnot_list"])
					# 	former, latter = q["cnot_list"][:]
					# 	list_monitoring_CNOT.remove(former)
					# 	list_monitoring_qubit.remove(q)
					# check 3
					if q["qubit"] == qubit:
						print("교환하자... {}".format(q["cnot_list"]))
						print("교환 이전: ")
						pprint(list_qasm)
						former, latter = q["cnot_list"][:]
						list_qasm[former["id"]] = ["CNOT", latter["control"], latter["target"]]
						list_qasm[latter["id"]] = ["CNOT", former["control"], former["target"]]
						
						print("교환 결과: ")
						pprint(list_qasm)
						# list_monitoring_CNOT.remove(former)
						list_monitoring_CNOT.remove(latter)
						list_monitoring_qubit.remove(q)

						print("monitoring cnot: ")
						pprint(list_monitoring_CNOT)
						print("monitoring qubit: ")
						pprint(list_monitoring_qubit)

			idx += 1

	with open(file_qasm, "w") as outfile:
		for idx, inst in list_qasm.items():
			if inst[0] in ["Qubit", "Cbit"]:
				str_command = "{} {}\n".format(inst[0], inst[1])

			elif inst[0] == "CNOT":
				str_command = "{} {},{}\n".format(inst[0], inst[1], inst[2])
			
			elif inst[0] in ["Rz", "rz"]: 
				str_command = "{}({}) {}\n".format(inst[0], inst[1], inst[2])
			
			elif inst[0] in ["MeasZ"]:
				str_command = "{} {} -> {}\n".format(inst[0], inst[1], inst[3])	
			
			else:
				str_command = "{} {}\n".format(inst[0], inst[1])

			outfile.write(str_command)

	return file_qasm
