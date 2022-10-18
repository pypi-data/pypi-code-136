"""Code for displaying the command sheet -catalog."""

from textwrap import dedent
from textwrap import wrap


def header():
    """
    ████████████████████████████████████████████████████████████████████████████
    █─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▀█▀─▄██▀▄─██▄─▀█▄─▄█▄─▄▄▀█─▄▄▄▄█─█─█▄─▄▄─█▄─▄▄─█─▄─▄─█
    █─███▀█─██─██─█▄█─███─█▄█─███─▀─███─█▄▀─███─██─█▄▄▄▄─█─▄─██─▄█▀██─▄█▀███─███
    ▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀
    """
    print(dedent(header.__doc__))


def format_section_heading(heading, index, surround='[]'):
    if not surround or not surround.strip():
        return heading if index is None else f'{index}. {heading}'
    if index is not None:
        return surround[0] + f'{index}. {heading}' + surround[1]
    return surround[0] + heading + surround[1]


# Tries to achieve the following:
#
#    <section command>............... <section's way too long description
#                                      string here, so it is split like
#                                      this, like the argparse does with
#                                      the help messages> :)
#
# Instead of:
#
#    <section command>............... <section's way too long description
#    string here, which is not split like the example above, and looks kinda
#    ugly and not readable, especially when more commands starts to pile up> :(
#
def format_section_content(cmd, desc, indent, fillchar, max_width):
    desc_split = wrap(desc, width=max_width)
    desc_indent = []

    for idx, sentence in enumerate(desc_split):
        # Don't indent the first line of the description,
        # we're going to do that with the f-string later.
        if idx == 0:
            desc_indent.append(sentence)
        else:
            desc_indent.append(' '*(indent + 1) + sentence)

    desc_wrapped = '\n'.join(desc_indent)
    return f'{cmd:{fillchar}<{indent}} {desc_wrapped}'


def display_commandsheet(commandsheet, *, fillchar, section_numbers):
    max_width = 40
    index_start = 1
    indent = 50

    for idx, section in enumerate(commandsheet, start=index_start):
        # Format section heading
        section_heading = format_section_heading(
            section.name, index=idx if section_numbers else None,
        )

        # Print section heading
        print(section_heading)

        # Print section contents
        for cmd, desc in section.contents:
            line = format_section_content(
                cmd,
                desc,
                indent=indent,
                fillchar=fillchar,
                max_width=max_width
            )
            print(line)
        print()
