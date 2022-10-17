import validators

from pyGuardPoint.guardpoint_dataclasses import Cardholder, Card
from pyGuardPoint.guardpoint_error import GuardPointError


class CardholdersAPI:
    def delete_card_holder(self, cardholder:Cardholder):
        if not validators.uuid(cardholder.uid):
            raise ValueError(f'Malformed Cardholder UID {cardholder.uid}')

        url = self.baseurl + "/odata/API_Cardholders"
        url_query_params = "(" + cardholder.uid + ")"

        code, json_body = self.gp_json_query("DELETE", url=(url + url_query_params))

        if code != 204:  # HTTP NO_CONTENT
            try:
                if 'error' in json_body:
                    raise GuardPointError(json_body['error'])
                else:
                    raise GuardPointError(str(code))
            except Exception:
                raise GuardPointError(str(code))

        return True


    # TODO use UpdateFullCardholder instead
    def update_card_holder(self, cardholder: Cardholder):
        if not validators.uuid(cardholder.uid):
            raise ValueError(f'Malformed Cardholder UID {cardholder.uid}')

        url = "/odata/API_Cardholders"
        url_query_params = f"({cardholder.uid})"

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            #'IgnoreNonEditable': ''
        }

        ch = cardholder.dict(editable_only=True)

        code, json_body = self.gp_json_query("PATCH", headers=headers, url=(url+url_query_params), json_body=ch)

        if code != 204:  # HTTP NO_CONTENT
            try:
                if 'error' in json_body:
                    raise GuardPointError(json_body['error'])
                else:
                    raise GuardPointError(str(code))
            except Exception:
                raise GuardPointError(str(code))

        return True

    def add_card_holder(self, cardholder: Cardholder, overwrite_cardholder=False, reassign_existing_cards=False):

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
        code, json_body = self.gp_json_query("POST", headers=headers, url=url, json_body=body)

        if code == 201:  # HTTP CREATED
            if cards and reassign_existing_cards:
                for card in cards:
                    card['cardholderUID'] = json_body['value'][0]
                    self.add_card(Card(card))
                    # TODO catch card already exists
            return json_body['value'][0]
        elif code == 422: # unprocessable Entity
            if "errorMessages" in json_body:
                if json_body["errorMessages"][0]["errorCode"] == 59: # Cardholder_0_AlreadyExists
                    self.update_card_holder(cardholder)
        else:
            if "errorMessages" in json_body:
                raise GuardPointError(json_body["errorMessages"][0]["other"])
            elif "error" in json_body:
                raise GuardPointError(json_body["error"]['message'])
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
                                       "securityGroup"

        code, json_body = self.gp_json_query("GET", url=(url + url_query_params))

        if code != 200:
            if isinstance(json_body, dict):
                if 'error' in json_body:
                    raise GuardPointError(json_body['error'])
            else:
                raise GuardPointError(str(code))

        # Check response body is formatted as expected
        if not isinstance(json_body, dict):
            raise GuardPointError("Badly formatted response.")
        if 'value' not in json_body:
            raise GuardPointError("Badly formatted response.")

        return Cardholder(json_body['value'][0])

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

        code, json_body = self.gp_json_query("GET", url=(url + url_query_params))

        if code != 200:
            if isinstance(json_body, dict):
                if 'error' in json_body:
                    raise GuardPointError(json_body['error'])

        if not isinstance(json_body, dict):
            raise GuardPointError("Badly formatted response.")
        if 'value' not in json_body:
            raise GuardPointError("Badly formatted response.")
        if not isinstance(json_body['value'], list):
            raise GuardPointError("Badly formatted response.")

        cardholders = []
        for x in json_body['value']:
            cardholders.append(Cardholder(x))
        return cardholders