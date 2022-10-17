# vim: set fileencoding=utf-8:


from coronado import TripleObject
from coronado.auth import Auth
from coronado.auth import Scope
from coronado.cardaccount import CardAccount
from coronado.cardaccount import CardAccountStatus
from coronado.cardaccount import SERVICE_PATH
from coronado.exceptions import CallError
from coronado.exceptions import ForbiddenError
from coronado.exceptions import InvalidPayloadError
from coronado.exceptions import NotImplementedError
from coronado.exceptions import UnexpectedError
from coronado.exceptions import UnprocessablePayload
from coronado.offer import CardholderOffer
from coronado.offer import CardholderOfferDetails
from coronado.offer import OfferCategory
from coronado.offer import OfferDeliveryMode
from coronado.offer import OfferType

import uuid

import pytest

import coronado.auth as auth


# +++ constants +++

KNOWN_ACCT_EXT_ID = 'pnc-card-69-3149b4780d6f4c2fa21fb45d2637efbb'
KNOWN_ACCT_ID = '1267'
KNOWN_CARD_PROG_EXT_ID = 'prog-66'
KNOWN_COUNTRY_CODE = 'US'
KNOWN_OFFER_ID = '4862'
KNOWN_POSTAL_CODE = '15212'
KNOWN_POSTAL_CODE_LONG = '%s-1641' % KNOWN_POSTAL_CODE
KNOWN_PUB_EXTERNAL_ID = '0d7c608a3df5'


# *** globals ***

_config = auth.loadConfig()
_auth = Auth(_config['tokenURL'], clientID = _config['clientID'], clientSecret = _config['secret'], scope = Scope.PUBLISHERS)

CardAccount.initialize(_config['serviceURL'], SERVICE_PATH, _auth)


# *** tests ***

def test_CardAccountStatus():
    x = CardAccountStatus('ENROLLED')

    assert x == CardAccountStatus.ENROLLED
    assert str(x) == 'ENROLLED'


def test_CardAccount_create():
    spec = {
        'card_program_external_id': KNOWN_CARD_PROG_EXT_ID,
        'external_id': 'pnc-card-69-%s' % uuid.uuid4().hex,
        'publisher_external_id': KNOWN_PUB_EXTERNAL_ID,
        'status': str(CardAccountStatus.ENROLLED),
    }

    account = CardAccount.create(
                extCardAccountID = spec['external_id'],
                extCardProgramID = spec['card_program_external_id'],
                extPublisherID = spec['publisher_external_id'],
                status = CardAccountStatus.ENROLLED
              )
    assert account

    with pytest.raises(InvalidPayloadError):
        CardAccount.create(
            extCardAccountID = KNOWN_ACCT_EXT_ID,
            extCardProgramID = spec['card_program_external_id'],
            extPublisherID = spec['publisher_external_id'],
            status = CardAccountStatus.ENROLLED
        )

    with pytest.raises(InvalidPayloadError):
        CardAccount.create(
            extCardAccountID = '****',
            extCardProgramID = spec['card_program_external_id'],
            extPublisherID = spec['publisher_external_id'],
            status = CardAccountStatus.ENROLLED
        )


def test_CardAccount_list():
    accounts = CardAccount.list()

    assert isinstance(accounts, list)

    if len(accounts):
        account = accounts[0]
        assert isinstance(account, TripleObject)
        assert account.objID

    accounts = CardAccount.list(pubExternalID = KNOWN_PUB_EXTERNAL_ID)
    assert accounts[0].status == CardAccountStatus.ENROLLED.value

    accounts = CardAccount.list(pubExternalID = KNOWN_PUB_EXTERNAL_ID, cardAccountExternalID = KNOWN_ACCT_EXT_ID)
    assert accounts[0].status == CardAccountStatus.ENROLLED.value


def test_CardAccount_byID():
    result = CardAccount.byID(KNOWN_ACCT_ID)
    assert isinstance(result, CardAccount)

    assert not CardAccount.byID({ 'bogus': 'test'})
    assert not CardAccount.byID(None)
    assert not CardAccount.byID('bogus')


def test_CardAccount_updateWith():
    control = CardAccountStatus.NOT_ENROLLED
    payload = { 'status' : str(control), }
    obj  = CardAccount.updateWith(KNOWN_ACCT_ID, payload)
    assert obj.status == str(control)

    # Reset:
    payload['status'] = 'ENROLLED'
    CardAccount.updateWith(KNOWN_ACCT_ID, payload)


_account = CardAccount(KNOWN_ACCT_ID)

# @pytest.mark.skip('Incomplete object returned; properties out of sync')
def test_CardAccount_offerActivations():
    activations = _account.offerActivations()
    assert isinstance(activations, list)
    if activations:
        # Validate the payloads for realz
        pass


def test_CardAccount_activateFor():
    with pytest.raises(CallError):
        _account.activateFor()

    with pytest.raises(CallError):
        _account.activateFor([ '4269', '6942', ], OfferCategory.AUTOMOTIVE)

    # Activate all offers for this account matching a specific category
    with pytest.raises(NotImplementedError):
        _account.activateFor(None, OfferCategory.AUTOMOTIVE)

    with pytest.raises(NotImplementedError):
        _account.activateFor([], OfferCategory.AUTOMOTIVE)

    activations = _account.activateFor(offerIDs = [ '4734', '5662', ])
    assert isinstance(activations, list)
    if activations:
        activation = activations[0]
        assert isinstance(activation, TripleObject)
        assert activation.objID
        assert activation.merchantName
        assert OfferDeliveryMode(activation.offerMode)


_viewAuth = Auth(_config['tokenURL'], clientID = _config['clientID'], clientSecret = _config['secret'], scope = Scope.VIEW_OFFERS)

def test_CardAccount_findOffers():
    offers = _account.findOffers(
        filterType = OfferType.CARD_LINKED,
        latitude = 40.46,
        longitude = -79.92,
        pageOffset = 0,
        pageSize = 25,
        radius = 35000,
        textQuery = "italian food",
        viewAuth = _viewAuth,
    )
    assert isinstance(offers, list)
    assert len(offers)
    assert offers[0].objID

    offers = _account.findOffers(
        countryCode = KNOWN_COUNTRY_CODE,
        postalCode = KNOWN_POSTAL_CODE,
        filterType = OfferType.CARD_LINKED,
        pageOffset = 0,
        pageSize = 25,
        radius = 35000,
        textQuery = "italian food",
        viewAuth = _viewAuth,
    )
    assert isinstance(offers, list)
    assert len(offers)
    assert offers[0].objID

    offers = _account.findOffers(
        countryCode = KNOWN_COUNTRY_CODE,
        postalCode = KNOWN_POSTAL_CODE_LONG,
        filterType = OfferType.CARD_LINKED,
        pageOffset = 0,
        pageSize = 25,
        radius = 35000,
        textQuery = "italian food",
        viewAuth = _viewAuth,
    )
    assert isinstance(offers, list)
    assert len(offers)
    assert offers[0].objID

    # Incomplete query - missing lat or long
    with pytest.raises(CallError):
        _account.findOffers(
            filterType = OfferType.CARD_LINKED,
            latitude = 40.46,
            pageOffset = 0,
            pageSize = 25,
            radius = 35000,
            textQuery = "italian food",
            viewAuth = _viewAuth,
        )

    # Incomplete query - missing country or postal code
    with pytest.raises(CallError):
        _account.findOffers(
            postalCode = KNOWN_POSTAL_CODE_LONG,
            filterType = OfferType.CARD_LINKED,
            pageOffset = 0,
            pageSize = 25,
            radius = 35000,
            textQuery = "italian food",
            viewAuth = _viewAuth,
        )

    # Invalid country test
    with pytest.raises(NotImplementedError):
        _account.findOffers(
            countryCode = 'RU',
            postalCode = '125009',
            filterType = OfferType.CARD_LINKED,
            pageOffset = 0,
            pageSize = 25,
            radius = 35000,
            textQuery = "italian food",
            viewAuth = _viewAuth,
        )


    # Valid Auth instance, wrong scope
    with pytest.raises(ForbiddenError):
        _account.findOffers(
            countryCode = KNOWN_COUNTRY_CODE,
            postalCode = KNOWN_POSTAL_CODE,
            filterType = OfferType.CARD_LINKED,
            pageOffset = 0,
            pageSize = 25,
            radius = 35000,
            textQuery = "italian food",
            viewAuth = _auth,
        )

    # Invalid auth instance
    with pytest.raises(InvalidPayloadError):
        _account.findOffers(
            countryCode = KNOWN_COUNTRY_CODE,
            postalCode = KNOWN_POSTAL_CODE,
            filterType = OfferType.CARD_LINKED,
            pageOffset = 0,
            pageSize = 25,
            radius = 35000,
            textQuery = "italian food",
            viewAuth = 42.69,
        )


def test_CardAccount_fetchOffer():
    offerViewerAccount = CardAccount(KNOWN_ACCT_ID)

    # Happy path test latitude, longitude:
    offerDetails = offerViewerAccount.fetchOffer(
            KNOWN_OFFER_ID,
            latitude = 49.46,
            longitude = -79.92,
            radius = 35000,
            viewAuth = _viewAuth
        )
    assert isinstance(offerDetails, CardholderOfferDetails)
    assert isinstance(offerDetails.offer, CardholderOffer)

    # Happy path test country, postalCode:
    offerDetails = offerViewerAccount.fetchOffer(
            KNOWN_OFFER_ID,
            countryCode = KNOWN_COUNTRY_CODE,
            postalCode = KNOWN_POSTAL_CODE_LONG,
            radius = 35000,
            viewAuth = _viewAuth
        )
    assert isinstance(offerDetails, CardholderOfferDetails)
    assert isinstance(offerDetails.offer, CardholderOffer)

    with pytest.raises(UnprocessablePayload):
        offerViewerAccount.fetchOffer(
            'BOGUs',
            countryCode = KNOWN_COUNTRY_CODE,
            postalCode = KNOWN_POSTAL_CODE_LONG,
            radius = 35000,
            viewAuth = _viewAuth
        )

    with pytest.raises(CallError):
        offerViewerAccount.fetchOffer(
                KNOWN_OFFER_ID,
                postalCode = KNOWN_POSTAL_CODE_LONG,
                viewAuth = _viewAuth
            )

    with pytest.raises(ForbiddenError):
        offerViewerAccount.fetchOffer(
            KNOWN_OFFER_ID,
            countryCode = KNOWN_COUNTRY_CODE,
            postalCode = KNOWN_POSTAL_CODE_LONG,
            radius = 35000,
        )


# @pytest.mark.skip('Implementation errors in CardProgram prevent test')
def test_CardAccount_byExternalID():
    acct = CardAccount.byExternalID(KNOWN_ACCT_EXT_ID, viewAuth = _viewAuth)
    control = CardAccount(KNOWN_ACCT_ID)
    assert acct.objID == control.objID

    # Try a non-existent ID
    acct = CardAccount.byExternalID('boguzz', viewAuth = _viewAuth)
    assert not acct

