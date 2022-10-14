import unittest
from datetime import datetime, timedelta, timezone
from typing import Optional
from unittest import skip

import pandas as pd

from chalk.df.ChalkDataFrameImpl import ChalkDataFrameImpl
from chalk.features import DataFrame, Filter, after, feature_time, features, has_many, has_one
from chalk.features.feature import Filter
from chalk.features.resolver import ResolverAnnotationParser


@features
class ToppingPrice:
    id: str
    topping_id: str
    wow: str
    ts: datetime = feature_time()


@features
class Nickname:
    id: str


@features
class Taco:
    id: str
    user_id: str
    price: int
    maybe_price: Optional[int]
    hat: str
    topping_id: str
    ts: datetime = feature_time()
    nicknames: DataFrame[Nickname] = has_many(lambda: Nickname.id == Taco.id)
    topping: "Topping" = has_one(lambda: Topping.id == Taco.topping_id)


@features
class Topping:
    id: str
    ts: datetime = feature_time()
    nicknames: DataFrame[Nickname] = has_many(lambda: Nickname.id == Topping.id)
    price: ToppingPrice = has_one(lambda: ToppingPrice.topping_id == Topping.id)


class TestDF(unittest.TestCase):
    @skip
    def test_indexing(self):
        # TODO: Make this work
        f = DataFrame.from_dict({Taco.id: [1, 2, 3], Taco.price: [5, 6, 7]})
        self.assertEqual(Taco(id=3, price=7), f[-1])
        self.assertEqual(Taco(id=2, price=6), f[-1])
        self.assertEqual(Taco(id=1, price=5), f[-1])

    def test_range(self):
        f = DataFrame.from_dict({Taco.id: [1, 2, 3]})
        self.assertTrue(f[0:].count() == f.count() == 3)
        self.assertTrue(f[1:].count() == 2)
        self.assertTrue(f[0:1].count() == 1)

    def test_eq(self):
        self.assertEqual(
            DataFrame.from_dict({Taco.id: [1, 1, 3]}),
            DataFrame.from_dict({Taco.id: [1, 1, 3]}),
        )
        self.assertNotEqual(
            DataFrame.from_dict({Taco.id: [1, 1]}),
            DataFrame.from_dict({Taco.id: [1, 1, 3]}),
        )

    def test_mode(self):
        f = DataFrame.from_dict({Taco.id: [1, 1, 3]})
        self.assertTrue(f.mode() == 1)
        self.assertTrue(f[Taco.id != 1].mode() == 3)

    def test_empty(self):
        non_empty = DataFrame.from_dict({Taco.id: [1]})
        self.assertTrue(non_empty.is_not_empty)
        self.assertFalse(non_empty.is_empty)

        for empty in [
            DataFrame.from_dict({Taco.id: []}),
            DataFrame.from_dict({}),
        ]:
            self.assertTrue(empty.is_empty)
            self.assertFalse(empty.is_not_empty)

    def test_in(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.price: [1, 2, 10],
            }
        )
        one_two_three_tacos = chalk_df[Taco.price in (1, 2, 3)]
        assert isinstance(one_two_three_tacos, ChalkDataFrameImpl)
        assert one_two_three_tacos.count() == 2
        assert one_two_three_tacos[Taco.price].max() == 2
        assert one_two_three_tacos[Taco.price].min() == 1
        self.assertEqual(chalk_df[Taco.price in []].count(), 0)
        self.assertEqual(chalk_df[Taco.price in [444]].count(), 0)
        self.assertEqual(chalk_df[Taco.price not in [1, 4]].count(), 2)
        self.assertEqual(chalk_df[not Taco.price in [1]].count(), 2)

    def test_is_none(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.maybe_price: [20, None, 10],
            }
        )
        self.assertEqual(chalk_df[Taco.maybe_price is None].count(), 1)
        self.assertEqual(chalk_df[Taco.maybe_price == None].count(), 1)
        self.assertEqual(chalk_df[Taco.maybe_price is not None].count(), 2)
        self.assertEqual(chalk_df[Taco.maybe_price != None].count(), 2)

    def test_bool_op(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.maybe_price: [20, None, 10],
                Taco.price: [1, 2, 3],
            }
        )
        self.assertEqual(chalk_df[Taco.maybe_price is None or Taco.id == "t_1"].count(), 2)
        self.assertEqual(chalk_df[Taco.maybe_price is None and Taco.id == "t_2"].count(), 1)
        self.assertEqual(
            chalk_df[not (Taco.maybe_price is not None or not Taco.id == "t_2")].count(),
            1,
        )

        self.assertEqual(chalk_df[Taco.maybe_price is None and Taco.id == "t_1"].count(), 0)
        self.assertEqual(
            chalk_df[Taco.maybe_price is not None and (Taco.id == "t_1" or Taco.price == 3)].count(),
            2,
        )
        self.assertEqual(
            chalk_df[Taco.maybe_price is not None and (Taco.id == "t_1" or Taco.price in [8, 4, 99])].count(),
            1,
        )

    def test_after(self):
        now = datetime.now()
        chalk_df = DataFrame.from_dict(
            {
                Taco.ts: pd.Series([now - timedelta(days=10), now], dtype="datetime64[ns, utc]"),
                Taco.price: [5, 10],
            }
        )
        new_price = chalk_df[after(days_ago=5)].sum()
        self.assertEqual(new_price, 10)

    def test_filtering(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.price: [1, 5, 10],
            }
        )
        expensive_tacos = chalk_df[Taco.price > 1]
        self.assertIsInstance(expensive_tacos, ChalkDataFrameImpl)
        self.assertEqual(expensive_tacos.count(), 2)
        with self.assertRaises(ValueError) as e:
            expensive_tacos.max()
        self.assertEqual(
            str(e.exception),
            (
                "Cannot compute max. DataFrame contains 2 features, and expected only one. Filter your "
                "DataFrame down to "
                "the feature for which you want to compute the max before calling .max()."
            ),
        )

        self.assertEqual(expensive_tacos[Taco.price].max(), 10)
        self.assertEqual(expensive_tacos[Taco.price].min(), 5)

    def test_filter_and_project(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.user_id: ["u_1", "u_1", "u_2"],
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.price: [1, 5, 10],
            }
        )
        expensive_tacos = chalk_df[Taco.price, Taco.price > 1, Taco.user_id == "u_1"]
        self.assertIsInstance(expensive_tacos, ChalkDataFrameImpl)
        self.assertEqual(expensive_tacos.count(), 1)
        self.assertEqual(expensive_tacos.max(), 5)
        self.assertEqual(expensive_tacos.min(), 5)

    def test_filter_many(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.user_id: ["u_1", "u_1", "u_2"],
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.price: [1, 5, 10],
            }
        )
        expensive_tacos = chalk_df[Taco.price > 1, Taco.user_id == "u_1"]
        self.assertIsInstance(expensive_tacos, ChalkDataFrameImpl)
        self.assertEqual(expensive_tacos.count(), 1)
        with self.assertRaises(ValueError) as e:
            expensive_tacos.max()
        self.assertEqual(
            str(e.exception),
            (
                "Cannot compute max. DataFrame contains 3 features, and expected only one. Filter your "
                "DataFrame down to "
                "the feature for which you want to compute the max before calling .max()."
            ),
        )

        self.assertEqual(expensive_tacos[Taco.price].max(), 5)
        self.assertEqual(expensive_tacos[Taco.price].min(), 5)

    def test_filtering_with_datetime(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.user_id: ["u_1", "u_1", "u_2"],
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.price: [1, 5, 10],
                Taco.ts: [
                    datetime.now(tz=timezone.utc) - timedelta(days=3),
                    datetime.now(tz=timezone.utc) - timedelta(days=1),
                    datetime.now(tz=timezone.utc),
                ],
            }
        )
        recent_tacos = chalk_df[Taco.ts >= datetime.now(tz=timezone.utc) - timedelta(hours=3)]
        self.assertIsInstance(recent_tacos, ChalkDataFrameImpl)
        self.assertEqual(recent_tacos.count(), 1)
        self.assertEqual(recent_tacos[Taco.price].max(), 10)

    def test_indexing_one(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.price: [100, 200, 300],
            }
        )
        self.assertEqual(chalk_df[Taco.price].mean(), 200)
        self.assertEqual(chalk_df[Taco.price].count(), 3)
        self.assertEqual(chalk_df[Taco.price].max(), 300)
        self.assertEqual(chalk_df[Taco.price].min(), 100)

    def test_indexing_many(self):
        chalk_df = DataFrame.from_dict(
            {
                Taco.id: ["t_1", "t_2", "t_3"],
                Taco.price: [100, 200, 300],
                Taco.hat: ["green", "red", "blue"],
            }
        )
        self.assertTrue(
            chalk_df[Taco.price, Taco.id].underlying.equals(
                pd.DataFrame(
                    {
                        Taco.price: [100, 200, 300],
                        Taco.id: ["t_1", "t_2", "t_3"],
                    }
                )
            )
        )

    def test_input_feature_types(self):
        df = DataFrame.from_dict({Taco.topping.id: ["1"]})
        self.assertEqual(df[Taco.topping.id].iloc[0, 0], "1")

    def test_feature_to_string(self):
        def _check(string: str, feat):
            self.assertEqual(string, str(feat))
            self.assertEqual(string, str(feat))

        # scalar feature
        _check("taco.price", Taco.price)

        # ts feature
        _check("taco.ts", Taco.ts)

        # has-one feature
        _check("taco.topping", Taco.topping)

        # scalar feature has-one
        _check("taco.topping.id", Taco.topping.id)

        # ts feature has-one
        _check("taco.topping.ts", Taco.topping.ts)

        _check("taco.topping.nicknames", Taco.topping.nicknames)

        _check("taco.topping.price.ts", Taco.topping.price.ts)

        # Double has-one
        _check("taco.topping.price.wow", Taco.topping.price.wow)

        _check("taco.nicknames", Taco.nicknames)

    def test_from_dict(self):
        df = DataFrame.from_dict(
            {
                Taco.topping.id: [100, 200],
                Taco.id: [1, 3],
            }
        )
        self.assertEqual(300, df[Taco.topping.id].sum())
        self.assertEqual(4, df[Taco.id].sum())

    def test_to_pandas(self):
        df = DataFrame.from_dict(
            {
                Taco.topping.id: [100, 200],
            }
        )
        pds = df.to_pandas()
        self.assertEqual(300, pds[Taco.topping.id].sum())

    def test_from_list(self):
        self.assertEqual(0, DataFrame.from_list().count())
        self.assertEqual(0, DataFrame.from_list([]).count())
        self.assertEqual(1, DataFrame.from_list(Taco(price=123, user_id="33")).count())
        self.assertEqual(1, DataFrame.from_list([Taco(price=123, user_id="33")]).count())
        self.assertEqual(
            2,
            DataFrame.from_list(Taco(price=123, user_id="33"), Taco(price=3, user_id="33")).count(),
        )
        self.assertEqual(
            2,
            DataFrame.from_list([Taco(price=123, user_id="33"), Taco(price=3, user_id="33")]).count(),
        )
        with self.assertRaises(ValueError):
            DataFrame.from_list(Taco(price=123, user_id="33"), Taco(price=3))

        with self.assertRaises(ValueError):
            DataFrame.from_list(Taco(), Taco(price=3, user_id="33"))

    def test_ast_parsing(self):
        container = {1, 2, 3}

        def my_resolver(
            my_arg: DataFrame[
                Taco.price,
                Taco.user_id > "33",
                Taco.maybe_price is not None,
                Taco.maybe_price is None,
                Taco.price not in container,
                Taco.price in container or (Taco.topping.price == -3 and (Taco.hat == "cool" or Taco.price == 4)),
            ]
        ):
            ...

        fancy_index = ResolverAnnotationParser(my_resolver, globals(), locals()).parse_annotation("my_arg")
        assert issubclass(fancy_index, DataFrame)

        self.assertEqual(">", fancy_index.filters[0].operation)
        self.assertEqual("taco.user_id", str(fancy_index.filters[0].lhs))
        self.assertEqual("33", fancy_index.filters[0].rhs)

        self.assertEqual("!=", fancy_index.filters[1].operation)
        self.assertEqual("taco.maybe_price", str(fancy_index.filters[1].lhs))
        self.assertEqual(None, fancy_index.filters[1].rhs)

        self.assertEqual("==", fancy_index.filters[2].operation)
        self.assertEqual("taco.maybe_price", str(fancy_index.filters[2].lhs))
        self.assertEqual(None, fancy_index.filters[2].rhs)

        self.assertEqual("not in", fancy_index.filters[3].operation)
        self.assertEqual("taco.price", str(fancy_index.filters[3].lhs))
        self.assertEqual(container, fancy_index.filters[3].rhs)

        fancy_clause = fancy_index.filters[4]
        assert isinstance(fancy_clause, Filter)
        first_fancy = fancy_clause.lhs
        assert isinstance(first_fancy, Filter)
        self.assertEqual("in", first_fancy.operation)
        self.assertEqual("taco.price", str(first_fancy.lhs))
        self.assertEqual(container, first_fancy.rhs)

        self.assertEqual("or", fancy_clause.operation)
