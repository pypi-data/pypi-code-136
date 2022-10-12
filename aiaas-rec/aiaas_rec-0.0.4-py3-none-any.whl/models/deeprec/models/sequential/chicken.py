# Copyright (c) Ingka IKEA. All rights reserved.
# Licensed under the MIT License.

import pandas as pd
import numpy as np
import random
from typing import List
from aiaas_rec.models.deeprec.models.sequential.sli_rec import (
    SLI_RECModel,
)
from aiaas_rec.utils.instance import Instance

__all__ = ["ChickenModel"]


class ChickenModel(SLI_RECModel):
    """Chicken model

    :Citation:

    """

    def create_auxiliary_data(self, instance_file):
        df_data = pd.read_csv(instance_file, sep='\t')
        items_with_popular = list(df_data.sku)
        item2cate = dict(zip(df_data.sku, df_data.hfb_no))
        return items_with_popular, item2cate

    def set_auxiliary_data(self, instance_file):
        (self.items_with_popular, self.item2cate) = self.create_auxiliary_data(instance_file)

    def predict_scores(self, instance: Instance, neg_nums: int, n: int):
        def sample(instance: Instance, neg_nums: int):
            res = []
            words = str(instance).strip().split("\t")
            positive_item = words[2]
            count = 0
            neg_items = set()
            while count < neg_nums:
                neg_item = random.choice(self.items_with_popular)
                if neg_item == positive_item or neg_item in neg_items:
                    continue
                count += 1
                neg_items.add(neg_item)
                words[0] = "0"
                words[2] = str(neg_item)
                words[3] = str(self.item2cate[neg_item])
                neg_inst = Instance(*words)
                res.append(neg_inst)
            return res

        samples = sample(instance, neg_nums)
        scores = self._predict_scores(samples)[0]
        flat_scores = np.array([item for sublist in scores for item in sublist])
        ind = np.argpartition(flat_scores, -n)[-n:]
        top_n_rec = ind[np.argsort(flat_scores[ind])][::-1]
        return dict(zip([samples[i].items for i in top_n_rec], [round(flat_scores[i], 6) for i in top_n_rec]))

    def _predict_scores(self, instances: List[Instance]):
        """
        Instance consists of:
            label: str,
            user_id: str,
            item_id: str,
            category_id: str,
            timestamp: str,
            history_item_ids: str,
            history_category_ids: str,
            history_timestamp: str
        """
        # input_line = ['\t'.join([label, user_id, item_id, category_id, timestamp,
        #                    history_item_ids, history_category_ids, history_timestamp])]
        # input_line = [str(instances[0])]
        input_line = [str(i) for i in instances]

        # suppose to load from one element Generator
        # the last (the only) line's result would be the output
        for batch_data_input in self.iterator.load_data_from_file(None, batch_num_ngs=0, inlines=input_line):
            if batch_data_input:
                pred = self.infer(self.sess, batch_data_input)
        return pred
