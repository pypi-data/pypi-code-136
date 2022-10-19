import pandas as pd

# def drawdown_calc(df, num_drawdowns, date_col='Date',
#                   value_col='Return', is_date_indexed=False):
#     """This is a util method to calculate the drawdowns from a series of date-indexed returns values
#
#     :param df: dataframe containing return or gross values with dates
#     :param num_drawdowns: number of drawdowns
#     :param date_col: specify the column name for dates
#     :param value_col:  column to calc drawdowns on
#     :param is_date_indexed: True if the dataframe is indexed by date
#
#     :return: A list of [[drawdown_begin_date, drawdown_end_date, drawdown_value]]
#     """
#     returns = df[value_col][1:]
#     returns = list(returns)
#     drawdown_list = []
#     rolling_drawdown = _recur_drawdown_calc(returns, drawdown_list, 0)
#     drawdown_list.sort(key=lambda x: x[2])
#     drawdown_list = drawdown_list[:num_drawdowns]
#     # Convert raw-index to dates
#     for dd in drawdown_list:
#         if is_date_indexed:
#             dd[0] = df.index[dd[0] + 1]
#             dd[1] = df.index[dd[1]]
#         else:
#             dd[0] = df[date_col].iloc[dd[0] + 1]
#             dd[1] = df[date_col].iloc[dd[1]]
#
#     # Remove all the dds with only 1 day length.
#     drawdown_list = [x for x in drawdown_list if x[0] != x[1]]
#     # logging.info("The drawdowns are computed as follows - {}".format(drawdown_list))
#     return drawdown_list, rolling_drawdown
#
#
# def _recur_drawdown_calc(returns, drawdown_list, add_to_index=0):
#     length = len(returns)
#     if length <= 1:
#         return None
#     values = [1.0 for i in range(length + 1)]
#     rolling_max = [-1 for i in range(length + 1)]
#     rolling_dd = [0 for i in range(length + 1)]
#
#     rolling_max[0] = 1
#     rolling_high_index = 0
#     max_dd = 0
#     trough_index = 0
#     peak_index = 0
#
#     # calc maxDD
#     for i in range(length):
#         values[1 + i] = values[i] * (1.0 + returns[i])
#         if values[1 + i] > rolling_max[i]:
#             rolling_high_index = 1 + i
#         rolling_max[1 + i] = max(rolling_max[i], values[1 + i])
#         rolling_dd[1 + i] = values[1 + i] / rolling_max[1 + i] - 1.0
#
#         if rolling_dd[1 + i] < max_dd:
#             max_dd = rolling_dd[1 + i]
#             trough_index = 1 + i
#             peak_index = rolling_high_index
#     peak_index += add_to_index
#     trough_index += add_to_index
#     if peak_index == trough_index:
#         return None
#     drawdown_list.append([peak_index, trough_index, max_dd])
#
#     # recursion steps
#     _recur_drawdown_calc(returns[: peak_index - add_to_index], drawdown_list, add_to_index)
#     _recur_drawdown_calc(returns[trough_index - add_to_index + 1:], drawdown_list, trough_index + 1)
#
#     return rolling_dd


def calc_cum_nmvs(returns):
    returns = list(returns).copy()
    returns.insert(0, 0.0)
    cum_nmvs = (pd.Series(returns) + 1).cumprod()

    return cum_nmvs


def _calc_drawdowns(returns, num_drawdowns=None):
    # get cumulative NMVs
    cum_nmvs = calc_cum_nmvs(returns)

    N = len(returns)

    # calc all candidates with cum_rets(i->j)<0
    drawdown_candidates = list()
    for i in range(N):
        candidates = list()
        for j in range(i, N):
            cum_return = cum_nmvs[j] / cum_nmvs[i] - 1
            if cum_return < 0:
                candidates.append([i, j, cum_return])

        drawdown_candidates.extend(candidates)

    if len(drawdown_candidates)==0:
        return drawdown_candidates

    # sort all candidates by cum_rets
    drawdown_candidates.sort(key=lambda x: x[2], reverse=False)

    # remove overlaps
    #     drawdowns = [drawdown_candidates[0]]
    #     N = len(drawdown_candidates)
    drawdowns = list()
    if num_drawdowns is None:
        num_drawdowns = 1e10

    for candidate in drawdown_candidates:  # for each candidate
        if not drawdowns:
            # add the first candiate anyway
            drawdowns.append(candidate)
            continue

        overlap = False
        # check exisiting drawdowns
        for drawdown in drawdowns:
            # if curr candidate has NO overlap with this existing drawdown, the continue
            if candidate[1] < drawdown[0] or candidate[0] > drawdown[1]:
                continue
            else:  # otherwise, overlap found, break here!
                overlap = True
                break

        # No overlaps with all existing drawdowns, then add this candidate to drawdown list
        if not overlap:
            drawdowns.append(candidate)

        if len(drawdowns)>=num_drawdowns:
            break

    return drawdowns


def calc_drawdowns(df, date_col='Date', return_col='Return',
                   num_drawdowns=None,
                   ret_as_df=True):
    if date_col=='index':
        df.sort_index(inplace=True)
        dates = df.index.values
    else:
        df.sort_values(date_col, inplace=True)
        dates = df[date_col].values

    drawdowns = _calc_drawdowns(df[return_col], num_drawdowns=num_drawdowns)

    for i, [start, end, dd] in enumerate(drawdowns):
        drawdowns[i][0] = pd.Timestamp(dates[start])
        drawdowns[i][1] = pd.Timestamp(dates[end])

    if ret_as_df:
        drawdowns = pd.DataFrame(drawdowns, columns=['StartDate', 'EndDate', 'DD'])

    return drawdowns
