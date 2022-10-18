
import re
from pprint import pprint
import globalVariable as g

def checkup_system_code(system_code, mapping_table, qchip, **kwargs):
	"""
		시스템 코드 checkup 함수
		합성 결과가 qubit connectivity 를 만족하는 지 확인하는 함수
	"""
	
	parser = re.compile("[\{a-zA-Z0-9_.*\->\+}]+")
	flag_verification = True
	
	if type(system_code) == dict:
		for instructions in list(system_code.values()):
			for inst in instructions:
				tokens = parser.findall(inst)
				if not len(tokens): continue
				
				if tokens[0] in [g.str_gate_cnot, g.str_gate_swap, g.str_gate_cz]:
					ctrl, trgt = map(int, tokens[1:])
					if trgt not in qchip["qubit_connectivity"][ctrl]:
						flag_verification = False
						break

	elif type(system_code) == list:
		for inst in system_code:
			if inst[0] in [g.str_gate_cnot, g.str_gate_swap, g.str_gate_cz]:
				ctrl, trgt = map(int, inst[1:])
				if trgt not in qchip["qubit_connectivity"][ctrl]:
					flag_verification = False
					break

	return flag_verification