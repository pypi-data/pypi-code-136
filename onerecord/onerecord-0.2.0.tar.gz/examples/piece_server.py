from onerecord import ONERecordClient
from onerecord.models.cargo import *
from datetime import datetime

"""
Freight on Hand Shipment with Pieces

Description:
Create a shipment with pieces and add FOH event to pieces and shipments
"""

COMPANY_IDENTIFIER: str = "gdpr"

pieces: list[Piece] = []
host = "localhost"
port = 8080
host = "team-gdpr.one-record.de"
port = 443
client = ONERecordClient(company_identifier=COMPANY_IDENTIFIER, ssl=True,
                         host=host, port=port)
# Pieces
for i in range(0, 10):
    pieces.append(
        Piece(
            **{
                "upid": f"4711-1337-{i + 1}",
                "company_identifier": COMPANY_IDENTIFIER,
                "goods_description": "six pack of Koelsch beer",
                "gross_weight": {"unit": "KGM", "value": 3.922},
                "handling_instructions": [{
                    "service_type": "OSI",
                    "service_description": "please dont stack",
                    "requested_by": {
                        "first_name": "Max",
                        "last_name": "Mustermann",
                        "job_title": "Brewmaster"
                    }
                },
                ]
            }
        )
    )

for piece in pieces:
 client.create_logistics_object(piece)

# Shipment
# Remark: Total Gross Weight includes extra packing material of 1.5 kg
shipment: Shipment = Shipment(

    company_identifier=COMPANY_IDENTIFIER,
    total_gross_weight=Value(
        unit="KGM",
        value=sum(piece.gross_weight.value for piece in pieces) + 1.5,
    ),
    volumetric_weight=[VolumetricWeight(chargeable_weight=Value(unit="KGM",
                                                                value=sum(
                                                                    piece.gross_weight.value
                                                                    for piece
                                                                    in
                                                                    pieces)))],
    contained_pieces=pieces,
    parties=[
        Party(party_role="SHIPPER", party_details=Company(company_name="Shipper United",
                                                          branch=CompanyBranch(
                                                              branch_name="Shipper United Germany",
                                                              contact_persons=[
                                                                  Person(
                                                                      first_name="John",
                                                                      last_name="Doe",
                                                                      job_title="CEO"),
                                                                  Person(
                                                                      first_name="Erika",
                                                                      last_name="Musterfrau",
                                                                      job_title="Driver"),
                                                                  Person(
                                                                      first_name="James",
                                                                      last_name="Bond",
                                                                      job_title="Agent")
                                                              ]
                                                              )))]
)

client.create_logistics_object(shipment)

# print result
for piece in pieces:
    print(f"created Piece: {piece.id}")
print(f"created Shipment: {shipment.id}")

## Create Waybill
waybill: Waybill = Waybill(
    id="https://team-gdpr.one-record.de/companies/gdpr/los/waybill-010-123458",
    company_identifier=COMPANY_IDENTIFIER,
    waybill_number="010-123458",
    carrier_declaration_signature="Austin Powers",
    carrier_declaration_place=Location(location_name="London Heathrow",
                                       location_type="AIRPORT", code="LHR"),
    carrier_declaration_date=datetime.strptime('09/19/18 13:55:26',
                                               '%m/%d/%y %H:%M:%S'),
    booking=BookingOption(
        company_identifier=COMPANY_IDENTIFIER,
        request_ref=BookingOptionRequest(
            company_identifier=COMPANY_IDENTIFIER,
        ),
        shipment_details=shipment
    )
)
client.create_logistics_object(waybill)
print(f"created Shipment: {waybill.id}")
