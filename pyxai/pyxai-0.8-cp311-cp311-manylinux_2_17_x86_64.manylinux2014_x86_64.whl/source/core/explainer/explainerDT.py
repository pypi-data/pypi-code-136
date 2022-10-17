import time
from pyxai.source.core.explainer.Explainer import Explainer
from pyxai.source.core.structure.decisionTree import DecisionTree, DecisionNode
from pyxai.source.core.structure.type import TypeReason, TypeCount, PreferredReasonMethod
from pyxai.source.core.tools.encoding import CNFencoding
from pyxai.source.solvers.MAXSAT.OPENWBOSolver import OPENWBOSolver
from pyxai.source.solvers.SAT.glucoseSolver import GlucoseSolver
from pyxai.source.solvers.COMPILER.D4Solver import D4Solver
from pyxai.source.core.tools.utils import compute_weight


class ExplainerDT(Explainer):

  def __init__(self, tree, instance=None):
    """Create object dedicated to finding explanations from a decision tree ``tree`` and an instance ``instance``. 

    Args:
        tree (DecisionTree): The model in the form of a DecisionTree object.
        instance (:obj:`list` of :obj:`int`, optional): The instance (an observation) on which explanations must be calculated. Defaults to None.
    """
    super().__init__()
    self.tree = tree  # The decision tree.
    if instance is not None: self.set_instance(instance)


  def to_implicant(self, instance):
    return self.tree.instance_to_binaries(instance)


  def is_implicant(self, implicant):
    return self.tree.is_implicant(implicant, self.target_prediction)


  def predict_instance(self, instance):
    return self.tree.predict_instance(instance)


  def to_features(self, implicant, *, eliminate_redundant_features=True, details=False):
    """_summary_

    Args:
        implicant (_type_): _description_

    Returns:
        _type_: _description_
    """
    return self.tree.to_features(implicant, details=details, eliminate_redundant_features=eliminate_redundant_features)


  def direct_reason(self):
    """

    Returns:
        _type_: _description_
    """
    self.elapsed_time = 0
    direct_reason = self.tree.direct_reason(self.instance)
    if any(not self._is_specific(l) for l in direct_reason): return None # The reason contains excluded features
    return Explainer.format(direct_reason)


  def contrastive_reason(self, *, n=1):
    self.elapsed_time = 0
    cnf = self.tree.to_CNF(self.instance)
    core = CNFencoding.extract_core(cnf, self.implicant)
    core = [c for c in core if all(self._is_specific(l) for l in c)]  # remove excluded
    contrastives = sorted(core, key=lambda clause: len(clause))
    return Explainer.format(contrastives, n) if type(n) != int else Explainer.format(contrastives[:n], n)


  def necessary_literals(self):
    self.elapsed_time = 0
    cnf = self.tree.to_CNF(self.instance, target_prediction=self.target_prediction)
    core = CNFencoding.extract_core(cnf, self.implicant)
    # DO NOT remove excluded features. If they appear, they explain why there is no sufficient
    return sorted({l for _, clause in enumerate(core) if len(clause) == 1 for l in clause})


  def relevant_literals(self):
    self.elapsed_time = 0
    cnf = self.tree.to_CNF(self.instance, target_prediction=self.target_prediction)
    core = CNFencoding.extract_core(cnf, self.implicant)
    return [l for _, clause in enumerate(core) if len(clause) > 1 for l in clause if self._is_specific(l)]  # remove excluded features

  def _excluded_features_are_necesssary(self, prime_cnf):
    for l in prime_cnf.necessary:
      if self._is_specific(l) is False:
        return True
    return False

  def sufficient_reason(self, *, n=1, time_limit=None):
    time_used = 0
    n = n if type(n) == int else float('inf')
    cnf = self.tree.to_CNF(self.instance, target_prediction=self.target_prediction)
    prime_implicant_cnf = CNFencoding.to_prime_implicant_CNF(cnf, self.implicant)

    if self._excluded_features_are_necesssary(prime_implicant_cnf):
      self.elapsed_time = 0
      return None

    SATsolver = GlucoseSolver()
    SATsolver.add_clauses(prime_implicant_cnf.cnf)

    # Remove excluded features
    SATsolver.add_clauses([[-prime_implicant_cnf.from_original_to_new(l)] for l in self._excluded_literals])

    sufficient_reasons = []
    while True:
      if (time_limit is not None and time_used > time_limit) or len(sufficient_reasons) == n:
        break
      result, time = SATsolver.solve(None if time_limit is None else time_limit - time_used)
      time_used += time
      if result is None: break
      sufficient_reasons.append(prime_implicant_cnf.get_reason_from_model(result))
      SATsolver.add_clauses([prime_implicant_cnf.get_blocking_clause(result)])
    self.elapsed_time = time_used if (time_limit is None or time_used < time_limit) else Explainer.TIMEOUT
    return Explainer.format(sufficient_reasons, n)


  def preferred_reason(self, *, method, n=1, time_limit=None, weights=None):
    n = n if type(n) == int else float('inf')
    cnf = self.tree.to_CNF(self.instance)
    self.elapsed_time = 0

    prime_implicant_cnf = CNFencoding.to_prime_implicant_CNF(cnf, self.implicant)

    # excluded are necessary => no reason
    if self._excluded_features_are_necesssary(prime_implicant_cnf): return None

    cnf = prime_implicant_cnf.cnf
    if len(cnf) == 0:  # TODO: test when this case append
      return [l for l in prime_implicant_cnf.necessary]

    weights = compute_weight(method, self.instance, weights, self.tree.ML_solver_information)
    weights_per_feature = {i + 1: weight for i, weight in enumerate(weights)}

    soft = [l for l in prime_implicant_cnf.mapping_original_to_new if l != 0]
    weights_soft = []
    for l in soft:  # soft clause 
      for i in range(len(self.instance)):
        if self.tree.to_features([l], eliminate_redundant_features=False, details=True)[0]["id"] == i + 1:
          weights_soft.append(weights[i])

    solver = OPENWBOSolver()

    # Hard clauses
    for c in cnf:
      solver.add_hard_clause(c)

    # Soft clauses
    for i in range(len(soft)):
      solver.add_soft_clause([-soft[i]], weights_soft[i])

    # Remove excluded features
    for l in self._excluded_literals:
      solver.add_hard_clause([-prime_implicant_cnf.from_original_to_new(l)])

    # Solving
    time_used = 0
    best_score = -1
    reasons = []
    first_call = True

    while True:
      status, model, time = solver.solve(time_limit=0 if time_limit is None else time_limit - time_used)
      time_used += time
      if model is None:
        break

      preferred = prime_implicant_cnf.get_reason_from_model(model)
      solver.add_hard_clause(prime_implicant_cnf.get_blocking_clause(model))
      # Compute the score
      score = sum([weights_per_feature[feature["id"]] for feature in
                   self.tree.to_features(preferred, eliminate_redundant_features=False, details=True)])
      if first_call:
        best_score = score
      elif score != best_score:
        break
      first_call = False
      reasons.append(preferred)
      if (time_limit is not None and time_used > time_limit) or len(reasons) == n:
        break
    self.elapsed_time = time_used if time_limit is None or time_used < time_limit else Explainer.TIMEOUT
    return Explainer.format(reasons, n)


  def minimal_sufficient_reason(self, *, n=1, time_limit=None):
    return self.preferred_reason(method=PreferredReasonMethod.Minimal, n=n, time_limit=time_limit)


  def n_sufficient_reasons_per_attribute(self, *, time_limit=None):
    cnf = self.tree.to_CNF(self.instance)
    prime_implicant_cnf = CNFencoding.to_prime_implicant_CNF(cnf, self.implicant)

    if self._excluded_features_are_necesssary(prime_implicant_cnf):
      self.elapsed_time = 0
      return None

    if len(prime_implicant_cnf.cnf) == 0:  # Special case where all in necessary
      return {l: 1 for l in prime_implicant_cnf.necessary}

    compiler = D4Solver()
    # Remove excluded features
    cnf = list(prime_implicant_cnf.cnf)
    for l in self._excluded_literals:
     cnf.append([-prime_implicant_cnf.from_original_to_new(l)])

    compiler.add_cnf(cnf, prime_implicant_cnf.n_literals - 1)
    compiler.add_count_model_query(cnf, prime_implicant_cnf.n_literals - 1, prime_implicant_cnf.n_literals_mapping)

    time_used = -time.time()
    n_models = compiler.solve(time_limit)
    time_used += time.time()

    self.elapsed_time = Explainer.TIMEOUT if n_models[1] == -1 else time_used

    n_necessary = n_models[0] if len(n_models) > 0 else 1

    n_sufficients_per_attribute = {n: n_necessary for n in prime_implicant_cnf.necessary}
    for l in range(1, prime_implicant_cnf.n_literals_mapping):
      n_sufficients_per_attribute[prime_implicant_cnf.mapping_new_to_original[l]] = n_models[l]
    return n_sufficients_per_attribute


  def is_reason(self, reason, *, n_samples=-1):
    return self.tree.is_implicant(reason, self.target_prediction)


  def rectify(self, tree, positive_rectifying_tree, negative_rectifying_tree):
    not_positive_rectifying_tree = positive_rectifying_tree.negating_tree()
    not_negative_rectifying_tree = negative_rectifying_tree.negating_tree()

    tree_1 = positive_rectifying_tree.concatenate_tree(not_negative_rectifying_tree)
    tree_2 = negative_rectifying_tree.concatenate_tree(not_positive_rectifying_tree)

    not_tree_2 = tree_2.negating_tree()

    tree_and_not_tree_2 = tree.concatenate_tree(not_tree_2)
    tree_and_not_tree_2.simplify()

    tree_and_not_tree_2_or_tree_1 = tree_and_not_tree_2.disjoint_tree(tree_1)
    tree_and_not_tree_2_or_tree_1.simplify()
    return tree_and_not_tree_2_or_tree_1
