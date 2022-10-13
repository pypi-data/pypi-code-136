
from ortools.linear_solver import pywraplp
import matplotlib.pyplot as plt
import numpy as np


class Knapsack:

  def __init__(self, dates, items, bin_capacities, numbers, bins_maximum, items_maximum, baseload, fact, n_bins_per_hour, flexibilities):
    """
    This class receives as input some arrays with information about the timeslots and the bins, as well as some global data (baseload, fact and n_bins_per_hour)

    Args:
      dates: array containing the bin in which the user wants to place the timeslot
      items: array containing the timeslot energy for each item of each timeslot
      bin_capacities: array containing the bin capactity of each bin
      numbers: array containing the number of the timeslot of each item of each timeslot
      bins_maximum: array containing the maximum power of the production of each bin
      items_maximum: array containing the maximum power of each item of each timeslot
      baseload: value that represents the value of energy that can be acquired from the grid in the 2nd step
      fact: minutes of each bin (e.g. if bins of 30 minutes, fact = 30)
      n_bins_per_hour: number of bins per hour (parameter of the strategy) to know the quantity of bins in a day (e.g. if bins of 30 minutes, n_bins_per_hour = 2)
      flexibilities: array contanining the flexibility of each item of each timeslot
    """
    self.dates = dates
    self.items = items
    self.numbers = numbers
    self.baseload = baseload
    self.bin_capacities = bin_capacities
    self.bins_maximum = bins_maximum
    self.items_maximum = items_maximum
    self.fact = fact
    self.n_bins_per_hour = n_bins_per_hour
    self.flexibilities = flexibilities


  def show_results(self, objective, title, type):
    """
    Shows graphically the results (curves) of different objective functions, in order to understand their behaviour.

    Args:
      objective: objective function (equation)
      title: title of the graph
      type: "min" or "max", depending if want to identify the min or the max values of the function
    """
    print(title)
    #plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    #plt.ylabel('some numbers')
    #plt.show()

    # Get the angles from 0 to 2 pie (360 degree) in narray object
    #X = [1, 2, 3, 4]
    X = np.arange(1, 200)

    # Using built-in trigonometric function we can directly plot
    # the given cosine wave for the given angles
    #Y1 = [1, 2, 3, 4]
    #Y2 = [1, 2, 3, 4]
    #sY3 = [1, 2, 3, 4]
    #Y4 = [1, 2, 3, 4]


    vec = np.vectorize(objective)

    Y1 = vec(X, 50)
    Y2 = vec(X, 100)
    Y3 = vec(X, 150)
    Y4 = vec(X, 200)


    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(2, 2)

    figure.suptitle(title, fontsize=14)

    axis[0, 0].plot(X, Y1)
    axis[0, 0].set_title("A) C = 50")

    axis[0, 1].plot(X, Y2)
    axis[0, 1].set_title("B) C = 100")

    axis[1, 0].plot(X, Y3)
    axis[1, 0].set_title("C) C = 150")

    axis[1, 1].plot(X, Y4)
    axis[1, 1].set_title("D) C = 200")


    axis[0, 0].set(xlabel="Load", ylabel="F(Load)")
    axis[0, 1].set(xlabel="Load", ylabel="F(Load)")
    axis[1, 0].set(xlabel="Load", ylabel="F(Load)")
    axis[1, 1].set(xlabel="Load", ylabel="F(Load)")

    # type = "min" or "max"
    axis[0, 0].scatter(X[np.where(Y1 == type(Y1))], type(Y1), c='blue')
    axis[0, 1].scatter(X[np.where(Y2 == type(Y2))], type(Y2), c='blue')
    axis[1, 0].scatter(X[np.where(Y3 == type(Y3))], type(Y3), c='blue')
    axis[1, 1].scatter(X[np.where(Y4 == type(Y4))], type(Y4), c='blue')


    plt.show()






  def create_data_model(self):
    """
    Creates the data model for the Multi Knapsack problem, according to the input received in the constructor

    Returns:
      data model (list with different arrays and values)
    """
    data = {}
    #weights = [[48, 30, 42, 70, 20], [36, 36, 48], [42, 42, 11, 60], [24, 30, 30], [42, 36, 36, 10], [98, 70, 80]]
    #weights = [[42], [29], [74, 110], [73, 10]]
    weights = [[42], [29], [74], [110], [73], [10]]
    #values = [[10, 30, 25, 12, 15], [50, 35, 30], [15, 40, 30, 50], [35, 45, 10], [20, 30, 25, 70]]
    # dates = [[3, 4, 5, 6, 7], [1, 2, 3], [4, 5, 6, 7], [12, 13, 14], [20, 21, 22, 23], [1, 2, 3]]
    dates = [[7], [8], [4], [3], [20], [16]]
    data['weights'] = self.items
    #data['values'] = values
    data['dates'] = self.dates
    data['numbers'] = self.numbers
    #data['items'] = list(range(len(weights)))
    data['items'] = list(range(len(self.items)))
    #data['num_items'] = len(weights)
    data['num_items'] = len(self.items)
    num_bins = len(self.bin_capacities)
    #num_bins = 6
    data['bins'] = list(range(num_bins))
    #data['bin_capacities'] = [30, 75, 105, 150, 80, 45]
    data['bin_capacities'] = self.bin_capacities
    #data['bin_capacities'] = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    data['bins_maximum'] = self.bins_maximum
    data['items_maximum'] = self.items_maximum
    data['baseload'] = self.baseload
    data['fact'] = self.fact
    data['n_bins_per_hour'] = self.n_bins_per_hour
    data['flexibilities'] = self.flexibilities
    return data


  def execute_knapsack(self, step):
    """
    Executes the Multi Knapsack problem in order to retrieve the optimal solution.
    1) Creates the solver
    2) Creates the data model (using the function create_data_model)
    3) Defines the variables and matrix
    4) Defines the constraint(s)
    5) Defines the objective function(s)
    6) Solves the problem
    7) Gets the result
    8) Gets some information from the output

    Args:
      step: 1 if refers to the 1st step of the optimization or 2 if refers to the 2nd one

    Returns:
      an array with 3 positions: array with all timeslots [0], array with the placed timeslots [1] and array with the unplaced timeslots [2]
    """

    print("Data Acquisition")

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')


    data = self.create_data_model()


    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}



    for i in data['items']:
      for p in range(len(data['weights'][i])):
      #for w in data['weights'][i]:
        for j in data['bins']:
          x[(i, p, (j+1))] = solver.IntVar(0, 1, 'x_%i_%i_%i' % (i, p, (j+1)))


    # Constraints
    # Each item can be in at most one bin.
    for i in data['items']:
      # for w in data['weights'][i]:
      for p in range(len(data['weights'][i])):
        sum = 0
        for j in data['bins']:
          sum = sum + x[(i, p, (j+1))]
        solver.Add(sum <= 1)




    # The amount packed in each bin cannot exceed its capacity.
    for j in data['bins']:
        weight = 0
        for i in data['items']:
          # for w in data['weights'][i]:
          for p in range(len(data['weights'][i])):
            w = data['weights'][i][p]
            weight = weight + w * x[(i, p, (j+1))] # if item in bin, x[(i, j)] = 1, otherwise x[(i, j)] = 0
        #print(weight)
        #solver.Add(weight <= data['bin_capacities'][j])
        solver.Add(weight <= data['bin_capacities'][j])
      #solver.Add(sum(x[(i, j)] * data['weights'][i] for i in data['items']) <= data['bin_capacities'][j])



    # each bin can have, at most, one timeslot
    ''' 
    for j in data['bins']:
      sum = 0
      for i in data['items']:
        for w in data['weights'][i]:
          sum = sum + x[(i, w, j)]
      solver.Add(sum <= 1)
    '''


    # a bin can't contain more than one item of the same timeslot (each item of a timeslot should be in different bins)
    for j in data['bins']:
      for i in data['items']:
        sum = 0
        # for w in data['weights'][i]:
        for p in range(len(data['weights'][i])):
          sum = sum + x[(i, p, (j+1))]
        solver.Add(sum <= 1)




    for i in data['items']:
      previous_bin = 0
      for p in range(len(data['weights'][i])):
        current_bin = 0
        for j in data['bins']:
            current_bin = current_bin + (j+1) * x[(i, p, (j+1))] # if item in bin, x[(i, j)] = 1, otherwise x[(i, j)] = 0

        if (p > 0):
          solver.Add(current_bin - previous_bin <= 1)
          solver.Add(current_bin - previous_bin >= 0)

        previous_bin = current_bin





    for i in data['items']:
      next_bin = 0
      for p in range(len(data['weights'][i])):
        current_bin = 0
        for j in data['bins']:
          current_bin = current_bin + (j+1) * x[(i, (len(data['weights'][i])-1-p), (j+1))]  # if item in bin, x[(i, j)] = 1, otherwise x[(i, j)] = 0

        if (p > 0):
          solver.Add(next_bin - current_bin <= 1)
          solver.Add(next_bin - current_bin >= 0)

        next_bin = current_bin





    for j in data['bins']:
      max_sum = 0
      max_bin = data['bins_maximum'][j]
      for i in data['items']:
        for p in range(len(data['weights'][i])):
          max_sum = max_sum + data['items_maximum'][i][p] * x[(i, p, (j+1))]

      solver.Add(max_sum <= max_bin)




    for i in data['items']:
      for p in range(len(data['weights'][i])):

        date = data['dates'][i][p]
        sum = 0

        for j in data['bins']:
          sum = sum + ((j+1)-date) * x[(i, p, (j+1))] # if item in bin, x[(i, j)] = 1, otherwise x[(i, j)] = 0

        #solver.Add(sum == 0)
        #solver.Add(sum >= -12*float(data['n_bins_per_hour'])*float(data['flexibilities'][i][p]))
        solver.Add(sum >= -float(data['n_bins_per_hour'])*float(data['flexibilities'][i][p]))
        #solver.Add(sum <= 12*float(data['n_bins_per_hour'])*float(data['flexibilities'][i][p]))
        solver.Add(sum <= float(data['n_bins_per_hour'])*float(data['flexibilities'][i][p]))



    # Objective
    objective = solver.Objective()


    if (step == 1):

      for i in data['items']:
        for p in range(len(data['weights'][i])):
          val = data['weights'][i][p]
          for j in data['bins']:
            bin_capacity = data['bin_capacities'][j]
            objec = bin_capacity / val - bin_capacity - min(0, bin_capacity - val)
            objective.SetCoefficient(x[(i, p, (j+1))], objec)

      objective.SetMinimization()

    elif (step == 2):

      for i in data['items']:
        for p in range(len(data['weights'][i])):
          val = data['weights'][i][p]
          for j in data['bins']:
            bin_capacity = data['bin_capacities'][j]
            objec = val + (bin_capacity-data['baseload'])
            objective.SetCoefficient(x[(i, p, (j+1))], objec)

      objective.SetMaximization()



    '''
    for j in data['bins']:
      total = 0
      bin_capacity = data['bin_capacities'][j]
      for i in data['items']:
        for p in range(len(data['weights'][i])):
          val = data['weights'][i][p]
          sum = sum + val * x[(i, p, (j+1))]

      objec = bin_capacity / sum
      objective.SetMinimization()
    '''


    placed_numbers = [] # Numbers of timeslots placed (to avoid having subitems of the same timeslot - just one subitem per timeslot)
    placed_timeslots = [] # timeslots placed in knapsack
    all_timeslots = [] # all timeslots
    not_placed_timeslots = [] # timeslots that are not placed

    first_item_date = ""
    for i in data['items']:
      for p in range(len(data['weights'][i])):
        w = data['weights'][i][p]
        d = data['dates'][i][p]
        n = data['numbers'][i][p]
        flex = data['flexibilities'][i][p]
        max = data['items_maximum'][i][p]
        if (p == 0):  # First item of the timeslot
          first_item_date = d
        all_timeslots.append(str(n) + "-" + str(p) + "-" + str(w) + "-" + str(d) + "-" + str(len(data['weights'][i])) + "-" + str(first_item_date) + "-" + str(max) + "-" + str(d) + "-" + str(flex))

    print("solver")
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('Total packed value:', objective.Value())
        total_weight = 0
        for j in data['bins']:
            bin_weight = 0
            print('Bin ', (j+1), '\n')
            for i in data['items']:
              for p in range(len(data['weights'][i])):
                w = data['weights'][i][p]
                d = data['dates'][i][p]
                n = data['numbers'][i][p]
                flex = data['flexibilities'][i][p]
                max = data['items_maximum'][i][p]
                if x[(i, p, (j+1))].solution_value() > 0:
                    print('Timeslot', n, 'Item', p , '- weight:', w)
                    bin_weight += w
                    firstItemDate = (j + 1) - p

                    if ((str(n)+"-"+str(p)) not in placed_numbers):
                      placed_numbers.append(str(n)+"-"+str(p))
                      placed_timeslots.append(str(n) + "-" + str(p) + "-" + str(w) + "-" + str((j + 1)) + "-" + str(len(data['weights'][i])) + "-" + str(firstItemDate) + "-" + str(max) + "-" + str(d) + "-" + str(flex))
            print('Packed bin weight: ', bin_weight)
            print('Bin capacity: ', data['bin_capacities'][j])
            print()
            total_weight += bin_weight
        print('Total packed weight: ', total_weight)
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())

    #not_placed_timeslots = [item for item in allTimeslots if item not in placedTimeslots]
    #not_placed_timeslots = allTimeslots[(allTimeslots.split("-")[0]+"-"+allTimeslots.split("-")[1]) not in placedNumbers]
    not_placed_timeslots = []
    for tim in all_timeslots:
      if ((tim.split("-")[0]+"-"+tim.split("-")[1]) not in placed_numbers):
        not_placed_timeslots.append(tim)



    '''
    objective1 = lambda t, bin_capacity: t / bin_capacity
    self.show_results(objective1, "F(L) = L/C ", max);

    objective2 = lambda t, bin_capacity: bin_capacity / t - (0.5 * max(0, t - bin_capacity) + 0.5 * abs(min(0, t - bin_capacity)))
    self.show_results(objective2, "F(L) = C/L - (0.5*max(0,L-C) + 0.5*abs(min(0, L-C)))", max);

    objective3 = lambda t, bin_capacity: bin_capacity / t - (0.2 * max(0, t - bin_capacity) + 0.8 * abs(min(0, t - bin_capacity)))
    self.show_results(objective3, "F(L) = C/L - (0.2*max(0,L-C) + 0.8*abs(min(0, L-C)))", max);

    objective4 = lambda t, bin_capacity: bin_capacity / t - (0.8 * max(0, t - bin_capacity) + 0.2 * abs(min(0, t - bin_capacity)))
    self.show_results(objective4, "F(L) = C/L - (0.8*max(0,L-C) + 0.2*abs(min(0, L-C)))", max);

    objective5 = lambda t, bin_capacity: bin_capacity * (1/t - 1)
    self.show_results(objective5, "F(L) = C/L - C = 1/L * C - C = C*(1/L - 1)", min);

    objective6 = lambda t, bin_capacity: bin_capacity/t - t*(bin_capacity/t)
    self.show_results(objective6, "F(L) = C/L - L*(C/L) = (1-L)*(C/L)", min);

    objective7 = lambda t, bin_capacity: bin_capacity / t * (1 - t) - min(0, bin_capacity - t)
    self.show_results(objective7, "F(L) = C/L - L*C/L - min(0, C-L) = C/L*(1-L) - min(0, C-L) = C/L - C - min(0, C-L)", min);

    objective8 = lambda t, bin_capacity: bin_capacity / t - min(0, bin_capacity - t)
    self.show_results(objective8, "F(L) = C/L - min(0, C-L)", min);

    objective9 = lambda t, bin_capacity: bin_capacity / t - t - min(0, bin_capacity - t)
    self.show_results(objective9, "F(L) = C/L - L - min(0, C-L)", min);
    '''

    return [all_timeslots, placed_timeslots, not_placed_timeslots];

  #print(objective6(100, 100))



    #b = {'a': 20, 'b': 20, 'c': 15, 'd': 10, 'e': 3, 'f': 2}
    #bins = binpacking.to_constant_volume(b, 12)
    #print("===== dict\n", b, "\n", bins)

    #b = list(b.values())
    #bins = binpacking.to_constant_bins(b, 4)
    #print("===== list\n", b, "\n", bins)



