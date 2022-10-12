import dash


def which_fired() -> str:
    """Define witch inputs is fired.

    Returns:
        input_name: Python `str`.
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        input_name = None
    else:
        input_name = ctx.triggered[0]["prop_id"].split(".")[0]

    return input_name


class GlobalData:
    data = {}

    @staticmethod
    def clear_all(exception=[]):
        GlobalData.data = {key: GlobalData.data[key] for key in exception if key in GlobalData.data}
        gc.collect()

    @staticmethod
    def store(data, key, to_list=False, to_dict=False):
        if to_dict and to_list:
            print("Do not select both to_list and to_dict, leave without storing!")
        elif to_list:
            GlobalData.data[key] = (
                [*GlobalData.data[key], data] if key in GlobalData.data else [data]
            )
        elif to_dict:
            GlobalData.data[key] = (
                {**GlobalData.data[key], **data} if key in GlobalData.data else data
            )
        else:
            GlobalData.data[key] = data

    @staticmethod
    def access(key):
        try:
            return GlobalData.data[key]
        except KeyError:
            return None
