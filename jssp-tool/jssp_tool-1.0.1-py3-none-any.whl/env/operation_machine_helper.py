import numpy as np


OP_STATUS_NOT_SCHEDULED = "not_scheduled"
OP_STATUS_READY = "ready"
OP_STATUS_PROCESSING = "processing"
OP_STATUS_DONE = "done"


class Operation:
    def __init__(
        self,
        op_id,
        job_id,
        machine_id,
        processing_time,
        job_processing_time,
        pre_op=None,
        start_time=None,
        end_time=None,
    ):
        """
        Args:
            op_id: operation id
            pre_op: 前一个operation
            processing_time: operation的处理时间
            job_processing_time: operation对应job的处理时间
            machine_id:
        """
        self.id = op_id
        self.job_id = job_id
        self.machine_id = machine_id
        self.pre_op = pre_op
        self.job_processing_time = job_processing_time

        self.node_status = OP_STATUS_NOT_SCHEDULED
        self.processing_time = processing_time  # 定值
        # 开始加工时间
        self.start_time = start_time
        # 结束加工时间
        self.end_time = end_time

    def set_start_end_time(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def to_array(self, n_m) -> np.ndarray:
        pass


class Machine:
    def __init__(self, machine_id, ops):
        self.id = machine_id
        # 该机器上未被机器调度的op
        self.unscheduled_ops = ops
        # 即action space，可以作为调度选项的ops：Job维度上pre_op为空，或者pre_op已加工完成或者正在加工 （即从unscheduled_ops去掉pre_op也未调度的op）
        self.ready_ops = []
        # 已进入该机器调度的op（正在加工或者已被选中等待加工）。
        self.processing_ops = []
        self.done_ops = []
        # 记录机器是否处理完所有的op
        self.done = False

    def available(self):
        return len(self.processing_ops) == 0
