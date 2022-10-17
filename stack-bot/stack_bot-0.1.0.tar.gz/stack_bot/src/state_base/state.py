from typing import Generic, List, Optional, TypeVar
from stack_bot.src.elements.api_elements import Message, Update
from stack_bot.src.elements.bot_elements import Event

T = TypeVar('T')


class State(Generic[T]):

    def parse_event(self, event: Event) -> Optional[T]:
        return None

    def handle_value(self, value: T, context: dict = {}) -> bool:
        return True

    def description(self) -> str:
        return "No description"

    def post_action(self, handle_result: bool):
        return None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}"

    def __repr__(self) -> str:
        return self.__str__()


class StateLine:
    __slots__ = ['pipeline', 'context', 'curr_state']

    def __init__(self):
        self.pipeline: List[State] = []
        self.context: dict = {}
        self.curr_state: Optional[State] = None

    def run(self, event: Event):
        if not self.pipeline:
            print("No state on pipeline")
        else:
            self.curr_state = self.pipeline.pop()

            state = self.curr_state
            value = state.parse_event(event)

            is_handling_succeed = False

            if value:
                is_handling_succeed = state.handle_value(value, self.context)

            if not is_handling_succeed:
                print("Incorrect awaiting type for state:", state.description())
                self.pipeline.append(state)

            state.post_action(is_handling_succeed)

    def append_state(self, state: State):
        self.pipeline.insert(0, state)

    def put_state_on_top(self, state: State):
        self.pipeline.append(state)

    def __rshift__(self, state: State):
        self.put_state_on_top(state)
        return self

    def __lshift__(self, state: State):
        self.append_state(state)
        return self

    def repeat_last_state(self):
        if self.curr_state:
            self >> self.curr_state

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.pipeline}"




