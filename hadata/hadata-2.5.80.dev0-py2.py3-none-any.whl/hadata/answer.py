from mongoengine import Document, StringField, DateTimeField, IntField, FloatField, BooleanField, \
    ListField

from hautils.s3 import delete_file


class MongoUserAssessmentsQuestionAnswerStatusHistory(Document):
    meta = {'collection': 'user_assessment_question_answer_status_history'}
    user_assessment_question_answer_id = StringField(required=True)
    status = StringField(required=True)
    created_datetime = DateTimeField(required=True)


class MongoQuestionAnswer(Document):
    meta = {'collection': 'question_answer'}
    job_id = StringField(required=True)
    question = StringField(required=True)
    answer = StringField(required=True)
    skill_id = StringField(required=False, default='62a684e3fd373bf47afdc511')
    level_id = StringField(required=False, default='62a684aaf34f1c2555b08747')
    subskill_1_id = StringField(required=False)
    subskill_2_id = StringField(required=False)
    subskill_3_id = StringField(required=False)
    question_type = StringField(required=False)
    question_theme = StringField(required=False)
    organization_id = StringField(required=False)
    time = IntField(required=False)
    points = IntField(required=False)
    media_question = BooleanField(required=False, default=False)
    file_name = StringField(required=False)
    file_hash = StringField(required=False)
    media_extension = StringField(required=False)
    file_encoded = StringField(required=False)
    file_uuid = StringField(required=False)
    roles = ListField(StringField(required=False), required=False)

    def reset_media_fields(self):
        """
        The reset_media_fields function resets the media_question, media_extension, file_name and file_hash fields of a
        Question object to their default values. This function is called when an error occurs while uploading a new image or
        video.

        :param self: Refer to an instance of the class
        :return: The media_question, media_extension, file_name and file_hash fields
        :doc-author: Trelent
        """
        if self.file_name is not None:
            delete_file(self.file_name)
        self.update(media_question=False, media_extension=None, file_name=None, file_hash=None)

    def set_media_fields(self, file_hash, file_name, media_type):
        """
        The set_media_fields function is used to set the media_question, media_extension, file_name and file_hash fields of a
            question object. This function is called when a user uploads an image or video for their question.

        :param self: Access the attributes and methods of the class in python
        :param file_hash: Store the hash of the file
        :param file_name: Store the name of the file that is uploaded
        :param media_type: Determine the extension of the file
        :return: The values of the file_hash, file_name and media_type variables
        :doc-author: Trelent
        """
        self.update(media_question=True, media_extension=media_type, file_name=file_name, file_hash=file_hash)


class MongoUserAssessmentsQuestionAnswer(Document):
    meta = {'collection': 'user_assessment_question_answer'}
    user_id = StringField(required=True)
    assessment_id = StringField(required=True)
    question_answer_id = StringField(required=True)
    user_assessment_id = StringField(required=False)
    score = IntField(required=False)
    time_expired = BooleanField(required=False)
    time_taken = IntField(required=False)
    time_started = DateTimeField(required=False)
    time_completed = DateTimeField(required=False)
    time_ping = DateTimeField(required=False)
    user_answer = StringField(required=False)
    system_answer = StringField(required=False)
    status = StringField(required=False)
    sort_order = IntField(required=False)
    system_question = StringField(required=True)
    max_score = IntField(required=False)
    question_type = StringField(required=False)
    allowed_time = IntField(required=False)
    face_detected = FloatField(required=False)
    similarity_score = FloatField(required=False)
    is_correct = BooleanField(required=False)
    personal_notes = StringField(required=False)
    media_question = BooleanField(required=False)
    media_extension = StringField(required=False)
    file_name = StringField(required=False)
    skill_id = StringField(required=False)
    level_id = StringField(required=False)
    subskill_1_id = StringField(required=False)
    subskill_2_id = StringField(required=False)
    subskill_3_id = StringField(required=False)
