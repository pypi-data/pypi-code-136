"""
database_path = 'C:\\Users\\usuario\\Desktop\\Practicas\\Practica_Lidar_despolarizacion\\data'
date = '20190711'
files_list = [database_path + '\\' + date + '\\' + file for file in os.listdir(database_path + '\\' + date)]
date += 'T'

plot_RCS_quicklook(files_list)
plot_volumdepol_quicklook(files_list)

ini_time = date + '01:00:00'
end_time = date + '23:00:00'
y_min = 0 #Sets the bottom value of the vertical axis (altitude) in meters asl
y_max = 16000 #Sets the top value of the vertical axix (altitude) in meters asl
RCS_min = 0 #Sets the minimum value of the RCS plot
RCS_max = 2e6 #Sets the maximum value of the RCS plot
d_min = 0 #Sets the minimum value of the depolarization plot
d_max = 0.3 #Sets the maximum value of the depolarization plot
average_profiles(files_list, ini_time, end_time, y_min, y_max, RCS_min, RCS_max, d_min, d_max)

h_ref = 7000
lr = 30
klett_window = 1000
ini_time = date + '06:00:00'
end_time = date + '22:00:00'
c_min = 0 #Sets the minimum value of the color axis.
c_max = 3.5 #Sets the maximum value of the color axis. As a first approach it is recommended to use the default value
plot_backs_quicklook(files_list, h_ref, lr, klett_window, y_min, y_max, ini_time, end_time, c_min, c_max)

ini_time = date + '07:00:00'
end_time = date + '22:00:00'
c_min = 0 #Sets the minimum value of the color axis.
c_max = 10 #Sets the maximum value of the color axis. As a first approach it is recommended to use the default value
plot_backsR_quicklook(files_list, h_ref, lr, klett_window, y_min, y_max, ini_time, end_time, c_min, c_max)

R_limit = 1.1
ini_time = date + '07:00:00'
end_time = date + '22:00:00'
c_min = 0 #Sets the minimum value of the color axis.
c_max = 0.5 #Sets the maximum value of the color axis. As a first approach it is recommended to use the default value
plot_partdepol_quicklook(files_list, h_ref, lr, klett_window, R_limit, y_min, y_max, ini_time, end_time, c_min, c_max)

ini_time = date + '01:00:00'
end_time = date + '16:00:00'
beta_min = 0 #Sets the minimum value of the backscatter plot
beta_max = 3.5 #Sets the maximum value of the backscatter plot
R_min = 0 #Sets the minimum value of the backscatter ratio plot
R_max = 6 #Sets the maximum value of the backscatter ratio plot
d_min = 0 #Sets the minimum value of the depolarization ratio plot
d_max = 0.5 #Sets the maximum value of the depolarization ratio plot
plot_relevant_variables(files_list, ini_time, end_time, h_ref, lr, klett_window, R_limit, y_min, y_max, beta_min, beta_max,
                        R_min, R_max, d_min, d_max)
"""
