import re

from bs4 import BeautifulSoup
from bs4.element import Tag

from attrDatas import TypoGraphy, EmojiGraph


class Parser(object):

    def __init__(self, markdown: str, cssFiles: list = None, jsFiles: list = None, title: str = "No Title") -> None:
        """
        Initialize the parser
        markdown: str
        cssFiles: list
        """
        self.typoParser = TypoGraphy()
        self.emojiParser = EmojiGraph()
        self.markdown = markdown
        self.html = ""
        self.cssFiles = cssFiles
        self.jsFiles = jsFiles
        self.title = title
        self.parse()
        self.soup = BeautifulSoup(self.html, "html.parser")
        # print(self.soup.prettify())

    def headingParser(self, heading: str) -> None:
        """
        # Heading -> level 1
        ## Heading -> level 2
        ### Heading -> level 3
        ...
        """
        level = heading.count("#")
        level = min(level, 6)
        heading = heading.replace("#", "")
        heading = heading.strip()

        # check for TypoGraphys and EmojiGraphs
        for typo in self.typoParser.LIST_TYPOS:
            if typo in heading:
                heading = heading.replace(
                    typo, self.typoParser.LIST_TYPOS[typo])

        for emoji in self.emojiParser.LIST_EMOJIS:
            if emoji in heading:
                heading = heading.replace(
                    emoji, self.emojiParser.LIST_EMOJIS[emoji])
        heading = f"<h{level}>{heading}</h{level}>"
        self.html += heading
        print(heading)
        return heading

    def codeParser(self, code: str) -> None:
        """
        ```python
        print("Hello World")
        ```
        """
        code = code.replace("```", "")
        code = code.splitlines()
        # print(code)
        language = code[0].split(" ").pop(0)
        # print(language)
        code = code[1:]
        theCode = "".join(f"\n{code[i]}" for i in range(len(code)))
        # print(theCode)
        code = f'<pre><code class="{language}">{theCode}</code></pre>'
        print(code)
        self.html += code
        return code

    def linkParser(self, link: str) -> None:
        """
        [Google](https://www.google.com)
        """
        link = link.replace("[", "")
        link = link.replace("]", "")
        link = link.split("(")
        link = f'<a href="{link[1].rstrip(")")}" target="_blank">{link[0]}</a>'
        print(link)

        self.html += link
        return link

    def imageParser(self, image: str) -> None:
        """
        ![Google](https://www.google.com)
        """
        image = image.replace("![", "")
        image = image.replace("]", "")
        image = image.split("(")
        image = f'<img src="{image[1].rstrip(")")}" alt="{image[0]}">'
        print(image)

        self.html += image
        return image

    def linkImageParser(self, linkImage: str) -> None:
        """
        [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
        """
        linkImage = linkImage.replace("[![", "")
        linkImage = linkImage.replace("]", "")
        linkImage = linkImage.split("(")
        linkImage = f'<a href="{linkImage[2].rstrip(")")}" target="_blank"><img src="{linkImage[1].rstrip(")")}" alt="{linkImage[0]}"></a>'
        print(linkImage)
        self.html += linkImage
        return linkImage

    def paragraphParser(self, paragraph: str) -> None:
        """
        Paragraph
        """
        # check if the paragraph is empty
        if not paragraph:
            print("<br>")
            self.html += "<br>"
            return "<br>"

        # check for TypoGraphys
        for typo in self.typoParser.LIST_TYPOS:
            if typo in paragraph:
                paragraph = paragraph.replace(
                    typo, self.typoParser.LIST_TYPOS[typo])

        # check for EmojiGraphs
        for emoji in self.emojiParser.LIST_EMOJIS:
            if emoji in paragraph:
                paragraph = paragraph.replace(
                    emoji, self.emojiParser.LIST_EMOJIS[emoji])

        # check if the paragraph is a list
        if paragraph.startswith("* ") or paragraph.startswith("- ") or paragraph.startswith("+ "):
            paragraph = paragraph.replace("* ", "")
            paragraph = paragraph.replace("- ", "")
            paragraph = paragraph.replace("+ ", "")

            paragraph = f"<li>{paragraph}</li>"
            print(paragraph)
            paragraph = f"<ul>{paragraph}</ul>"
            self.html += paragraph
            return paragraph

        # check if the paragraph is a blockquote
        if paragraph.startswith(">"):
            paragraph = paragraph.replace(">", "")
            paragraph = f"<blockquote>{paragraph}</blockquote>"
            print(paragraph)
            self.html += paragraph
            return paragraph

        # check if the paragraph is a horizontal rule
        if paragraph.startswith("---") or paragraph.startswith("***"):
            paragraph = "<hr>"
            print(paragraph)
            self.html += paragraph
            return paragraph

        # check if the paragraph is a table
        if paragraph.startswith("|"):
            paragraph = paragraph.replace("|", "")
            paragraph = paragraph.splitlines()
            # print(paragraph)
            table = "<table>"
            for line in paragraph:
                line = line.split()
                # print(line)
                table += "<tr>"
                for cell in line:
                    table += f"<td>{cell}</td>"
                table += "</tr>"
            table += "</table>"
            print(table)
            self.html += table
            return table

        # use regex to find and match all the links, bold, italic, strikethrough, inline code
        # and replace them with their html tags
        paragraph = re.sub(r"\[(.*?)\]\((.*?)\)",
                           r'<a href="\2">\1</a>', paragraph)
        paragraph = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", paragraph)
        paragraph = re.sub(r"\*\*\*(.*?)\*\*\*",
                           r"<strong><em>\1</em></strong>", paragraph)
        paragraph = re.sub(r"\*(.*?)\*", r"<em>\1</em>", paragraph)
        paragraph = re.sub(r"__(.*?)__", r"<strong>\1</strong>", paragraph)
        paragraph = re.sub(r"_(.*?)_", r"<em>\1</em>", paragraph)
        paragraph = re.sub(r"~~(.*?)~~", r"<del>\1</del>", paragraph)
        paragraph = re.sub(r"`(.*?)`", r"<code>\1</code>", paragraph)

        paragraph = f"<p>{paragraph}</p>"
        print(paragraph)

        self.html += paragraph
        return paragraph

    def parse(self) -> None:
        lines = self.markdown.splitlines()
        while lines:
            line = lines.pop(0)
            if line.startswith("#"):
                self.headingParser(line)
            elif line.startswith("```"):
                theLine = line + "\n"
                while lines:
                    # find the line with ``` at the end
                    if lines[0].endswith("```"):
                        theLine += f" {lines.pop(0)}\n"
                        break
                    else:
                        theLine += f" {lines.pop(0)}\n"
                self.codeParser(theLine)

            elif line.startswith("["):
                if line.startswith("[!["):
                    self.linkImageParser(line)
                elif line.startswith("!["):
                    self.imageParser(line)
                else:
                    self.linkParser(line)
            elif line.startswith("!"):
                self.imageParser(line)
            else:
                self.paragraphParser(line)

        # Last regex match for bold and italic
        self.html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", self.html)
        self.html = re.sub(r"\*\*\*(.*?)\*\*\*",
                           r"<strong><em>\1</em></strong>", self.html)
        self.html = re.sub(r"\*(.*?)\*", r"<em>\1</em>", self.html)
        self.soup = BeautifulSoup(self.html, "html.parser")

        htmlTop = f"""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>{self.title}</title>
                        </head>
                        <body>
                            <article class='markdown-body'>
                        """
        htmlBottom = """
                            </article>
                        </body>
                        </html>
                    """
        # Add a html top and bottom
        self.html = htmlTop + self.html + htmlBottom

    def toHTML(self) -> str:
        return self.soup.prettify()

    def addCSSs(self) -> None:
        for css in self.cssFiles:
            # if there is no head tag, create one
            if not self.soup.head:
                self.soup.head = self.soup.new_tag("head")
            # add the link tag
            link = self.soup.new_tag("link", rel="stylesheet", href=css)
            self.soup.head.append(link)

            # insert the head tag to the html tag
            self.soup.html.insert(0, self.soup.head)

    def addstyle(self) -> None:
        self.soup.head.append(self.soup.new_tag("style", type="text/css"))
        self.soup.head.style.append(self.style)

    def addJSs(self) -> None:
        for js in self.jsFiles:
            # if there is no body tag, create one
            if not self.soup.body:
                self.soup.body = self.soup.new_tag("body")
            # add the script tag
            script = self.soup.new_tag("script", src=js)
            self.soup.body.append(script)

            # insert the body tag to the html tag
            self.soup.html.append(self.soup.body)


if __name__ == "__main__":
    md = open("TEST.md", "r").read()
    ccs = ["TEST.css"]
    # js = ["https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/highlight.min.js"]
    parser = Parser(markdown=md, cssFiles=ccs, title="TEST")
    parser.addCSSs()
    # parser.addJSs()

    with open("TEST.html", "w") as f:
        f.write(parser.toHTML())
