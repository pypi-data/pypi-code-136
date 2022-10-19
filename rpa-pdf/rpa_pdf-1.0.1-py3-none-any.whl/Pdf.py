"""
Pdf module provides features to work with pdf files: merge pdfs, add stamps, print to the printer
"""
from io import BufferedReader
import os.path
from typing import Literal
import tempfile
import subprocess
import PyPDF2.filters
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from fpdf import FPDF
from barcode import Code39
from barcode.writer import ImageWriter

class Pdf():
    """ Pdf class """
    def __init__(self) -> None:
        self.__root_dir__: str = os.path.dirname(os.path.abspath(__file__))
        self.__fonts_dir__: str = os.path.join(self.__root_dir__, 'fonts')
        self.__exec_dir__: str = os.path.join(self.__root_dir__, 'exec')

    def compress(self, pdf_file_path: str) -> None:
        """ Compress pdf file to decrease the file size """
        try:
            if os.path.exists(pdf_file_path) is False:
                raise FileNotFoundError

            writer = PyPDF2.PdfFileWriter()
            reader = PyPDF2.PdfFileReader(pdf_file_path)
            for i in range(0, reader.numPages):
                page: PyPDF2.pdf.PageObject = reader.getPage(i)
                page.compressContentStreams()
                writer.addPage(page)
            with open(pdf_file_path, 'wb') as pdf:
                writer.write(pdf)
        except Exception as ex:
            raise Exception from ex


    def text_to_pdf(
        self,
        text: str,
        output_file_path: str,
        font_family: str = 'DejaVu Sans',
        font_file_path: str | bool = False,
        font_unicode: bool = True,
        font_style: Literal['', 'B', 'I', 'U', 'BU', 'UB', 'BI', 'IB', 'IU', 'UI', 'BIU', 'BUI', 'IBU', 'IUB', 'UBI', 'UIB'] = '',
        font_size: int = 12,
        text_vertical_position: Literal['top', 'center', 'bottom'] = 'top',
        text_horizontal_position: Literal['left', 'center', 'right'] = 'left',
        page_orientation: Literal['', 'portrait', 'landscape'] = 'portrait',
        page_units: Literal['', 'mm', 'pt', 'cm', 'in'] = 'mm',
        page_format: Literal['', 'A3', 'A4', 'A5', 'Letter', 'Legal'] | tuple[float, float] = 'A4',
        page_vertical_margin: int = 10,
        page_horizontal_margin: int = 10
    ) -> None:
        """
        Convert text to pdf file.\n\r
        Default font is DejaVu. You can change that by providing the font_family (ex. 'Arial') and the font_file_path (ex. 'c:/windows/fonts/Arial.ttf').\n\r
        Possible font formats: B - bold, I - italic, U - underline, and combinations: BI, BU, UIB, etc.\n\r
        Default font size is 12.\n\r
        Position of the text is determined by text_vertical_position: top (default), center, bottom and text_horizontal_position: left (default), center, right.\n\r
        """
        try:
            fpdf: FPDF = FPDF(orientation=page_orientation, unit=page_units, format=page_format)
            fpdf.compress = True
            # set style and size of font that you want in the pdf
            fpdf.add_font(font_family, '', font_file_path if isinstance(font_file_path, str) else f'{self.__fonts_dir__}\\DejaVuSans.ttf', font_unicode)
            fpdf.set_font(family=font_family, style=font_style, size=font_size)
            # add a page
            fpdf.add_page()
            # get text width
            string_width: float = fpdf.get_string_width(text)
            # set position of text
            x_pos: float = self._set_x_pos_(text_horizontal_position, page_horizontal_margin, fpdf.w, string_width)
            y_pos: float = self._set_y_pos_(text_vertical_position, page_vertical_margin, fpdf.h, font_size)
            # add text
            fpdf.text(x_pos, y_pos, text)
            # save the pdf with name .pdf
            fpdf.output(output_file_path)
        except Exception as ex:
            raise Exception from ex

    def add_code39_stamp(
        self,
        input_pdf_file_path: str,
        output_pdf_file_path: str,
        code: str,
        width: float = 40,
        height: float = 20,
        apply_for_pages: Literal['all', 'first', 'last'] | list[int] = 'first',
        remove_input_file: bool = False,
        vertical_position: Literal['top', 'center', 'bottom'] = 'top',
        horizontal_position: Literal['left', 'center', 'right'] = 'left',
        page_orientation: Literal['portrait', 'landscape'] = 'portrait',
        page_units: Literal['mm', 'pt', 'cm', 'in'] = 'mm',
        page_format: Literal["a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"] | tuple[float, float] = 'A4',
        page_vertical_margin: int = 0,
        page_horizontal_margin: int = 0
    ) -> None:
        """
        Add CODE39 barcode to the pdf file and save the output as a new pdf file.\n\r
        The barcode can be applied to all pages, only to the first (default) or the last page, or to specified pages (ex. [0,3,5]).\n\r
        Position of the barcode is controlled by vertical_position: top (default), center, bottom and horizontal_position: left (default), center, right.\n\r
        """
        
        try:
            # check if input file exists
            if os.path.exists(input_pdf_file_path) is False:
                raise FileNotFoundError
            # render barcode image
            barcode_image_path: str = tempfile.gettempdir() + '\\barcode.png'
            Code39(code=code, writer=ImageWriter(), add_checksum=False).write(barcode_image_path)

            # generate a stamp pdf file
            stamp: str = tempfile.gettempdir() + '\\stamp.pdf'
            fpdf: FPDF = FPDF(orientation=page_orientation, unit=page_units, format=page_format)
            fpdf.compress = False
            fpdf.add_page()
            fpdf.image(
                name=barcode_image_path,
                x=self._set_x_pos_(horizontal_position, page_horizontal_margin, fpdf.w, width),
                y=self._set_y_pos_(vertical_position, page_vertical_margin, fpdf.h, height),
                w=width,
                h=height,
                type='PNG'
            )
            fpdf.output(stamp)
        
            # get watermark page
            watermark_file: BufferedReader = open(stamp, 'rb')
            watermark = PdfFileReader(watermark_file).getPage(0)

            # get input pdf file
            input_file: BufferedReader = open(input_pdf_file_path, 'rb')
            pdf_document: PdfFileReader = PdfFileReader(input_file)

            # get indexes of pages where the stamp should be added
            if not isinstance(apply_for_pages, list):
                match apply_for_pages:
                    case 'all':
                        apply_for_pages = [index for index in range(
                            0, pdf_document.getNumPages())]
                    case 'last':
                        apply_for_pages = [-1]
                    case 'first':
                        apply_for_pages = [0]
                    case _:
                        raise Exception('incorrect value of apply_for_pages argument')

            # prepare output pdf
            output: PdfFileWriter = PdfFileWriter()
            
            # add a stamps
            for page_index in range(0, pdf_document.getNumPages()):
                page = pdf_document.getPage(page_index)
                if page_index in apply_for_pages:
                    page.mergePage(watermark)
                output.addPage(page)

            # save the output file
            with open(output_pdf_file_path, 'wb') as output_file:
                output.write(output_file)

            # close files
            watermark_file.close()
            input_file.close()

            # try to clean out temp files
            try:
                if os.path.exists(stamp):
                    os.remove(stamp)
                if os.path.exists(barcode_image_path):
                    os.remove(barcode_image_path)
                if remove_input_file and os.path.exists(input_pdf_file_path):
                    os.remove(input_pdf_file_path)
            except (FileNotFoundError) as ex:
                print(ex)
        except Exception as ex:
            raise Exception from ex

    def merge(self, pdf_files: list, output_pdf_file_path: str) -> None:
        """
        Merge given pdf files.\n\r
        Inputs: 
        - pdf_files: list - list of paths to pdf files, 
        - output_pdf_file_path: str - path of the output pdf file
        \n\r
        """
        try:
            # check if input file exists
            for file_path in pdf_files:
                if os.path.exists(file_path) is False:
                    raise FileNotFoundError

            merge_file: PdfFileMerger = PdfFileMerger()
            for pdf_file in pdf_files:
                with open(pdf_file, 'rb') as content:
                    merge_file.append(PdfFileReader(content))

            merge_file.write(output_pdf_file_path)
            merge_file.close()
        except Exception as ex:
            raise Exception from ex

    def add_text_stamp(
        self,
        input_pdf_file_path: str,
        output_pdf_file_path: str,
        text: str, *,
        apply_for_pages: Literal['all', 'first', 'last'] | list[int] = 'first',
        remove_input_file: bool = False,
        font_family: str = 'DejaVu',
        font_file_path: str | bool = False,
        font_unicode: bool = True,
        font_style: Literal["", "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB"] = '',
        font_size: int = 12,
        text_vertical_position: Literal['top', 'center', 'bottom'] = 'top',
        text_horizontal_position: Literal['left', 'center', 'right'] = 'left',
        page_orientation: Literal['', 'portrait', 'landscape'] = 'portrait',
        page_units: Literal['', 'mm', 'pt', 'cm', 'in'] = 'mm',
        page_format: Literal["", "a3", "A3", "a4", "A4", "a5", "A5", "letter", "Letter", "legal", "Legal"] | tuple[float, float] = 'A4',
        page_vertical_margin: int = 10,
        page_horizontal_margin: int = 10
    ) -> None:
        """
        Add text (watermark/stamp) to the pdf document.\n\r
        Default font is DejaVu. You can change that by providing the font_family (ex. 'Arial') and the font_file_path (ex. 'c:/windows/fonts/Arial.ttf').\n\r
        Possible font formats: B - bold, I - italic, U - underline, and combinations: BI, BU, UIB, etc.\n\r
        Default font size is 12.\n\r
        Position of the text is determined by text_vertical_position: top (default), center, bottom and text_horizontal_position: left (default), center, right.\n\r
        The barcode can be applied to all pages, only to the first (default) or the last page, or to specified pages (ex. [0,3,5]).\n\r
        """
        try:
            # check if input file exists
            if os.path.exists(input_pdf_file_path) is False:
                raise FileNotFoundError

            # generate watermark pdf
            watermark_pdf_file_path = tempfile.gettempdir() + '\\stamp.pdf'
            self.text_to_pdf(
                text=text,
                output_file_path=watermark_pdf_file_path,
                font_family=font_family,
                font_file_path=font_file_path,
                font_unicode=font_unicode,
                font_style=font_style,
                font_size=font_size,
                text_vertical_position=text_vertical_position,
                text_horizontal_position=text_horizontal_position,
                page_orientation=page_orientation,
                page_units=page_units,
                page_format=page_format,
                page_vertical_margin=page_vertical_margin,
                page_horizontal_margin=page_horizontal_margin
            )

            # get watermark page
            watermark_file: BufferedReader = open(watermark_pdf_file_path, 'rb')
            watermark = PdfFileReader(watermark_file).getPage(0)

            # get input pdf file
            input_file: BufferedReader = open(input_pdf_file_path, 'rb')
            pdf_document: PdfFileReader = PdfFileReader(input_file)

            # get indexes of pages where the stamp should be added
            if not isinstance(apply_for_pages, list):
                match apply_for_pages:
                    case 'all':
                        apply_for_pages: list[int] = list(range(0, pdf_document.getNumPages()))
                    case 'last':
                        apply_for_pages = [-1]
                    case _:
                        apply_for_pages = [0]

            # prepare output pdf
            output: PdfFileWriter = PdfFileWriter()
            # add a stamps
            for page_index in range(0, pdf_document.getNumPages()):
                page = pdf_document.getPage(page_index)
                if page_index in apply_for_pages:
                    page.mergePage(watermark)
                output.addPage(page)

            # save the output file
            with open(output_pdf_file_path, 'wb') as output_file:
                output.write(output_file)

            # close files
            watermark_file.close()
            input_file.close()

            # try to clean out temp files
            try:
                if os.path.exists(watermark_pdf_file_path):
                    os.remove(watermark_pdf_file_path)
                if remove_input_file and os.path.exists(input_pdf_file_path):
                    os.remove(input_pdf_file_path)
            except (FileNotFoundError, FileExistsError) as ex:
                print(ex)

        except Exception as ex:
            raise Exception from ex

    def print(
        self,
        pdf_file_path: str,
        printer: str = 'default',
        pages: Literal['all', 'first', 'last'] | list = 'all',
        odd_or_even: Literal['odd', 'even'] | bool = False,
        orientation: Literal['portrait', 'landscape'] = 'portrait',
        scale: Literal['noscale', 'shrink', 'fit'] = 'fit',
        color: Literal['color', 'monochrome'] = 'color',
        mode: Literal['duplex', 'duplexshort', 'duplexshort', 'simplex'] = 'simplex',
        paper: Literal['A2', 'A3', 'A4', 'A5', 'A6', 'letter', 'legal', 'tabloid', 'statement'] = 'A4'
    ) -> None:
        """
        Print the pdf file on a given printer.\n\r
        Default printer will be used unless the printer name is defined with printer argument.
        """
        try:
            # check if input file exists
            if os.path.exists(pdf_file_path) is False:
                raise FileNotFoundError

            sumatra_path: str = f'{self.__exec_dir__}\\sumatra.exe'
            printer_mode: str = '-print-to-default' if printer == 'default' else f'-print-to "{printer}"'
            
            settings: list = []
            # page range to print
            if isinstance(pages, list):
                settings.append(",".join(pages))
            match pages.lower():
                case "first":
                    settings.append("1")
                case "last":
                    settings.append("-1")
                case "all":
                    settings.append("*")
                case _:
                    raise Exception("incorrect range of pages to print; correct vaules: all, first, last, or list (ex. [1,2,3-5,-1])")
            
            # page to print: odd or even or all
            if isinstance(odd_or_even, str):
                match odd_or_even.lower():
                    case 'odd':
                        settings.append('odd')
                    case 'even':
                        settings.append('even')
                    case _:
                        raise Exception("incorrect value for odd_or_even attribute; correct values: odd, even")

            # page orientation
            settings.append(orientation)

            # content scale
            settings.append(scale)

            # color
            settings.append(color)

            # print mode
            settings.append(mode)

            # paper size
            settings.append(f'paper={paper}')
            

            print_settings: str = f'-print-settings "{",".join(settings)}"'

            subprocess.run(f'{sumatra_path} {printer_mode} {print_settings} -silent {pdf_file_path}', check=True)
        except Exception as ex:
            raise Exception from ex
    
    def _set_x_pos_(self, horizontal_position, page_horizontal_margin, page_width, stamp_width) -> float:
        match horizontal_position:
            case 'center':
                return (page_width / 2) - (stamp_width / 2) + page_horizontal_margin
            case 'right':
                return page_width - stamp_width - page_horizontal_margin
            case _:
                return page_horizontal_margin

    def _set_y_pos_(self, vertical_position, page_vertical_margin, page_height, stamp_height) -> float:
        match vertical_position:
            case 'center':
                return (page_height / 2) - (stamp_height / 2) + page_vertical_margin
            case 'bottom':
                return page_height - stamp_height - page_vertical_margin
            case _:
                return page_vertical_margin
