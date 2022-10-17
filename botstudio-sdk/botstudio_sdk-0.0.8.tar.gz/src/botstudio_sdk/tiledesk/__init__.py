class Image:
    @staticmethod
    def td_image(
        image_url: str,
        width: int = None,
        height: int = None,
    ) -> str:
        """

        :param image_url: address of the image on the web
        :type image_url: str
        :param width:
        :type width: int
        :param height:
        :type height: int
        :return: string in Markbot language from Tiledesk
        :rtype: str
        """
        if width and height:
            return f"\ntdImage,w{width} h{height}:{image_url}"
        if width:
            return f"\ntdImage,w{width}:{image_url}"
        if height:
            return f"\ntdImage,h{height}:{image_url}"
        return f"\ntdImage:{image_url}"


class Button:
    @staticmethod
    def td_text_button(
        button_text: str,
    ) -> str:
        """

        :param button_text:
        :type button_text: str
        :return: string in Markbot language from Tiledesk
        :rtype: str
        """
        return f"\n* {button_text}"

    @staticmethod
    def td_new_tab_button(
        button_text: str,
        button_url: str,
    ) -> str:
        return f"\n* {button_text} {button_url}"

    @staticmethod
    def td_parent_tab_button(
        button_text: str,
        button_url: str,
    ) -> str:
        return f"\n* {button_text} < {button_url}"

    @staticmethod
    def td_widget_frame_button(
        button_text: str,
        button_url: str,
    ) -> str:
        return f"\n* {button_text} > {button_url}"


def td_frame(
    frame_url: str,
    width: int = None,
    height: int = None,
) -> str:
    if width and height:
        return f"\ntdFrame,w{width} h{height}:{frame_url}"
    if width:
        return f"\ntdFrame,w{width}:{frame_url}"
    if height:
        return f"\ntdFrame,h{height}:{frame_url}"
    return f"\ntdFrame:{frame_url}"


def td_video(
    video_url: str,
) -> str:
    return f"\ntdVideo:{video_url}"


def td_horizontal_rule_1() -> str:
    return "\n   \n***\n   "


def td_horizontal_rule_2() -> str:
    return "\n   \n---\n   "


def td_horizontal_rule_3() -> str:
    return "\n   \n___\n   "


def td_white_line() -> str:
    return "\n   "


def td_bold_text(text: str) -> str:
    return f"\n**{text}**"


def td_italic_text(text: str) -> str:
    return f"\n*{text}*"


def td_bold_and_italic_text(text: str) -> str:
    return f"\n***{text}***"


def td_heading_1(text: str) -> str:
    return f"\n   \n# {text}\n   "


def td_heading_2(text: str) -> str:
    return f"\n   \n## {text}\n   "


def td_heading_3(text: str) -> str:
    return f"\n   \n### {text}\n   "


def td_heading_4(text: str) -> str:
    return f"\n   \n#### {text}\n   "


def td_heading_5(text: str) -> str:
    return f"\n   \n##### {text}\n   "


def td_heading_6(text: str) -> str:
    return f"\n   \n###### {text}\n   "


if __name__ == "__main__":
    message = Image.td_image("video_url")

    message = td_video("video_url")
    message += Button.td_text_button("Ja")
    message += Button.td_text_button("Nee")

    print(message)
