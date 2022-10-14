# coding=utf-8

from datetime import datetime

from bson import ObjectId
from flask import current_app
from flask_restful import fields, reqparse

from mercury.services.database_nosql_mongo import db as mongo
from mercury.services.signals import signals
from mercury.services.dictionaries import merge_dicts

"""Signals"""
notification_dispatch = signals.signal('notification-dispatch')

"""Fields to marshal notification to JSON."""
notification_fields = {
    'category': fields.String,
    'datetime_schedule': fields.String,
    'datetime_dispatch': fields.String,
    'links': {
        # Replaces Notification ID with Notification Uri (HATEOAS) through endpoint 'notification'
        'self': fields.Url('notification')
    }
}

'''CRUD Functions'''


def get_request_parser(request_parser=None):
    """Get request parser for notification.

    :param request_parser: If exists, add request parser argument to request_parser param.
    :return: Notification request parser.
    """
    if not request_parser:
        result = reqparse.RequestParser()
    else:
        result = request_parser
    result.add_argument('category', type=str, required=True, help='No notification category provided', location='json')
    result.add_argument('datetime_schedule', type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'), required=False,
                        help='No notification datetime_schedule provided', location='json')
    return result


def select_notification(id, user_id):
    """Get notification by id param and user_id.

    :param id: Notification's id to find.
    :param user_id: Notification's user_id to find.
    :return: Notification found or error 404.
    """
    return mongo.db.notification.find_one_or_404({'_id': ObjectId(id), 'user_id': user_id})


def select_notifications(user_id):
    """Get all notifications by user_id.

    :param user_id: Notification's user_id to find.
    :return: All notifications.
    """
    return mongo.db.notification.find({'user_id': user_id})


def insert_notification(notification, user_id):
    """Post new notification from notification param (MongoDB has limit of 16 megabytes per document) for user_id.

    :param notification: Notification to persist.
    :param user_id: Notification's user_id to persist.
    :return: Persisted notification's base informations or error.
    """
    notification['user_id'] = user_id
    notification['datetime_schedule'] = notification.get('datetime_schedule',
                                                         datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    notification.pop('_id', None)
    notification['_id'] = str(mongo.db.notification.insert_one(notification).inserted_id)
    instant_dispatch(notification)
    return notification


def update_notification(id, notification, user_id=None):
    """Put the notification passed by notification param (MongoDB has limit of 16 megabytes per document) for user_id.

    :param id: Notification's id to find.
    :param user_id: Notification's user_id to find.
    :param notification: Notification to persist.
    :return: Persisted notification's base informations or error.
    """
    if user_id:
        notification['user_id'] = user_id
    else:
        user_id = notification['user_id']
    notification.pop('_id', None)
    notification_found = mongo.db.notification.find_one_or_404({'_id': ObjectId(id), 'user_id': user_id})
    if mongo.db.notification.update_one({'_id': notification_found['_id']}, {'$set': notification}).acknowledged:
        notification = merge_dicts(notification_found, notification)
        notification['_id'] = str(notification['_id'])
        instant_dispatch(notification)
        return notification
    else:
        return None


def delete_notification(id, user_id):
    """Delete the notification that have the passed notification id.

    :param id: Notification's id to find.
    :param user_id: Notification's user_id to find.
    :return: True if elimination was successful or False if elimination was not possible.
    """
    return mongo.db.notification.remove({'_id': ObjectId(id), 'user_id': user_id})['ok'] == 1.0


'''Other Functions'''


def find_notifications_to_dispatch():
    """Find all notifications that have datetime_schedule lower than now (local time) and that they haven't already been
     dispatched.

    :return: Cursor to manage notifications to dispatch.
    """
    return mongo.db.notification.find({
        'datetime_schedule': {'$lte': datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
        'datetime_dispatch': None
    })


def instant_dispatch(notification):
    """Check if it's must to do notification's instant dispatch.

    :param notification: notification to check and eventually immediately dispatch.
    """
    if notification and (
            (not notification.get('datetime_schedule')) or (
                datetime.strptime(notification['datetime_schedule'], '%Y-%m-%d %H:%M:%S') <= datetime.now() and
                (not notification.get('datetime_dispatch'))
            )
    ):
        notification_dispatch.send(current_app._get_current_object(), notification=notification)
