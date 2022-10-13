from mypackage.filter_via_name import filter_character_data_via_name
from mypackage.filter_via_others import filter_character_data


def filtering_data(marvel_df):
    ''' This function is taking the dataframe as parameter and 
        gets the filter conditions from the user and gives the corresponding results '''

    print('Columns in a dataframe:')
    print('1. Character Name')
    print('2. Event Appearances')
    print('3. Series Appearances')
    print('4. Stories Appearances')
    print('5. Comics Appearances')
    print('6. Character ID')
    column = int(input('Enter the column(1-6) to filter on: '))

    column_dict = {1: 'character_name', 2: 'event_appearances', 3: 'series_appearances',
                   4: 'stories_appearances', 5: 'comics_appearances', 6: 'character_id'}

    if column == 1:
        value = input('Enter the character to search for: ')
        marvel_filtered_df = filter_character_data_via_name(
            marvel_df, column_dict[column], value)
    elif column >= 2 and column <= 5:
        print('1. Greater than')
        print('2. Lesser than')
        print('3. Equal to')
        condition = int(input('Enter the condition(1-3): '))
        if condition > 3 or condition < 1:
            marvel_filtered_df = 'Wrong Choice'
        else:
            value = int(input('Enter value: '))
            marvel_filtered_df = filter_character_data(
                marvel_df, column_dict[column], condition, value)
    elif column == 6:
        value = int(input('Enter character id: '))
        marvel_filtered_df = filter_character_data(
            marvel_df, column_dict[column], 3, value)
    else:
        marvel_filtered_df = 'Wrong Choice'

    return marvel_filtered_df
