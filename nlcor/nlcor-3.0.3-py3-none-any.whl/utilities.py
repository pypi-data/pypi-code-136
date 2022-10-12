import pandas as pd
import numpy as np
from scipy import stats
import math
import statsmodels.api as sm

MIN_SEGMENT_SIZE = 3

def update_segments_cor(x_seg,
                      y_seg,
                      segmentsCor):
    segcor = stats.pearsonr(x_seg, y_seg)
    if segmentsCor['cor'] == None:
        segmentsCor['cor'] = [segcor[0]]
        segmentsCor['p_value'] = [segcor[1]]
    else:
        if not isinstance(segmentsCor['cor'], list):
            segmentsCor['cor'] = [segmentsCor['cor']]
            segmentsCor['p_value'] = [segmentsCor['p_value']]
        segmentsCor['cor'].append(segcor[0])
        segmentsCor['p_value'].append(segcor[1])

    return segmentsCor


def segment(l,
            s):
    # This function creates the segments
    # on which linear correlation will be calculated
    windowLen = math.floor(s * l)

    numSegments = l // windowLen
    segments = []
    upp = windowLen
    low = 1
    for i in range(1, numSegments + 1):
        segments.insert(i + 1, list(range(low, upp + 1)))
        low = upp + 1
        upp = upp + windowLen
    # If the segment doesn't cover all the elements in X,
    # those will be added to the end of the segment
    if l % windowLen != 0:
        seg = list(np.arange(low, l + 1))
        if len(seg) <= MIN_SEGMENT_SIZE:
            # Merge with the last segment
            for i in (0,len(seg)-1):
                segments[len(segments) - 1].append(seg[i])
        else:
            segments.append(seg)
    return segments


def segment_correlation(x_seg,
                        y_seg):
    temp = stats.pearsonr(x_seg,
                          y_seg)
    cor = 0 if pd.isna(temp[0]) == True else temp[0]
    p_value = 1 if pd.isna(temp[0]) else temp[1]
    segmentcorrelation = {'cor': cor, 'p_value': p_value}
    return segmentcorrelation


def validate_refine(l,
                    refine):
    # This function validates the size of refine
    if math.floor(refine * l) < MIN_SEGMENT_SIZE:
        # Means too few data points in a segment.
        # Therefore, increase it.
        while math.floor(refine * l) <= MIN_SEGMENT_SIZE:
            refine = refine + 0.01
    return refine


def update_df_fit(seg,
                  df,
                  df_fit):
    df.index = range(1, len(df) + 1)
    # seg = seg[0]
    data = df.loc[seg]
    y = data['y']
    x = data['x']
    x = sm.add_constant(x)
    fit = sm.OLS(y,
                 x).fit()

    if len(fit.pvalues) == 2:
        fit_significance = fit.pvalues['x']
    else:
        fit_significance = None

    if (pd.isna(fit_significance)) or (fit_significance > 0.01):
        # TODO: Make the pvalue threshold of 0.01 adjusted as per Bonferroni
        # When the fit is not statistically significant.
        data = {'x': df["x"].loc[seg],
                'fit': fit.predict()}
        df_fit = pd.concat([df_fit,
                            pd.DataFrame.from_dict(data)],
                           ignore_index=True)
        # Adding the fitted values as NA for plotting because no real
        # correlation exist here.
        df_fit.loc[
            len(df_fit.index)] = None
        # Last point set to NA for plotting beautification. It results into disjoint
        # lines. Otherwise, the plot is ugly with several cliffs.
    else:
        # Fit is statistically significant.
        data = {'x': df["x"].loc[seg],
                'fit': fit.predict()}
        df_fit = pd.concat([df_fit,
                            pd.DataFrame.from_dict(data)])  # Adding the fitted values for plotting.
        df_fit.loc[
            len(df_fit.index)] = None
        # Last point set to NA for plotting beautification. It results into disjoint lines.
        # Otherwise, the plot is ugly with several cliffs
    return df_fit
