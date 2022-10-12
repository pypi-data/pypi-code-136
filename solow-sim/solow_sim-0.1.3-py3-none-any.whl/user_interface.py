from solow_library import solow

print('Welcome to the Solow Model Simulator.\n'
      'Before before you can experiment on your own, we will start with an example.\n')

print('We will first simulate an Economy, for 100 years, called "canada" with the following characteristics: \n'
      'A savings rate of 30%\n'
      'A depreciation rate of 5%\n'
      'A population growth rate of 2%\n'
      'A Capital Ratio of 30%\n')

input('Press "Enter" to continue: ')
canada = solow.Economy('canada', 0.3, 0.05, 0.02, 0.3, 100)
print(canada)

print('\nThe program computes the relevant time path for important economic variables such as \n'
      'Capital per person, Population, Output, Interest rate and Wage. Lets print for the first 5 years \n\n')
print(canada.data[0:5])

print('\nWe can also plot the time Paths of such important variables.')
input('Press "Enter" to see the plots: ')
canada.plot_all()

print('\nMore interestingly, we can induce external shocks to our economy. Say for example that \nwe wanted'
      'to understand the effect of a large population change on different economic variables.'
      '\n\nThe program can indeed perform such a task.\n'
      'Lets see what the effect of an overnight reduction in population of 50% looks like at time 50.')

input('\n\nPress "Enter to see the effect of the shock:')
canada.population_shock(0.5, 50)
print('Lets print once again our economic Data:\n\n')
print(canada.data.iloc[45:55, 6:9])

input('\n\nPress "Enter to continue:')

print('\n\nI have printed only some of the variables to show that new columns have been added.\n'
      'When computing the shock, the program adds the time paths of the variables given the population shock.\n'
      'We can see here for example that the population was cut in half, that the amount of capital per \n'
      'person grew by a factor of two and that the wage increased directly after the shock.')

print('\n\nHowever, we can graph these new changes and understand their longterm impact.')
input('Press "enter" to continue: ')
canada.plot_all_shock()

print('\nAs we can see, the long term effects are null. That is, all of the variables\n'
      'converge to the same values with or without the external Shock. However, the short\n'
      'term effect are quite clear. As the amount of Capital per person jumps, the availability of\n'
      'capital reduces the interest rate. As Capital is more abundant relative to labor,\n'
      'wages increase. However, since the amount of Capital per person is unsustainable\n'
      'because total output and savings cannot account for the total capital depreciation,\n'
      'capital per person is bound to fall to its long term level.')
