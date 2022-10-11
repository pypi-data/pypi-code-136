
# ==================================================================
#                                          _           
#                                         | |          
#              ___  ___ _ __ __ ___      _| | ___ _ __ 
#             / __|/ __| '__/ _` \ \ /\ / / |/ _ \ '__|
#             \__ \ (__| | | (_| |\ V  V /| |  __/ |   
#             |___/\___|_|  \__,_| \_/\_/ |_|\___|_|   
#                                                      
#                                                     fidle.Scrawler
# ==================================================================
# A simple module to host usefull functions for Fidle practical work
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022


import matplotlib
import matplotlib.pyplot as plt
import math
import itertools
import numpy as np
import sklearn.metrics
import pandas as pd

from IPython.display import display,Image,Markdown,HTML

import fidle.config as config
import fidle.utils  as utils


__version__   = config.VERSION

__save_figs   = False
__figs_dir    = './figs'
__figs_name   = 'fig_'
__figs_id     = 0


# -------------------------------------------------------------
# Plot images
# -------------------------------------------------------------
#
def images(x,y=None, indices='all', columns=12, x_size=1, y_size=1,
                colorbar=False, y_pred=None, cm='binary', norm=None, y_padding=0.35, spines_alpha=1,
                fontsize=20, interpolation='lanczos', save_as='auto'):
    """
    Show some images in a grid, with legends
    args:
        x             : images - Shapes must be (-1,lx,ly) (-1,lx,ly,1) or (-1,lx,ly,3)
        y             : real classes or labels or None (None)
        indices       : indices of images to show or 'all' for all ('all')
        columns       : number of columns (12)
        x_size,y_size : figure size (1), (1)
        colorbar      : show colorbar (False)
        y_pred        : predicted classes (None)
        cm            : Matplotlib color map (binary)
        norm          : Matplotlib imshow normalization (None)
        y_padding     : Padding / rows (0.35)
        spines_alpha  : Spines alpha (1.)
        font_size     : Font size in px (20)
        save_as       : Filename to use if save figs is enable ('auto')
    returns: 
        nothing
    """
    if indices=='all': indices=range(len(x))
    if norm and len(norm) == 2: norm = matplotlib.colors.Normalize(vmin=norm[0], vmax=norm[1])
    draw_labels = (y is not None)
    draw_pred   = (y_pred is not None)
    rows        = math.ceil(len(indices)/columns)
    fig=plt.figure(figsize=(columns*x_size, rows*(y_size+y_padding)))
    n=1
    for i in indices:
        axs=fig.add_subplot(rows, columns, n)
        n+=1
        # ---- Shape is (lx,ly)
        if len(x[i].shape)==2:
            xx=x[i]
        # ---- Shape is (lx,ly,n)
        if len(x[i].shape)==3:
            (lx,ly,lz)=x[i].shape
            if lz==1: 
                xx=x[i].reshape(lx,ly)
            else:
                xx=x[i]
        img=axs.imshow(xx,   cmap = cm, norm=norm, interpolation=interpolation)
#         img=axs.imshow(xx,   cmap = cm, interpolation=interpolation)
        axs.spines['right'].set_visible(True)
        axs.spines['left'].set_visible(True)
        axs.spines['top'].set_visible(True)
        axs.spines['bottom'].set_visible(True)
        axs.spines['right'].set_alpha(spines_alpha)
        axs.spines['left'].set_alpha(spines_alpha)
        axs.spines['top'].set_alpha(spines_alpha)
        axs.spines['bottom'].set_alpha(spines_alpha)
        axs.set_yticks([])
        axs.set_xticks([])
        if draw_labels and not draw_pred:
            axs.set_xlabel(y[i],fontsize=fontsize)
        if draw_labels and draw_pred:
            if y[i]!=y_pred[i]:
                axs.set_xlabel(f'{y_pred[i]} ({y[i]})',fontsize=fontsize)
                axs.xaxis.label.set_color('red')
            else:
                axs.set_xlabel(y[i],fontsize=fontsize)
        if colorbar:
            fig.colorbar(img,orientation="vertical", shrink=0.65)
    save_fig(save_as)
    plt.show()

    
def image(x,cm='binary', figsize=(4,4),interpolation='lanczos', save_as='auto'):
    """
    Draw a single image.
    Image shape can be (lx,ly), (lx,ly,1) or (lx,ly,n)
    args:
        x       : image as np array
        cm      : color map ('binary')
        figsize : fig size (4,4)
    """
    # ---- Shape is (lx,ly)
    if len(x.shape)==2:
        xx=x
    # ---- Shape is (lx,ly,n)
    if len(x.shape)==3:
        (lx,ly,lz)=x.shape
        if lz==1: 
            xx=x.reshape(lx,ly)
        else:
            xx=x
    # ---- Draw it
    plt.figure(figsize=figsize)
    plt.imshow(xx,   cmap = cm, interpolation=interpolation)
    save_fig(save_as)
    plt.show()


# -------------------------------------------------------------
# Plot history
# -------------------------------------------------------------

def history(history, figsize=(8,6), 
                 plot={"Accuracy":['accuracy','val_accuracy'], 'Loss':['loss', 'val_loss']},
                 save_as='auto'):
    """
    Show history
    args:
        history: history
        figsize: fig size
        plot: list of data to plot : {<title>:[<metrics>,...], ...}
    """
    fig_id=0
    for title,curves in plot.items():
        plt.figure(figsize=figsize)
        plt.title(title)
        plt.ylabel(title)
        plt.xlabel('Epoch')
        for c in curves:
            plt.plot(history.history[c])
        plt.legend(curves, loc='upper left')
        if save_as=='auto':
            figname='auto'
        else:
            figname=f'{save_as}_{fig_id}'
            fig_id+=1
        save_fig(figname)
        plt.show()


# -------------------------------------------------------------
# Plot confusion matrix
# -------------------------------------------------------------
def confusion_matrix(y_true,y_pred,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True,
                          figsize=(10, 8),
                          digit_format='{:0.2f}',
                          save_as='auto'):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

    """
    cm = sklearn.metrics.confusion_matrix( y_true,y_pred, normalize=None, labels=target_names)
    
    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=figsize)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=90)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, digit_format.format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    save_fig(save_as)
    plt.show()


    
def confusion_matrix_txt(y_true,y_pred,labels=None,color='green',
                             font_size='12pt', title="#### Confusion matrix is :"):
    """
    Show a confusion matrix for a predictions.
    see : sklearn.metrics.confusion_matrix

    Args:
        y_true:       Real classes
        y_pred:       Predicted classes
        labels:       List of classes to show in the cm
        color:        Color for the palette (green)
        font_size:    Values font size 
        title:        the text to display at the top of the matrix        
    """
    assert (labels!=None),"Label must be set"
    
    if title != None :  display(Markdown(title)) 
    
    cm = sklearn.metrics.confusion_matrix( y_true,y_pred, normalize="true", labels=labels)
    df=pd.DataFrame(cm)

#     cmap = sn.light_palette(color, as_cmap=True)

    colorsList = ['whitesmoke','bisque']
    cmap = matplotlib.colors.ListedColormap(colorsList)
    cmap = matplotlib.colors.ListedColormap(cmap(np.linspace(0, 1, 256)))

    df.style.set_properties(**{'font-size': '20pt'})
    display(df.style.format('{:.2f}') \
            .background_gradient(cmap=cmap)
            .set_properties(**{'font-size': font_size}))
    

# -------------------------------------------------------------
# Plot donut
# -------------------------------------------------------------

def donut(values, labels, colors=["lightsteelblue","coral"], figsize=(6,6), title=None, save_as='auto'):
    """
    Draw a donut
    args:
        values   : list of values
        labels   : list of labels
        colors   : list of color (["lightsteelblue","coral"])
        figsize  : size of figure ( (6,6) )
    return:
        nothing
    """
    # ---- Title or not
    if title != None :  display(Markdown(title))
    # ---- Donut
    plt.figure(figsize=figsize)
    # ---- Draw a pie  chart..
    plt.pie(values, labels=labels, 
            colors = colors, autopct='%1.1f%%', startangle=70, pctdistance=0.85,
            textprops={'fontsize': 18},
            wedgeprops={"edgecolor":"w",'linewidth': 5, 'linestyle': 'solid', 'antialiased': True})
    # ---- ..with a white circle
    circle = plt.Circle((0,0),0.70,fc='white')
    ax = plt.gca()
    ax.add_artist(circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    plt.tight_layout()
    save_fig(save_as)
    plt.show()
    

    
def multivariate_serie(sequence, labels=None, predictions=None, only_features=None,
                            columns=3, width=5,height=4,wspace=0.3,hspace=0.2,ms=6,lw=1,
                            save_as='auto', time_dt=1, hide_ticks=False):
    
    sequence_len = len(sequence)
    features_len = sequence.shape[1]
    if only_features is None : only_features=range(features_len)
    if labels is None        : labels=range(features_len)
    
    t  = np.arange(sequence_len)    
    if predictions is None:
        dt = 0
    else:
        dt = len(predictions)
        sequence_with_pred = sequence.copy()
        sequence_with_pred[-dt:]=predictions

    rows = math.ceil(features_len/columns)
    fig  = plt.figure(figsize=(columns*width, rows*height))
    fig.subplots_adjust(wspace=0.3,hspace=0.2)
    n=1
    for i in only_features:
        ax=fig.add_subplot(rows, columns, n)
        
        # ---- Real sequence without prediction
        #
        ax.plot( t[:-dt],sequence[:-dt,i], 'o',  markersize=ms, color='C0', zorder=2)
        ax.plot( t,sequence[:,i],          '-',  linewidth=lw,  color='C0', label=labels[i],zorder=1)

        # ---- What we expect
        #
        ax.plot(t[-dt:], sequence[-dt:,i], 'o', markeredgecolor='C0',markerfacecolor='white',ms=6)
        
        if predictions is not None:
            ax.plot(t[-dt-1:], sequence_with_pred[-dt-1:,i], '--',  lw=lw, fillstyle='full',  ms=ms, color='C1',zorder=1)
            ax.plot(t[-dt:],   predictions[:,i],             'o',   lw=lw, fillstyle='full',  ms=ms, color='C1',zorder=2)

        if hide_ticks:
            ax.set_yticks([])
            ax.set_xticks([])
        
        ax.legend(loc="upper left")
        n+=1
    save_fig(save_as)
    plt.show()

    
# -------------------------------------------------------------
# Show 2d series and segments
# -------------------------------------------------------------
#

def serie_2d(data, figsize=(10,8), monocolor=False, hide_ticks=True, lw=2, ms=4, save_as='auto'):
    """
    Plot a 2d dataset as a trajectory
    args:
        data:      Dataset to plot
        figsize:   Figure size ( (10,8))
        monocolor: Monocolor line or not. (False)
    return:
        nothing
    """
    # ---- Get x,y, min and max
    #
    n     = len(data)
    k     = int(n/100)
    x,y   = data[:,0], data[:,1]
 
    # ---- Draw it
    #
    fig = plt.figure(figsize=figsize)
    ax = plt.axes()

    # ---- Monocolor or gray gradient
    #
    if monocolor:
        ax.plot(x,y)
    else:
        for i in range(0,100):
            a= (200-i)/200
            ax.plot(x[i*k:(i+1)*k+1], y[i*k:(i+1)*k+1], '-', color=(a,a,a),lw=lw,zorder=1)

    # ---- Last point
    #
    ax.plot(x[n-1], y[n-1], 'o', color='C1',ms=ms,zorder=2)
    
    ax.set_aspect('equal', 'box')
    ax.set_xlabel('axis=0')
    ax.set_ylabel('axis=1')
    
    if hide_ticks:
        ax.set_yticks([])
        ax.set_xticks([])

    save_fig(save_as)
    plt.show()
    
    
def segment_2d(sequence_real, sequence_pred, figsize=(10,8), ms=6, lw=1, hide_ticks=True, save_as='auto'):
    """
    Plot a 2d segment real and predicted
    args:
        sequence_real: Real sequence
        sequence_pred: Predicted sequence
        figsize:       Figure size ( (10,8) )
        ms:            Marker size (6)
    return:
        nothing
    """
    k = len(sequence_pred)
    x,y = sequence_real[:,0],sequence_real[:,1]
    u,v = sequence_pred[:,0],sequence_pred[:,1]
    
    fig = plt.figure(figsize=figsize)

    ax = plt.axes()
    
    # ---- Draw real sequence without prediction
    #
    ax.plot(x[:-k], y[:-k],   'o', color='C0', fillstyle='full', zorder=2, ms=ms)
    ax.plot(x, y,             '-', color='C0', lw=lw, zorder=1)
    
    # ---- What we expect
    #
    ax.plot(x[-k:], y[-k:], 'o', ms=ms, markeredgecolor='C0', markerfacecolor='white', zorder=2)

    # ---- What we have
    #
    ax.plot(u, v,                            'o',  color='C1',fillstyle='full',zorder=2, ms=ms)
    ax.plot( [x[-1-k],u[0]], [y[-1-k],v[0]], '--', color='C1',lw=lw, zorder=1)
    ax.plot(u, v,                            '--', color='C1',lw=lw, zorder=1)

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('axis=0')
    ax.set_ylabel('axis=1')
    
    if hide_ticks:
        ax.set_yticks([])
        ax.set_xticks([])

    save_fig(save_as)
    plt.show()

    
    

# -------------------------------------------------------------
# Saving figs stuff
# -------------------------------------------------------------
   
def set_save_fig(save=True, figs_dir='./figs', figs_name='fig_', figs_id=0):
    """
    Set save_fig parameters
    Default figs name is <figs_name><figs_id>.{png|svg}
    args:
        save      : Boolean, True to save figs (True)
        figs_dir  : Path to save figs (./figs)
        figs_name : Default basename for figs (figs_)
        figs_id   : Start id for figs name (0)
    """
    global __save_figs, __figs_dir, __figs_name, __figs_id
    __save_figs = save
    __figs_dir  = figs_dir
    __figs_name = figs_name
    __figs_id   = figs_id
    
    
def save_fig(filename='auto', png=True, svg=False):
    """
    Save current figure
    args:
        filename : Image filename ('auto')
        png      : Boolean. Save as png if True (True)
        svg      : Boolean. Save as svg if True (False)
    """
    global __figs_id

    if filename is None  : return
    if not __save_figs   : return

    utils.mkdir(__figs_dir)
    
    if filename=='auto': 
        path=f'{__figs_dir}/{__figs_name}{__figs_id:02d}'
        __figs_id+=1
    else:
        path=f'{__figs_dir}/{filename}'

    if png : plt.savefig( f'{path}.png')
    if svg : plt.savefig( f'{path}.png')
    
    utils.display_html(f'<div class="comment">Saved: {path}</div>')
    
