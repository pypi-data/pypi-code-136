import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import doctest


class Economy:
    """
    Represents a certain area's economy

    Instance Attributes: name (str), savings (float), depreciation (float),
                         population_growth (float), capital_ratio (float), time (int)
    """

    def __init__(self, name="Canada", savings=0.3, depreciation=0.03,
                 population_growth=0.02, capital_ratio=0.3, time=2):
        self.name = name
        self.savings = savings
        self.depreciation = depreciation
        self.population_growth = population_growth
        self.capital_ratio = capital_ratio
        self.time = time
        self.data = pd.DataFrame({'Time':[t for t in range(0,time)]})

        self.capital_capita()
        self.output_capita()
        self.interest_rate()
        self.wage()


    def __str__(self):
        """
        (Economy) -> str

        >>> canada = Economy()
        >>> print(canada)
        Canada
        Savings: 0.3
        Depreciation: 0.03
        Population Growth: 0.02
        Capital Ratio: 0.3
        """
        info = self.name + "\nSavings: " + str(self.savings) + "\nDepreciation: " + str(self.depreciation) \
               + "\nPopulation Growth: " + str(self.population_growth) + "\nCapital Ratio: " + str(self.capital_ratio)
        return info

    def capital_capita(self):
        """
        (Economy) -> None

        >>> canada = Economy()
        >>> canada.capital_capita()
        >>> print(canada.data['Capital'].tolist())
        [1.25, 1.5082703799973565]
        """
        t, s, d, n, a = self.time, self.savings, self.depreciation, self.population_growth, self.capital_ratio
        self.data['Capital'] = Economy.get_capital_capita(t, s, d, n, a)[1]
        self.data['Population'] = [(1+n)**i for i in self.data['Time'].tolist()]

    def output_capita(self):
        """
        (Economy) -> None

        This method takes as input and Economy object and
        outputs a list representing output per capita for each time t.

        >>> canada = Economy()
        >>> canada.output_capita()
        >>> print(canada.data['Output'].tolist())
        [1.069234599991188, 1.131211367506459]
        >>> usa = Economy(capital_ratio=0.4)
        >>> usa.capital_capita()
        >>> usa.output_capita()
        >>> print(usa.data['Output'].tolist())
        [1.0933620739432781, 1.1809278496201596]
        """
        if 'Capital' not in self.data.columns:
            self.capital_capita()

        a = self.capital_ratio
        output = [(k_i)**a for k_i in self.data['Capital'].tolist()]
        self.data['Output'] = output


    def output_capita_growth(self):
        """
        (float, float, float, float, float) -> None

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> canada = Economy()
        >>> canada.output_capita_growth()
        >>> print(canada.data['Output'].tolist())
        [1.069234599991188, 1.131211367506459]
        >>> usa = Economy(capital_ratio=0.4)
        >>> usa.capital_capita()
        >>> usa.output_capita_growth()
        >>> print(usa.data['Output'].tolist())
        [1.0933620739432781, 1.1809278496201596]
        """
        if 'Output' not in self.data.columns:
            self.output_capita()

        # Add 1 at beginning otherwise growth list length is smaller that others lists in dataframe
        output = [1] + self.data['Output'].tolist()
        growth = np.exp(np.diff(np.log(output))) - 1
        growth_list = growth.tolist()
        self.data['Output Growth'] = growth_list

    def capital_capita_growth(self, column='Capital'):
        """
        The column is capital by default, but this function
        is also used when computing external shocks such that, we might
        use other columns from external shock data. The second argument
        is really mostly for internal use. The user shouldn't have to worry about it.
        """
        if 'Capital' not in self.data.columns:
            self.capital_capita()

        capital = [1] + self.data[column].tolist()
        growth = np.exp(np.diff(np.log(capital))) - 1
        growth_list = growth.tolist()
        self.data[column + 'Growth'] = growth_list
        return

    def kapital_plot(self, column='Capital'):
        """
        This Function makes a plot with time as the x value and capital as
        the y value. If the Capital Path had not been computed before, compute it,
        then show the plot.
        """
        if 'Capital' not in self.data.columns:
            self.capital_capita()

        plt.plot(self.data['Time'].tolist(), self.data[column].tolist())
        plt.show()

    def kapital_g_plot(self, column='Capital'):
        if 'Capital Growth' not in self.data.columns:
            self.capital_capita_growth()
        plt.plot(self.data['Time'].tolist(), self.data[column + 'Growth'].tolist())
        plt.show()

    def wage(self, column='Wage'):
        """
        (int, float, float, float, float) -> None

        This method takes as input floats describing economic variables and
        outputs a list representing wages for every t.

        >>> canada = Economy()
        >>> canada.wage()
        >>> print(canada.data['Wage'].tolist())
        [0.7484642199938316, 0.7918479572545213]
        >>> usa = Economy(capital_ratio=0.4)
        >>> usa.wage()
        >>> print(usa.data['Wage'].tolist())
        [0.6560172443659669, 0.7085567097720957]
        """
        t, s, d, n, a = self.time, self.savings, self.depreciation, self.population_growth, self.capital_ratio
        wage = Economy.get_wage(t, s, d, n, a)
        self.data[column] = wage


    def interest_rate(self, column = 'Interest'):
        """
        (int, float, float, float, float) -> list

        This method takes as input floats describing economic variables and
        outputs a list containing the interest rate for each time t.

        >>> canada = Economy()
        >>> canada.interest_rate()
        >>> print(canada.data['Interest'].tolist())
        [0.2566163039978851, 0.22500170708950246]
        >>> usa = Economy(savings=0.4)
        >>> usa.interest_rate()
        >>> print(usa.data['Interest'].tolist())
        [0.2431574704343747, 0.20521963923411404]
        """
        t, s, d, n, a = self.time, self.savings, self.depreciation, self.population_growth, self.capital_ratio

        interest = Economy.get_interest_rate(t, s, d, n, a)
        self.data[column] = interest


    def population_shock(self, shock_size, impact_time):
        """
        (Economy,float, int) -> list

        This method takes as input floats describing the intensity of the population shock
        and an integer representing the timing of the impact. If shock_size = 0.5, then 50% of
        the population is wiped out. The function returns a list of capital path of each time t.
        At the time of the impact, capital does not grow. At impact t+1, capital has grown by
        the standard solow model differential equation.
        """
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio

        #Build New Capital Path with Population Shock
        k_list_preshock = self.data['Capital'].tolist()
        capital_at_shock = k_list_preshock[impact_time]
        time_left = len(k_list_preshock) - impact_time
        k_list_postshock = Economy.get_capital_capita(time_left, s, d, n, a, k=capital_at_shock / shock_size)[1]
        time_list = []
        for i in range(0,len(k_list_preshock)):
            time_list.append(i)

        new_k_list = k_list_preshock[0:impact_time] + [capital_at_shock / shock_size] + k_list_postshock[0:-1]
        self.data['Capital - Pop.Shock'] = new_k_list

        #Build New Population path with population Shock
        pop_list_preshock = self.data['Population'].tolist()
        pop_at_shock = pop_list_preshock[impact_time]

        #Calculate population given the new Capital Path
        pop_list_postshock = [(pop_at_shock * shock_size)*(1+n)**i for i in range(0, time_left)]
        new_pop_list = pop_list_preshock[0:impact_time] + [pop_at_shock * shock_size] + pop_list_postshock[0:-1]
        self.data['Population - Pop.Shock'] = new_pop_list

        #Repeat
        #Build New Wage path with population Shock
        wage_list_preshock = self.data['Wage'].tolist()
        wage_at_shock = wage_list_preshock[impact_time]
        wage_list_postshock = [(1 - a) * (k ** a) for k in self.data['Capital - Pop.Shock'].tolist()]
        new_wage_list = wage_list_preshock[0:impact_time] + [wage_at_shock] + wage_list_postshock[impact_time:-1]
        self.data['Wage - Pop.Shock'] = new_wage_list

        #Repeat
        #Build New Interest rate path with population Shock
        interest_list_preshock = self.data['Interest'].tolist()
        interest_at_shock = interest_list_preshock[impact_time]
        interest_list_postshock = [a * k ** (a - 1) for k in self.data['Capital - Pop.Shock']]
        new_interest_list = interest_list_preshock[0:impact_time] + [interest_at_shock] + interest_list_postshock[impact_time:-1]
        self.data['Interest - Pop.Shock'] = new_interest_list

        #Build New Output Path with population shock K^(a) = Y
        #Plotting
        #plt.plot(time_list, new_wage_list)
        #plt.show()

    def plot_all_shock(self):
        fig, axs = plt.subplots(2, 2)
        axs[0, 0].plot(self.data['Time'], self.data['Capital - Pop.Shock'].tolist())
        axs[0, 0].set_title('Capital Per Capita')
        axs[0, 1].plot(self.data['Time'], self.data['Wage - Pop.Shock'].tolist())
        axs[0, 1].set_title('Wage')
        axs[1, 0].plot(self.data['Time'], self.data['Interest - Pop.Shock'].tolist())
        axs[1, 0].set_title('Interest Rate')
        axs[1, 1].plot(self.data['Time'], self.data['Population - Pop.Shock'].tolist())
        axs[1, 1].set_title('Population')
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.3, hspace=0.5)
        plt.show()
    def plot_all(self):
        s = self.savings
        d = self.depreciation
        n = self.population_growth
        a = self.capital_ratio
        t = self.time
        return Economy.get_plot_all(t, s, n, d, a)

    @staticmethod
    def get_kapital_dot(k, s, d, n, a):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> print(round(Economy.get_kapital_dot(1, 0.3, 0.03, 0.02, 0.3), 2))
        0.25
        >>> print(round(Economy.get_kapital_dot(2, 0.3, 0.03, 0.02, 0.3), 2))
        0.27
        """
        # Definition of ODE
        return s * (k ** a) - (n + d) * k

    # Solution to Diff equation
    @staticmethod
    def get_capital_capita(t, s, d, n, a, k=1):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> result = Economy.get_capital_capita(2, 0.3, 0.03, 0.02, 0.3)
        >>> result[0] == result[1][-1]
        True
        >>> print(result[1])
        [1.25, 1.5082703799973565]
        >>> print(result[2])
        [0.25, 0.20661630399788514]
        >>> print(result[3])
        [1, 2]
        """
        year = []
        capital_list = []
        capital_g_list = []
        # Initialize changing values
        delta_t = 1
        current_year = 0
        for time in np.arange(current_year, t, delta_t):
            capital_g_list.append(Economy.get_kapital_dot(k, s, d, n, a) / k)
            k += Economy.get_kapital_dot(k, s, d, n, a)  # * delta_t

            current_year += delta_t
            year.append(current_year)
            capital_list.append(k)

        return k, capital_list, capital_g_list, year

    @staticmethod
    def get_output_capita(t, s, d, n, a):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> print(Economy.get_output_capita(2, 0.3, 0.03, 0.02, 0.3))
        [1.069234599991188, 1.131211367506459]
        >>> print(Economy.get_output_capita(2, 0.4, 0.03, 0.02, 0.3))
        [1.0942086169546863, 1.1767180878835704]
        """
        capital_list = Economy.get_capital_capita(t, s, d, n, a)[1]
        output_list = []
        for k in capital_list:
            output_list.append(k ** a)

        return output_list

    @staticmethod
    def get_output_capita_growth(t, s, d, n, a):
        """
        (float, float, float, float, float) -> float

        This method takes as input floats describing economic variables and
        inputs the change in Capital from time t to t+1.

        >>> print(Economy.get_output_capita_growth(2, 0.3, 0.03, 0.02, 0.3))
        [0.05478796385496634, 0.05478796385496634]
        >>> print(Economy.get_output_capita_growth(2, 0.4, 0.03, 0.02, 0.3))
        [0.0701182991733258, 0.0701182991733258]
        """
        output_list = Economy.get_output_capita(t, s, d, n, a)
        growth_list = []
        for i in range(1, len(output_list)):
            growth = (output_list[i] - output_list[i - 1]) / output_list[i]
            growth_list.append(growth)
        growth_list.append(growth_list[-1])
        return growth_list

    @staticmethod
    def get_kapital_plot(t, s, n, d, a):
        plt.plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[1])
        plt.show()

    @staticmethod
    def get_kapital_g_plot(t, s, n, d, a):
        plt.plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[2])
        plt.show()

    @staticmethod
    def get_wage(t, s, d, n, a, pop = 1):
        """
        (int, float, float, float, float) -> list

        This method takes as input floats describing economic variables and
        outputs a list representing wages for every t.

        >>> print(Economy.get_wage(2, 0.3, 0.03, 0.02, 0.3))
        [0.7484642199938316, 0.7918479572545213]
        >>> print(Economy.get_wage(2, 0.4, 0.03, 0.02, 0.3))
        [0.7659460318682804, 0.8237026615184992]
        """
        # Use Cobb-Douglas Function
        capital_list = Economy.get_capital_capita(t, s, d, n, a)[1]
        wage_list = [(1 - a) * (k ** a) for k in capital_list]

        return wage_list

    @staticmethod
    def get_interest_rate(t, s, d, n, a, pop=1):
        """
        (int, float, float, float, float) -> list

        This method takes as input floats describing economic variables and
        outputs a list containin the interest rate for each time t.

        >>> print(Economy.get_interest_rate(2, 0.3, 0.03, 0.02, 0.3))
        [0.2566163039978851, 0.22500170708950246]
        >>> print(Economy.get_interest_rate(2, 0.4, 0.03, 0.02, 0.3))
        [0.2431574704343747, 0.20521963923411404]
        """
        # Use Cobb-Douglas Function
        capital_list = Economy.get_capital_capita(t, s, d, n, a)[1]
        get_interest_rate_list = [a * k ** (a - 1) for k in capital_list]

        return get_interest_rate_list

    @staticmethod
    def get_plot_all(t, s, n, d, a):
        fig, axs = plt.subplots(3, 2)
        axs[0, 0].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[1])
        axs[0, 0].set_title('Capital Per Capita')
        axs[0, 1].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_capital_capita(t, s, d, n, a)[2])
        axs[0, 1].set_title('Capital Growth')
        axs[1, 0].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_output_capita(t, s, d, n, a))
        axs[1, 0].set_title('Output per Capita')
        axs[1, 1].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_output_capita_growth(t, s, d, n, a))
        axs[1, 1].set_title('Output Per Capita Growth')
        axs[2, 1].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_interest_rate(t, s, d, n, a))
        axs[2, 1].set_title('Interest Rate')
        axs[2, 0].plot(Economy.get_capital_capita(t, s, d, n, a)[3], Economy.get_wage(t, s, d, n, a))
        axs[2, 0].set_title('Wage')
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.3, hspace=0.5)
        plt.show()


if __name__ == "__main__":
    """
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    canada = Economy(time=100)
    canada.capital_capita()
    canada.output_capita()
    canada.capital_capita_growth()
    canada.output_capita_growth()
    canada.population_shock(0.5, 50)
    print(canada)
    print(canada.data)
    doctest.testmod()
    """