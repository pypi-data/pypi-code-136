from typing import Iterable
from pyxai.source.core.tools.utils import count_dimensions
import random


class Explainer:
  TIMEOUT = -1

  def __init__(self):
    self.implicant = None
    self.elapsed_time = 0
    self._excluded_literals = []
    self._excluded_features = []

  def set_instance(self, instance):
    """Change the instance on which explanations must be calculated.
    Args:
        instance (obj:`list` of :obj:`int`): The instance (an observation) on which explanations must be calculated.
    """
    if count_dimensions(instance) != 1:
      raise ValueError("The instance parameter should be an iterable of only one dimension (not " + str(count_dimensions(instance)) + ").")

    # The target observation.
    self.instance = instance
    # An implicant of self.tree (a term that implies the tree)
    self.implicant = self.to_implicant(instance)

    # The target prediction (0 or 1)
    self.target_prediction = self.predict_instance(self.instance)
    self.set_excluded_features(self._excluded_features)


  def set_excluded_features(self, excluded_features):
    if len(excluded_features) == 0:
      self.unset_specific_features()
      return

    if self.implicant is None:
      implicant = self.extend_reason_to_complete_implicant([]) # we want to know if binary lits are related to excluded features
    else:
      implicant = self.implicant
    self._excluded_literals = [l for l in implicant if self.to_features([l], eliminate_redundant_features=False, details=True)[0]['name'] in excluded_features]
    self._excluded_features = excluded_features
    print("imp", implicant)
    print('excluded', self._excluded_literals)

  # TODO a changer en je veux ces features
  def _set_specific_features(self, specific_features):
    excluded = []
    if self.tree is not None:
      excluded = [f for f in self.tree.ML_solver_information.feature_name if f not in specific_features]
    if self.random_forest is not None:
      excluded = [f for f in self.random_forest.ML_solver_information.feature_name if f not in specific_features]
    if self.boosted_tree is not None:
      excluded = [f for f in self.boosted_tree.ML_solver_information.feature_name if f not in specific_features]

    if excluded is None:
      raise NotImplementedError
    self.set_excluded_features(excluded)


  def unset_specific_features(self):
    self._excluded_literals = []
    self._excluded_features = []


  def _is_specific(self, l):
    return l not in self._excluded_literals


  def reason_contains_features(self, reason, features_name):
    return any(self.to_features([l], eliminate_redundant_features=False, details=True)[0]['name'] in features_name for l in reason)


  def to_implicant(self, instance):
    raise NotImplementedError


  def to_features(self, implicant, eliminate_redundant_features=True, details=False):
    raise NotImplementedError


  def sufficient_reason(self, *, n=1, seed=0):
    raise NotImplementedError


  def direct_reason(self):
    """
    Raises:
        NotImplementedError: _description_
    """
    raise NotImplementedError


  def predict_instance(self, instance):
    raise NotImplementedError


  def is_implicant(self, implicant):
    raise NotImplementedError


  def is_reason(self, reason, *, n_samples=1000):
    for _ in range(n_samples):
      implicant = self.extend_reason_to_complete_implicant(reason)
      if not self.is_implicant(implicant):
        return False
    return True


  def is_sufficient_reason(self, reason, *, n_samples=50):
    print(reason)
    if not self.is_reason(reason, n_samples=n_samples):
      return False # We are sure it is not a reason
    tmp = list(reason)
    random.shuffle(tmp)
    i = 0
    for lit in tmp:
      copy_reason = list(reason).copy()
      copy_reason.remove(lit)
      copy_reason.append(-lit)
      if self.is_reason(copy_reason, n_samples=n_samples):
        return None
      i += 1
      if i > n_samples: break
    return True


  def is_contrastive_reason(self, reason):
    copy_implicant = list(self.implicant).copy()
    for lit in reason:
      copy_implicant[copy_implicant.index(lit)] = -lit
    return not self.is_implicant(copy_implicant)


  def extend_reason_to_complete_implicant(self, reason):
    complete = list(reason).copy()
    to_add = [literal for literal in self.implicant if literal not in complete and -literal not in complete]
    for literal in to_add:
      sign = random.choice([1, -1])
      complete.append(sign * abs(literal))
    assert len(complete) == len(self.implicant)
    return complete


  @staticmethod
  def format(reasons, n=1):
    if len(reasons) == 0:
      return tuple()
    if len(reasons) == 1 and isinstance(reasons[0], Iterable):
      if type(n) != int:
        return tuple(tuple(sorted(reason, key=lambda l: abs(l))) for reason in reasons)
      elif type(n) == int and n != 1:
        return tuple(tuple(sorted(reason, key=lambda l: abs(l))) for reason in reasons)
      else:
        return Explainer.format(reasons[0])
    if not isinstance(reasons[0], Iterable):
      return tuple(sorted(reasons, key=lambda l: abs(l)))

    return tuple(tuple(sorted(reason, key=lambda l: abs(l))) for reason in reasons)



