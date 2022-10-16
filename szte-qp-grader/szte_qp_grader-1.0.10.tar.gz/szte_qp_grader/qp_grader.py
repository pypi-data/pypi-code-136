from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Operator, process_fidelity
from qiskit.circuit.library import CCXGate, CXGate
from pymongo import MongoClient
from datetime import datetime
import hashlib


def ex1(name, circuit):
    if not isinstance(circuit, QuantumCircuit):
        print("Failed.  You have to pass me a QuantumCircuit object! 😠")
        return

    op_toffoli = Operator(CCXGate())
    op_to_check = Operator(circuit)

    if op_toffoli.equiv(op_to_check):
        ops = circuit.count_ops()
        cx_count = ops.get('cx', 0)
        if cx_count != circuit.num_nonlocal_gates():
            print("Failed. You have to decompose the Toffoli gate, not use it 🙂")
            return
        
        
        score = cx_count*9 + sum(ops.values())
        gate_set = ['cx', 'id', 'rz', 'sx', 'x']
        if sum([ops.get(gate, 0) for gate in gate_set]) == sum(ops.values()):
            score -= 20
        db_helper("ex1", name, datetime.now().isoformat(), score)
        print(f"Congrats, you succeded 🥳 🎉 Your score: {score}, number of CNOTs: {cx_count}")
        
    else:
        print("Failed. Your circuit does not match the Toffoli gate 😢")
        return


def ex2a(circuit):
    op_toffoli = Operator(CCXGate())
    op_to_check = Operator(circuit)

    if op_toffoli.equiv(op_to_check):
        print("Congrats, you succeded 🥳 🎉")
    else:
        print("Failed. Your circuit does not match the CU operator 😢")

def ex2b(circuit):
    c_checker = QuantumCircuit(3)
    c_checker.cx(0,2)
    op_checker = Operator(c_checker)
    op_to_check = Operator(circuit)

    if op_checker.equiv(op_to_check):
        print("Congrats, you succeded 🥳 🎉")
    else:
        print("Failed. Your circuit does not match the CU2 operator 😢")
    pass

def ex2c(circuit):
    c_checker = QuantumCircuit(3)
    op_checker = Operator(c_checker)
    op_to_check = Operator(circuit)

    if op_checker.equiv(op_to_check):
        print("Congrats, you succeded 🥳 🎉")
    else:
        print("Failed. Your circuit does not match the CU4 operator 😢")


def ex2(name, circuit):
    cqr = QuantumRegister(3, 'control')
    tqr = QuantumRegister(2, 'target')
    cux = QuantumCircuit(cqr, tqr)
    solutions = prep_ex2()
    for i in range(3):
        cux = cux.compose(solutions[i], [cqr[i], tqr[0], tqr[1]])
    
    op_checker = Operator(cux)
    op_to_check = Operator(circuit)

    if op_checker.equiv(op_to_check):
        score = 20
        gate_set =  ['u1', 'u2', 'u3', 'cx', 'id']
        ops = circuit.count_ops()
        text=""
        if sum([ops.get(gate, 0) for gate in gate_set]) == sum(ops.values()):
            score -= 20
            text="You successfully decomposed your circuit to U and CX gates, good job!"
        score += ops.get('cx', 0)
        if ops.get('ccx', 0) != 0:
            score += 10
        db_helper("ex2", name, datetime.now().isoformat(), score)
        print(f"Congrats, you succeded 🥳 🎉 Your score is {score}. {text}")
    else:
        print("Failed. Your circuit does not match the operator 😢")


n2021f=['afea7f8ac398ea4d40c0f7074823294c79e1607a354e13878ba8fbf9e592c2e1', '874dee3c0d2cd9011416078186547321b770d8932ac074334dd20276a19bd451', 'dc6a452fbafc6b95adee5bf2c0611936b903330ec60b3724dbe331dbfe7d8df1', 'b23ffd57279cc0e6c0690f00c07dddb287abe8513b90cbb76f87931398b298b9', 'bd4cad070e1d5015bbf6575fc01469ee3584e1a49de80b2ac4687faed9f52d6f', '6bbbf6ddcf5cfedc8fa65bef02b3549017811a67dede3dd432cb62b1716c634a', 'd05f8db48bf6a0828e22d988eb68c2fceb3ed841590a9699c63ab4847a7e5c09', 'b824c5e80a46c822a94f258cd864d9b1dffb73afd15ceb57a0978d5db16ae2e1', '631dff88c4b030a04782a7558caaa9ff1f0c85ff153452b5cee25bc7d703c578', '98231ca9d5b83665f8a6b741644aa9eabe4d7d7868001823e2eaa40d0ad8a482', '40805c1add449c79bcb208e65d88a84af16fc8e698408ac2f60fcd21aafdff3d', '57cfd81e24aea4d7e04f90533971e92beee4eeca442f38d39605e5c8c4d55aeb', '7bcbdd452774b8825766c3c26959ff850f19e6b5c9572749f740bcfd328e04ad', '6d5d4d45b3d89be98c30c565d71815bf3052725e58a7256104364067a2f587a7', '5f03e3d6504364a88b37d065c9998ac026d2c998a5a73fa7425b7f1a122c8208', 'da69d42eb7692d9db04e8c1578fb81348cfe081d17ea57618148bd1732c473b7', 'f358d66e98034d7b89fcc4809a24d199b0338b644a7fe3ff54829f3768abf2b3', '12c3d61521a3a27711588dd54f60a44d0b58b93e706c6fb3861e6a4f11c541a9', '79b204ec1ececf6a69f068c65eb5ec8823a0b8acb57eaa1c0e2c5714c34f0371', '58f7c4cc05af8397635c196acaa61db897721a55af565d8d7ec7b2f30c1a9170', '2b427550967cac4e5aca76ad74890b6f41c6b54382cc034b1080454ac89f2c3e', '1c7c375e46850f5b61baa69d47a7a635c058a5b99e52e4b8d353fd0985d887f4', '97c8fb74c4e1e8e6ac3b79aa8b01f5f70cd80f72407d87599953aa0893e76ac0']
n2022s=['afea7f8ac398ea4d40c0f7074823294c79e1607a354e13878ba8fbf9e592c2e1', '874dee3c0d2cd9011416078186547321b770d8932ac074334dd20276a19bd451', '78a8ebdcc101b021d08b410197029114214ab428f9357635143913c20395f240', '1993f3b3401821a0d2e6df2eca8e393646a8027583a0a74c74460881991d6185', 'd84fc40bcdf53a27b62202f3d409034da8a59b759bcd82ab43df872777b791e3', '7062f3b64753f86b6c0507d84eac54254d85d2a38653c896024c9a3bb12e2579', '8cda9f5a18f2949304ce390b84202a0a0b3b298e87fda957cfa133a9e0dac388', '4e74cc8091595f23bdc743bbb6564b0af2a1185351836bb7fe9b24e478159696', '3f3f8a3a8e59289f761ade43fbb233e0373f3762a9d81e36ee02e748ccb60009', '703ad64aba37d445c9241bdc92ce4c493ced2e0aba8ae72ff269f5f0ec5eedfb', '1ef29b3c7706c1d5fe69d64ee08dedb347a1695633d2b909f9fe9e437e743d05', '854cd78ac57ac90674d7eaf46d86f5e04ead34b8d9412a9239f81dbf9dc31c89', 'aa2ec24feb395119a80d9d2fecce33e50def720319a706ad0c7c184aebc62b72', '5f03e3d6504364a88b37d065c9998ac026d2c998a5a73fa7425b7f1a122c8208', '12de0de3e44b75d8786948c384489f35acf91c5edb09a72168d2eb9b2c7fbc0c', '2b2c477802fcfc22b1c24908fc201a9d8477c3f0281528e4a6038ae36aba573d', '4ca57dfb6d6ffb7500074064d599e77e3875cbf3692671f7cac70995ce2320b4', 'fbba2e9621ee7f0784f4b440f46cb1269ec352c5abd39a725fb0a78a7431822b', '0c7a61e746c6d4b1b41954c8ecd682851a9aa194b638922a0dc5c3d306c173f1', '97c8fb74c4e1e8e6ac3b79aa8b01f5f70cd80f72407d87599953aa0893e76ac0', 'c58b234192744ad5349d08fd34cf88bbdb2f208d436cec5e479524a2c22da47b']
n2022f=['afea7f8ac398ea4d40c0f7074823294c79e1607a354e13878ba8fbf9e592c2e1', '874dee3c0d2cd9011416078186547321b770d8932ac074334dd20276a19bd451', 'dd8a41b6acc1a80d72e3daac23bd5fda172ffb51fc88adaf152b26362be6743e', '97ed4f61a1812c2c1d781e7ef53d3c5b3f7abe0d38b8f3a206b19a2c216be86b', '7223707f966f07496473255c1e282cb42ce646b099858084250d61a5fb5e7120', '45dbacc1cec8304e99a4e6d7a42ce7407792888eb73bef28ab21d1c198c15e31', 'dbcfeffe8605e37f73830e95b6512ff0693dd81ad20f05154c9bfd2b7e5d63c7', '84884049fe41f1fbbc286619f1d9e7a640a159e5145af3e423716c11e2c4f8bd', 'd1779390d3a0dbfacf16e58a5559dbd6cf3f755ada3cb0f1a226922224e103b8', '0d83b5d1091ba3c4abfa63a6f75535eef0bb7df3b3405b22636b311f5ce47146', '9568a9afc742aeed28d57304a4464ef284c286b98094b4a2d9a42785ba61b08e', '8c16f7e6302df3ae87fa67612835d32c2f02043b1f4b884467f2c140863729d9', 'e35d290410e2ac757742f11e0ea34439179e9d6ead707fc2db104b08528e1e27', '32091ffddbcdcddb0420901b14d394afab968d7dcd706a81a9267be5654ad5df', '5b1995279b5141bfdd2fc148a43fcc6c0f90a4f67e6a2d841fc4a2ca127b99dc', 'f22a343ae5916f6a1066ed10e2d12da0f64e73dd4fb2cc65dd3dceb6c662fe57', '73d6ccbf2ec8f2fd9ccc552b6424b9e720d4eec22ff1bf24a35c14d2b9e6b6b9', '0fe21357d7a29d6bfdb675054d3f5ff2da864e0856c93740856bc7b4c26b8d2f', '18665f7d579684087c1558bdae36eb0286da28d802e9196b2d14e6b523ac5ba0', '3751c8460375030bab3d8e0c86bdc32f66db61298e6ac3681d1d038a044516fe', 'e58226631f1d4f5a58257a4de9fdf1da55325490ad104317b04ae2d4f50dbbeb']

def db_helper(collection_name, name_str, time, score):
    name = hashlib.sha256(name_str.encode('UTF-8')).hexdigest()
    if name not in n2022f:
        print("Please enter your last name properly!")
        return
    cluster = MongoClient("mongodb+srv://auto:TaMovHp8O8iVOD4r@cluster0.6jl6a.mongodb.net/qp_2022_fall?retryWrites=true&w=majority")
    db = cluster["qp_2022_fall"]
    collection = db[collection_name]
    data = collection.find({"_id":name})
    # try: 
    cnt = collection.count_documents({"_id":name})
    if cnt == 0:
        collection.insert_one({"_id":name, "time":time, "score":score, "up_count": 0})
    elif cnt == 1:
        upload_count = data[0]["up_count"] + 1
        if score <= data[0]["score"]:
            collection.update_one({"_id":name},{"$set":{"time":time, "score":score, "up_count": upload_count}})
        else:
            collection.update_one({"_id":name},{"$set":{"up_count": upload_count}})
    # except:
    #     print("Database connection failed, please try again.")

def prep_ex2():
    u = QuantumCircuit(3)
    u2 = QuantumCircuit(3)
    u4 = QuantumCircuit(3)

    u.ccx(0,1,2)
    u.cx(0,1)
    u2.cx(0,2)

    return [u, u2, u4]