import time
from kiwrious.service import KiwriousService
import matplotlib
from matplotlib import animation
from matplotlib import pyplot as plt


# This is a program in which you can plot live data from any of the sensors. Just plug in your sensor and run the program and a plot will appear.
# It also works with multiple sensors at the same time!
# NOTE: You must have matplotlib installed, to do this type in the commmand 'pip install matplotlib' into a terminal


service = KiwriousService()
service.start_service()
timelist = list()
matrix = list()

def animated_plot_demo():
        time.sleep(1)
        con_sensors = service.get_connected_sensors()

        no_samples = 100
        sample_rate = 0.1  # seconds per reading
        animated_plot(con_sensors, no_samples, sample_rate, True)
        service.stop_service()

def animated_plot(connected_sensors, no_samples=10, sample_rate=1, display_results=False):
            """Animated plot which saves the data when the plot is closed"""
            time.sleep(1)
            init_data_matrix(connected_sensors)
            start = time.time()

            fargs1 = connected_sensors, no_samples, sample_rate, start

            ani = animation.FuncAnimation(plt.gcf(), func=draw_animated_plot, fargs=fargs1, interval=0)

            plt.show()

def draw_animated_plot(i, connected_sensors, no_samples, sample_rate, start_time):
        try:
            if len(plt.get_fignums()) == 0:
                service.stop_service(True)
            plt.cla()

            begin = time.time()
            add_to_matrix(connected_sensors)
            fin = time.time()
            timelist.append(fin - start_time)

            for j in range(len(connected_sensors) * 2):
                plt.plot(timelist, matrix[j][2:], label=matrix[j][0])
                plt.legend()
                plt.xlabel = "Time"

            time.sleep(sample_rate - (fin - begin))
        except:
            pass

def init_data_matrix(connected_sensors):
        for j in connected_sensors:
            if j.sensor_type == 1:
                matrix.append(["Lux, Lux ", 1])
                matrix.append(["UV Index, λ", 1])
            elif j.sensor_type == 4:
                matrix.append(["Resistance, Ω", 4])
                matrix.append(["Conductance, G", 4])
            elif j.sensor_type == 6:
                matrix.append(["V0C, V0C", 6])
                matrix.append(["C02, ppb", 6])
            elif j.sensor_type == 7:
                matrix.append(["Ambient Temperature, °C", 7])
                matrix.append(["Humidity, %", 7])
            elif j.sensor_type == 9:
                matrix.append(["IR Temperature, °C", 9])
                matrix.append(["Ambient Temperature, °C", 9])
            elif j.sensor_type == 10:
                matrix.append(["BPM, bpm", 10])
                matrix.append(["BPM, bpm", 10])
        return connected_sensors

def add_to_matrix(connected_sensors):
        n = 0

        for k in connected_sensors:
            matrix[n].append([k.sensor_data[0].data_value][0])
            matrix[n + 1].append([k.sensor_data[1].data_value][0])

            n += 2

animated_plot_demo()