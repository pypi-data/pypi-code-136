from markdown import markdown


def joke(a: str) -> object:
    """

    :param a:
    :type a:
    :return:
    :rtype:
    """
    return markdown(
        "Wenn ist das Nunst\u00fcck git und Slotermeyer?"
        "Ja! ... **Beiherhund** das Oder die Flipperwaldt "
        "gersput."
    )
