import uuid
import subprocess
import os

D4_DIRECTORY = os.sep.join(__file__.split(os.sep)[:-1]) + os.sep
D4_EXEC = D4_DIRECTORY + "d4_static"

class D4Solver():

  def __init__(self, filenames="/tmp/heat", hash=str(uuid.uuid4().fields[-1])[:8]):
    self.hash = hash
    self.filename_cnf = "/tmp/heat-"+self.hash+".cnf"
    self.filename_query = "/tmp/heat-"+self.hash+".query"

  def add_cnf(self, cnf, n_literals):
    file = open(self.filename_cnf, "w")
    file.write(f"p cnf {n_literals} {len(cnf)}\n")
    for clause in cnf: 
      file.write(" ".join(str(l) for l in clause) + " 0\n")
    file.close()

  def add_count_model_query(self, cnf, n_literals, n_literals_limit):
    file = open(self.filename_query, "w")
    file.write(f"p cnf {n_literals} {len(cnf)}\n")
    file.write("m 0\n")
    for l in range(1, n_literals_limit):
      file.write("m" + str(l) + ' 0\n')
    file.close()


  def solve(self, time_limit=None):
    try:
        p = subprocess.run([D4_EXEC, "-m", "ddnnf-compiler", "-i",
                            self.filename_cnf, "--query", self.filename_query], timeout=time_limit,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    except subprocess.TimeoutExpired:
        return {1: -1}   

    n_models = [int(line.split(" ")[1]) for line in p.stdout.split("\n") if len(line) > 0 and line[0] == "s"]
    return n_models