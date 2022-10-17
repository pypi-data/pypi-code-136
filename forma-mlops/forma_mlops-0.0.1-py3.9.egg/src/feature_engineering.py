import numpy as np
import pandas as pd
from typing import Tuple


def names(train: pd.DataFrame, test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Creates two separate columns: a numeric column indicating the length of a
    passenger's Name field, and a categorical column that extracts the
    passenger's title.

    Args:
        train: The train set
        test: The test set

     Returns:
        new_train
        new_test

    """
    for i in [train, test]:
        i['Name_Len'] = i['Name'].apply(lambda x: len(x))
        i['Name_Title'] = i['Name'].apply(lambda x: x.split(',')[1]).apply(lambda x: x.split()[0])
        del i['Name']
    return train, test


def age_impute(train: pd.DataFrame, test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Imputes the null values of the Age column by filling in the mean value of
    the passenger's corresponding title and class.

    Args:
        train: The train set
        test: The test set

     Returns:
        new_train
        new_test

    """
    for i in [train, test]:
        i['Age_Null_Flag'] = i['Age'].apply(lambda x: 1 if pd.isnull(x) else 0)
        data = train.groupby(['Name_Title', 'Pclass'])['Age']
        i['Age'] = data.transform(lambda x: x.fillna(x.mean()))
    return train, test


def fam_size(train: pd.DataFrame, test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Combines the SibSp and Parch columns into a new variable that indicates
    family size, and group the family size variable into three categories.

    Args:
        train: The train set
        test: The test set

     Returns:
        new_train
        new_test

    """
    for i in [train, test]:
        i['Fam_Size'] = np.where((i['SibSp'] + i['Parch']) == 0, 'Solo',
                                 np.where((i['SibSp'] + i['Parch']) <= 3, 'Nuclear', 'Big'))
        del i['SibSp']
        del i['Parch']
    return train, test


def ticket_grouped(train: pd.DataFrame, test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    The Ticket column is used to create two new columns: Ticket_Lett, which
    indicates the first letter of each ticket (with the smaller-n values being
    grouped based on survival rate); and Ticket_Len, which indicates the length
    of the Ticket field.

    Args:
        train: The train set
        test: The test set

    Returns:
        new_train
        new_test

    """
    for i in [train, test]:
        i['Ticket_Lett'] = i['Ticket'].apply(lambda x: str(x)[0])
        i['Ticket_Lett'] = i['Ticket_Lett'].apply(lambda x: str(x))
        i['Ticket_Lett'] = np.where((i['Ticket_Lett']).isin(['1', '2', '3', 'S', 'P', 'C', 'A']), i['Ticket_Lett'],
                                    np.where((i['Ticket_Lett']).isin(['W', '4', '7', '6', 'L', '5', '8']),
                                             'Low_ticket', 'Other_ticket'))
        i['Ticket_Len'] = i['Ticket'].apply(lambda x: len(x))
        del i['Ticket']
    return train, test


def cabin(train: pd.DataFrame, test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Extracts the first letter of the Cabin column

    Args:
        train: The train set
        test: The test set

    Returns:
        new_train
        new_test

    """
    for i in [train, test]:
        i['Cabin_Letter'] = i['Cabin'].apply(lambda x: str(x)[0])
        del i['Cabin']
    return train, test


def cabin_num(train: pd.DataFrame, test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Extracts the number of the Cabin column

    Args:
        train: The train set
        test: The test set

    Returns:
        new_train
        new_test

    """
    for i in [train, test]:
        i['Cabin_num1'] = i['Cabin'].apply(lambda x: str(x).split(' ')[-1][1:])
        i['Cabin_num1'].replace('an', np.NaN, inplace=True)
        i['Cabin_num1'] = i['Cabin_num1'].apply(lambda x: int(x) if not pd.isnull(x) and x != '' else np.NaN)
        i['Cabin_num'] = pd.qcut(train['Cabin_num1'], 3)
    train = pd.concat((train, pd.get_dummies(train['Cabin_num'], prefix='Cabin_num')), axis=1)
    test = pd.concat((test, pd.get_dummies(test['Cabin_num'], prefix='Cabin_num')), axis=1)
    del train['Cabin_num']
    del test['Cabin_num']
    del train['Cabin_num1']
    del test['Cabin_num1']
    return train, test


def embarked_impute(train: pd.DataFrame, test: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Fills the null values in the Embarked column with the most commonly
    occuring value, which is 'S.'

    Args:
        train: The train set
        test: The test set

    Returns:
        new_train
        new_test

    """
    for i in [train, test]:
        i['Embarked'] = i['Embarked'].fillna('S')
    return train, test


def dummies(train: pd.DataFrame, test: pd.DataFrame, columns: list) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Converts our categorical columns into dummy variables, and then drops the
    original categorical columns. It also makes sure that each category is
    present in both the training and test datasets.

    Args:
        train: The train set
        test: The test set
        columns: The columns to be dummified. If None is passed,
            default values are applied.

    Returns:
        new_train
        new_test

    """
    for column in columns:
        train[column] = train[column].apply(lambda x: str(x))
        test[column] = test[column].apply(lambda x: str(x))
        good_cols = [column + '_' + i for i in train[column].unique() if i in test[column].unique()]
        train = pd.concat((train, pd.get_dummies(train[column], prefix=column)[good_cols]), axis=1)
        test = pd.concat((test, pd.get_dummies(test[column], prefix=column)[good_cols]), axis=1)
        del train[column]
        del test[column]
    return train, test


def drop(train: pd.DataFrame, test: pd.DataFrame, bye: list) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Drops any columns that haven't already been dropped

    Args:
        train: The train set
        test: The test set
        bye: The columns to be dropped. If None, default is ['PassengerId'].

    Returns:
        new_train
        new_test

    """
    for i in [train, test]:
        for z in bye:
            del i[z]
    return train, test
