from dataclasses import dataclass
from threading import Thread
from typing import Type, Callable

import easy_pysi as ez
from easy_pysi.plugin import Plugin


class Event:
    pass


@dataclass
class EventSubscriber:
    callback: Callable[[Event], str]
    event_type: Type[Event]
    asynchronous: bool


class EventPlugin(Plugin):
    subscribers: list[EventSubscriber] = []

    def start(self):
        self.subscribers = [
            subscriber
            for subscriber in _ALL_SUBSCRIBERS
            if self.app.is_available(subscriber.callback)
        ]


_ALL_SUBSCRIBERS: list[EventSubscriber] = []


def on(*event_types: Type[Event], asynchronous=False):
    # TODO: auto detect async function?
    def decorator(func):
        for event_type in event_types:
            subscriber = EventSubscriber(func, event_type, asynchronous)
            _ALL_SUBSCRIBERS.append(subscriber)
        return func
    return decorator


def emit(event: Event):
    event_type = type(event)

    # Synchronous event
    for subscriber in _get_subscribers(event_type):
        if not subscriber.asynchronous:
            _notify_subscriber(event, subscriber)
        else:
            _async_notify_subscriber(event, subscriber)


def _get_subscribers(event_type: Type[Event]) -> list[EventSubscriber]:
    available_subscribers = ez.plugin(EventPlugin).subscribers
    return [
        subscriber
        for subscriber in available_subscribers
        if issubclass(event_type, subscriber.event_type)
    ]


def _notify_subscriber(event: Event, subscriber: EventSubscriber):
    subscriber.callback(event)


def _async_notify_subscriber(event: Event, subscriber: EventSubscriber):
    thread = Thread(target=_notify_subscriber, args=(event, subscriber), daemon=True)
    thread.start()

