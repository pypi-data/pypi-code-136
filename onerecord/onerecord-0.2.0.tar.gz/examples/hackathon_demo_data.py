from onerecord.models.api import PatchRequest
from onerecord.models.cargo import Piece, Shipment, Location, Event, Value
from onerecord import ONERecordClient
from datetime import datetime

"""
Patch Piece

Description:
Create a piece and patch the gross weight
"""

COMPANY_IDENTIFIER: str = "cgnbeerbrewery"

# Create ONERecordClient
client = ONERecordClient(company_identifier=COMPANY_IDENTIFIER)

# Create Piece
piece: Piece = Piece(
    **{
        "upid": f"4711-1337-1",
        "company_identifier": COMPANY_IDENTIFIER,
        "goods_description": "six pack of Koelsch beer",
        "gross_weight": {"unit": "KGM", "value": 3.922},
    }
)

client.create_logistics_object(piece)

print(piece.id)

piece.gross_weight = Value(unit="KGM", value=4.0)

# Update Piece
client.update_logistics_object(piece)
print(piece.gross_weight)
print(client.get_logistics_object_by_uri(piece.id))
