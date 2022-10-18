from classiq.interface.generator.function_call import FunctionCall


def _get_wire_name(
    source_call: FunctionCall,
    source_pin_name: str,
    dest_pin_name: str,
    dest_call: FunctionCall,
) -> str:
    return f"{source_call.name}:{source_pin_name}->{dest_call.name}:{dest_pin_name}"


def _set_model_output(call: FunctionCall, pin_name: str, wire_name: str):
    call.outputs_dict[pin_name] = wire_name
    call.non_zero_output_wires.append(wire_name)


def _set_model_input(call: FunctionCall, pin_name: str, wire_name: str):
    call.inputs_dict[pin_name] = wire_name
    call.non_zero_input_wires.append(wire_name)


def handle(
    source_call: FunctionCall,
    source_pin_name: str,
    dest_pin_name: str,
    dest_call: FunctionCall,
) -> None:
    wire_name = _get_wire_name(source_call, source_pin_name, dest_pin_name, dest_call)
    _set_model_output(source_call, source_pin_name, wire_name)
    _set_model_input(dest_call, dest_pin_name, wire_name)
