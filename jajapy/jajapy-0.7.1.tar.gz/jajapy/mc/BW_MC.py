from .MC import MC, MC_random
from ..base.BW import *
from ..base.Set import Set
from numpy import log, newaxis, inf

class BW_MC(BW):
	"""
	class for general Baum-Welch algorithm on MC.
	"""
	def __init__(self):
		super().__init__()
	
	def fit(self, traces, initial_model: MC=None, nb_states: int=None,
			random_initial_state: bool=False, output_file: str=None,
			epsilon: float=0.01, max_it: int = inf, pp: str='',
			verbose: bool = True, return_data: bool= False,
			stormpy_output: bool = True):
		"""
		Fits the model according to ``traces``.

		Parameters
		----------
		traces : Set or list or numpy.ndarray
			training set.
		initial_model : MC, optional.
			first hypothesis. If not set it will create a random MC with
			``nb_states`` states. Should be set if ``nb_states`` is not set.
		nb_states: int
			If ``initial_model`` is not set it will create a random MC with
			``nb_states`` states. Should be set if ``initial_model`` is not set.
			Default is None.
		random_initial_state: bool
			If ``initial_model`` is not set it will create a random MC with
			random initial state according to this sequence of probabilities.
			Should be set if ``initial_model`` is not set.
			Default is False.
		output_file : str, optional
			if set path file of the output model. Otherwise the output model
			will not be saved into a text file.
		epsilon : float, optional
			the learning process stops when the difference between the
			loglikelihood of the training set under the two last hypothesis is
			lower than ``epsilon``. The lower this value the better the output,
			but the longer the running time. By default 0.01.
		max_it: int
			Maximal number of iterations. The algorithm will stop after `max_it`
			iterations.
			Default is infinity.
		pp : str, optional
			Will be printed at each iteration. By default ''
		verbose: bool, optional
			Print or not a small recap at the end of the learning.
			Default is True.
		return_data: bool, optional
			If set to True, a dictionary containing following values will be
			returned alongside the hypothesis once the learning is done.
			'learning_rounds', 'learning_time', 'training_set_loglikelihood'.
			Default is False.
		stormpy_output: bool, optional
			If set to True the output model will be a Stormpy sparse model.
			Default is True.

		Returns
		-------
		MC
			fitted MC.
		"""
		if type(traces) != Set:
			traces = Set(traces, t=0)
		if not initial_model:
			if not nb_states:
				print("Either nb_states or initial_model should be set")
				return
			initial_model = MC_random(nb_states,traces.getAlphabet(),random_initial_state)
		self.alphabet = initial_model.getAlphabet()
		return super().fit(traces, initial_model, output_file, epsilon, max_it, pp, verbose,return_data,stormpy_output)

	def _processWork(self,sequence,times):
		alpha_matrix = self.computeAlphas(sequence)
		beta_matrix = self.computeBetas(sequence)
		proba_seq = alpha_matrix.T[-1].sum()
		if proba_seq != 0.0:
			den = (alpha_matrix.T[:-1]*beta_matrix.T[:-1]*times/proba_seq).sum(axis=0)
			num = zeros(shape=(self.nb_states,self.nb_states,len(self.alphabet)))
			for s in range(self.nb_states):
				for ss in range(self.nb_states):
					p = array([self.h_tau(s,ss,o) for o in sequence])
					alph_bet = alpha_matrix[s][:-1]*p*beta_matrix[ss][1:]*times/proba_seq
					for o,obs in enumerate(self.alphabet):
						arr_dirak = [1 if t == obs else 0 for t in sequence]
						num[s,ss,o] = (alph_bet*arr_dirak).sum()
			####################
			num_init = alpha_matrix.T[0]*beta_matrix.T[0]*times/proba_seq
			####################
			return [den,num, proba_seq,times,num_init]
		return False

	def _generateHhat(self,temp):
		den = array([i[0] for i in temp]).sum(axis=0)
		num = array([i[1] for i in temp]).sum(axis=0)
		lst_proba=array([i[2] for i in temp])
		lst_times=array([i[3] for i in temp])
		lst_init =array([i[4] for i in temp]).T

		currentloglikelihood = dot(log(lst_proba),lst_times)

		for s in range(len(den)):
			if den[s] == 0.0:
				den[s] = 1.0
				num[s] = self.h.matrix[s]

		matrix = num/den[:, newaxis, newaxis]
		initial_state = [lst_init[s].sum()/lst_init.sum() for s in range(self.nb_states)]
		return [MC(matrix,self.alphabet,initial_state),currentloglikelihood]
		