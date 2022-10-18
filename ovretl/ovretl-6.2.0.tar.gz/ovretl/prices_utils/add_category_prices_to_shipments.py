from ovretl.prices_utils.sum_multiple_billings_prices import sum_multiple_billings_prices
import pandas as pd


def add_initial_category_prices_to_shipments(
    shipments_with_prices: pd.DataFrame, prices_propositions_by_category_df: pd.DataFrame,
) -> pd.DataFrame:
    initial_prices = (
        prices_propositions_by_category_df.dropna(
            subset=["purchase_price_in_eur", "price_in_eur", "margin_price_in_eur"],
            how="all").rename(columns={"purchase_price_in_eur": "initial_purchase_price_in_eur",
                                       "price_in_eur": "initial_price_in_eur",
                                       "margin_price_in_eur": "initial_margin_price_in_eur",
                                       "proposition_id": "initial_proposition_id",
                                       }
                              )
    )

    shipments_with_prices = pd.merge(
        shipments_with_prices,
        initial_prices[
            [
                "initial_proposition_id",
                "category",
                "initial_margin_price_in_eur",
                "initial_price_in_eur",
                "initial_purchase_price_in_eur",
            ]
        ],
        on=("initial_proposition_id", "category"),
        how="left",
    )
    return shipments_with_prices


def add_category_prices_to_shipments(
    shipments_with_prices_ids: pd.Series,
    prices_final_check_by_category_df: pd.DataFrame,
    prices_billings_by_category_df: pd.DataFrame,
    prices_propositions_by_category_df: pd.DataFrame,
) -> pd.DataFrame:
    shipments_with_prices_billings_ids = shipments_with_prices_ids[[
        'shipment_id', 'foresea_name', 'billing_id']].drop_duplicates(subset=['billing_id'])
    shipments_with_prices_billings = pd.merge(
        shipments_with_prices_billings_ids,
        prices_billings_by_category_df.dropna(subset=["price_in_eur"], how="all"),
        on="billing_id",
        how="inner",
    )
    shipments_with_prices_final_check_ids = shipments_with_prices_ids[[
        'shipment_id', 'foresea_name', 'final_check_id', 'initial_proposition_id']].drop_duplicates(
        subset=['final_check_id'])
    shipments_with_prices_final_check = pd.merge(
        shipments_with_prices_final_check_ids,
        prices_final_check_by_category_df.dropna(subset=["margin_price_in_eur", "purchase_price_in_eur"], how="all"),
        on="final_check_id",
        how="inner",
    )
    shipments_with_prices = pd.concat([shipments_with_prices_billings, shipments_with_prices_final_check])
    if len(shipments_with_prices_final_check[(shipments_with_prices_final_check["margin_price_in_eur"].isnull()) | (
            shipments_with_prices_final_check["purchase_price_in_eur"].isnull())]) > 0:
        shipments_with_prices_propositions_ids = shipments_with_prices_ids[[
            'shipment_id', 'foresea_name', 'proposition_id']].drop_duplicates(subset=['proposition_id'])
        shipments_with_prices_propositions = pd.merge(
            shipments_with_prices_propositions_ids,
            prices_propositions_by_category_df[['category',
                                                'prices_origin',
                                                'proposition_id',
                                                'margin_price_in_eur',
                                                'purchase_price_in_eur']].dropna(
                subset=["margin_price_in_eur", "purchase_price_in_eur"], how="all"),
            on="proposition_id",
            how="inner",
        )
        shipments_with_prices = pd.concat([shipments_with_prices, shipments_with_prices_propositions])
    shipments_with_prices = add_initial_category_prices_to_shipments(
        shipments_with_prices=shipments_with_prices,
        prices_propositions_by_category_df=prices_propositions_by_category_df,
    )
    return sum_multiple_billings_prices(shipments_with_prices=shipments_with_prices)
