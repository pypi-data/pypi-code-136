from pyxai.source.core.explainer.Explainer import Explainer
from pyxai.source.core.tools.encoding import CNFencoding
from pyxai.source.core.structure.type import Encoding, PreferredReasonMethod, TypeReason
from pyxai.source.solvers.MUS.MUSERSolver import MUSERSolver
from pyxai.source.solvers.MUS.OPTUXSolver import OPTUXSolver
from pyxai.source.solvers.SAT.glucoseSolver import GlucoseSolver
from pyxai.source.solvers.MAXSAT.OPENWBOSolver import OPENWBOSolver
from pyxai.source.core.tools.utils import compute_weight
from pyxai.source.core.structure.type import TypeReason, ReasonExpressivity

import c_explainer

import numpy
import random

class ExplainerRF(Explainer):

  def __init__(self, random_forest, instance=None):
    """Create object dedicated to finding explanations from a random forest ``random_forest`` and an instance ``instance``. 

    Args:
        random_forest (RandomForest): The model in the form of a RandomForest object.
        instance (:obj:`list` of :obj:`int`, optional): The instance (an observation) on which explanations must be calculated. Defaults to None.
    
    Raises:
        NotImplementedError: Currently, the explanations from a random forest are not available in the multi-class scenario (work in progress).
    """
    super().__init__()
    if random_forest.n_classes > 2:
      raise NotImplementedError("Currently, the explanations from a random forest are not available in the multi-class scenario (work in progress).")

    self.random_forest = random_forest
    self.c_RF = None
    if instance is not None: self.set_instance(instance)


  def to_features(self, implicant, *, eliminate_redundant_features=True, details=False):
    """
    Convert each literal of the implicant (representing a condition) to a tuple (``id_feature``, ``threshold``, ``sign``, ``weight``). 
      - ``id_feature``: the feature identifier.
      - ``threshold``: threshold in the condition id_feature < threshold ?
      - ``sign``: indicate if the condition (id_feature < threshold) is True or False in the reason.
      - ``weight``: possible weight useful for some methods (can be None).
      
    Remark: Eliminate the redundant features (example: feature5 < 0.5 and feature5 < 0.4 => feature5 < 0.4).
    
    Args:
        implicant (obj:`list` of :obj:`int`): The reason or an implicant.

    Returns:
        obj:`tuple` of :obj:`tuple` of size 4: Represent the reason in the form of features (with their respective thresholds, signs and possible weights)  
    """
    return self.random_forest.to_features(implicant, eliminate_redundant_features=eliminate_redundant_features, details=details)


  def to_implicant(self, instance):
    return  self.random_forest.instance_to_binaries(instance)


  def is_implicant(self, implicant):
    return self.random_forest.is_implicant(implicant, self.target_prediction)

  def predict_instance(self, instance):
    return self.random_forest.predict_instance(instance)


  def direct_reason(self):
    """The direct reason of an instance x is the term t of the implicant (binary form of the instance) corresponding to the unique root-to-leaf path of the tree that covers x. (see the Trading Complexity for Sparsity
    in Random Forest Explanations paper (Gilles Audemard, Steve Bellart, Louenas Bounia, Frederic Koriche,
    Jean-Marie Lagniez and Pierre Marquis1) for more information)

    Returns:
        (obj:`list` of :obj:`int`): Reason in the form of literals (binary form). The to_features() method allows to obtain the features of this reason.
    """
    self.elapsed_time = 0
    direct_reason = set()
    for tree in self.random_forest.forest:
      local_target_prediction = tree.predict_instance(self.instance)
      if local_target_prediction == self.target_prediction:
        local_direct = tree.direct_reason(self.instance)
        direct_reason |= set(local_direct)

    # remove excluded features
    if any(not self._is_specific(l) for l in direct_reason): return None
    return Explainer.format(list(direct_reason))


  def minimal_contrastive_reason(self, *, n=1, time_limit=None):
    """Formally, a contrastive explanation for an instance x given f is a subset t of the characteristics of x that is minimal w.r.t. set inclusion among those such that at least one other instance x' that coincides with x except on the characteristics from t is not classified by f as x is. See the On the Explanatory Power of Decision Trees paper (Gilles Audemard, Steve Bellart, Louenas Bounia, Frédéric Koriche, Jean-Marie Lagniez, and Pierre Marquis) for more details. This method compute one or several minimal (in size) contrastive reasons.

    Args:
        n (int, optional): The desired number of reasons. Defaults to 1.

    Returns:
        (:obj:`tuple` of :obj:`tuple` of `int`): Reasons in the form of literals (binary form). The to_features() method allows to obtain the features of reasons. When only one reason is requested through the 'n' parameter, return just one :obj:`tuple` of `int` (and not a :obj:`tuple` of :obj:`tuple`).
    """
    n = n if type(n) == int else float('inf')
    first_call = True
    time_limit = 0 if time_limit is None else time_limit
    best_score = 0
    tree_cnf = self.random_forest.to_CNF(self.instance, self.implicant, target_prediction=1 if self.target_prediction == 0 else 0)
    max_id_variable = CNFencoding.compute_max_id_variable(self.implicant)
    MAXSATsolver = OPENWBOSolver()
    for l in self.implicant:
      MAXSATsolver.add_soft_clause([l], weight=1)
    for clause in tree_cnf:
      MAXSATsolver.add_hard_clause(clause)

    # Remove excluded features
    for l in self._excluded_literals:
      MAXSATsolver.add_hard_clause([l])

    time_used = 0
    results = []
    while True:
      status, reason, time = MAXSATsolver.solve(time_limit=time_limit)
      time_used += time
      if time_limit != 0 and time_used > time_limit:
        break
      if reason is None: break
      # We have to invert the reason :)
      true_reason = [-l for l in reason if -l in self.implicant]
      MAXSATsolver.add_hard_clause([-l for l in reason if abs(l) <= max_id_variable])


      # Compute the score
      score = len(true_reason)
      if first_call:
        best_score = score
      elif score != best_score:
        break
      first_call = False

      results.append(true_reason)
      if (time_limit != 0 and time_used > time_limit) or len(results) == n:
        break
    self.elapsed_time = time_used if time_limit == 0 or time_used < time_limit else Explainer.TIMEOUT
    return Explainer.format(results, n)


  def sufficient_reason(self, *, time_limit=None):
    """A sufficient reason (also known as prime implicant explanation) for an instance x given a class described by a Boolean function f is a subset t of the characteristics of x that is minimal w.r.t. set inclusion such that any instance x' sharing this set t of characteristics is classified by f as x is. 

    Returns:
        (obj:`list` of :obj:`int`): Reason in the form of literals (binary form). The to_features() method allows to obtain the features of this reason.
    """
    hard_clauses = self.random_forest.to_CNF(self.instance, self.implicant, self.target_prediction, tree_encoding=Encoding.MUS)
    # Check if excluded features produce a SAT problem => No sufficient reason

    if len(self._excluded_literals) > 0:
      SATSolver = GlucoseSolver()
      SATSolver.add_clauses(hard_clauses)
      SATSolver.add_clauses([[l] for l in  self.implicant if self._is_specific(l)])
      result, time  = SATSolver.solve(time_limit=time_limit)
      if result is not None: return None

    hard_clauses = list(hard_clauses)
    soft_clauses = tuple((l,) for l in self.implicant if self._is_specific(l))
    mapping = [0 for _ in range(len(self.implicant) + 2)]
    i = 2 # first good group for literals is 2 (1 is for the CNF representing the RF.
    for l in self.implicant:
      if self._is_specific(l):
        mapping[i] = l
        i+= 1
    n_variables = CNFencoding.compute_n_variables(hard_clauses)
    muser_solver = MUSERSolver()
    muser_solver.write_gcnf(n_variables, hard_clauses, soft_clauses)
    model, status, self.elapsed_time = muser_solver.solve(time_limit)
    reason = [mapping[i] for i in model if i > 1]
    return Explainer.format(reason, 1)

  def minimal_sufficient_reason(self, time_limit=None):
    """A sufficient reason (also known as prime implicant explanation) for an instance x given a class described by a Boolean function f is a subset t of the characteristics of x that is minimal w.r.t. set inclusion such that any instance x' sharing this set t of characteristics is classified by f as x is. 

    This method compute minimal sufficient reason. A minimal sufficient reason for x given f is a sufficient reason for x given f that contains a minimal number of literals.

    Returns:
        (obj:`list` of :obj:`int`): Reason in the form of literals (binary form). The to_features() method allows to obtain the features of this reason.
    """


    hard_clauses = self.random_forest.to_CNF(self.instance, self.implicant, self.target_prediction, tree_encoding=Encoding.MUS)


    if len(self._excluded_literals) > 0:
      SATSolver = GlucoseSolver()
      SATSolver.add_clauses(hard_clauses)
      SATSolver.add_clauses([[l] for l in  self.implicant if self._is_specific(l)])
      result = SATSolver.solve(time_limit=time_limit)
      if result is not None : return None

    soft_clauses = tuple((l,) for l in self.implicant if self._is_specific(l))
    optux_solver = OPTUXSolver()
    optux_solver.add_hard_clauses(hard_clauses)
    optux_solver.add_soft_clauses(soft_clauses, weight=1)
    reason = optux_solver.solve(self.implicant)
    return Explainer.format(reason)


  def majoritary_reason(self, *, n=1, n_iterations=50, time_limit=None, seed=0):
    """Informally, a majoritary reason for classifying a instance x as positive by some random forest f
    is a prime implicant t of a majority of decision trees in f that covers x. (see the Trading Complexity for Sparsity
    in Random Forest Explanations paper (Gilles Audemard, Steve Bellart, Louenas Bounia, Frederic Koriche,
    Jean-Marie Lagniez and Pierre Marquis1) for more information)

    Args:
        n (int|ALL, optional): The desired number of reasons. Defaults to 1, currently needs to be 1 or Exmplainer.ALL.
        time_limit (int, optional): The maximum time to compute the reasons. None to have a infinite time. Defaults to None.
    """
    reason_expressivity = ReasonExpressivity.Conditions  # TODO
    if seed is None: seed = -1
    if isinstance(n, int) and n == 1:
      if self.c_RF is None:
        # Preprocessing to give all trees in the c++ library
        self.c_RF = c_explainer.new_RF(self.random_forest.n_classes)
        for tree in self.random_forest.forest:
          try:
            c_explainer.add_tree(self.c_RF, tree.raw_data_for_CPP())
          except Exception as e:
            print("Erreur", str(e))
            exit(1)

      if time_limit is None: time_limit = 0
      implicant_id_features = ()  # FEATURES : TODO
      c_explainer.set_excluded(self.c_RF, tuple(self._excluded_literals))
      reason = c_explainer.compute_reason(self.c_RF, self.implicant, implicant_id_features, self.target_prediction, n_iterations, time_limit, int(reason_expressivity), seed)
      if reason_expressivity == ReasonExpressivity.Conditions:
        return reason
      elif reason_expressivity == ReasonExpressivity.Features:
        return self.to_features_indexes(reason)

    if isinstance(n, int) and n != 1:
      raise NotImplementedError("Currently, only n set to 1 or All is available.")

    n = n if type(n) == int else float('inf')

    clauses = self.random_forest.to_CNF(self.instance, self.implicant, self.target_prediction, tree_encoding=Encoding.SIMPLE)
    max_id_variable = CNFencoding.compute_max_id_variable(self.implicant)
    solver = GlucoseSolver()

    solver.add_clauses([[l for l in clause if l in self.implicant or abs(l) > max_id_variable] for clause in clauses])

    if len(self._excluded_literals) > 0:
      solver.add_clauses([-l] for l in self._excluded_literals)

    majoritaries = []
    time_used = 0
    while True:
      result, time = solver.solve()
      time_used += time
      if result is None or (time_limit is not None and time_used > time_limit) or (time_limit is None and len(majoritaries) >= n):
        break

      majoritary = [l for l in result if l in self.implicant]
      if majoritary not in majoritaries: majoritaries.append(majoritary)
      solver.add_clauses([[-l for l in result if abs(l) <= max_id_variable]])  # block this implicant
    self.elapsed_time = time_used if (time_limit is None or time_used < time_limit) else Explainer.TIMEOUT
    return Explainer.format(CNFencoding.remove_subsumed(majoritaries), n)


  def preferred_majoritary_reason(self, *, method, n=1, time_limit=None, weights=None):
    """This approach consists in exploiting a model, making precise her / his
    preferences about reasons, to derive only preferred reasons. See the On Preferred Abductive Explanations for Decision Trees and Random Forests paper (Gilles Audemard, Steve Bellart, Louenas Bounia, Frederic Koriche, Jean-Marie Lagniez and Pierre Marquis) for more details. 
    
    Several methods are available thought the method parameter:
      `PreferredReasonMethod.MINIMAL`: Equivalent to minimal_majoritary_reason().
      `PreferredReasonMethod.WEIGHTS`: Weight given bu the user thought the weights parameters.
      `PreferredReasonMethod.SHAPELY`: Shapely values for the model trained on data. Only available with a model from scikitlearn or a save from scikitlearn (not compatible with a generic save). For each random forest F, the opposite of the SHAP score [Lundberg and Lee, 2017; Lundberg et al., 2020] of each feature of the instance x at hand given F computed using SHAP (shap.readthedocs.io/en/latest/api.html)
      `PreferredReasonMethod.FEATURE_IMPORTANCE`: The opposite of the f-importance of each feature in F as computed by Scikit-Learn [Pedregosa et al., 2011]. Only available with a model from scikitlearn or a save from scikitlearn (not compatible with a generic save).
      `PreferredReasonMethod.WORD_FREQUENCY`: The opposite of the Zipf frequency of each feature viewed as a word in the wordfreq library.
      `PreferredReasonMethod.WORD_FREQUENCY_LAYERS`: WORD_FREQUENCY with layers.
      
    Args:
        n (int|ALL, optional): The desired number of reasons. Defaults to Explainer.ALL.
        time_limit (int, optional): The maximum time to compute the reasons. None to have a infinite time. Defaults to None.
        method (Explainer.MINIMAL|Explainer.WEIGHTS|, optional): _description_. Defaults to None.
        weights (:obj:`list` of `int`|:obj:`list`, optional): Can be a list representing the weight of each feature or a dict where a key is a feature and the value its weight. Defaults to None.

    Returns:
        _type_: _description_
    """

    n = n if type(n) == int else float('inf')

    clauses = self.random_forest.to_CNF(self.instance, self.implicant, self.target_prediction, tree_encoding=Encoding.SIMPLE)
    n_variables = CNFencoding.compute_n_variables(clauses)
    id_features = [feature["id"] for feature in self.random_forest.to_features(self.implicant, eliminate_redundant_features=False, details=True)]

    weights = compute_weight(method, self.instance, weights, self.random_forest.forest[0].ML_solver_information)

    solver = OPENWBOSolver()
    max_id_variable = CNFencoding.compute_max_id_variable(self.implicant)
    map_abs_implicant = [0 for i in range(0, n_variables + 1)]
    for l in self.implicant: map_abs_implicant[abs(l)] = l

    # Hard clauses
    for c in clauses:
      solver.add_hard_clause([l for l in c if abs(l) > max_id_variable or map_abs_implicant[abs(l)] == l])

    # excluded features
    for l in self.implicant:
      if not self._is_specific(l): solver.add_hard_clause([-l])

    # Soft clauses
    for i in range(len(self.implicant)):
      solver.add_soft_clause([-self.implicant[i]], weights[id_features[i] - 1])

    # Solving
    time_used = 0
    best_score = -1
    reasons = []
    first_call = True

    while True:
      status, model, time = solver.solve(time_limit=None if time_limit is None else time_limit - time_used)
      time_used += time
      if model is None:
        if first_call: return None
        return Explainer.format(reasons, n)

      prefered_reason = [l for l in model if l in self.implicant]
      solver.add_hard_clause([-l for l in model if abs(l) <= max_id_variable])

      # Compute the score
      score = numpy.sum([weights[id_features[abs(l) - 1] - 1] for l in prefered_reason])
      if first_call:
        best_score = score
      elif score != best_score:
        return Explainer.format(reasons)
      first_call = False

      reasons.append(prefered_reason)
      if (time_limit is not None and time_used > time_limit) or len(reasons) == n:
        break
    self.elapsed_time = time_used if time_limit is None or time_used < time_limit else Explainer.TIMEOUT
    return Explainer.format(reasons, n)


  def minimal_majoritary_reason(self, *, n=1, time_limit=None):
    return self.preferred_majoritary_reason(method=PreferredReasonMethod.Minimal, n=n, time_limit=time_limit)


  def is_majoritary_reason(self, reason):
    if not self.is_implicant(reason): return False
    tmp = list(reason)
    random.shuffle(tmp)
    for lit in tmp:
      copy_reason = list(reason).copy()
      copy_reason.remove(lit)
      if self.is_implicant(tuple(copy_reason)): return False
    return True



