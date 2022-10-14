from sysflow.utils.common_utils.bash_utils import bash
from sysflow.utils.common_utils.file_utils import dump
from glob import glob
import re
from sysflow.utils.common_utils.re_utils import num_regex


def merge_pdf():
    """
    Merge all pdf files in a directory into one pdf file.
    """

    # Note: One might need to manually name the file with the number
    # For example, 1.pdf, 2.pdf, 3.pdf, etc.
    pdf_files = glob("*.pdf")
    pdf_files = list(
        filter(lambda pdf_file: re.findall(rf"{num_regex}.pdf", pdf_file), pdf_files)
    )
    pdf_files = sorted(pdf_files, key=lambda x: int(re.findall(num_regex, x)[0]))
    pdf_filestr = "\n".join(
        [
            r"\includepdf[pages=-,pagecommand={},width=\textwidth]{" + pdf_file + r"}"
            for pdf_file in pdf_files
        ]
    )

    tex_str = (
        r"""\documentclass{article}   	% use "amsart" instead of "article" for AMSLaTeX format
    \usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.
    \geometry{letterpaper}                   		% ... or a4paper or a5paper or ... 


    \usepackage{pdfpages}
    \begin{document}
    """
        + pdf_filestr
        + r"""
    \end{document}"""
    )

    dump(tex_str, "out.tex")  # For debugging purposes
    bash("pdflatex out.tex")  # Compile the tex file to pdf
    bash("rm *.aux *.log *.tex *.dvi")  # Remove auxiliary files
