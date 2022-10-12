import seaborn as sns
from sklearn import metrics
import numpy as np
import os
import matplotlib.pyplot as plt


def evaluate(data, y_df):
    np_model = np.array(data['np_model'])
    y = np.array(y_df)
    root_sqr_err = round(np.sqrt(metrics.mean_squared_error(y, np_model)), 2)
    rse = 'Root Mean Square Error: ' + str(root_sqr_err)

    residuals = y - np_model

    sns.histplot(residuals, kde=True).set(title='Histogram of residuals')
    filename = 'hist_satellite' + data['sat'] + '_file' + data['filename']
    plt.savefig(os.path.join(data['save'], filename) + '.png')

    # Confidence interval
    min_error = round(np.percentile(residuals, 2.5), 2)
    max_error = round(np.percentile(residuals, 97.5), 2)

    interval = '95% confidence interval in Degrees: [' + str(min_error) + ', ' + str(max_error) + ']'

    data['evaluation'] = [rse, interval]

    return data
