
# -*-coding:utf-8-*-

# import os
# import sys
# import simplejson as json
# from pprint import pprint
# import collections
# import time
# sys.path.insert(0, "support")

# import error
# import math
# import userproperty
# import path_list
# import layout_generator
import pandas
# import globalVariable as g
from icecream import ic


def checkup_fault_tolerance(system_code, lattice_size, **kwargs):
    '''
        function to investigate the fault tolerance of the circuit
    '''

    # initial mapping
    qubit_mapping = system_code["initial_mapping"]
    inverse_mapping = {v: k for k, v in qubit_mapping.items()}

    layout = [[0 for i in range(lattice_size["width"])] for j in range(lattice_size["height"])]
    
    for idx, qubit in inverse_mapping.items():
        x_coord = int(idx/lattice_size["width"])
        z_coord = int(idx%lattice_size["width"])

        layout[x_coord][z_coord] = qubit
    
    print(" =====================================================  ")
    print("Initial Mapping: ")
    print(" -----------------------------------------------------  ")
    print(pandas.DataFrame(layout).to_string())
    print(" =====================================================  ")

    circuit_depth = max(list(system_code["circuit"].keys())) + 1
    
    qubit_usage_status = {k: True if "data" in k else False for k in qubit_mapping.keys()}

    ic(qubit_usage_status)

    # circuit
    for idx in range(circuit_depth):
        instructions = system_code["circuit"][idx]

        flag_swap = False
        print(" =====================================================  ")
        print("instructions at {}-th index : {}".format(idx, instructions))
        print(" -----------------------------------------------------  ")
        
        for inst in instructions:
            tokens = inst.split(" ")

            if tokens[0] in ["PrepZ"]:
                physical_qubit = int(tokens[1])
                logical_qubit = inverse_mapping[physical_qubit]
                
                print(" {} {} ({}) -> {}".format(tokens[0], physical_qubit, logical_qubit, qubit_usage_status[logical_qubit]))

                qubit_usage_status[logical_qubit] = True

            elif tokens[0] in ["MeasZ"]:
                physical_qubit = int(tokens[1])
                logical_qubit = inverse_mapping[physical_qubit]

                print(" {} {} ({}) -> {}".format(tokens[0], physical_qubit, logical_qubit, qubit_usage_status[logical_qubit]))

                qubit_usage_status[logical_qubit] = False

            elif tokens[0] in ["CNOT"]:
                qubits = list(map(int, tokens[1].split(",")))
                
                print(" {} {}, {} ({}, {}) -> {}, {}".format(tokens[0], qubits[0], qubits[1], inverse_mapping[qubits[0]], inverse_mapping[qubits[1]],
                											qubit_usage_status[inverse_mapping[qubits[0]]], qubit_usage_status[inverse_mapping[qubits[1]]]))

                flag_swap = False

            elif tokens[0] in ["SWAP"]:
                qubits = list(map(int, tokens[1].split(",")))
#                 logical_qubit0 = 
#                 logical_qubit1 = 

#                 print(" {} {}, {} ({}, {})".format(tokens[0], qubits[0], qubits[1], logical_qubit0, logical_qubit1))
                print(" {} qubits ({}, {}) -> ({}, {}) {} {}".format(tokens[0], qubits[0], qubits[1], inverse_mapping[qubits[0]], inverse_mapping[qubits[1]],
                                                                    qubit_usage_status[inverse_mapping[qubits[0]]], qubit_usage_status[inverse_mapping[qubits[1]]]))

                inverse_mapping[qubits[0]], inverse_mapping[qubits[1]] =\
                    inverse_mapping[qubits[1]], inverse_mapping[qubits[0]]
                
                flag_swap = True

                # activated 큐빗간 interaction (SWAP)에 대해서, 오류 발생시킴
                if qubit_usage_status[logical_qubit0] and qubit_usage_status[logical_qubit1]:
                    raise error.Error("Stop: SWAP between activated qubits")

            # barrier - All : for all qubits
            elif tokens[0] in [g.str_barrier_all]:
                print(" {} ".format(tokens[0]))
                flag_swap = False

            # selective barrier for selected qubits
            elif tokens[0] in [g.str_barrier]:
                print(" {} {}".format(tokens[0], tokens[1:]))
                ic(inverse_mapping)
                flag_swap = False
            
            else:
                qubit = int(tokens[1])
                print(" {} {} ({})".format(tokens[0], qubit, inverse_mapping[qubit]))
                flag_swap = False

        if flag_swap:
            # 2d array 재 구성
            for idx, qubit in inverse_mapping.items():
                x_coord = int(idx/lattice_size["width"])
                z_coord = int(idx%lattice_size["width"])

                layout[x_coord][z_coord] = qubit

        # ic(qubit_usage_status)
        print(" -----------------------------------------------------  ")
        print(pandas.DataFrame(layout).to_string())
        print(" =====================================================  ")


def display_qubit_movements(system_code, lattice_size, **kwargs):
    
    # initial mapping
    qubit_mapping = system_code["initial_mapping"]
    inverse_mapping = {v: k for k, v in qubit_mapping.items()}

    layout = [[0 for i in range(lattice_size["width"])] for j in range(lattice_size["height"])]
    
    for idx, qubit in inverse_mapping.items():
        x_coord = int(idx/lattice_size["width"])
        z_coord = int(idx%lattice_size["width"])

        layout[x_coord][z_coord] = qubit
    
    print(" =====================================================  ")
    print("Initial Mapping: ")
    print(" -----------------------------------------------------  ")
    print(pandas.DataFrame(layout).to_string())
    print(" =====================================================  ")

    circuit_depth = max(list(system_code["circuit"].keys())) + 1
    # circuit
    for idx in range(circuit_depth):
        instructions = system_code["circuit"][idx]

        flag_swap = False
        print(" =====================================================  ")
        print("instructions at {}-th index : {}".format(idx, instructions))
        print(" -----------------------------------------------------  ")
        
        for inst in instructions:
            tokens = inst.split(" ")

            if tokens[0] in ["CNOT"]:
                qubits = list(map(int, tokens[1].split(",")))
                
                print(" {} qubits ({}, {}) -> ({}, {})".format(tokens[0], qubits[0], qubits[1], inverse_mapping[qubits[0]], inverse_mapping[qubits[1]]))

                flag_swap = False

            elif tokens[0] in ["SWAP"]:
                qubits = list(map(int, tokens[1].split(",")))
                
                print(" {} qubits ({}, {}) -> ({}, {})".format(tokens[0], qubits[0], qubits[1], inverse_mapping[qubits[0]], inverse_mapping[qubits[1]]))

                inverse_mapping[qubits[0]], inverse_mapping[qubits[1]] =\
                    inverse_mapping[qubits[1]], inverse_mapping[qubits[0]]
                
                flag_swap = True

            elif tokens[0] in [g.str_barrier_all]:
                print(" {} ".format(tokens[0]))
                flag_swap = False

            else:
                qubit = int(tokens[1])
                print(" {} ({}) -> {}".format(tokens[0], qubit, inverse_mapping[qubit]))
                flag_swap = False

        if flag_swap:
            # 2d array 재 구성
            for idx, qubit in inverse_mapping.items():
                x_coord = int(idx/lattice_size["width"])
                z_coord = int(idx%lattice_size["width"])

                layout[x_coord][z_coord] = qubit

        print(pandas.DataFrame(layout).to_string())
        print(" =====================================================  ")


def display_qubit_movements1(system_code, lattice_size, **kwargs):
    
    # initial mapping
    qubit_mapping = system_code["initial_mapping"]
    inverse_mapping = {v: k for k, v in qubit_mapping.items()}

    layout = [[0 for i in range(lattice_size["width"])] for j in range(lattice_size["height"])]
    
    for idx, qubit in inverse_mapping.items():
        x_coord = int(idx/lattice_size["width"])
        z_coord = int(idx%lattice_size["width"])

        layout[x_coord][z_coord] = qubit
    
    print(" =====================================================  ")
    print("Initial Mapping: ")
    print(" -----------------------------------------------------  ")
    print(pandas.DataFrame(layout).to_string())
    print(" =====================================================  ")

    circuit_depth = max(list(system_code["circuit"].keys())) + 1
    # circuit
    for idx in range(circuit_depth):
        instructions = system_code["circuit"][idx]

        flag_swap = False
        print(" =====================================================  ")
        print("instructions at {}-th index : {}".format(idx, instructions))
        print(" -----------------------------------------------------  ")
        
        for inst in instructions:
            if inst["gate"] in ["CNOT"]:
                # qubits = list(map(int, tokens[1].split(",")))
                
                print(" {} qubits ({}, {}) -> ({}, {})".format(inst["gate"], inst["ctrl"], inst["trgt"], 
                                                inverse_mapping[inst["ctrl"]], inverse_mapping[inst["trgt"]]))

                flag_swap = False

            elif inst["gate"] in ["SWAP"]:
                qubits = list(map(int, tokens[1].split(",")))
                
                print(" {} qubits ({}, {}) -> ({}, {})".format(inst["gate"], inst["ctrl"], inst["trgt"], 
                                                inverse_mapping[inst["ctrl"]], inverse_mapping[inst["trgt"]]))

                inverse_mapping[inst["ctrl"]], inverse_mapping[inst["trgt"]] =\
                    inverse_mapping[inst["trgt"]], inverse_mapping[inst["ctrl"]]
                
                flag_swap = True

            elif inst["gate"] in [g.str_barrier_all]:
                print(" {} ".format(inst["gate"]))
                flag_swap = False

            else:
                qubit = int(inst["trgt"])
                print(" {} ({}) -> {}".format(inst["gate"], qubit, inverse_mapping[qubit]))
                flag_swap = False

        if flag_swap:
            # 2d array 재 구성
            for idx, qubit in inverse_mapping.items():
                x_coord = int(idx/lattice_size["width"])
                z_coord = int(idx%lattice_size["width"])

                layout[x_coord][z_coord] = qubit

        print(pandas.DataFrame(layout).to_string())
        print(" =====================================================  ")



def display_qubit_mapping(qubit_mapping, layout_size):
    layout = [[0 for i in range(layout_size["width"])] for j in range(layout_size["height"])]

    for key, value in qubit_mapping.items():
        x_coord = int(value/layout_size["width"])
        z_coord = int(value%layout_size["width"])

        layout[x_coord][z_coord] = key
    
    print()
    print("===============================================")
    print(pandas.DataFrame(layout))
    print("===============================================")


def merge_qubit_layout(mapping1, mapping2, direction, layout_size):
    # function merge two blocks 

    extended_qubit_layout = {}

    if direction == "horizon":
        for key, value in mapping1.items():
            x_coord = int(key/layout_size["width"])
            z_coord = int(key%layout_size["width"])

            extended_index = x_coord * 2 * layout_size["width"] + z_coord
            extended_qubit_layout[extended_index] = value


        for key, value in mapping2.items():
            x_coord = int(key/layout_size["width"])
            z_coord = int(key%layout_size["width"])

            extended_index = x_coord * 2 * layout_size["width"] + z_coord + layout_size["width"]
            extended_qubit_layout[extended_index] = value


    elif direction == "vertical":
        extended_qubit_layout = mapping1
        for key, value in mapping2.items():
            x_coord = int(key/layout_size["width"])
            z_coord = int(key%layout_size["width"])

            index_in_extended_layout = (layout_size["height"] + x_coord) * layout_size["width"] + z_coord
            extended_qubit_layout[index_in_extended_layout] = value

    return {v: int(k) for k, v in extended_qubit_layout.items()}