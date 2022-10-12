import pandas as pd


def calculate_turnover(prices_df: pd.DataFrame):
    categories_to_sum = [
        "departure_truck_freight",
        "departure_fees",
        "freight",
        "arrival_fees",
        "arrival_truck_freight",
        "insurance",
    ]
    prices_df_filtered = prices_df[prices_df["category"].isin(categories_to_sum)]

    # the turnover calculation uses purchase and margin prices coming from the final_check (or from the proposition when
    # at least one purchase or one margin price is missing from the final_check)
    prices_df_filtered.loc[:, "turnover"] = prices_df_filtered.loc[:, "purchase_price_in_eur"
                                            ] + prices_df_filtered.loc[:, "margin_price_in_eur"]

    # the initial turnover calculation uses initial purchase and initial margin prices coming from the proposition
    prices_df_filtered.loc[:, "turnover_initial"] = prices_df_filtered.loc[:, "initial_purchase_price_in_eur"
                                                    ] + prices_df_filtered.loc[:, "initial_margin_price_in_eur"]

    return prices_df_filtered.groupby("shipment_id", as_index=False).agg({"turnover": sum, "turnover_initial": sum})
