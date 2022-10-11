# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['classically']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'networkx>=2.6.3,<3.0.0',
 'numpy>=1.22.2,<2.0.0',
 'scikit-learn>=1.1.2,<2.0.0',
 'scipy>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'classically',
    'version': '1.0.0',
    'description': 'Classifier Comparison and Evaluation Tools',
    'long_description': '# CLASSIC\nClassifier Comparison and Evaluation Tools\n\nA python package for the analysis of classification performance.\n\n## Applications\n\n### Critical Difference Diagram\n\nA main application is the comparison of categorized paired metric data, e.g. accuracy results of\ndifferent classification methods in machine learning.\nTherefore __Classic__ implements the *critical difference diagram* (described in [[1]](#1)).\n\n<a id="2"><u>Example</u></a>\n\nImagine that we have five different classification methods tested on 14 different datasets.\nEvery classifiers returns an accuracy result on each test set in the corresponding dataset.\nWe collect the results in a table like this:\n\nClassifier |      |      |      |      |      |      |      |      |      |      |      |      |      |      |\n-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|\nA          | 0.60 | 0.81 | 0.62 | 0.19 | 0.93 | 0.54 | 0.53 | 0.41 | 0.21 | 0.97 | 0.32 | 0.82 | 0.38 | 0.75 |\nB          | 0.33 | 0.68 | 0.43 | 0.23 | 0.90 | 0.43 | 0.32 | 0.20 | 0.22 | 0.86 | 0.21 | 0.82 | 0.41 | 0.73 |\nC          | 0.25 | 0.64 | 0.40 | 0.10 | 0.85 | 0.39 | 0.31 | 0.19 | 0.18 | 0.90 | 0.23 | 0.78 | 0.43 | 0.71 |\nD          | 0.64 | 0.84 | 0.60 | 0.26 | 0.95 | 0.60 | 0.36 | 0.37 | 0.19 | 0.95 | 0.44 | 0.84 | 0.41 | 0.84 |\nE          | 0.37 | 0.68 | 0.47 | 0.18 | 0.88 | 0.37 | 0.27 | 0.25 | 0.24 | 0.79 | 0.25 | 0.83 | 0.36 | 0.64 |\n\nWe load this table in a `numpy array` of shape `(5, 14)` and call the function\n`classic.critical_difference_diagram`. The resulting plot can be seen below.\n\n![critical difference diagram](example/cdd_example.png)\n\nMarkings on this number line represent the average ranks of one classifier based on his accuracy\nover all datasets. The lowest rank corresponds to the highest accuracy. Classifiers are connected\nby a horizontal line if they do not have a significant difference. This significance is based on\npost-hoc Wilcoxon signed rank tests for each pair of classifiers.\n\nTherefore, it seems like classifier D is the best choice for the overall classification task.\nIt works best on the 14 chosen datasets, altough it\'s not the best classfier for every single\ndataset on its own. But we can also see, that there is no significant (`alpha=0.05`) difference in\nthe accuracy results of classifier D and A. If D would be much more computationally expensive than\nA, then we should consider choosing A as the better classifier.\n\n### Scatter Matrix\n\nFor an in-depth comparison of the classifiers on single datasets a special type of scatter matrix\nthat is designed to compare multiple categories of data can be found in __Classic__.\n\n<u>Example</u>\n\nFor a more elaborate decision in the [example above](#2) we could directly compare the best three\nclassifiers A, B and D using the function `classic.scatter_comparison.`\n\n![scatter comparison](example/scatter_example.png)\n\nPoints above the diagonal line represent datasets that are better classified by the method in the\nupper left corner. A horizontal and vertical line indicates the mean accuracy of the corresponding\nclassifier. A solid line marks the higher mean.\nA choice can now be easily made for the comparison of classifier A and B as well as B and D.\nWe also see that D is better than A in mean accuracy but that A has a big advantage on one dataset\nthat is well beyond the diagonal line for five percent difference.\nThe datasets could now be further analyzed by, for example, looking at the number of training and\ntest instances. An option for setting the opacity value of points in the scatterplots accordingly\nis available.\n\n### Feature Score\n\nEvaluating the importance of features in data can be very helpful in reducing the dimensionality of\nthe feature space. While principal component analysis transforms original features into new ones,\nit can also be used to creating a ranking of those features. __Classic__ is able to compute the\nfeature score for a given dataset.\n\n<u>Example</u>\n\nWe can analyze the importance of the four features in the well-known IRIS dataset by using the\nmethod `classic.plot_feature_score`.\n\n<p align="center"> <img width=512 src="example/score_example.png"> </align>\n\nThe plot shows the normalized feature score. The \'most important\' feature based on that score is\n\'petal length (cm)\'. All other features then have a relatively low score, e.g. sepal length\'s score\nis about 80% lower. The red markings show the accuracy results of a ridge classifier where only the\nfirst `n` features (in descending score order) are used (`n` gets incremented with each step on the\nx-axis).\n\n## References\n\n<a id="1">[1]</a>\nDemšar, Janez (2006).\n"Statistical comparisons of classifiers over multiple data sets."\nThe Journal of Machine learning research 7, 1-30.\n',
    'author': 'alienkrieg',
    'author_email': 'alienkrieg@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/alienkrieg/classic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
