from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses_json import CatchAll, DataClassJsonMixin, Undefined, config, dataclass_json


@dataclass_json
@dataclass
class User(DataClassJsonMixin):
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    is_premium: bool = True
    added_to_attachment_menu: bool = True
    can_join_groups: bool = True
    can_read_all_group_messages: bool = True
    supports_inline_queries: bool = True


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class Chat(DataClassJsonMixin):
    id: int
    chat_type: str = field(metadata=config(field_name="type"))

    unknown_things: CatchAll

    title: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class Message(DataClassJsonMixin):
    message_id: int
    date: int
    chat: Chat

    unknown_things: CatchAll

    text: Optional[str] = None
    from_user: Optional[User] = field(metadata=config(field_name="from"), default=None)
    sender_chat: Optional[Chat] = None

    forward_from: Optional[User] = None
    forward_from_chat: Optional[Chat] = None
    forward_from_message_id: Optional[int] = None
    forward_signature: Optional[str] = None
    forward_sender_name: Optional[str] = None
    forward_date: Optional[int] = None

    edit_date: Optional[int] = None
    

@dataclass_json
@dataclass
class PollOption(DataClassJsonMixin):
    text: str
    voter_count: int


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class Poll(DataClassJsonMixin):
    id: str
    question: str
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    allows_multiple_answers: bool

    unknown_things: CatchAll

    poll_type: str = field(metadata=config(field_name='type'))
    options: List[PollOption] = field(default_factory=list)
    correct_option_id: Optional[int] = None
    explanation: Optional[str] = None


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class CallbackQuery:
    id: str

    unknown_things: CatchAll

    from_user: User = field(metadata=config(field_name="from"))
    message: Optional[Message] = None
    inline_message_id: Optional[str] = None
    chat_instance: Optional[str] = None
    data: Optional[str] = None
    game_short_name: Optional[str] = None


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class Update(DataClassJsonMixin):
    update_id: int

    unknown_things: CatchAll

    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None

    callback_query: Optional[CallbackQuery] = None

    poll: Optional[Poll] = None

    def get_chat(self) -> Optional[Chat]:
        if self.message:
            return self.message.chat
        if self.edited_message:
            return self.edited_message.chat
        if self.channel_post:
            return self.channel_post.chat
        if self.edited_channel_post:
            return self.edited_channel_post.chat

        return None

    def get_from_id(self) -> Optional[int]:
        if self.get_chat():
            return self.get_chat().id
        if self.callback_query:
            # better to change it but
            return self.callback_query.from_user.id

        return None
    