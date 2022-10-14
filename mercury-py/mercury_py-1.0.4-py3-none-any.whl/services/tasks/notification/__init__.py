# coding=utf-8

from base64 import b64decode
from datetime import datetime
from os import linesep

from flask_mail import Mail, Message

from mercury.services.notification import notification_dispatch, update_notification, find_notifications_to_dispatch
from .. import celery

mail = Mail()


def init_app(app):
    """Initializes the application with the extension.

    :param app: The Flask application object.
    """
    mail.init_app(app)

    notification_dispatch.connect(when_notification_dispatch, app)


def when_notification_dispatch(sender, notification, **extra):
    """Celery task routine to execute route_notification task.

    :param sender: Sender.
    :param notification: Notification to dispatch.
    :param extra: other params.
    """
    dispatch_notification.delay(notification)


@celery.task()
def dispatch_notification(notification):
    """Celery task routine to find and route notification to dispatch to correct notification channel
    (executed by Celery worker).

    :param notification: Notification to dispatch.
    :return: Operations logs.
    """
    if not notification:
        return 'Nothing to dispatch.'
    return route_notification(notification)


@celery.task()
def route_notifications():
    """Celery task routine to find and route notifications to dispatch to correct notification channel
    (executed by Celery worker).

    :return: Operations logs.
    """
    notifications = find_notifications_to_dispatch()
    if (not notifications) or (len(list(notifications.clone())) < 1):
        return 'Nothing to dispatch.'
    result = ''
    for notification in notifications:
        result = f'{result}{linesep}{route_notification(notification)}'
    return result


def route_notification(notification):
    """Routes a notification to correct notification channel.

    :param notification: Notification to route to correct notification channel.
    :return: Operations logs.
    """
    return {
        'email': route_notification_mail(notification)
    }.get(notification['category'], 'email')


def route_notification_mail(notification):
    """Routes a notification to mail notification channel.

    :param notification: Notification to route to mail notification channel.
    :return: Operations logs.
    """
    recipients = notification['recipients']
    if isinstance(recipients, str):
        recipients = [recipients]
    msg = Message(recipients=recipients, subject=notification['subject'],
                  body=notification.get('body'), html=notification.get('html'),
                  cc=notification.get('cc'), bcc=notification.get('bcc'), reply_to=notification.get('reply_to'))
    try:
        attachments = notification.get('attachments')
        if attachments is not None:
            [msg.attach(filename=attachment.get('filename'), content_type=attachment.get('content_type'),
                        data=b64decode(attachment['data'])) for attachment in attachments]
    except Exception as ex:
        raise Exception(f'Mail attachments with _id {notification["_id"]} failed to load at '
                        f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}!{linesep}Detail: {ex}')
    try:
        mail.send(msg)
    except Exception as ex:
        raise Exception(f'Dispatch mail with _id {notification["_id"]} failed at '
                        f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}!{linesep}Detail: {ex}')
    success_msg = f'Successfully dispatched mail with _id {notification["_id"]} at ' \
                  f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.'
    notification_id = notification["_id"]
    try:
        notification['datetime_dispatch'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = update_notification(notification['_id'], notification)
        if not result:
            raise Exception('Acknowledged: False.')
        return f'{success_msg}{linesep}Successfully updated mail datetime_dispatch with _id {result["_id"]}.'
    except Exception as ex:
        raise Exception(f'Update mail datetime_dispatch with _id {notification_id} failed at '
                        f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}!{linesep}Detail: {ex}')
