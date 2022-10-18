import json

import pytest
from seeq.spy._errors import SPyValueError
from seeq.spy.notifications._emails import EmailRequestInput, EmailRecipient


@pytest.mark.unit
def test_email_recipient():
    recipient1 = EmailRecipient('test1@seeq.com')
    assert recipient1.email == 'test1@seeq.com'
    assert recipient1.name is None

    recipient2 = EmailRecipient(name="alex", email='test2@seeq.com')
    assert recipient2.name == 'alex'
    assert recipient2.email == 'test2@seeq.com'

    with pytest.raises(SPyValueError, match='Invalid email address provided'):
        EmailRecipient("test3")

    with pytest.raises(SPyValueError, match='Invalid email address provided'):
        EmailRecipient("test4", "test5")


@pytest.mark.unit
def test_email_request_input():
    recipient1 = EmailRecipient('test1@seeq.com')
    email_request_input_1 = EmailRequestInput(toEmails=[recipient1], subject="test subject",
                                              content="<p>Hello World</p>")
    assert json.dumps(email_request_input_1.to_dict()) == \
           '{"toEmails": [{"email": "test1@seeq.com"}], "subject": "test subject", "content": "<p>Hello World</p>"}'

    recipient2 = EmailRecipient('test2@seeq.com')
    recipient3 = EmailRecipient('test3@seeq.com', name="test3name")
    email_request_input_2 = EmailRequestInput(toEmails=[recipient1], ccEmails=[recipient2],
                                              bccEmails=[recipient1, recipient3],
                                              subject="test subject", content="Hello World")
    assert json.dumps(email_request_input_2.to_dict()) == '{"toEmails": [{"email": "test1@seeq.com"}], ' \
                                                          '"subject": "test subject", "content": "Hello World", ' \
                                                          '"ccEmails": [{"email": "test2@seeq.com"}], ' \
                                                          '"bccEmails": [{"email": "test1@seeq.com"}, ' \
                                                          '{"email": "test3@seeq.com", "name": "test3name"}]}'

    email_request_input_3 = EmailRequestInput(toEmails=[recipient1], ccEmails=[], bccEmails=None,
                                              subject="subject", content="content")
    assert email_request_input_3.toEmails == [recipient1]
    assert email_request_input_3.ccEmails == []
    assert email_request_input_3.bccEmails is None

    with pytest.raises(SPyValueError, match='At least one recipient needs to be provided'):
        EmailRequestInput(toEmails=[], subject="some subject", content="some content")

    with pytest.raises(SPyValueError, match='A non blank subject must be provided'):
        EmailRequestInput(toEmails=[recipient1], subject="", content="some content")

    with pytest.raises(SPyValueError, match='A non blank content must be provided'):
        EmailRequestInput(toEmails=[recipient1], subject="some subject", content="")
