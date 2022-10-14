from PyQt6.QtWidgets import QFileDialog, QMessageBox
import os
import numpy as np


def saveDataToCSV(parent,data,description):
    fname = QFileDialog.getSaveFileName(parent=parent,caption='Save data',directory=os.path.expanduser("~"),filter="CSV file (*.csv)",initialFilter="CSV file (*.csv)")[0]

    with open(fname, "w") as file:
        file.write(description.replace('\n',';'))
        file.write('\n')
        for dataItem in data:
            file.write(dataItem[0])
            for i in range(np.size(dataItem[1],axis=1)):
                 file.write(';')
            file.write('\n')
            for i in range(np.size(dataItem[1],axis=1)):
                 file.write(f'{i+1}')
                 file.write(';')
            file.write('\n')
            for i in range(np.size(dataItem[1],axis=0)):
                for j in range(np.size(dataItem[1],axis=1)):
                    file.write(f'{dataItem[1][i][j]}')
                    file.write(';')
                file.write('\n')