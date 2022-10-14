import numpy as np


class AHPWeight:
    def __init__(self, ahp_weight):
        self.ahp_weight = ahp_weight

    def algorithm_ahp_scale(self, list_scale):
        def reciprocal(num):
            return [1. / np.array(abs(num))]

        dict_distance = {}
        # list_scale = [1, 2, -3, -4]
        list_array = []
        list_A_arr = []
        for i in list_scale:
            if i < 1:
                list_array.append(reciprocal(i)[0])
            else:
                list_array.append(i)
        # print(list_array)
        list_A_arr.append(list_array)

        for y in range(len(list_scale)):
            if y == 0:
                dict_distance[y] = list_array
            else:
                one_list = []
                for x in range(len(list_scale)):
                    # ====================正級距======================
                    if x == 0:
                        record = reciprocal(list_array[y])[0]
                        one_list.append(record)

                    if x != 0 and list_scale[y] > list_scale[x] and list_scale[x] > 0 and list_scale[y] > 0:
                        one_list.append(list_scale[x] / list_scale[y])
                    elif x != 0 and list_scale[y] == list_scale[x]:
                        one_list.append(1)
                    elif x != 0 and list_scale[y] < list_scale[x] and list_scale[y] > 0:
                        one_list.append(list_array[x] / list_array[y])
                    # y是正的，比較級距是負的
                    elif x != 0 and list_scale[y] > list_scale[x] and list_scale[x] < 0 and list_scale[y] > 0:
                        one_list.append(1 / (list_scale[y] - list_scale[x] + 1))

                    # ====================負級距======================
                    elif x != 0 and list_scale[y] > list_scale[x] and list_scale[y] < 0:
                        one_list.append((1 / list_scale[x]) / (1 / list_scale[y]))

                    elif x != 0 and list_scale[y] < list_scale[x] and list_scale[x] < 0 and list_scale[y] < 0:
                        one_list.append((1 / list_scale[x]) / (1 / list_scale[y]))

                    elif x != 0 and list_scale[y] < list_scale[x] and list_scale[x] > 0 and list_scale[y] < 0:
                        one_list.append(list_scale[x] - list_scale[y] + 1)

                list_A_arr.append(one_list)
        return list_A_arr

    def algorithm_ahp(self, A_arr):
        # 矩阵
        A = np.array(A_arr)
        a_sum0 = A.sum(axis=0)
        B = A / a_sum0
        b_sum = B.sum(axis=1)
        W = b_sum.sum()
        w_arr = []
        for w in b_sum:
            w_arr.append(w / W)
        return w_arr

    def output_weight(self):
        model_list, weight_list = list(self.ahp_weight.keys()), list(self.ahp_weight.values())
        idx = weight_list.index(1)

        weight_list[idx], weight_list[0] = weight_list[0], weight_list[idx]
        model_list[idx], model_list[0] = model_list[0], model_list[idx]
        ahp_weight = dict(zip(model_list, weight_list))

        list_scale = self.algorithm_ahp(self.algorithm_ahp_scale(weight_list))
        for i, (k, _) in enumerate(ahp_weight.items()):
            ahp_weight[k] = round(list_scale[i], 6)
        return ahp_weight




if __name__ == '__main__':
    ahp_weight = {
        "robot_detection_score": 1,
        "ip_connection_score": 2,
        "internet_info_score": 2,
        "ip_change_score": 3,
        "device_consistency_score": 4,
        "device_connection_score": 5,
        "personal_device_score": 6,
        "bio_behavior_score": 7
    }
    ahpw = AHPWeight(ahp_weight)
    dict_weight = ahpw.output_weight()
    dict_weight
