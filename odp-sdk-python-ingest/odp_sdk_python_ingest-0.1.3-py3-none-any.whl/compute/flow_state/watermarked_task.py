from functools import update_wrapper

from prefect import Task
import inspect
from .watermark_store import WatermarkStore, get_watermark_store
from .watermark import Watermark

from typing import Any, cast, Callable, Optional, Union


class WatermarkedFunctionTask(Task):
    """Task reflecting prefect's built-in FunctionTask, but with flow_state support

    Enables users to add arguments with "_watermark"-postfix, that will be populated
    at call-time
    """

    WATERMARK_ARG_POSTFIX = "_watermark"
    WATERMARK_STORE_ARG_NAME = "store"

    def __init__(
        self,
        fn: Callable,
        watermark_store: Optional[WatermarkStore] = None,
        name: Optional[str] = None,
        **kwargs: Any,
    ):
        """
        Args:
            fn: Function callback
            watermark_store: Watermark store/client
            name:  Function name
            **kwargs: Task kwargs
        """
        if not callable(fn):
            raise TypeError("`fn` must be callable")
        if name is None:
            name = getattr(fn, "__name__", type(self).__name__)

        self.watermark_store = watermark_store
        self.fn = fn

        self._watermark_args = None
        self._provide_store = False
        self._fn_signature = None

        self._prepare_watermarks()

        update_wrapper(self, fn)
        super().__init__(name=cast(str, name), **kwargs)

    def _prepare_watermarks(self):
        """Prepare flow_state by reading function signature and store what arguments
        are flow_state-arguments (has "_watermark"-postfix")
        """

        self._fn_signature = inspect.signature(self.fn)
        watermarked_args = []

        for arg in self._fn_signature.parameters:

            if arg.endswith(self.WATERMARK_ARG_POSTFIX):
                watermarked_args.append(arg)
            elif arg == self.WATERMARK_STORE_ARG_NAME:
                self._provide_store = True

        self._watermark_args = watermarked_args

    def run(self, **kwargs) -> Any:

        watermark_store = self.watermark_store or get_watermark_store()

        for watermark_arg in self._watermark_args:  # type: ignore

            # Remove flow_state argument postfix
            argname = watermark_arg[: -len(self.WATERMARK_ARG_POSTFIX)]

            parameter = self._fn_signature.parameters.get(argname)  # type: ignore
            if parameter:
                default_value = parameter.default
                if default_value is inspect.Parameter.empty:
                    default_value = None
            else:
                default_value = None

            # Read flow_state
            watermark_obj = Watermark(
                key=self.watermark_key_prefix(argname),
                value=kwargs.get(argname, default_value),
                store=watermark_store,
            )

            # Update kwarg
            if kwargs.get(watermark_arg) is not None:
                raise UserWarning(f"Overwriting flow_state argument '{watermark_arg}'")
            kwargs[watermark_arg] = watermark_obj

        if self._provide_store:
            local_store = kwargs.get("store")

            if local_store and not isinstance(local_store, WatermarkStore):
                raise UserWarning("Input argument overwrites reserved argument 'store'")
            kwargs["store"] = self.watermark_store

        return self.fn(**kwargs)

    @staticmethod
    def watermark_key_prefix(key) -> str:
        """Convenience-function returning a key prefixed with flow name and task name

        Args:
            key: Key to be prefixed

        Returns:
            Prefixed key
        """
        flow_id = context.get("flow_name")
        task_id = context.get("task_name")

        return f"{flow_id}:{task_id}:{key}"


def watermarked_task(
    fn: Callable = None, **task_init_kwargs: Any
) -> Union[WatermarkedFunctionTask, Callable[[Callable], WatermarkedFunctionTask]]:
    """Decorator reflecting prefect.task, but with flow_state-support

    Args:
        fn: Function callback
        **task_init_kwargs:  Task init-args

    Returns:
        WatermarkedFunctionTask
    """
    if fn is None:
        return lambda fn: WatermarkedFunctionTask(
            fn=fn,
            **task_init_kwargs,
        )
    return WatermarkedFunctionTask(fn, **task_init_kwargs)
