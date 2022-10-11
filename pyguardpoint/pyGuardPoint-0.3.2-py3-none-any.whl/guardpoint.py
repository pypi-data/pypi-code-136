import json
import logging
from json import JSONDecodeError

import validators as validators

from pyGuardPoint.guardpoint_dataclasses import Cardholder, SecurityGroup, Card
from pyGuardPoint.guardpoint_connection import GuardPointConnection, GuardPointAuthType

log = logging.getLogger(__name__)


class GuardPointError(Exception):
    pass


class GuardPoint(GuardPointConnection):

    def __init__(self, **kwargs):
        # Set default values if not present
        host = kwargs.get('host', "localhost")
        port = kwargs.get('port', 10695)
        auth = kwargs.get('auth', GuardPointAuthType.BEARER_TOKEN)
        user = kwargs.get('username', "admin")
        pwd = kwargs.get('pwd', "admin")
        key = kwargs.get('key', "00000000-0000-0000-0000-000000000000")
        super().__init__(host=host, port=port, auth=auth, user=user, pwd=pwd, key=key)

    def get_security_groups(self):
        url = self.baseurl + "/odata/api_SecurityGroups"
        # url_query_params = "?$select=uid,name&$filter=name%20ne%20'Anytime%20Anywhere'"
        url_query_params = ""
        code, response_body = self.query("GET", url=(url + url_query_params))

        # Try to convert body into json
        try:
            response_body = json.loads(response_body)
        except JSONDecodeError:
            response_body = None
        except Exception as e:
            log.error(e)
            response_body = None

        if code != 200:
            if isinstance(response_body, dict):
                if 'error' in response_body:
                    raise GuardPointError(response_body['error'])
            raise GuardPointError(str(code))

        # Check response body is formatted as expected
        if not isinstance(response_body, dict):
            raise GuardPointError("Badly formatted response.")
        if 'value' not in response_body:
            raise GuardPointError("Badly formatted response.")
        if not isinstance(response_body['value'], list):
            raise GuardPointError("Badly formatted response.")

        # Compose list of security groups
        security_groups = []
        for entry in response_body['value']:
            if isinstance(entry, dict):
                sg = SecurityGroup(entry)
                security_groups.append(sg)
        return security_groups

    def get_cardholder_count(self):
        url = self.baseurl + "/odata/GetCardholdersCount"
        code, response_body = self.query("GET", url=url)

        # Try to convert body into json
        try:
            response_body = json.loads(response_body)
        except JSONDecodeError:
            response_body = None
        except Exception as e:
            log.error(e)
            response_body = None

        if code != 200:
            if isinstance(response_body, dict):
                if 'error' in response_body:
                    raise GuardPointError(response_body['error'])
            else:
                raise GuardPointError(str(code))

        # Check response body is formatted as expected
        if not isinstance(response_body, dict):
            raise GuardPointError("Badly formatted response.")
        if 'totalItems' not in response_body:
            raise GuardPointError("Badly formatted response.")

        return int(response_body['totalItems'])


    def delete_card_holder(self, uid):
        if not validators.uuid(uid):
            raise ValueError(f'Malformed UID {uid}')

        url = self.baseurl + "/odata/API_Cardholders"
        url_query_params = "(" + uid + ")"

        code, response_body = self.query("DELETE", url=(url + url_query_params))

        if code != 204:  # HTTP NO_CONTENT
            try:
                response_body = json.loads(response_body)
                if 'error' in response_body:
                    raise GuardPointError(response_body['error'])
                else:
                    raise GuardPointError(str(code))
            except Exception:
                raise GuardPointError(str(code))

        return True

    def add_new_card(self, card: Card):
        url = "/odata/API_Cards"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        body = card.dict()
        code, response_body = self.query("POST", headers=headers, url=url, body=json.dumps(body))

        # Try to convert body into json
        try:
            response_body = json.loads(response_body)
        except JSONDecodeError:
            response_body = None
        except Exception as e:
            log.error(e)
            response_body = None

        if code == 201:  # HTTP CREATED
            return response_body['uid']
        else:
            if "errorMessages" in response_body:
                raise GuardPointError(response_body["errorMessages"][0]["other"])
            elif "error" in response_body:
                raise GuardPointError(response_body["error"]['message'])
            else:
                raise GuardPointError(str(code))

    def add_card_holder(self, cardholder: Cardholder):

        url = "/odata/API_Cardholders/CreateFullCardholder"

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'IgnoreNonEditable': ''
        }

        ch = cardholder.dict()

        # Filter out un-settable variables
        if 'uid' in ch:
            ch.pop('uid')
        if 'status' in ch:
            ch.pop('status')
        # if 'cardholderType' in body['cardholder']:
        #    body['cardholder'].pop('cardholderType')
        if 'securityGroup' in ch:
            ch.pop('securityGroup')
        if 'cards' in ch:  # Need to add cards in a second call
            cards = ch['cards']
            ch.pop('cards')

        body = {'cardholder': ch}
        # print(json.dumps(body))
        code, response_body = self.query("POST", headers=headers, url=url, body=json.dumps(body))

        # Try to convert body into json
        try:
            response_body = json.loads(response_body)
        except JSONDecodeError:
            response_body = None
        except Exception as e:
            log.error(e)
            response_body = None

        if code == 201:  # HTTP CREATED
            if cards:
                for card in cards:
                    card['cardholderUID'] = response_body['value'][0]
                    self.add_new_card(Card(card))
                    #TODO catch card already exists
            return response_body['value'][0]
        else:
            if "errorMessages" in response_body:
                raise GuardPointError(response_body["errorMessages"][0]["other"])
            elif "error" in response_body:
                raise GuardPointError(response_body["error"]['message'])
            else:
                raise GuardPointError(str(code))

    def get_card_holder(self, uid):
        if not validators.uuid(uid):
            raise ValueError(f'Malformed UID {uid}')

        url = "/odata/API_Cardholders"
        url_query_params = "(" + uid + ")?" \
                                       "$expand=" \
                                       "cardholderType($select=typeName)," \
                                       "cards($select=cardCode)," \
                                       "cardholderPersonalDetail($select=email,company,idType,idFreeText)," \
                                       "securityGroup($select=name)"

        code, response_body = self.query("GET", url=(url + url_query_params))

        # Try to convert body into json
        try:
            response_body = json.loads(response_body)
        except JSONDecodeError:
            response_body = None
        except Exception as e:
            log.error(e)
            response_body = None

        if code != 200:
            if isinstance(response_body, dict):
                if 'error' in response_body:
                    raise GuardPointError(response_body['error'])
            else:
                raise GuardPointError(str(code))

        # Check response body is formatted as expected
        if not isinstance(response_body, dict):
            raise GuardPointError("Badly formatted response.")
        if 'value' not in response_body:
            raise GuardPointError("Badly formatted response.")

        return Cardholder(response_body['value'][0])




    @staticmethod
    def _compose_filter(search_words, cardholder_type_name):
        filter_str = ""
        if cardholder_type_name or search_words:
            filter_str = "$filter="
        if cardholder_type_name:
            filter_str += f"(cardholderType/typeName%20eq%20'{cardholder_type_name}')"
            if search_words:
                filter_str += "%20and%20"
        if search_words:
            words = list(filter(None, search_words.split(" ")))[
                    :5]  # Split by space, remove empty elements, ignore > 5 elements
            fields = ["firstName", "lastName", "CardholderPersonalDetail/company"]
            phrases = []
            for f in fields:
                for v in words:
                    phrases.append(f"contains({f},'{v}')")
            filter_str += f"({'%20or%20'.join(phrases)})"
        if cardholder_type_name or search_words:
            filter_str += "&"
        return filter_str

    def get_card_holders(self, offset=0, limit=10, searchPhrase=None, cardholder_type_name=None):
        url = "/odata/API_Cardholders"
        filter_str = self._compose_filter(search_words=searchPhrase, cardholder_type_name=cardholder_type_name)
        url_query_params = ("?" + filter_str +
                            "$expand="
                            "cardholderType($select=typeName),"
                            "cards($select=cardCode),"
                            "cardholderPersonalDetail($select=email,company,idType,idFreeText),"
                            "securityGroup($select=name)&"
                            "$orderby=fromDateValid%20desc&"
                            "$top=" + str(limit) + "&$skip=" + str(offset)
                            )

        code, response_body = self.query("GET", url=(url + url_query_params))

        # Try to convert body into json
        try:
            response_body = json.loads(response_body)
        except JSONDecodeError:
            response_body = None
        except Exception as e:
            log.error(e)
            response_body = None

        if code != 200:
            if isinstance(response_body, dict):
                if 'error' in response_body:
                    raise GuardPointError(response_body['error'])

        if not isinstance(response_body, dict):
            raise GuardPointError("Badly formatted response.")
        if 'value' not in response_body:
            raise GuardPointError("Badly formatted response.")
        if not isinstance(response_body['value'], list):
            raise GuardPointError("Badly formatted response.")

        cardholders = []
        for x in response_body['value']:
            cardholders.append(Cardholder(x))
        return cardholders

