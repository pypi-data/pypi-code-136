import fastnumbers
from typing import Callable, Dict, List, Literal, Tuple, cast
from numparser.fsm.engine import Bound, FSMResult, FSMResultParser, State, FSM
from numparser.fsm.engine import ID
from numparser.fsm.tokenizer import TokenType
from numparser.output import ParsedNumber


T = TokenType


us_num_fmt = FSM.from_string(
    r"""
    sign: name=num registry=r0 args=[+\-]{0,1}
    wN: name=num registry=r0 args=[0-9]{1,}
    wS: args=[,]{1} | [ ]{1,3}
    wD: name=num registry=r0 args=[.]{1}
    dN: name=num registry=r0 args=[0-9]{1,}
    dS: args=[,]{1} | [ ]{1,3}
    e: name=num registry=r0 args=[eE]{1}
    esign: name=num registry=r0 args=[+\-]{0,1}
    epow: name=num registry=r0 args=[0-9]{1,}
    ---
    start -> sign -> wN <-> wS
                e <- wN -> wD -> dN <-> dS
                                 dN -> e -> esign -> epow
    # allow ending with decimal separator
    (wN; wD; dN; epow) -> end
    """
)

eu_num_fmt = FSM.from_string(
    r"""
    sign: name=num registry=r0 args=[+\-]{0,1}
    wN: name=num registry=r0 args=[0-9]{1,}
    wS: args=[.]{1} | [ ]{1,3}
    wD: name=num registry=r0 args=[,]{1}
    dN: name=num registry=r0 args=[0-9]{1,}
    dS: args=[.]{1} | [ ]{1,3}
    e: name=num registry=r0 args=[eE]{1}
    esign: name=num registry=r0 args=[+\-]{0,1}
    epow: name=num registry=r0 args=[0-9]{1,}
    ---
    start -> sign -> wN <-> wS
                e <- wN -> wD -> dN <-> dS
                                 dN -> e -> esign -> epow
    # allow ending with decimal separator
    (wN; wD; dN; epow) -> end
    """
)


def default_parser(result: FSMResult, origin_text: str) -> List[ParsedNumber]:
    outputs = []
    for registry, lst in result.items():
        for values in lst:
            num_string = ""
            unit_string = ""
            for state_name, value in values:
                if state_name == "num":
                    num_string += "".join(
                        origin_text[x.index : x.index + len(x.value)] for x in value
                    )
                elif state_name == "unit":
                    unit_string += "".join(
                        origin_text[x.index : x.index + len(x.value)] for x in value
                    )

            number = fastnumbers.fast_real(num_string, coerce=False)
            assert isinstance(number, (int, float)), number
            outputs.append(
                ParsedNumber(
                    number_string=num_string,
                    number=number,
                    unit=unit_string if unit_string != "" else None,
                    prob=None,
                )
            )
    return outputs


def predefined_patterns(
    locale: Literal["us", "eu"]
) -> Dict[str, Tuple[FSM, FSMResultParser]]:
    fsms = {}
    if locale == "us":
        fsms["num"] = us_num_fmt
    else:
        assert locale == "eu"
        fsms["num"] = eu_num_fmt

    fsms["n_num"] = FSM.from_string(
        """
        sep: registry=r0 args=[ \t\\n]{1,}
        ---
        start -> num:start
        end <- num:end -> sep -> start
        """,
        num=fsms["num"],
    )
    fsms["num_unit"] = FSM.from_string(
        """
        sep: registry=r0 args=[ \t]{0,2}
        unit: name=unit registry=r0 args=%s{1}
        unknown: name=unit registry=r0 args=^%s^[a-zA-Z]{1,}
        ---
        start -> num:start
        num:end -> sep -> (unit; unknown) -> end
        """
        % (TokenType.Unit.value, TokenType.NotUnit.value),
        num=fsms["num"],
    )
    # e.g., 6 ft 1 in
    fsms["n_num_units"] = FSM.from_string(
        """
        sep: registry=r0 args=[ \t\\n]{0,}
        ---
        start -> num_unit:start
        end <- num_unit:end -> sep -> start
        """,
        num_unit=fsms["num_unit"],
    )
    # two different units: 1.73m (5 ft 8 in)
    fsms["2_diff_num_units"] = FSM.from_string(
        """
        sep: registry=r0 args=[ \t]{0,2}
        sep2: registry=r0 args=[ \t]{0,2}
        sep3: registry=r0 args=[ \t]{0,2}
        open: args=[(]{1}
        close: args=[)]{1}
        ---
        start -> n_num_units:start
        n_num_units:end -> sep -> open -> sep2 -> n_num_units2:start 
        n_num_units2:end -> sep3 -> close -> end
        """,
        n_num_units=fsms["n_num_units"],
        n_num_units2=fsms["n_num_units"].rename("n_num_units2", {"r0": "r1"}),
    )

    return {name: (fsm, default_parser) for name, fsm in fsms.items()}
