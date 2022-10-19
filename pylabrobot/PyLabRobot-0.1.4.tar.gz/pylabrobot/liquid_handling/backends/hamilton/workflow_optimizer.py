PRINT = False



import enum
from typing import __annotations__
import math

class Well:
  def __init__(self, row, column):
    self.row = row
    self.column = column

  def distance_to_well(self, other):
    return abs(self.column - other.column)

  def __repr__(self) -> str:
    return f"Well({self.row}, {self.column})"

class Operation:
  def __init__(self, source, target):
    self.source = source
    self.target = target

  def distance(self):
    return self.source.distance_to_well(self.target)

  def __eq__(self, other) -> bool:
    return self.source == other.source and self.target == other.target

  def __str__(self) -> str:
    return f"{self.source} -> {self.target}"

  def __repr__(self) -> str:
    return f"Dispense(source={repr(self.source)}, target={repr(self.target)})"

class Aspiration:
  def __init__(self, source: Well):
    self.source = source
    self.dispense = None # is gonna be a backlink

  def __eq__(self, other):
    return self.source == other.source

  def __repr__(self) -> str:
    return f"Aspiration(source={repr(self.source)})"

class Dispense:
  def __init__(self, source: Well, asp: Aspiration):
    self.source = source
    self.asp = asp

    self.asp.dispense = self

  def __repr__(self) -> str:
    return f"Dispense(source={repr(self.source)})"


def is_valid(order): # is valid sub order: meaning, we could create a valid order from this sub order

  # loop over operations `order` and checks whether each new aspiration is "below" the previous
  # aspiration. a dispense clears an aspiration. the dispense has to be after the aspiration

  aspirations = []
  dispenses = []

  for op in order:
    if isinstance(op, Aspiration):
      # check if this aspiration is "below" the previous aspiration
      # TODO: this could be improved, we don't actually need to have this ordering to be valid
      if len(aspirations) > 0 and op.source.row < aspirations[-1].source.row:
        return False
      # check if this aspiration has already been used
      if op in aspirations:
        return False
      # check that length of aspirations <= 8
      if len(aspirations) > 8:
        return False
      aspirations.append(op)
    elif isinstance(op, Dispense):
      # check that this dispense is after its aspiration
      if not op.asp in aspirations:
        return False
      # check that this dispense has not been used
      if op in dispenses:
        return False
      aspirations.remove(op.asp)
      dispenses.append(op)

  return True #len(aspirations) == 0


asp = Aspiration(Well(1, 1))
disp = Dispense(Well(1, 1), asp)

asp2 = Aspiration(Well(2, 2))
disp2 = Dispense(Well(2, 2), asp2)

asp3 = Aspiration(Well(1, 2))
disp3 = Dispense(Well(1, 3), asp3)


# simple and true
operations1 = [
  asp,
  disp
]
print(is_valid(operations1), "should be True")

# false because the aspirate is not dispensed
operations2 = [
  asp,
  asp2,
  disp
]
print(is_valid(operations2), "should be False")

# false beacuse the dispense is not after the aspiration
operations3 = [
  asp,
  disp,
  disp2
]
print(is_valid(operations3), "should be False")

# true
operations4 = [
  asp,
  disp,
  asp2,
  disp2
]
print(is_valid(operations4), "should be True")

operations5 = [ # cost 62
  asp,
  disp,
  # move here has cost 1
  asp2,
  disp2,
  # here there is no move
  asp3,
  # move here has cost 1
  disp3
]
print(is_valid(operations5), "should be True")

ASPIRATE_COST = 10
DISPENSE_COST = 10
COST_PER_MOVE = 1

current_cost = 0
def current_cost_add(current_cost, current_order, op) -> int:
  # if can group, or not...
  if not (len(current_order) > 0 and \
    isinstance(op, type(current_order[-1])) and op.source.column == current_order[-1].source.column):
    if isinstance(op, Aspiration):
      current_cost += ASPIRATE_COST
    elif isinstance(op, Dispense):
      current_cost += DISPENSE_COST

    # If can't gruop, check if we need to move to come here
    if len(current_order) > 0 and (op.source.column != current_order[-1].source.column):
      current_cost += COST_PER_MOVE * op.source.distance_to_well(current_order[-1].source)

  return current_cost


# def cost(order):
#   # we assume the order is valid

#   cost = 0

#   i = 0

#   op_type = Aspiration

#   prev_x = None

#   while i < len(order):
#     op = order[i]
#     group = [op]

#     op_type = type(op)

#     # group all operations after this one while they are of the same type, and have the same column
#     while i+1 < len(order) and isinstance(order[i+1], op_type) and order[i].source.column == order[i+1].source.column:
#       group.append(order[i+1])
#       i += 1

#     if PRINT: print("group:", group)

#     # calculate the cost of this group
#     if op_type == Aspiration:
#       cost += ASPIRATE_COST
#     elif op_type == Dispense:
#       cost += DISPENSE_COST

#     # for each instance where a new group is created, add the cost of moving (just the x direction)
#     if prev_x is not None:
#       if PRINT: print("prev_x:", prev_x)
#       cost += abs(op.source.column - prev_x) * COST_PER_MOVE
#     prev_x = op.source.column

#     i += 1

#   return cost

def cost(order):
  current_cost = 0
  for i, op in enumerate(order):
    current_cost = current_cost_add(current_cost, order[:i], op)
  return current_cost


print(cost(operations1), "should be 20")

print(cost(operations4), "should be 41")



print(cost(operations5), "should be 62")


minimal_order = []
minimal_cost = None
# PRINT = True

def optimize(order, operations_left, current_cost=0):
  global minimal_cost
  if PRINT: print("enter optimize", order, operations_left)

  if len(operations_left) == 0:
    global minimal_order
    if minimal_cost is None or current_cost < minimal_cost:
      if PRINT or True: print("new min:", order, "cost:", current_cost)
      minimal_order = order
      minimal_cost = current_cost

    if PRINT: print("exit optimize", order, operations_left)
    return

  # options are operations that are either aspirations or dispenses where the aspiration is already used
  options = []
  # for op in operations_left:
  #   if PRINT: print("considering op:", op, order)
  #   if isinstance(op, Aspiration):
  #     options.append(op)
  #   elif isinstance(op, Dispense) and op.asp in order:
  #     options.append(op)

  # if len(options) == 0:
  #   raise Exception("no options")

  # find the best option
  # for opt in options:
  for opt in operations_left:
    if PRINT: print("considering order:", order + [opt], "is valid:", is_valid(order + [opt]))
    # if is_valid(order + [opt]) and (minimal_cost is None or cost(order + [opt]) < minimal_cost):
    aspiration_cost_left = 0#ASPIRATE_COST if any(isinstance(op, Aspiration) for op in operations_left) else 0
    dispense_cost_left = 0#DISPENSE_COST if any(isinstance(op, Dispense) for op in operations_left) else 0
    if is_valid(order + [opt]) and \
        (minimal_cost is None or \
          ((current_cost_add(current_cost, order, opt) + dispense_cost_left + aspiration_cost_left) < minimal_cost)):
      # add this option to the order
      dc = current_cost_add(current_cost, order, opt) - current_cost
      current_cost += dc
      order.append(opt)
      operations_left.remove(opt)

      if PRINT: print("order:", order)
      optimize(order.copy(), operations_left.copy(), current_cost)

      # remove the option
      current_cost -= dc
      order.pop()
      operations_left.append(opt)

  # return order

print("optimizing operations1")
minimal_order = []
minimal_cost = None
optimize([], operations1)
print(minimal_order, "should be asp,disp", cost(minimal_order), "should be 20")

print("optimizing operations4")
minimal_order = []
minimal_cost = None
optimize([], operations4)
print(minimal_order, "should be asp,disp, asp2,disp2", cost(minimal_order), "should be 41")

print("optimizing operations5")
minimal_order = []
minimal_cost = None
optimize([], operations5)
print(minimal_order, "should be asp,disp, asp2, asp3, disp2, disp3", cost(minimal_order), "should be 52")


asp4 = Aspiration(Well(4, 3))
disp4 = Dispense(Well(4, 3), asp4)

operations6 = [
  asp,
  disp,
  asp2,
  disp2,
  asp3,
  disp3,
  asp4,
  disp4
]

print("optimizing operations6")
minimal_order = []
minimal_cost = None
optimize([], operations6)
print(minimal_order, "should be asp,disp, asp2,disp2, asp3,disp3", cost(minimal_order), "should be 62")


import random
random.seed(42)

random_operations = []
for i in range(10):
  random_asp = Aspiration(Well(random.randint(1, 8), random.randint(1, 8)))
  random_disp = Dispense(Well(random.randint(1, 8), random.randint(1, 8)), random_asp)
  random_operations.append(random_asp)
  random_operations.append(random_disp)

random.shuffle(random_operations)
print("random operations:", random_operations[:10])
print("random operations cost:", cost(random_operations))
print("optimizing random operations")
minimal_order = []
minimal_cost = None
import time
start = time.time()
optimize([], random_operations)
end = time.time()
print(minimal_order, "has cost", cost(minimal_order))
print("optimization took", end - start, "seconds")
# best: 136 in ~100 (?) seconds




