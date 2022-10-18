import pandas as pd


def pivot_category_all_prices(prices_df):
    # for the category price, we take the purchase + margin price from final_check || proposition instead of the billing
    # price
    prices_df["price_in_eur"] = prices_df.apply(lambda x: x["purchase_price_in_eur"] + x["margin_price_in_eur"], axis=1)
    prices_df = pd.pivot_table(
        prices_df,
        index=["shipment_id"],
        columns=["category"],
        values=["price_in_eur", "initial_price_in_eur", "purchase_price_in_eur", "initial_purchase_price_in_eur"],
    )
    prices_df.columns = ["_".join(col).strip() for col in prices_df.columns.values]
    prices_df = prices_df.rename(
        columns={
            "price_in_eur_arrival_fees": "arrival_fees_price",
            "price_in_eur_arrival_truck_freight": "arrival_truck_freight_price",
            "price_in_eur_customs": "customs_price",
            "price_in_eur_departure_fees": "departure_fees_price",
            "price_in_eur_departure_truck_freight": "departure_truck_freight_price",
            "price_in_eur_freight": "freight_price",
            "price_in_eur_insurance": "insurance_price",
            "price_in_eur_other": "other_price",
            "initial_price_in_eur_arrival_fees": "arrival_fees_initial_price",
            "initial_price_in_eur_arrival_truck_freight": "arrival_truck_freight_initial_price",
            "initial_price_in_eur_departure_fees": "departure_fees_initial_price",
            "initial_price_in_eur_departure_truck_freight": "departure_truck_freight_initial_price",
            "initial_price_in_eur_freight": "freight_initial_price",
            "initial_price_in_eur_insurance": "insurance_initial_price",
            "purchase_price_in_eur_arrival_fees": "arrival_fees_purchase_price",
            "purchase_price_in_eur_arrival_truck_freight": "arrival_truck_freight_purchase_price",
            "purchase_price_in_eur_departure_fees": "departure_fees_purchase_price",
            "purchase_price_in_eur_departure_truck_freight": "departure_truck_freight_purchase_price",
            "purchase_price_in_eur_freight": "freight_purchase_price",
            "purchase_price_in_eur_insurance": "insurance_purchase_price",
            "initial_purchase_price_in_eur_arrival_fees": "arrival_fees_initial_purchase_price",
            "initial_purchase_price_in_eur_arrival_truck_freight": "arrival_truck_freight_initial_purchase_price",
            "initial_purchase_price_in_eur_departure_fees": "departure_fees_initial_purchase_price",
            "initial_purchase_price_in_eur_departure_truck_freight": "departure_truck_freight_initial_purchase_price",
            "initial_purchase_price_in_eur_freight": "freight_initial_purchase_price",
            "initial_purchase_price_in_eur_insurance": "insurance_initial_purchase_price",
        }
    )
    return prices_df.drop(
        [
            "initial_price_in_eur_customs",
            "initial_price_in_eur_other",
            "purchase_price_in_eur_customs",
            "purchase_price_in_eur_other",
        ],
        axis=1,
    )


def pivot_category_main_prices(prices_df):
    # for the category price, we take the purchase + margin price from final_check || proposition instead of the billing
    # price
    prices_df["price_in_eur"] = prices_df.apply(lambda x: x["purchase_price_in_eur"] + x["margin_price_in_eur"], axis=1)
    prices_df = pd.pivot_table(
        prices_df,
        index=["shipment_id"],
        columns=["category"],
        values=["price_in_eur", "initial_price_in_eur", "purchase_price_in_eur", "initial_purchase_price_in_eur"],
    )
    prices_df.columns = ["_".join(col).strip() for col in prices_df.columns.values]
    prices_df = prices_df.rename(
        columns={
            "price_in_eur_arrival_truck_freight": "arrival_truck_freight_main_price",
            "price_in_eur_departure_truck_freight": "departure_truck_freight_main_price",
            "initial_price_in_eur_arrival_truck_freight": "arrival_truck_freight_initial_main_price",
            "initial_price_in_eur_departure_truck_freight": "departure_truck_freight_initial_main_price",
            "purchase_price_in_eur_arrival_truck_freight": "arrival_truck_freight_purchase_main_price",
            "purchase_price_in_eur_departure_truck_freight": "departure_truck_freight_purchase_main_price",
            "initial_purchase_price_in_eur_arrival_truck_freight": "arrival_truck_freight_initial_purchase_main_price",
            "initial_purchase_price_in_eur_departure_truck_freight":
                "departure_truck_freight_initial_purchase_main_price",
        }
    )
    return prices_df
