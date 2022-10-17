def identify_social_network(df):
    '''
    This function receives as a parameter a dataframe
    and identifies what social network is data and return
    the social network identified.
    :param df: type dataframe, dataframe to be analyzed
    :return: social_network: type str, string with the social
    network
    '''

    if 'comment_id' in df and 'message' in df:
        social_network = 'fb'
    elif 'comment_id' in df and 'text' in df:
        social_network = 'ig'
    elif 'tweet_id' in df and 'text' in df:
            social_network = 'tw'
    else:
        social_network = "undefined"
    return social_network