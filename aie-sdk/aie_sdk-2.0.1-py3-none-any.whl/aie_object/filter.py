#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import abc
import inspect
from typing import Union

import aie
from aie.variable_node import VariableNode
from aie.function_node import FunctionNode
from aie.customfunction_node import CustomFunctionNode
from aie.function_helper import FunctionHelper
from aie.error.aie_error import AIEError, AIEErrorCode


class Filter(FunctionNode):
    @staticmethod
    def date(start: str, end: str = None) -> aie.Filter:

        if start is not None and not isinstance(start, str):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"start 只支持str类型参数, 传入类型为{type(start)}"
            )

        if end is not None and not isinstance(end, str):
            raise AIEError(AIEErrorCode.ARGS_ERROR, f"end 只支持str类型参数, 传入类型为{type(end)}")

        invoke_args = {
            "start": start,
            "end": end,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "start" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数start不能为空")

        return FunctionHelper.apply("Filter.date", "aie.Filter", invoke_args)

    @staticmethod
    def bounds(geometry: aie.Geometry) -> aie.Filter:

        if geometry is not None and not isinstance(geometry, aie.Geometry):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR,
                f"geometry 只支持aie.Geometry类型参数, 传入类型为{type(geometry)}",
            )

        invoke_args = {
            "geometry": geometry,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "geometry" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数geometry不能为空")

        return FunctionHelper.apply("Filter.bounds", "aie.Filter", invoke_args)

    @staticmethod
    def eq(name: str, value: object) -> aie.Filter:

        if name is not None and not isinstance(name, str):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"name 只支持str类型参数, 传入类型为{type(name)}"
            )

        if value is not None and not isinstance(value, object):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"value 只支持object类型参数, 传入类型为{type(value)}"
            )

        invoke_args = {
            "name": name,
            "value": value,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "name" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数name不能为空")

        if "value" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数value不能为空")

        return FunctionHelper.apply("Filter.eq", "aie.Filter", invoke_args)

    @staticmethod
    def gt(name: str, value: object) -> aie.Filter:

        if name is not None and not isinstance(name, str):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"name 只支持str类型参数, 传入类型为{type(name)}"
            )

        if value is not None and not isinstance(value, object):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"value 只支持object类型参数, 传入类型为{type(value)}"
            )

        invoke_args = {
            "name": name,
            "value": value,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "name" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数name不能为空")

        if "value" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数value不能为空")

        return FunctionHelper.apply("Filter.gt", "aie.Filter", invoke_args)

    @staticmethod
    def gte(name: str, value: object) -> aie.Filter:

        if name is not None and not isinstance(name, str):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"name 只支持str类型参数, 传入类型为{type(name)}"
            )

        if value is not None and not isinstance(value, object):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"value 只支持object类型参数, 传入类型为{type(value)}"
            )

        invoke_args = {
            "name": name,
            "value": value,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "name" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数name不能为空")

        if "value" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数value不能为空")

        return FunctionHelper.apply("Filter.gte", "aie.Filter", invoke_args)

    @staticmethod
    def lt(name: str, value: object) -> aie.Filter:

        if name is not None and not isinstance(name, str):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"name 只支持str类型参数, 传入类型为{type(name)}"
            )

        if value is not None and not isinstance(value, object):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"value 只支持object类型参数, 传入类型为{type(value)}"
            )

        invoke_args = {
            "name": name,
            "value": value,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "name" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数name不能为空")

        if "value" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数value不能为空")

        return FunctionHelper.apply("Filter.lt", "aie.Filter", invoke_args)

    @staticmethod
    def lte(name: str, value: object) -> aie.Filter:

        if name is not None and not isinstance(name, str):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"name 只支持str类型参数, 传入类型为{type(name)}"
            )

        if value is not None and not isinstance(value, object):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"value 只支持object类型参数, 传入类型为{type(value)}"
            )

        invoke_args = {
            "name": name,
            "value": value,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "name" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数name不能为空")

        if "value" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数value不能为空")

        return FunctionHelper.apply("Filter.lte", "aie.Filter", invoke_args)

    @staticmethod
    def neq(name: str, value: object) -> aie.Filter:

        if name is not None and not isinstance(name, str):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"name 只支持str类型参数, 传入类型为{type(name)}"
            )

        if value is not None and not isinstance(value, object):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"value 只支持object类型参数, 传入类型为{type(value)}"
            )

        invoke_args = {
            "name": name,
            "value": value,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "name" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数name不能为空")

        if "value" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数value不能为空")

        return FunctionHelper.apply("Filter.neq", "aie.Filter", invoke_args)

    @staticmethod
    def And(filters: list) -> aie.Filter:

        if filters is not None and not isinstance(filters, list):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"filters 只支持list类型参数, 传入类型为{type(filters)}"
            )

        invoke_args = {
            "filters": filters,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "filters" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数filters不能为空")

        return FunctionHelper.apply("Filter.and", "aie.Filter", invoke_args)

    @staticmethod
    def Or(filters: list) -> aie.Filter:

        if filters is not None and not isinstance(filters, list):
            raise AIEError(
                AIEErrorCode.ARGS_ERROR, f"filters 只支持list类型参数, 传入类型为{type(filters)}"
            )

        invoke_args = {
            "filters": filters,
        }

        invoke_args = {k: v for k, v in invoke_args.items() if v is not None}

        if "filters" not in invoke_args:
            raise AIEError(AIEErrorCode.ARGS_ERROR, "参数filters不能为空")

        return FunctionHelper.apply("Filter.or", "aie.Filter", invoke_args)
