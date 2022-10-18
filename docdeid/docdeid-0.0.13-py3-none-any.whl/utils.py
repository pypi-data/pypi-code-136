from docdeid.doc.document import Document


def annotate_intext(doc: Document) -> str:

    annotations = doc.annotations.sorted(
        by=["end_char"],
        callbacks={"end_char": lambda x: -x},
    )

    text = doc.text

    for annotation in annotations:

        text = (
            f"{text[:annotation.start_char]}"
            f"<{annotation.tag.upper()}>{annotation.text}</{annotation.tag.upper()}>"
            f"{text[annotation.end_char:]}"
        )

    return text
