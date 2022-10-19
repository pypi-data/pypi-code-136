from pandas import DataFrame

from ingestor.user_profile.preferences.generate_preferences import PreferenceGenerator
from ingestor.user_profile.preprocessing.behaviour import PreprocessBehaviour
from ingestor.utils import class_custom_exception


class MainImplementation:
    def __init__(self, df: DataFrame):
        """
        :param df: Dataframe object pandas
        """
        self.df = df

    @class_custom_exception()
    def controller(
        self,
        resource=None,
        bucket_name=None,
        object_name=None,
        feature: str = None,
        value: str = None,
    ) -> DataFrame:
        """
        Driver method for class MainImplementation which produces
        final_merged_df after complete preprocessing and
        preferences generation for user profile part.
        :return: preprocessed and user preference dataframe object pandas
        """

        behaviour = PreprocessBehaviour()
        pref = PreferenceGenerator(feature=feature, feature_cutoff=2, user_cutoff=2)
        print("Preprocessing for feature ---> ", feature)
        temp = behaviour.controller(
            data=self.df, to_explode=True, feature=feature, key=value
        )
        print("Successfully preprocessed.....")
        print("Generating User Preferences for the feature ---> ", feature)
        temp = pref.controller(
            data=temp,
            resource=resource,
            bucket_name=bucket_name,
            object_name=object_name,
        )

        return temp
