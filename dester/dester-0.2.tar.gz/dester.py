"""
A linter to modify LaTeX files.
"""
__version__ = "0.2"

# pylint: disable=no-value-for-parameter, line-too-long, too-many-arguments, too-many-locals
import os
import platform
import re
import click

@click.command()
@click.argument("input_file", type=click.Path(exists=True), required=True)
@click.option("--comment", default=1, type=int, help="How many spaces to insert after %?")
@click.option("--newline", default=True, type=bool, help="Insert a new line after a sentence?")
@click.option("--indent", default=4, type=int, help="Indent content within the block.")
@click.option("--blank_lines", default=1, type=int, help="Number of blank lines to be inserted before section/chapter etc.")
@click.option("--overwrite", default=False, type=bool, help="Overwrite the original input file.")
def main(input_file, comment, newline, indent, blank_lines, overwrite):
    """
    the main function to check all the parameters and execute the program
    """
    file_name, file_extension = os.path.splitext(input_file)
    if platform.system() == "Windows":
        escape_seq = "\r\n"
    else :
        escape_seq = "\n"

    if overwrite:
        output_file = input_file
    else:
        output_file = f"{file_name}-edited{file_extension}"

    if file_extension in (".tex", ".bib", ".tikz"):
        with open(input_file, "r", encoding="utf-8") as _f:
            content = _f.readlines()
            formatted_comments_content = comment_rule_main(content, comment)
            if newline:
                formatted_newline_content = newline_rule_main(formatted_comments_content, escape_seq)
                formatted_indent_content = indentation_rule_main(formatted_newline_content, indent)
                formatted_sections_content = blank_line_rule_main(formatted_indent_content, blank_lines, escape_seq)
            else:
                formatted_indent_content = indentation_rule_main(formatted_comments_content, indent)
                formatted_sections_content = blank_line_rule_main(formatted_indent_content, blank_lines, escape_seq)
        with open(output_file, "w", encoding="utf-8") as output:
            for lines in formatted_sections_content:
                output.write(lines)
        print(f"Successfully modified the file {input_file}")
    else:
        print("Wrong file extension")
        return

def blank_line_rule_main(content, number_of_blank_lines, escape_seq):
    """
    indentifies section\\subsection\\subsubsection\\chapter\\paragraph\\subparagraph
    and insertes a blank line before it
    """
    content_formatted_sections = []
    blank_lines = escape_seq * number_of_blank_lines
    for line in content:
        current_line_index = content.index(line)
        prev_line_index = current_line_index - 1
        if re.search(r"^\\section|^\\subsection|^\\chapter|^\\subsubsection|^\\paragraph|^\\subparagraph", line) \
           and content[prev_line_index] != "\n":
            content_formatted_sections.append(f"{blank_lines}{line}")
        else:
            content_formatted_sections.append(line)
    return content_formatted_sections

def comment_rule_main(content, number_of_space):
    """
    the main function which identifies the lines with comments
    """
    content_formatted_comments = []
    for line in content:
        # if there are more than one % sign as a comment
        if re.search(r"^%{2,}[^ %]", line):
            result = comment_rule_many_percent_signs(number_of_space, line)
            content_formatted_comments.append(result)
        # one % sign as a comment
        elif re.search(r"^%[^ %]", line):
            result = comment_rule_one_percent_sign(number_of_space, line)
            content_formatted_comments.append(result)
        else:
            content_formatted_comments.append(line)
    return content_formatted_comments

def comment_rule_one_percent_sign(comment, line):
    """
    modifies the line with one % sign as a comment
    """
    num_of_spaces = comment * " "
    modified_line = f"{line[0]}{num_of_spaces}{line[1:]}"
    return modified_line

def comment_rule_many_percent_signs(comment, line):
    """
    modifies the line where there are more than one % sign
    """
    num_of_spaces = comment * " "
    match = re.search(r"%{2,}[^\s]", line)
    end = match.span()[1]
    modified_line = f"{line[0:end-1]}{num_of_spaces}{line[end-1:]}"
    return modified_line

def indentation_rule_main(content, number_of_spaces):
    """
    identifies the block and inserts indentation within that block
    """
    content_formatted_indentation = []
    marker = False
    number_of_spaces = number_of_spaces * " "
    for index, line in enumerate(content):
        # finds where the block starts
        if re.search(r"^\\begin{(?!document).*}", line):
            content_formatted_indentation.append(line)
            # loops through the lines within the block
            for line_within_the_block in content[index+1:]:
                # finds where the block stops,
                # sets marker to False to help the main for loop skip already indented block
                if re.search(r"^\\end{(?!document).*}", line_within_the_block):
                    marker = True
                    break
                # indents the line within the block
                if not re.search(r"^\s", line_within_the_block):
                    index +=1
                    content_formatted_indentation.append(number_of_spaces + line_within_the_block)
                else:
                    index +=1
                    content_formatted_indentation.append(line_within_the_block)
        # reverses marker to start appending the lines outside of the block
        elif re.search(r"^\\end{(?!document).*}", line):
            content_formatted_indentation.append(line)
            marker = False
        else:
            if marker:
                pass
            else:
                content_formatted_indentation.append(line) # appends lines outside of the block
    return content_formatted_indentation

def newline_rule_main(content, escape_seq):
    """
    identifies a sentence and inserts a newline after it
    """
    content_formatted_newlines = []
    for original_line in content:
        current_line_index = content.index(f"{original_line}")
        next_line_index = current_line_index + 1
        if re.search(r"^(?![%]).*[\.!?;:]$", original_line) and content[next_line_index] != "\n":
            content_formatted_newlines.append(f"{original_line}{escape_seq}")
        else:
            content_formatted_newlines.append(original_line)
    return content_formatted_newlines

if __name__ == "__main__":
    main()
