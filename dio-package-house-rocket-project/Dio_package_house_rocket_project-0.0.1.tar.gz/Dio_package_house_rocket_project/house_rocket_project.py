##############################################################
#   Import Library
##############################################################
import streamlit as st
import pandas as pd
import plotly.express as px

##############################################################
#   Set Browser Layout
##############################################################
st.set_page_config(layout='wide')
@st.cache(allow_output_mutation=True)

##############################################################
#  Load Dataset
##############################################################
def get_data(path):
    data = pd.read_csv(path)
    return data

##############################################################
#   Set Sidebar
#   Show dataset
#   Plot map
##############################################################
def set_zipcode_map(data):
    # Set sidebar
    st.header('-- Purchase Suggestion --')
    st.sidebar.title('-- Purchase Suggestion --')
    v_zipcode = st.sidebar.selectbox('Select Zipcode:', data['zipcode'].sort_values().unique())

    check_buy = st.sidebar.selectbox('Only house for purchase?', ['Yes', 'No'])
    df = data[data['zipcode'].isin([v_zipcode])]

    # Count total houses by zipcode and show the dataset able
    if check_buy == "Yes":
        df_buy = df[df['status'] == 'Buy']
        st.subheader('1 - Location and purchase suggestion - {:}  houses'.format(df_buy.shape[0]))
        st.write(df_buy)
        file_name_download = "Purchase_Suggestion.csv"
    else:
        df_buy = df
        st.subheader('1 - All houses per zipcode - {:}  houses'.format(df.shape[0]))
        st.write(df)
        file_name_download = "All_Data.csv"

    ##############################################################
    # Create Map
    ##############################################################
    fig = px.scatter_mapbox(df_buy,
                            lat="lat",
                            lon="long",
                            size="price",
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=15,
                            zoom=10,
                            hover_data={'zipcode': True,
                                        'id': True,
                                        'yr_built': True,
                                        'status': True,
                                        'condition': True,
                                        'road': True,
                                        'house_number': True,
                                        'city': True,
                                        'county': True,
                                        'state': True,
                                        'lat': False,
                                        'long': False
                                        }
                            )

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=400, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    st.plotly_chart(fig, use_container_width=True)

    ##############################################################
    # Download button
    ##############################################################
    csv = df_buy.to_csv().encode('utf-8')
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=file_name_download,
        mime='text/csv')

    return None

##############################################################
#   Exploratory Data Analysis (EDA)
##############################################################

# Set sidebar for EDA Question
def f_question(list_hypothesis):
    st.header('-- Exploratory Data Analysis (EDA) --')
    st.sidebar.title('-- EDA --')
    v_list = st.sidebar.selectbox('Select the Business Hypothesis', list_hypothesis)
    return v_list

# Print Question/Answer business
def f_business_answer(business_question, business_answer):
    st.subheader(business_question)
    st.subheader(business_answer)
    return None

# Plot the histogram
def f_plot_histogram(df, x, y):
    fig = px.bar(df, x, y)
    st.plotly_chart(fig, use_container_width=True)
    return None

# Profit Dataframe
def f_df_profit(data):
    # Calculate median value to price and sell price
    df_sum_buy = data[['price', 'zipcode']].loc[data['status'] == 'Buy'].groupby(['zipcode']).sum().reset_index()
    df_sum_sell = data[['sell_price', 'zipcode']].loc[data['status'] == 'Buy'].groupby(['zipcode']).sum().reset_index()

    # merge df
    df_prof = pd.merge(df_sum_buy, df_sum_sell, on='zipcode')
    df_prof['profit_diff'] = df_sum_sell['sell_price'] - df_sum_buy['price']

    return df_prof

##############################################################
#   Call Main
##############################################################

if __name__ == "__main__":
    result = ''

    # Set database path
    path = 'kc_house_data_custom.csv'
    data = get_data(path)
    set_zipcode_map(data)

    # Set EDA list question
    list_hypothesis = ['Waterfront houses are 30% more expensive than average?',
                       'House build before 1955 are 50%  more cheap than average?',
                       'Properties without a basement are 50% larger than those with a basement?',
                       'Houses prices growthing 10% Year over Year(YoY)?',
                       'Houses with 3 bathrooms have a 15 % growth of Month over Month(MoM)?',
                       'Whats the TOTAL PROFIT, if sales all houses?',
                       'Whats the Cheapest zipcode and what is the average value?',
                       'Whats the most expensive zipcode and what is the highest value house?'
                       ]
    # Call function (EDA Question)
    v_ret = f_question(list_hypothesis)

    # Set list question
    if v_ret == 'Waterfront houses are 30% more expensive than average?':
        # Select only waterfront houses by zipcode
        aux0 = data[data['waterfront'] == 1].reset_index()
        mean_aux0 = aux0[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
        mean0 = mean_aux0['price'].mean()

        # Select NO waterfront houses by zipcode
        aux1 = data[data['waterfront'] == 0].reset_index()
        mean_aux1 = aux1[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
        mean1 = mean_aux1['price'].mean()

        # Calculate percentage value
        df = pd.DataFrame({'attribute': ['no_waterfront', 'waterfront'], 'mean_value': [mean1, mean0]})
        df['pct'] = df['mean_value'].pct_change()

        # Hypothesis validation
        var = df.loc[1, 'pct'] * 100
        if mean0 > mean1:
            result = 'True'
        else:
            result = 'False'

        # Answer to businesses questions
        business_question = v_ret
        business_answer = '{:}. The waterfront houses has {:.2f}% higher than the average.'.format(result, var)

        # Call print function
        f_business_answer(business_question, business_answer)

        # Call histogram function
        x = 'attribute'
        y = 'mean_value'
        f_plot_histogram(df, x, y)

    elif v_ret == 'House build before 1955 are 50%  more cheap than average?':
        # Mean houses build before 1955
        aux_before1955 = data[['yr_built', 'price']].loc[data['yr_built'] < 1955].groupby(['price']).mean().reset_index()
        mean0 = aux_before1955['price'].mean()

        # Mean houses build after 1955
        aux_after1955 = data[['yr_built', 'price']].loc[data['yr_built'] > 1955].groupby(['price']).mean().reset_index()
        mean1 = aux_after1955['price'].mean()

        # Calculate percentage value
        df = pd.DataFrame({'attribute': ['before_1955', 'after_1955'], 'mean_value': [mean0, mean1]})
        df['pct'] = df['mean_value'].pct_change()

        # Hypothesis validation
        var = df.loc[1, 'pct'] * 100
        if (mean0 < mean1) & (var>= 50):
            result = 'True'
        else:
            result = 'False'

        # Answer to businesses questions
        business_question = v_ret
        business_answer = '{:}. The houses build before 1955 is {:.2f}% cheap than the average.'.format(result, var)

        # Call print function
        f_business_answer(business_question, business_answer)

        # Call Histogram function
        x = 'attribute'
        y = 'mean_value'
        f_plot_histogram(df, x, y)

    elif v_ret == 'Properties without a basement are 50% larger than those with a basement?':
        # Select houses with basement
        aux_basement = data[['sqft_lot', 'sqft_basement']].loc[data['sqft_basement'] != 0].groupby(['sqft_basement']).mean().reset_index()
        mean0 = aux_basement['sqft_lot'].mean()

        # Select houses without basement
        aux_no_basement = data[['sqft_lot', 'sqft_basement']].loc[data['sqft_basement'] == 0].groupby(['sqft_basement']).mean().reset_index()
        mean1 = aux_no_basement['sqft_lot'].mean()

        # Calculate percentage value
        df = pd.DataFrame({'attribute': ['mean_without_basement', 'mean_basement'], 'mean_value': [mean1, mean0]})
        df['pct'] = df['mean_value'].pct_change()

        # Hypothesis validation
        var = df.loc[1, 'pct'] * 100
        if mean0 < mean1:
            result = 'True'
        else:
            result = 'False'

        # Answer to businesses questions
        business_question = v_ret
        business_answer = '{:}. Houses without basement are {:.2f}% bigger than the average.'.format(result, var)

        # Call print function
        f_business_answer(business_question, business_answer)

        # Call Histogram function
        x = 'attribute'
        y = 'mean_value'
        f_plot_histogram(df, x, y)

    elif v_ret == 'Houses prices growthing 10% Year over Year(YoY)?':
        # Calculate the Percentual
        df = data[['year', 'price']].groupby('year').mean().reset_index()
        df = df.rename(columns={'price': 'mean'})
        df['pct'] = df['mean'].pct_change()

        # Hypothesis validation
        var = df.loc[1, 'pct'] * 100
        if var == 0.1:
            result = 'True'
        else:
            result = 'False'

        # Answer to businesses questions
        business_question = v_ret
        business_answer = '{:}. The house price growing {:.2f}%'.format(result, var)

        # Call print function
        f_business_answer(business_question, business_answer)

        # Call Histogram function
        x = 'year'
        y = 'mean'
        f_plot_histogram(df, x, y)

    elif v_ret == 'Houses with 3 bathrooms have a 15 % growth of Month over Month(MoM)?':
        # Calculate the Percentual
        df = data[['price', 'bathrooms', 'month']].loc[data['bathrooms'] == 3].groupby(['month']).mean().reset_index()
        df['pct'] = df['price'].pct_change()

        # Hypothesis validation
        var = df.loc[1, 'pct']*100
        if var == 0.15:
            result = 'True'
        else:
            result = 'False'

        # Answer to businesses questions
        business_question = v_ret
        business_answer = '{:}. The house price growing {:.2f}%'.format(result, var)

        # Call print function
        f_business_answer(business_question, business_answer)

        # Call Histogram function
        x = 'month'
        y = 'pct'
        f_plot_histogram(df, x, y)

    elif v_ret == 'Whats the TOTAL PROFIT, if sales all houses?':
        # Call profit dataframe function
        df = f_df_profit(data)
        var = df['profit_diff'].sum()

        # Answer to business question
        business_question = v_ret
        business_answer = 'If sold all houses, the profit will be U$ {:.2f} . '.format(var)

        # Call print function
        f_business_answer(business_question, business_answer)

    elif v_ret == 'Whats the Cheapest zipcode and what is the average value?':
        # Searching cheap value
        df_condition = data[data['condition'] >= 4]

        df_cheap = df_condition[['price', 'zipcode', 'condition']].sort_values('price', ascending=True)
        zip_cheap = df_cheap.iloc[0, 1]
        price_cheap = df_cheap.iloc[0, 0]

        # Answer to business question
        business_question = v_ret
        business_answer = 'The cheapest zipcode is {:}, with the average value of U$ {:.2f} . '.format(zip_cheap, price_cheap)

        # Call print function
        f_business_answer(business_question, business_answer)

    else:
        # 'What is the most expensive zipcode and what is the highest value house?'
        # Searching Expensive Value
        df_condition = data[data['condition'] >= 4]

        df_expensive = df_condition[['price', 'zipcode', 'condition']].sort_values('price', ascending=False)
        zip_exp = df_expensive.iloc[0, 1]
        price_exp = df_expensive.iloc[0, 0]

        # Answer to business question
        business_question = v_ret
        business_answer = 'The expensive zipcode is {:}, with the average value of U$ {:.2f} . '.format(zip_exp, price_exp)

        # Call print function
        f_business_answer(business_question, business_answer)
