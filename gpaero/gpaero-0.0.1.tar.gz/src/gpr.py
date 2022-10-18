"""
Makes aerodynamic maps from CFD data.

TODO list:
+ Should we return values (not arrays) when single output?
+ Use generic 'index' instead of 'refinement_level'?
+ Is there any reason to consider parameters (i.e., wingspan) separately from
  xvars (i.e., Mach)?
  We could regress models for x and p simultaneously (so effectively, treat
  everything currently considered as in 'x').
  It would be possible to regress a model for all flight states and parameters
  simultaneously so that we don't need to train models for each dyi/dpi.
  However, training this larger model will take longer anyway, and we aren't
  (likely) computationally constrained by the GPR -- running the CFD will take
  much longer.
+ Handle loading errors when model doesn't match user specified model in inputs?
+ Number of noise parameters for gradient kernels
+ Implement proper job files w/ saving and loading!
+ Add manual normalization code to aerodecks.
+ Variational models?
+ Current approach treats all aero coeffs separately (even though they have
  known relationships) -- is this appropriate?
  Alternative is to predict pressure coefficient then use some vector operations
  to recover CD, CL, MZ, etc.
+ Currently using rank=1 Hadamard kernel always (scaling only) -- change?
+ Unit handling for plotting (integrate with data files)
"""

import itertools
import gpytorch
import math
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import re
import torch

class MultitaskGPModel(gpytorch.models.ExactGP):
    """
    Inputs:
      n_tasks:  number of correlated outputs to predicted (for CFD, this is the
        number of different mesh refinement levels)
      n_x:      number of input sampling dimensions (for CFD with Mach-alpha, nx=2)
    """
    # Note: train_x in __init__ def is really tuple (train_x, train_i); has to
    # be like this for gpytorch.
    def __init__(self, n_tasks, n_x, train_x, train_y, likelihood):
        super(MultitaskGPModel, self).__init__(train_x, train_y, likelihood)
        self.mean_module = gpytorch.means.ConstantMean()
        self.covar_module = gpytorch.kernels.RBFKernel(ard_num_dims=n_x)
        self.task_covar_module = gpytorch.kernels.IndexKernel(num_tasks=n_tasks,
                rank=1)
        self.covar_x = None
        self.covar_i = None
        self.covar   = None
    def forward(self, x, i):
        mean_x = self.mean_module(x)
        self.covar_x = self.covar_module(x) # Get input-input covariance
        self.covar_i = self.task_covar_module(i) # Get task-task covariance
        self.covar = self.covar_x.mul(self.covar_i) # Multiply together
        return gpytorch.distributions.MultivariateNormal(mean_x, self.covar)

class HadamardGradGPModel(gpytorch.models.ExactGP):
    """ Multifidelity gradient kernel. """
    # Note: train_x in __init__ def is really tuple (train_x, train_i); has to
    # be like this for gpytorch.
    def __init__(self, n_tasks, n_x, train_x, train_y, likelihood):
        super(HadamardGradGPModel, self).__init__(train_x, train_y, likelihood)
        self.mean_module = gpytorch.means.ConstantMeanGrad()
        self.covar_module = gpytorch.kernels.RBFKernelGrad(ard_num_dims=n_x)
        self.task_covar_module = gpytorch.kernels.IndexKernel(num_tasks=n_tasks, rank=1)
        self.covar_x = None
        self.covar_i = None
        self.covar   = None
    def forward(self, x, i):
        n, d = x.shape[-2:] # n: input dim, d: gradient dim
        mean_x = self.mean_module(x)
        self.covar_x = self.covar_module(x) # input-input covariance
        self.covar_i = self.task_covar_module(i) # task-task covariance
        self.covar_i_tiled = self.covar_i.repeat(d+1, d+1)
        # Apply perfect shuffle permutation so ordering matches covar_x (see
        # rbf_kern_grad.py source code for details)
        pi = torch.arange(n*(d+1)).view(d+1,n).t().reshape((n*(d+1)))
        self.covar_i_tiled = self.covar_i_tiled[pi, :][:, pi]
        self.covar = self.covar_x.mul(self.covar_i_tiled) # multiply elementwise
        return gpytorch.distributions.MultitaskMultivariateNormal(mean_x, self.covar)

class GradGPModel(gpytorch.models.ExactGP):
    """ Gradients only. """
    def __init__(self, n_x, train_x, train_y, likelihood):
        super(GradGPModel, self).__init__(train_x, train_y, likelihood)
        self.mean_module = gpytorch.means.ConstantMeanGrad()
        self.base_kernel = gpytorch.kernels.RBFKernelGrad(ard_num_dims=n_x)
        # Explicitly use ScaleKernel here (IndexKernel includes one -- see above)
        self.covar_module = gpytorch.kernels.ScaleKernel(self.base_kernel)
    def forward(self, x):
        mean_x = self.mean_module(x)
        covar_x = self.covar_module(x)
        return gpytorch.distributions.MultitaskMultivariateNormal(mean_x, covar_x)

class GprModel:
    def __init__(self, gpr_ops={}):
        """
        Multifidelity GPR model to predict 'outvars' from inpuuts 'xvars' and
        'refinement_level'.
          outvars:      outputs that we can query from the GPR model (can
                        include derivative outputs dydx and dydp)
          xvars:        input variables to GPR model
          yvars:        native output variables (no derivatives)
          parameters:   each GPR model (i.e., instantiation of this class) is
                        constructed for a fixed set of parameters

        Option to normalize data according to nominal values of each input,
        output, and parameter:
          y' = y / y_nom --> dy'/dy = 1/y_nom
          x' = x / x_nom --> dx/dx' = x_nom
          p' = p / p_nom --> dp/dp' = p_nom

          dy'   dy   dy'   dx
          --- = -- * --- * --- = dy/dx * x_nom / y_nom
          dx'   dx   dy    dx'

          dy'   dy   dy'   dp
          --- = -- * --- * --- = dy/dp * p_nom / y_nom
          dp'   dp   dy    dp'
        """
        self.gpr_ops = gpr_ops
        if "save_name"   not in self.gpr_ops: self.gpr_ops["save_name"]   = None
        if "load_dir"    not in self.gpr_ops: self.gpr_ops["load_dir"]    = ""
        if "train_iters" not in self.gpr_ops: self.gpr_ops["train_iters"] = 1000
        if "learn_rate"  not in self.gpr_ops: self.gpr_ops["learn_rate"]  = 0.05
        if "min_noise"   not in self.gpr_ops: self.gpr_ops["min_noise"]   = 1E-8
        if "auto_norm"   not in self.gpr_ops: self.gpr_ops["auto_norm"]   = False

        # Opts w/ input checking
        if "data_path" in self.gpr_ops:
            if Path("./datafiles/" + self.gpr_ops["data_path"]).exists(): # automatically look in './datafiles'
                data_path = "./datafiles/" + self.gpr_ops["data_path"]
            else:
                data_path = self.gpr_ops["data_path"]
        else:
            raise Exception("'data_path' must be specified in input dict to 'GprModel'.")
        if "model_type" in self.gpr_ops:
            MODELS = ["multi_fidelity", "grad", "multi_fidelity_grad", "mf", "mf_grad"]
            if not self.gpr_ops["model_type"] in MODELS:
                raise Exception("Invalid GPR model '{}' specified. Please select one of ".format(
                    self.gpr_ops["model_type"]) + ", ".join(MODELS))
        else: self.gpr_ops["model_type"] = "multi_fidelity" # default
        if self.gpr_ops["model_type"] in ["grad", "multi_fidelity_grad", "mf_grad"]:
            self.grad_enhanced = True
        else:
            self.grad_enhanced = False
        if self.gpr_ops["save_name"]:
            save_name = "./saved_models/" + self.gpr_ops["save_name"] + '_' + \
                self.gpr_ops["model_type"]
        else: save_name = None

        with open(data_path) as f:
            while True:
                line = f.readline()
                if line.startswith('# x_labels: '):
                    self.xvars = re.sub('# x_labels: ', '', line).strip('\n').split(', ')
                    self.x_nom = np.ones(len(self.xvars))
                elif line.startswith('# y_labels: '):
                    self.yvars = re.sub('# y_labels: ', '', line).strip('\n').split(', ')
                    self.y_nom = np.ones(len(self.yvars))
                elif line.startswith('# params: '):
                    self.params = re.sub('# params: ', '', line).strip('\n').split(', ')
                    self.p_nom  = np.ones(len(self.params))
                elif line.startswith('# x_nom: '):
                    self.x_nom = np.array(re.sub('# x_nom: ', '', line).strip('\n').split(', '),
                            dtype=np.double)
                elif line.startswith('# y_nom: '):
                    self.y_nom = np.array(re.sub('# y_nom: ', '', line).strip('\n').split(', '),
                            dtype=np.double)
                elif line.startswith('# p_nom: '):
                    self.p_nom = np.array(re.sub('# p_nom: ', '', line).strip('\n').split(', '),
                            dtype=np.double)
                elif line.startswith('# header: '):
                    raw_header = re.sub(' ', '', re.sub('# header: ', '', line)).strip(
                            '\n').split(',')
                    break
                else:
                    raise Exception("Reading data file at " + data_path + " went bad.")
        raw_data = np.loadtxt(data_path)
        self.max_ref_lvl = int(max(raw_data[:,0]))
        raw_df = pd.DataFrame(raw_data, columns=raw_header)
        if self.gpr_ops["auto_norm"]:
            for i, xv in enumerate(self.xvars):
                self.x_nom[i] = max(abs(raw_df[self.xvars[0]]))
            for i, yv in enumerate(self.yvars):
                self.y_nom[i] = max(abs(raw_df[self.yvars[0]]))
            # can't auto-normalize parameters
        self.fit_params = self.gpr_ops['fit_params'] \
                if 'fit_params' in self.gpr_ops else self.params.copy()
        self.fit_x = self.gpr_ops['fit_x'] \
                if 'fit_x' in self.gpr_ops else self.xvars.copy()
        self.fit_y = self.gpr_ops['fit_y'] \
                if 'fit_y' in self.gpr_ops else self.yvars.copy()
        self.n_tasks = self.max_ref_lvl + 1 # number of refinement levels
        self.outvars = self.fit_y.copy()
        norm_keys = ['refine_level'] + self.xvars + self.yvars
        norm_vals = np.hstack((1, 1 / self.x_nom, 1 / self.y_nom))
        self.dydx_fit = [] # these outputs are handled automatically for grad-enhanced kernel
        self.dydp_fit = []
        for yi in self.fit_y:
            self.outvars += [yi+'*d/d'+xi for xi in self.fit_x]
            self.dydx_fit += [yi+'*d/d'+xi for xi in self.fit_x]
            norm_keys += [yi+'*d/d'+xi for xi in self.xvars] # copy of above
            norm_vals = np.hstack((norm_vals, np.array(
                [self.x_nom[self.xvars.index(xi)] / self.y_nom[self.yvars.index(yi)]
                    for xi in self.xvars])))
            self.outvars += [yi+'*d/d'+pi for pi in self.fit_params]
            self.dydp_fit += [yi+'*d/d'+pi for pi in self.fit_params]
            norm_keys += [yi+'*d/d'+pi for pi in self.params] # copy of above
            norm_vals = np.hstack((norm_vals, np.array(
                [self.p_nom[self.params.index(pi)] / self.y_nom[self.yvars.index(yi)]
                    for pi in self.params])))
        self.norm_map = dict(zip(norm_keys, norm_vals))
        self.data = dict.fromkeys(self.outvars)
        for var in self.norm_map: raw_df[var] *= self.norm_map[var]

        # Train; for gradient-enhanced models, we train (and can thus predict)
        # for y and dy/dx at once, so we don't need individual models for dy/dx.
        # For ex, for grad-enhanced models, we can predict dCD/dMach from the CD model.
        if self.grad_enhanced:
            trainvars = list(set(self.outvars).difference(set(self.dydx_fit)))
        else:
            trainvars = self.outvars
        self.gpr_sub_models = {}
        for yv in trainvars: # train a model for each var in trainvars
            # For grad-enhanced models, predict 'dydx' from model for 'y'
            if self.grad_enhanced and yv in self.yvars:
                y_predict = [yv] + [yv+'*d/d'+x_lab for x_lab in self.xvars]
                model_type = self.gpr_ops["model_type"]
            # Currently, we train independent models for 'dydp' (can't grad-enhance)
            else:
                y_predict = [yv]
                model_type = "multi_fidelity" # can only do 'mf' for these submodels
                
            data_hdr = ['refine_level'] + self.xvars + y_predict
            mask = [True if d in data_hdr else False for d in raw_header]
            cols = list(itertools.compress(raw_header, mask))
            sub_model_data = pd.DataFrame(raw_df.to_numpy()[:, mask], columns=cols)

            # Build, train, and save model
            if self.gpr_ops["load_dir"] != "": load_dir = "./saved_models/" \
                + self.gpr_ops["load_dir"] + '/' \
                + yv.replace("*", "x").replace("/", "") + '.pth'
            else: load_dir = "" # don't load results
            self.gpr_sub_models[yv] = GprSubModel(model_type,
                    self.xvars, y_predict, self.x_nom, self.norm_map,
                    sub_model_data, self.n_tasks, self.gpr_ops["train_iters"],
                    self.gpr_ops["learn_rate"], self.gpr_ops["min_noise"],
                    load_dir, save_name)

    def get_raw_data(self, out):
        if self.grad_enhanced:
            if out in self.fit_y + self.dydx_fit:
                return self.gpr_sub_models[out.split("*")[0]].get_raw_data()
            elif out in self.fit_params + self.dydp_fit:
                return self.gpr_sub_models[out].get_raw_data()
            else:
                raise Exception("Invalid output '{}' specified.".format(out))
                    # "valid outputs are {}".format(out)) # TODO
        else:
            return self.gpr_sub_models[out].get_raw_data()

    def eval(self, out, x, i, **kwargs):
        if self.grad_enhanced:
            if out in self.fit_y + self.dydx_fit: # TODO-1010 remove list join
                return self.gpr_sub_models[out.split("*")[0]].eval(out, x, i, **kwargs)
            elif out in self.dydp_fit:
                return self.gpr_sub_models[out].eval(out, x, i, **kwargs)
            else:
                raise Exception("Invalid output '{}' specified.".format(out))
                    # "valid outputs are {}".format(out, )) # TODO
        else:
            return self.gpr_sub_models[out].eval(out, x, i, **kwargs)

    def plot(self, output, input_dict, index, **kwargs):
        """
        Inputs:
          index:      index value for Hadamard kernel (e.g. refinement level for CFD)
          output:     output to plot
          input_dict: dictionary specifying the slice to plot, see example in main

        KWInputs:
          ns:               number of sampling points in each dimension
          scale:            scaling param for figure window
          save_path:        path to save output figure
          plot_train_data:  plot data used to train GPR model
          plot_mf_data:     from training data, plot results for all fidelities
          validation_data:  external data for validation
          eps:              epsilon for selecting data points (training or
                              validation) that lie on the plotting slice
        """
        # TODO-1010:
        # + handling derivatives?

        ns              = kwargs['ns']              if 'ns'              in kwargs else 25
        scale           = kwargs['scale']           if 'scale'           in kwargs else 0.42
        save_path       = kwargs['save_path']       if 'save_path'       in kwargs else False
        plot_train_data = kwargs['plot_train_data'] if 'plot_train_data' in kwargs else False
        plot_mf_data    = kwargs['plot_mf_data']    if 'plot_mf_data'    in kwargs else False
        validation_data = kwargs['validation_data'] if 'validation_data' in kwargs else None
        eps             = kwargs['eps']             if 'eps'             in kwargs else 5E-3
        # dvar          = kwargs['dvar']       if 'dvar'       in kwargs else None # TODO-1010

        # Find the variables to plot over (either one or two)
        xins     = []
        plotvars = []
        for xi in self.xvars:
            if input_dict[xi] == 'all': plotvars.append(xi)
            elif isinstance(input_dict[xi], tuple): plotvars.append(xi)
        input_dict['ns'] = ns
        mean, lower, upper, test_x, test_i = self.eval(
            output, input_dict, index, return_covar=True, return_input=True)

        # Selects the data points corresponding to desired input slice (within
        # tolerance eps)
        data_pts = self.get_raw_data(output) # get the training data
        const_vars = list(set(self.xvars).difference(set(plotvars)))
        for var in const_vars: # select data in the chosen x slice
            data_pts = data_pts[data_pts[var].between(
                input_dict[var] - eps, input_dict[var] + eps)]

        # All the indices (i.e., refinement levels) to plot
        if len(data_pts['refine_level']) == 0: # no data pts selected
            n_levels = 1
        else:
            n_levels = 1 + data_pts['refine_level'].max()
        data_colours = [ cm.plasma(x) for x in np.linspace(0.0, 0.95, int(n_levels)) ]
        data_colours[index] = (0.0, 0.0, 0.0, 1.0)
        data_inds = list(range(int(data_pts['refine_level'].min()),
            int(data_pts['refine_level'].max()) + 1)) if plot_mf_data else [index]

        if len(plotvars) == 1: # plot a slice
            f, ax = plt.subplots(1, 1, figsize=(scale*16, scale*10))
            plot_x = test_x[:, self.xvars.index(plotvars[0])]
            for i in data_inds:
                plt_data = data_pts[data_pts["refine_level"] == i]
                ax.plot(plt_data[plotvars[0]], plt_data[output],
                        color=data_colours[i],
                        marker='*',
                        markerfacecolor=data_colours[i],
                        markeredgecolor=data_colours[i],
                        linestyle = 'None',
                        label='Training, lvl ' + str(i))
            ax.plot(plot_x, mean, 'b', label='Mean')
            ax.fill_between(plot_x, lower, upper, alpha=0.5, label='Confidence')

            if validation_data:
                # TODO-1010: Take max refine level for validation data?
                val_df = self.load_validation_data_file(validation_data)
                for var in const_vars: # select data in the chosen x slice
                    val_df = val_df[val_df[var].between(
                        input_dict[var] - eps, input_dict[var] + eps)]
                ax.plot(val_df[plotvars[0]], val_df[output],
                        color='red',
                        marker='.',
                        markerfacecolor='red',
                        markeredgecolor='red',
                        linestyle = 'None',
                        label='Validation')

            ax.set_xlabel(plotvars[0])
            ax.set_ylabel(output)
            ax.legend()
            ax.autoscale(enable=True, axis='x', tight=True)
            ax.grid(which='major', axis='y', linestyle=':', color='grey')
            ax.set_facecolor('silver')
            plt.tight_layout()
            if save_path: plt.savefig(save_path)
            plt.show()

        elif len(plotvars) == 2: # plot a surface
            f, ax = plt.subplots(subplot_kw={"projection": "3d"})
            plot_x = test_x[:, self.xvars.index(plotvars[0])].reshape((ns, ns))
            plot_y = test_x[:, self.xvars.index(plotvars[1])].reshape((ns, ns))
            mean_z = mean.reshape((ns, ns))
            surf = ax.plot_surface(plot_x, plot_y, mean_z, cmap=cm.magma,
                    linewidth=0, antialiased=False)
            data_pts_plt = data_pts[data_pts["refine_level"] == index]
            ax.scatter3D(data_pts_plt[plotvars[0]], data_pts_plt[plotvars[1]],
                    data_pts_plt[output])

            if validation_data:
                val_df = self.load_validation_data_file(validation_data)
                for var in const_vars: # select data in the chosen x slice
                    val_df = val_df[val_df[var].between(
                        input_dict[var] - eps, input_dict[var] + eps)]
                ax.scatter3D(val_df[plotvars[0]], val_df[plotvars[1]],
                        val_df[output], color='red')

            # f.colorbar(surf, shrink=0.5, aspect=5)
            ax.set_xlabel(plotvars[0])
            ax.set_ylabel(plotvars[1])
            ax.set_title(output)
            if save_path: plt.savefig(save_path)
            plt.show()
        else:
            raise Exception("Invalid input: plotting ranges for more than two "
                    "variables specified.")

    def load_validation_data_file(self, data_path):
        # TODO: Could amalgamate this with main data file reading code (but that
        #   routine is much more complex)
        # Check first by default in './datafiles'
        if Path("./datafiles/" + data_path).exists():
            data_path = "./datafiles/" + data_path
        with open(data_path) as f:
            while True:
                line = f.readline()
                if line.startswith('# header: '):
                    raw_header = re.sub(' ', '', re.sub('# header: ', '', line)).strip(
                            '\n').split(',')
                    break
                elif line.startswith('#'):
                    continue
                else:
                    raise Exception("Reading data file at " + data_path + " went bad.")
        raw_data = np.loadtxt(data_path)
        raw_df = pd.DataFrame(raw_data, columns=raw_header)
        return raw_df

class GprSubModel:
    """
    GPR model; predicts raw outputs y from inputs x using one of the predefined
    model classes 'MultitaskGPModel', 'HadamardGradGPModel', 'GradGPModel', etc.
    Outputs can be either a scalar -- e.g., CD (drag coefficent) -- or a vector
    -- e.g., CD, dCD/dMach, dCD/dalpha (for a gradient-enhanced kernel).
    """
    def __init__(self, model_type, xvars, yvars, x_nom, norm_map, data,
            n_tasks, train_iters=1000, learn_rate=0.05, min_noise=1E-9,
            load_dir=None, save_name=None):
        self.xvars = xvars
        self.yvars = yvars
        self.data  = data
        self.norm_map = {k: norm_map[k]
                for k in ['refine_level'] + xvars + yvars if k in norm_map}
        self.x_nom = x_nom

        train_i = torch.tensor(
                np.array([self.data['refine_level'].to_numpy()]).T,
                dtype=torch.long).contiguous()
        train_x = torch.tensor(self.data[self.xvars].to_numpy()).contiguous()
        train_y = torch.tensor(self.data.reindex(columns=yvars).to_numpy()).contiguous()
        n_x = train_x.shape[1]
        if train_x.shape[1] == 1: train_x = train_x[:,0]
        if train_i.shape[1] == 1: train_i = train_i[:,0]
        if train_y.shape[1] == 1: train_y = train_y[:,0]

        # Build the likelihood and model
        if model_type in ["multi_fidelity_grad", "mf_grad"]:
            self.grad_enhanced = True
            ttrain_y = train_y # Hack to handle weird backend behaviour
            self.likelihood = gpytorch.likelihoods.MultitaskGaussianLikelihood(
                    num_tasks=train_y.shape[1],
                    # has_global_noise=False,
                    noise_constraint=gpytorch.constraints.GreaterThan(min_noise))
            self.model = HadamardGradGPModel(n_tasks, n_x, (train_x, train_i), train_y,
                    self.likelihood)
        elif model_type in ["grad"]:
            self.grad_enhanced = True
            ttrain_y = train_y # Hack to handle weird backend behaviour
            self.likelihood = gpytorch.likelihoods.MultitaskGaussianLikelihood(
                    num_tasks=train_y.shape[1],
                    noise_constraint=gpytorch.constraints.GreaterThan(min_noise))
            self.model = GradGPModel(n_x, train_x, train_y, self.likelihood)
        elif model_type in ["multi_fidelity", "mf"]:
            self.grad_enhanced = False
            ttrain_y = train_y.T
            self.likelihood = gpytorch.likelihoods.GaussianLikelihood(
                    noise_constraint=gpytorch.constraints.GreaterThan(min_noise))
            self.model = MultitaskGPModel(n_tasks, n_x, (train_x, train_i), train_y,
                    self.likelihood)
        else:
            raise Exception("Invalid model specified (shouldn't get here).")

        # TODO: when loading model, load jobfile as well to crosscheck options?
        if load_dir:
            if Path(load_dir).exists(): self.model.load_state_dict(torch.load(load_dir))
        # Here we need to set any constraints to overwrite (use spec'd value, not
        # saved value)
        if isinstance(self.likelihood, gpytorch.likelihoods.GaussianLikelihood):
            self.likelihood.noise_covar.register_constraint("raw_noise",
                    gpytorch.constraints.GreaterThan(min_noise))
        elif isinstance(self.likelihood, gpytorch.likelihoods.MultitaskGaussianLikelihood):
            self.likelihood.register_constraint("raw_noise",
                    gpytorch.constraints.GreaterThan(min_noise))
            self.likelihood.register_constraint("raw_task_noises",
                    gpytorch.constraints.GreaterThan(min_noise))

        self.model.train()
        self.likelihood.train()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=learn_rate)
        mll = gpytorch.mlls.ExactMarginalLogLikelihood(self.likelihood, self.model)

        # Unfortunately, due to some internal gpytorch behaviour, I don't think
        # there is a way around having split training loops (can't handle having
        # different numbers of inputs to 'model' using model(*train_data)... or something.
        if model_type in ["grad"]:
            for i in range(train_iters):
                optimizer.zero_grad()
                output = self.model(train_x)
                loss = -mll(output, ttrain_y)
                loss.backward()
                print("Iter %d - Loss: %.3f    Lengthscale: %s    Noise: %.3g"%(
                    i + 1, loss.item(),
                    np.array2string(self.model.covar_module.base_kernel.lengthscale.detach().numpy(),
                        precision=3, separator=', ', formatter=
                        {'float_kind': lambda x: "%.4g" % x}).strip('[').strip(']'),
                    self.model.likelihood.noise.item()
                ))
                optimizer.step()

        elif model_type in ["multi_fidelity", "mf"]:
            for i in range(train_iters):
                optimizer.zero_grad()
                output = self.model(train_x, train_i)
                loss = -mll(output, ttrain_y)
                loss.backward()
                print('Iter %d - Loss: %.3f   Lengthscale: %s   GlobalNoise: %.3g' % (
                   i+1, loss.item(),
                    np.array2string(self.model.covar_module.lengthscale.detach().numpy(),
                        precision=3, separator=', ', formatter=
                        {'float_kind': lambda x: "%.4g" % x}).strip('[').strip(']'),
                    self.model.likelihood.noise.item(),
                ))
                optimizer.step()

        elif model_type in ["multi_fidelity_grad", "mf_grad"]:
            for i in range(train_iters):
                optimizer.zero_grad()
                output = self.model(train_x, train_i)
                loss = -mll(output, ttrain_y)
                loss.backward()
                print('Iter %d - Loss: %.3f   Lengthscale: %s   GlobalNoise: %.3g   TaskNoises: %s' % (
                   i+1, loss.item(),
                    np.array2string(self.model.covar_module.lengthscale.detach().numpy(),
                        precision=3, separator=', ', formatter=
                        {'float_kind': lambda x: "%.4g" % x}).strip('[').strip(']'),
                    self.model.likelihood.noise.item(),
                    np.array2string(self.model.likelihood.task_noises.detach().numpy(),
                        precision=3, separator=', ', formatter=
                        {'float_kind': lambda x: "%.4g" % x}).strip('[').strip(']'),
                ))
                optimizer.step()

        else:
            raise Exception("Training loop for model type {} not implemented.".format(
                    gpr_ops["model_type"]))

        if save_name:
            Path(save_name).mkdir(parents=True, exist_ok=True)
            torch.save(self.model.state_dict(), save_name + '/' \
                    + self.yvars[0].replace("*", "x").replace("/", "") + '.pth')

        self.model.eval()
        self.likelihood.eval()

    def get_raw_data(self):
        """ Un-normalizes and returns training data. """
        data = self.data.copy()
        for col in data.columns: data[col] *= 1 / self.norm_map[col]
        return data

    def eval(self, out, x, i, **kwargs):
        """
        Evaluate the actual (unscaled) predicted outputs with the GPR model.
        Inputs:
          out -- str, output to evaluate
          i   -- fidelity level to evaluate
          x   -- sampling point in x
        x input types:
          1D array -- single sampling point (can also use list)
          2D array -- array of x arrays (so rows are x sampling points).
          dictionary -- specify sampling points by xvar name, can sample range
            or 'all' in up to two dimensions (slower, use other ops if speed reqd)
        """
        return_covar = kwargs['return_covar'] if 'return_covar' in kwargs else False
        return_input = kwargs['return_input'] if 'return_input' in kwargs else False
        return_der   = kwargs['return_der']   if 'return_der'   in kwargs else False
        outs = []
        if isinstance(x, list): x = np.array(x) # handle list input

        if isinstance(x, dict):
            ns = x['ns'] if 'ns' in x else 25
            xins  = []
            xouts = []
            for xi in self.xvars:
                if x[xi] == 'all': # plot entire range in data
                    xins.append(np.linspace(self.data[xi].min(), self.data[xi].max(), ns))
                    xouts.append(np.linspace(
                        self.data[xi].min() / self.norm_map[xi],
                        self.data[xi].max() / self.norm_map[xi], ns))
                elif isinstance(x[xi], tuple):
                    xins.append(np.linspace(x[xi][0] * self.norm_map[xi],
                        x[xi][1] * self.norm_map[xi], ns))
                    xouts.append(np.linspace(x[xi][0], x[xi][1], ns))
                else:
                    xins.append([x[xi] * self.norm_map[xi]])
                    xouts.append([x[xi]])
            test_x = torch.tensor(np.array(list(itertools.product(*xins))))
            test_i = torch.ones(test_x.shape[0], dtype=torch.long) * i
            x_out = np.array(list(itertools.product(*xouts)))
            i_out = test_i.numpy()
            if max(test_x.shape) > 1764:
                print("Warning: gpytorch often silently fails when evaluating a"
                    + " model at more than 1764 sampling points.")
                # TODO: 1764 is a close guess... real number?

        # 1D input
        elif len(x.shape) == 1 or (len(x.shape) == 2 and 1 in x.shape):
            x = x.ravel()
            x_out = x[:]
            x = x / self.x_nom
            test_x = torch.tensor(x.reshape(1, len(self.xvars)))
            test_i = torch.tensor([[i]])
            i_out = test_i.numpy()

        elif len(x.shape) == 2:
            x_out = x[:]
            x_nom_mat = np.tile(self.x_nom, (x.shape[0], 1))
            test_x = torch.tensor(x / x_nom_mat)
            test_i = torch.ones(test_x.shape[0], dtype=torch.long) * i
            i_out = test_i.numpy()

        else:
            raise Exception("'x' input type not understood.")

        if not return_der: # return primal soln for 'out'
            with torch.no_grad(), gpytorch.settings.fast_pred_var():
                pred_y = self.likelihood(self.model(test_x, test_i))
            if return_covar:
                if self.grad_enhanced:
                    out_i = self.yvars.index(out)
                    rtrn = (pred_y.mean[:,out_i].detach().numpy() * 1/self.norm_map[out],
                            pred_y.confidence_region()[0][:,out_i].detach().numpy() * 1/self.norm_map[out],
                            pred_y.confidence_region()[1][:,out_i].detach().numpy() * 1/self.norm_map[out],)
                else: # due to gpytorch behaviour, can't return col vector for single output case
                    rtrn = (pred_y.mean[:].detach().numpy() * 1/self.norm_map[out],
                            pred_y.confidence_region()[0][:].detach().numpy() * 1/self.norm_map[out],
                            pred_y.confidence_region()[1][:].detach().numpy() * 1/self.norm_map[out])
            else:
                if self.grad_enhanced:
                    out_i = self.yvars.index(out)
                    rtrn = (pred_y.mean.detach().numpy()[:,out_i] * 1/self.norm_map[out])
                else:
                    rtrn = (pred_y.mean.detach().numpy()[:] * 1/self.norm_map[out])

        else: # return derivative info
            # Via autograd and inverting the 'norm_map', we obtain d/dx'f(x).
            # We want d/dx f(x), i.e.,
            #   d/dx f(x) = dx'/dx * d/dx' f(x)
            #   d/dx f(x) = (1 / x_nom) * d/dx' f(x)
            # (this inverse scaling needs to be applied element-wise).
            test_x = torch.autograd.Variable(test_x, requires_grad=True)
            with gpytorch.settings.fast_pred_var():
                pred_y = self.likelihood(self.model(test_x, test_i))
            if return_covar:
                if self.grad_enhanced:
                    raise Exception(
                        "gpytorch does not provide derivatives of uncertainty bands.")
            else:
                if self.grad_enhanced:
                    out_i = self.yvars.index(out)
                    dy_mean = pred_y.mean[0,out_i].backward()
                    dydx = np.array(test_x.grad).reshape(len(self.xvars))
                    rtrn = (dydx * 1/self.norm_map[out] * (1 / self.x_nom))
                else:
                    dy_mean = pred_y.mean.backward()
                    dydx = np.array(test_x.grad).reshape(len(self.xvars))
                    rtrn = (dydx * 1/self.norm_map[out] * (1 / self.x_nom))

        if return_input: rtrn = rtrn + (x_out, i_out)
        return rtrn

def test_drive_model(gpr_model, test_plots=False, validation_df=None):
    # Test evaluating the model at a particular point
    from math import isclose
    mach_test = 2.7
    alpha_test = np.deg2rad(4)
    delta_test = np.deg2rad(0)
    x_test = np.array([mach_test, alpha_test, delta_test])
    i_test = 0 # ref_lvl=0
    out = 'CD' # predict drag coefficient
    y_test_0 = gpr_model.eval(out, x_test, i_test)
    x_test = {
        'Mach'  : mach_test,
        'alpha' : alpha_test,
        'delta' : delta_test,
    }
    y_test_1 = gpr_model.eval(out, x_test, i_test)
    # Should get same result for vector and dictionary input
    assert (y_test_0 == y_test_1).all()

    # Two ways of querying gradients 'dydx' for gradient models:
    # + query gradient output directly
    # + take derivative of GPR output.
    # These values should be CLOSE (not same) due to GPR noise, so use rel_tol=1E-3.
    # (Using x_test, i_test as above.)
    dydx = gpr_model.eval(out, x_test, i_test, return_der=True)
    out_der = 'CD*d/dMach'
    dydMach = gpr_model.eval(out_der, x_test, i_test)
    if gpr_model.grad_enhanced: # don't expect to agree otherwise
        assert math.isclose(dydx[gpr_model.xvars.index('Mach')], np.double(dydMach),
                rel_tol=1E-3)

    # Take second-derivatives as follows:
    # out_der = 'CD*d/dMach' (as above), x_test, i_test as above
    d2ydx2 = gpr_model.eval(out_der, x_test, i_test, return_der=True)
    # Compare against d^2/(dMach*dalpha) at x, computed using finite diffs.
    # Approximate as ( d/dMach*CD(x) d/dMach*CD(x+dalpha) ) / dalpha.
    x_test_plus = x_test.copy()
    dalpha = x_test_plus['alpha'] * 1E-6
    x_test_plus['alpha'] += dalpha
    out_der = 'CD*d/dMach'
    dydMach_plus = gpr_model.eval(out_der, x_test_plus, i_test)
    d2y_dMach_dalpha = float(dydMach_plus - dydMach) / dalpha
    if gpr_model.grad_enhanced: # don't expect to agree otherwise
        assert math.isclose(d2ydx2[gpr_model.xvars.index('alpha')],
                np.double(d2y_dMach_dalpha), rel_tol=1E-3)

    # 2D evaluation: array of x arrays
    x_test = np.array([
        [mach_test, np.deg2rad(3), delta_test],
        [mach_test, alpha_test   , delta_test], # alpha_test = 4 deg
        [mach_test, np.deg2rad(5), delta_test],
        ])
    y_test_2d = gpr_model.eval(out, x_test, i_test)
    assert isclose(float(y_test_0), y_test_2d[1], rel_tol=1E-6)

    # Show how to evaluate over a grid in Mach-alpha
    ns = 6
    mach_test_arr  = [2.0, 5.0]
    alpha_test_arr = [np.deg2rad(-4.0), np.deg2rad(3.0)]
    delta_test_arr = [np.deg2rad(0.0)]
    x_arr = [
        np.linspace(mach_test_arr[0], mach_test_arr[1], ns),
        np.linspace(alpha_test_arr[0], alpha_test_arr[1], ns),
        np.array(delta_test_arr)]
    x_test = np.array(list(itertools.product(*x_arr)))
    i_test = 0
    y_test_grid = gpr_model.eval(out, x_test, i_test)

    if test_plots:
        # To plot 1D slice, need to make input dict with xlabels as keys.
        # For one input, specify a range as either (min, max) or 'all' (to plot
        # entire range spanned by data).
        plot_slice = { # results for Mach
            'Mach'  : 'all', # plot whole Mach domain
            'alpha' : 0.04363,
            'delta' : 0.0,
        }
        plot_output = 'CD' # 'CD*d/drt0' # 'CD*d/dMach'
        plot_index = 0 # plot for mesh adaptation level 0 (here, finest)
        gpr_model.plot(plot_output, plot_slice, plot_index,
            scale=0.32,
            ns=51,
            plot_mf_data=True,
            validation_data=validation_df)
        # Same, but plot vs alpha
        plot_slice = {
            'Mach'  : 6.1,
            'alpha' : 'all',
            'delta' : 0.0,
        }
        gpr_model.plot(plot_output, plot_slice, plot_index,
            scale=0.32,
            ns=51,
            plot_mf_data=True,
            validation_data=validation_df)
        # Finally, plot some parameter derivatives
        plot_output = 'CD*d/drt0' # 'CD*d/dMach'
        gpr_model.plot(plot_output, plot_slice, plot_index,
            scale=0.32,
            ns=51,
            plot_mf_data=True,
            validation_data=validation_df)

        # Same to plot 2D surface, but need to specify ranges for two inputs.
        plot_surf = { # Mach-alpha slice
            'Mach'  : 'all',
            'alpha' : 'all',
            'delta' : 0.0,
        }
        plot_output = 'CD'
        plot_index = 0 # plot for first mesh adaptation level
        gpr_model.plot(plot_output, plot_surf, plot_index,
            ns=25)#, validation_data='aero_data_validation.txt')
    pass


if __name__ == "__main__":
    plot_flag = True
    validation_data = 'aero_data_validation.txt'
    gpr_ops_mf = {
        "train_iters"  : 5,
        "learn_rate"   : 0.03, # learning rate for optimizer
        "min_noise"    : 1E-8, # minimum noise value for GPR model
        # "auto_norm"    : True,
        "fit_params"   : ["rt0", "at0"], # fit derivatives for these params only
        "fit_x"        : ["Mach", "alpha"], # fit derivatives for these states only
        "fit_y"        : ["CD"], # fit models for these outputs only

        "data_path"    : 'aero_data_mf_noisy.txt',
        "model_type"   : "multi_fidelity",
        # "save_name"    : "mf_test",
        "load_dir"     : "mf_test_multi_fidelity",
    }
    print("Testing multi-fidelity model...")
    test_drive_model(GprModel(gpr_ops_mf), plot_flag, validation_data)

    gpr_ops_grad = {
        "train_iters"  : 5,
        "learn_rate"   : 0.03, # learning rate for optimizer
        "min_noise"    : 1E-8, # minimum noise value for GPR model
        # "auto_norm"    : True,
        "fit_params"   : ["rt0", "at0"], # fit derivatives for these params only
        "fit_x"        : ["Mach", "alpha"], # fit derivatives for these states only
        "fit_y"        : ["CD"], # fit models for these outputs only

        "data_path"    : 'aero_data_noisy.txt',
        "model_type"   : "grad",
        # "save_name"    : "grad_test",
        "load_dir"     : "grad_test_grad",
    }
    print("Testing gradient-enhanced model...")
    test_drive_model(GprModel(gpr_ops_grad), plot_flag, validation_data)

    gpr_ops_mf_grad = {
        "train_iters"  : 5,
        "learn_rate"   : 0.03, # learning rate for optimizer
        "min_noise"    : 1E-8, # minimum noise value for GPR model
        # "auto_norm"    : True,
        "fit_params"   : ["rt0", "at0"], # fit derivatives for these params only
        "fit_x"        : ["Mach", "alpha"], # fit derivatives for these states only
        "fit_y"        : ["CD"], # fit models for these outputs only

        "data_path"    : 'aero_data_mf.txt',
        "model_type"   : "mf_grad",
        # "save_name"    : "mf_grad_test",
        "load_dir"     : "mf_grad_test_mf_grad",
    }
    print("Testing multi-fidelity gradient-enhanced model...")
    test_drive_model(GprModel(gpr_ops_mf_grad), plot_flag, validation_data)

    print("\n\nTesting passed.\n\n")


    # Goals:
    # + Complete test suite for all model types.
    # + Integration with aero_forces.
    # + SU2-pointwise pipeline.
    # + Output interpolant.
    # + Add manual normalization code to aerodecks.
    # + Fix noise model so that we have low error at sample points.


    # Now what?
    # + Put Hessian into 'aero_forces'.
    # + Fast interpolators for online evaluation.
    # + Test full pipeline.





