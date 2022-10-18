def return_function(node):
    if node["data"]["value"] == "Logistic Regression":
        return logistic_regression(node['data']['parameters'])
    elif node["data"]["value"] == "SVM (SVC)":
        return svm_svc(node['data']['parameters'])
    elif node["data"]["value"] == "Gaussian Naive Bayes":
        return gaussian_naive_bayes(node['data']['parameters'])
    elif node["data"]["value"] == "Multinomial Naive Bayes":
        return multinomial_naive_bayes(node['data']['parameters'])
    elif node["data"]["value"] == "Stochastic Gradient Descent Classifier":
        return st_gradient_descent(node['data']['parameters'])
    elif node["data"]["value"] == "KNN":
        return knn(node['data']['parameters'])
    elif node["data"]["value"] == "Decision Tree Classifier":
        return decision_tree(node['data']['parameters'])
    elif node["data"]["value"] == "Random Forest Classifier":
        return random_forest(node['data']['parameters'])
    elif node["data"]["value"] == "Gradient Boosting Classifier":
        return gradient_boosting(node['data']['parameters'])
    elif node["data"]["value"] == "LGBM Classifier":
        return lgbm(node['data']['parameters'])
    elif node["data"]["value"] == "XGBoost Classifier":
        return xgboost(node['data']['parameters'])


def logistic_regression(params):
    parameters = {
        "penalty": params["penalty"],
        "fit_intercept": params["fit_intercept"],
        "random_state": params["random_state"],
        "solver": params["solver"],
        "max_iter": params["max_iter"],
        "multi_class": params["multi_class"],
        "tol": params["tol"],
    }
    return f"model = huble.sklearn.logistic_regression(parameters={parameters})"


def svm_svc(params):
    parameters = {
        "C" : params['C'], 
        "kernel" : params['kernel'],
        "probability" : params['probability'],
        "random_state": params["random_state"],
        "max_iter": params["max_iter"],
        "decision_function_shape": params["decision_function_shape"],
        "tol": params["tol"],
    }
    return f"model = huble.sklearn.svm_svc(parameters={parameters})"

def gaussian_naive_bayes(params):
    parameters = {
        "priors" : params['priors'],
        "var_smoothing" : params['var_smoothing'],
    }
    return f"model = huble.sklearn.gaussian_naive_bayes(parameters={parameters})"

def multinomial_naive_bayes(params):
    parameters = {
        "class_prior" : params['class_prior'],
        "alpha" : params['alpha'],
        "fit_prior" : params['fit_prior'],
    }
    return f"model = huble.sklearn.multinomial_naive_bayes(parameters={parameters})"

def st_gradient_descent(params):
    parameters = {
        "loss" : params['loss'], 
        "penalty": params["penalty"],
        "fit_intercept": params["fit_intercept"],
        "alpha" : params['alpha'],
        "max_iter": params["max_iter"],
        "tol": params["tol"],
        "random_state": params["random_state"],
        "shuffle" : params['shuffle'],
        "learning_rate" : params['learning_rate'],
        "initial_learning_rate" : params['initial_learning_rate'],
        "early_stopping" : params['early_stopping'],
        "validation_fraction" : params['validation_fraction'],
    }
    return f"model = huble.sklearn.st_gradient_descent(parameters={parameters})"


def knn(params):
    parameters = {
        "n_neighbors" : params['n_neighbors'], 
        "weights" : params['weights'], 
        "algorithm" : params['algorithm'],
        "metric" : params['metric'],
    }
    return f"model = huble.sklearn.knn(parameters={parameters})"


def decision_tree(params):
    parameters = {
        "criterion" : params['criterion'],
        "splitter" : params['splitter'],
        "max_depth" : params['max_depth'],
        "max_leaf_nodes" : params['max_leaf_nodes'],
        "random_state" : params['random_state'],
    }
    return f"model = huble.sklearn.decision_tree(parameters={parameters})"


def random_forest(params):
    parameters = {
        "criterion" : params['criterion'],
        "n_estimators" : params['n_estimators'],
        "max_depth" : params['max_depth'],
        "max_leaf_nodes" : params['max_leaf_nodes'],
        "random_state" : params['random_state'],
    }
    return f"model = huble.sklearn.random_forest(parameters={parameters})"


def gradient_boosting(params):
    parameters = {
        "criterion" : params['criterion'],
        "n_estimators" : params['n_estimators'],
        "max_depth" : params['max_depth'],
        "max_leaf_nodes" : params['max_leaf_nodes'],
        "random_state" : params['random_state'],
        "loss" : params['loss'],
        "learning_rate" : params['learning_rate'],
        "subsample" : params['subsample'],
        "tol" : params['tol'],
    }
    return f"model = huble.sklearn.gradient_boosting(parameters={parameters})"


def lgbm(params):
    parameters = {
        "boosting_type" : params['boosting_type'],
        "num_leaves" : params['num_leaves'],
        "n_estimators" : params['n_estimators'],
        "max_depth" : params['max_depth'],
        "random_state" : params['random_state'],     
        "learning_rate" : params['learning_rate'],
    }
    return f"model = huble.sklearn.lgbm(parameters={parameters})"


def xgboost(params):
    parameters = {
        "n_estimators" : params['n_estimators'],
        "max_depth" : params['max_depth'],
        "random_state" : params['random_state'],     
        "learning_rate" : params['learning_rate'],
    }
    return f"model = huble.sklearn.xgboost(parameters={parameters})"


