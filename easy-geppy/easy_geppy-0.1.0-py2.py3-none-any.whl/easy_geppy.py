#!/usr/bin/env python3
# coding=utf-8
"""
.. moduleauthor:: Eduardo Henrique Vieira dos Santos
This :mod:`easy_geppy` module provides a minimized and pre-defined workflow setup 
for using Geppy along with Pandas and Numpy to solve regression problems.
Nonetheless, it allows you to set your custom configuration to this setup.
Its content is base on the following implementation:
Based on https://github.com/ShuhuaGao/geppy/blob/master/examples/sr/numerical_expression_inference-ENC.ipynb

"""

import geppy as gep
from deap import creator, base, tools
import numpy as np
import random
import operator
import pandas as pd

import dill

"""
note:
Currently, it is defined as::
    DEFAULT_SYMBOLIC_FUNCTION_MAP = {
        operator.and_.__name__: sp.And,
        operator.or_.__name__: sp.Or,
        operator.not_.__name__: sp.Not,
        operator.add.__name__: operator.add,
        operator.sub.__name__: operator.sub,
        operator.mul.__name__: operator.mul,
        operator.neg.__name__: operator.neg,
        operator.pow.__name__: operator.pow,
        operator.abs.__name__: operator.abs,
        operator.floordiv.__name__: operator.floordiv,
        operator.truediv.__name__: operator.truediv,
        'protected_div': operator.truediv,
        math.log.__name__: sp.log,
        math.sin.__name__: sp.sin,
        math.cos.__name__: sp.cos,
        math.tan.__name__: sp.tan
    }
"""

def add(x,y):
	return np.add(x,y)
def sub(x,y):
	return np.subtract(x,y)
def mul(x,y):
	return np.multiply(x,y)

# Avoid error while dividing by zero
def protected_div(x1, x2):
	res = np.divide(x1,x2)
	try:
		res[np.isinf(res)] = 1
		res[np.isnan(res)] = 1
	except:
		return np.divide(x1,x2)
	return res

class EasyGeppy:
	def __init__(self, data, x_columns, y_column, random_seed=0):
		random.seed(random_seed)
		np.random.seed(random_seed)

		self.data = data.copy()

		self.x_columns = x_columns
		self.y_column = y_column

		self.logs = []

	
	def default_initialization(self, n_pop=100):

		self.pset = self.define_operators()

		self.creator = self.get_creator()

		self.creator = self.get_creator_of_individuals(self.creator)

		self.toolbox = self.get_toolbox()

		self.tools = self.get_tools()

		self.toolbox = self.set_create_population()
		
		evaluator = self.get_evaluator()

		self.toolbox.register('evaluate', evaluator)

		self.toolbox = self.register_genetic_operators()

		self.stats = self.get_generation_statistics()

		self.pop = self.toolbox.population(n=n_pop)

		self.top_best_individuals = self.tools.HallOfFame(3)   # only record the best three individuals ever found in all generations

	
	def define_operators(self):
		pset = gep.PrimitiveSet('Main', input_names=self.x_columns)
		#pset.add_function(operator.add, 2)
		#pset.add_function(operator.sub, 2)
		#pset.add_function(operator.mul, 2)
		#pset.add_function(protected_div, 2)
		pset.add_function(add, 2)
		pset.add_function(sub, 2)
		pset.add_function(mul, 2)
		pset.add_function(protected_div, 2)
		pset.add_ephemeral_terminal(name='enc', gen=lambda: random.random()*random.randint(-1000000, 1000000)) # each ENC is a random integer within [-10, 10]
		
		return pset
	
	def get_creator_of_individuals(self,creator_):
		try:
			del creator_.FitnessMin
			del creator_.Individual
		except:
			pass
		creator_.create("FitnessMin",
						base.Fitness,
						weights=(-1,))  # to minimize the objective (fitness)
		creator_.create("Individual",
						gep.Chromosome,
						fitness=creator_.FitnessMin)
		return creator_
	
	def get_creator(self):
		return dill.loads(dill.dumps(creator))

	def get_toolbox(self):
		return gep.Toolbox()
	
	def get_tools(self):
		return dill.loads(dill.dumps(tools))
	
	def set_create_population(self):
		head_length = 7 # head length
		n_genes = 2   # number of genes in a chromosome

		self.toolbox.register('gene_gen', gep.Gene, pset=self.pset, head_length=head_length)
		self.toolbox.register('individual',
							self.creator.Individual,
							gene_gen=self.toolbox.gene_gen,
							n_genes=n_genes,linker=operator.add)

		self.toolbox.register("population",
							self.tools.initRepeat,
							list,
							self.toolbox.individual)

		# compile utility: which translates an individual into an executable function (Lambda)
		self.toolbox.register('compile', gep.compile_, pset=self.pset)
		return self.toolbox

	def individual_solver(self, individual, df):
		func = self.toolbox.compile(individual)
		args_n = []
		for col in self.x_columns:
			args_n.append('pd.Series('+str(df[col].to_list())+')')
		args = ', '.join(args_n)
		code = 'func({})'.format(args)
		results = eval(code)
		return results
	
	def get_individual_solver_as_func(self, individual):
		def solver(df):
			return self.individual_solver(individual, df)
		return solver

	def get_evaluator(self):
		def evaluate_(individual):
			"""Evalute the fitness of an individual: MAPE (mean absolute percent error)"""
			results = self.individual_solver(individual, self.data)
			#print(results)
			try:
				Yp = results
			except:
				Yp = np.array(results)
			minimum = np.min(self.data[self.y_column].values)
			maximum = np.max(self.data[self.y_column].values)
			amplitude = maximum-minimum
			return np.mean(np.abs(self.data[self.y_column].values - Yp))/amplitude,
		
		return evaluate_

	def register_genetic_operators(self):
		self.toolbox.register('select', self.tools.selTournament, tournsize=3)
		# 1. general operators
		self.toolbox.register('mut_uniform', gep.mutate_uniform, pset=self.pset, ind_pb=0.05, pb=1)
		self.toolbox.register('mut_invert', gep.invert, pb=0.1)
		self.toolbox.register('mut_is_transpose', gep.is_transpose, pb=0.1)
		self.toolbox.register('mut_ris_transpose', gep.ris_transpose, pb=0.1)
		self.toolbox.register('mut_gene_transpose', gep.gene_transpose, pb=0.1)
		self.toolbox.register('cx_1p', gep.crossover_one_point, pb=0.4)
		self.toolbox.register('cx_2p', gep.crossover_two_point, pb=0.2)
		self.toolbox.register('cx_gene', gep.crossover_gene, pb=0.1)
		self.toolbox.register('mut_ephemeral', gep.mutate_uniform_ephemeral, ind_pb=0.05)  # 1p: expected one point mutation in an individual
		self.toolbox.pbs['mut_ephemeral'] = 1  # we can also give the probability via the pbs property
		return self.toolbox
	
	def get_generation_statistics(self):
		stats = self.tools.Statistics(key=lambda ind: ind.fitness.values[0])
		stats.register("size", len)
		stats.register("avg", np.mean)
		stats.register("std", np.std)
		stats.register("min", np.min)
		stats.register("max", np.max)
		return stats
	
	def launch_evolution(self, n_pop=100, n_gen=300):

		# start evolution
		self.pop, self.log = gep.gep_simple(self.pop, self.toolbox, n_generations=n_gen, n_elites=1,
								stats=self.stats, hall_of_fame=self.top_best_individuals, verbose=True)

		self.best_individual = self.top_best_individuals[0]

		self.logs.append(self.log)

	def get_individual_simplified(self, individual=0):
		return gep.simplify(self.pop[individual])

	def get_best_solution_simplified(self):
		return gep.simplify(self.best_individual)

	def get_best_solution_as_function(self):
		return self.get_individual_solver_as_func(self.best_individual)
	
	def clean_logs(self):
		del self.logs
		self.logs = []