from mongoengine import Document, EmailField, StringField, ObjectIdField, DateTimeField, IntField, FloatField, \
    BooleanField, ListField


class MongoUser(Document):
    meta = {'collection': 'user'}
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=8, sensitive=True)
    organization_id = StringField(required=True)
    profile_type = IntField(required=True)
    is_verified = BooleanField(required=True, default=False)
    clear_password = StringField(required=False, min_length=8, sensitive=True, clear_before_save=True)
    def ids(self):
        return str(self.id)

    def save(
        self,
        force_insert=False,
        validate=True,
        clean=True,
        write_concern=None,
        cascade=None,
        cascade_kwargs=None,
        _refs=None,
        save_condition=None,
        signal_kwargs=None,
        **kwargs,
    ):
        super(MongoUser, self).save(
            force_insert=force_insert,
            validate=validate,
            clean=clean,
            write_concern=write_concern,
            cascade=cascade,
            cascade_kwargs=cascade_kwargs,
            _refs=_refs,
            save_condition=save_condition,
            signal_kwargs=signal_kwargs,
            **kwargs,
        )
        try:
            history = MongoPasswordHistory(user_id=str(self.id),password=self.password)
            history.save()
        except Exception as e:
            print(e)
            pass

        return self

class MongoPasswordHistory(Document):
    meta = {'collection': 'password_history'}
    user_id = StringField(required=True)
    password = StringField(required=True, min_length=8)


class MongoUserProfile(Document):
    meta = {'collection': 'user_profile'}
    user_id = StringField(required=True, unique=True)
    role = StringField()
    focus_area = StringField()
    projects = ListField(StringField())


class MongoUserAssessmentsQuestionAnswerStatusHistory(Document):
    meta = {'collection': 'user_assessment_question_answer_status_history'}
    user_assessment_question_answer_id = StringField(required=True)
    status = StringField(required=True)
    created_datetime = DateTimeField(required=True)


class MongoUserObjectives(Document):
    meta = {'collection': 'user_objectives'}
    user_id = StringField(required=True, unique=True)
    sample_field = StringField()



