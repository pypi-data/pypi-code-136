# Look into model recommendation I (AutoML as well)

## Recommend which models to use for training


def recommend_model(dataset):
    """Recommend which models to use for training"""
    THRESHOLD = 0.01
    for column in dataset.columns:
        if "label" in column:
            if isinstance(column, str):
                return {"recommended_model": "classification"}
                break
            else:
                num_unique_values = len(dataset[column].unique())
                threshold = 0.01  # can be changed
                num_rows = len(dataset[column])

                if num_unique_values / num_rows < threshold:
                    return {"recommended_model": "classification"}
                else:
                    return {"recommended_model": "regression"}
