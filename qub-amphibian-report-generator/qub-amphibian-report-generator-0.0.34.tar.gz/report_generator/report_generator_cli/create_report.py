"""# Create Report.

Application to create pdf report based on parameters passed into it

@Params:
        data_source         - Data source for report creation
        report_name         - Title of the report and the file name
        report_author       - Author of the report
        university_name     - Name of the university
        university_school   - Name of the university school

@Todo:
    - Implement detect data source type to allow for differing file types/sources?
    - Error handling
    - Remove hardcoded elements
    - Split functions further or into their own file
    - Refactor the create_x_section functions into one function that takes a section arg
    - Add a font loader
    - add a font specification

"""


import os
import sys
import time
from pathlib import Path

import fitz
import pandas
from fpdf import FPDF, TextMode
from loguru import logger

import report_generator.fonts as fonts
import report_generator.read_from_db.query_db
from report_generator.config import load_config
from report_generator.report_generator_cli.amphibian import AmphibianData


def create_report(
    data_source: str,
    options: dict,
    report_name: str,
    report_author: str,
    university_name: str,
    university_school: str,
    font_options: dict = None,
    pdf_chapters: str = None,
) -> None:
    """Create Report.

    Primary function that creates pdf object, sets fonts, calls
    component creation methods and saves output.

    Args:
        data_source         - Data source for report creation
        options  (dict)     - Dict with options passed from cli or gui
        font_options (dict) - Dict with options passed from font selection
        report_name         - Title of the report and the file name
        report_author       - Author of the report
        university_name     - Name of the university
        university_school   - Name of the university school

    """

    # Create report
    config = load_config()
    BASE_DIR_PATH = config["dir_path"]
    DATA_DIR_PATH = os.path.join(BASE_DIR_PATH, "data")
    os.path.join(DATA_DIR_PATH, "fonts")
    os.path.join(DATA_DIR_PATH, "images")
    os.path.join(DATA_DIR_PATH, "location")
    (Path(os.path.dirname(os.path.realpath(__file__)))).parent
    logger.debug(pdf_chapters)
    startTime = time.time()
    logger.info(f"Create Report Started: {report_name}")

    # load config
    config = load_config()

    if font_options is None:
        font_options = config["fonts"]

    curtime = time.time()
    logger.info("Started reading data source")
    ds = read_data_source(data_source, options)
    logger.info(f"Finished reading data source: {round(time.time() - curtime, 2)}s")

    pdf = FPDF()
    curtime = time.time()
    logger.info("Started adding fonts")
    fonts.add_font_choices_to_pdf(pdf, font_options)
    logger.info(f"Finished adding fonts: {round(time.time() - curtime,2)}s")

    curtime = time.time()
    logger.info("Started creating title page")
    pdf = create_title_page(
        report_name,
        report_author,
        university_name,
        university_school,
        pdf,
        config,
        font_options,
    )
    logger.info("Finished creating title page: {round(time.time() - curtime, 2)}s")

    curtime = time.time()
    logger.info("Started creating contents pages")
    pdf = create_contents_page(pdf, ds)
    logger.info(f"Finished creating contents pages: {round(time.time() - curtime, 2)}s")

    curtime = time.time()

    logger.info("Started inserting chapters")
    create_chapter_space(pdf, pdf_chapters)
    logger.info("Finished inserting chapters")

    logger.info("Started creating report pages")

    pdf = create_report_order_sections(ds, pdf, config, font_options)
    pdf_title = f"{'_'.join(report_name.split(' '))}.pdf"
    pdf_ouput_path = os.path.join(config["dir_path"], "report", pdf_title)
    pdf.output(pdf_ouput_path)

    logger.info(f"Finished creating report pages: {round(time.time() - curtime, 2)}s")
    fp = pdf_ouput_path
    fs = round(os.path.getsize(fp) / (1 << 20), 2)

    insert_chapter_pdf(fp, pdf_chapters)

    debug_mess = f"Create Report Finished: {report_name} - "
    debug_mess += f"Time Taken: {round((time.time() - startTime), 2)}s"
    debug_mess += ", File Size: "
    debug_mess += f"{fs}MB"
    logger.info(debug_mess)


def create_chapter_space(pdf, chapter_file_loc) -> object:
    """Create Space for chapters"""
    if chapter_file_loc != "":
        config = load_config()
        header_font = config["fonts"]["header_font"]
        header_size = config["fonts"]["header_size"]
        pdf.start_section(name="Introduction", level=0)
        pdf.set_font(header_font, "", header_size)
        pdf.ln(20)
        pdf.write(30, f"Report Section: ", "C")
    return pdf


def insert_chapter_pdf(pdf_file_loc, chapter_file_loc=None) -> object:
    """Insert Chapter into pdf report."""
    if chapter_file_loc == "":
        chapter_file_loc = None
    if chapter_file_loc is not None:
        file1 = fitz.open(pdf_file_loc)
        file2 = fitz.open(chapter_file_loc)
        file1.insert_pdf(file2, start_at=13)
        file1.saveIncr()


# create title page


def create_title_page(
    report_name: str,
    report_author: str,
    university_name: str,
    university_school: str,
    pdf: object,
    config: dict,
    font_options: dict = None,
) -> object:
    """Create title page.

    Creates a title page based upon passed args. Adds text and images
    to pdf.page() then returns pdf object.

    Process:
        Adds page
        Designates contents section
        Adds background image
        Adds banner image
        Adds Text
        Returns pdf obj

    Args:
        data_source         - Data source for report creation
        report_name         - Title of the report and the file name
        report_author       - Author of the report
        university_name     - Name of the university
        university_school   - Name of the university school

    Return:
        pdf(obj) - pdf object

    """
    BASE_DIR_PATH = config["dir_path"]
    DATA_DIR_PATH = os.path.join(BASE_DIR_PATH, "data")
    os.path.join(DATA_DIR_PATH, "fonts")
    IMAGES_PATH = os.path.join(DATA_DIR_PATH, "images")
    os.path.join(DATA_DIR_PATH, "location")
    (Path(os.path.dirname(os.path.realpath(__file__)))).parent
    pdf = FPDF()
    pdf.add_page()
    pdf.start_section(name="Title Page", level=0)
    with pdf.local_context(fill_opacity=0.5, stroke_opacity=0.5):
        pdf.image(f"{ os.path.join(IMAGES_PATH ,'back.png')}", x=0, y=0, h=300)
        pdf.image(
            f"{ os.path.join(IMAGES_PATH ,'school_banner.png')}", x=30, y=250, h=50
        )
    with pdf.local_context(
        text_mode=TextMode.FILL, text_color=(227, 6, 19), line_width=2
    ):
        title_font = font_options["title_font"]
        title_font_size = font_options["title_size"]
        if "title_sub_font" in font_options.keys():
            title_sub_font = font_options["title_sub_font"]
            font_options["title_sub_size"]
        else:
            title_sub_font = font_options["title_font"]
            font_options["title_size"]

        pdf = fonts.add_font_choices_to_pdf(pdf, None)
        pdf.set_font(title_font, "b", title_font_size)

        pdf.set_draw_color(255, 255, 255)
        pdf.ln(30)
        # pdf.write(20, report_name)
        pdf.cell(w=20)
        pdf.multi_cell(w=150, txt=report_name, align="L", border=0)
        pdf.ln(85)
        pdf.set_font(title_font, "", title_font_size / 2)
        # pdf.write(10, report_author)
        pdf.cell(w=20)
        pdf.cell(w=150, txt=report_author, align="L", border=0)
        pdf.set_font(title_sub_font, "", (title_font_size / 2) - 6)

        pdf.ln(20)
        # pdf.write(10, university_name)
        pdf.cell(w=20)
        pdf.cell(w=150, txt=university_name, align="L", border=0)

        pdf.ln(10)
        # pdf.write(10, university_school)
        pdf.cell(w=20)
        pdf.cell(w=150, txt=university_school, align="L", border=0)

    return pdf


# Contents page


def create_contents_page(pdf: object, data_frame: object) -> object:
    """Create contents page.

    Creates space for contents to be created in the document. Currently hardcoded.
    Will throw exception if the space isn't the correct amount.

    53 on first contents page
    63 every page after

    Args:
        pdf - pdf object

    Return:
        pdf - pdf object

    """
    num_of_pages = calc_number_of_contents_pages(data_frame)
    pdf.add_page()
    pdf.set_text_color(0, 0, 0)
    pdf.start_section(name="Table Of Contents", level=0)
    pdf.insert_toc_placeholder(render_toc, num_of_pages)
    return pdf


def calc_number_of_contents_pages(data_frame: object) -> int:
    """Calc number of contents pages.

    Works out the number of contents pages required for
    pdf.insert_to_placeholder(render_toc, num_of_pages)

    Currently hardcoded.

    Formula used currently:
        53 on first contents page
        63 every page after

    Args:
        data_frame: Pandas DataFrame object

    Returns:
        count: integer of count

    """
    order_len = len((data_frame["Order"]).value_counts())
    family_len = len((data_frame["Family"]).value_counts())
    genus_len = len((data_frame["Genus"]).value_counts())

    total = order_len + family_len + genus_len

    additional_count = 0
    if ((total - 53) % 63) != 0:
        additional_count += 1

    count = 1 + ((total - 53) // 63) + additional_count

    return count


def create_report_order_sections(
    ds: object, pdf: object, config: dict, font_options: dict
) -> object:
    """Create report order sections.

    Filter function that splits the data frame (ds) into smaller dataframes
    based on the 'Order' column in the dataframe.

    Process:
        Creates dataframe subsections
        Sorts the new dataframes.
        Loops through each of smaller dataframes to create contents section and level
        Writes section title
        Passes section to the next filter function.

    Args:
        ds - Pandas Dataframe object
        pdf - pdf object
        config - config dict
        font_options - fonts dict
    Returns:
        pdf - pdf object

    """
    order = ds["Order"]
    order_names = order.value_counts().index.tolist()
    order_names.sort()
    header_font = font_options["header_font"]
    header_font_size = font_options["header_size"]
    for name in order_names:
        sect = ds[ds["Order"] == name]
        pdf.add_page()
        pdf.start_section(name=name, level=0)
        pdf.set_font(header_font, "b", header_font_size)
        pdf.ln(20)
        pdf.write(30, f"Order {name}", "C")
        pdf.ln(20)
        pdf = create_report_family_sections(sect, pdf, config, font_options)

    return pdf


def create_report_family_sections(
    section_list: object, pdf: object, config: dict, font_options: dict
) -> object:
    """Create report family sections.

    Filter function that splits the data frame (section_list)
    into smaller dataframes based on the 'Family' column in the dataframe.

    Process:
        Creates dataframe subsections
        Sorts the new dataframes.
        Loops through each of smaller dataframes to create contents section and level
        Writes section title
        Passes section to the next filter function.

    Args:
        section_list - Pandas Dataframe object
        pdf - pdf object
        config - config dict

    Returns:
        pdf - pdf object

    """
    family = section_list["Family"]
    family_names = family.value_counts().index.tolist()
    family_names.sort()
    header_font = font_options["header_font"]
    header_font_size = font_options["header_size"]
    for name in family_names:
        sect = section_list[section_list["Family"] == name]
        pdf.start_section(name=name, level=1)
        pdf.set_font(header_font, "b", (header_font_size / 4) * 3)
        pdf.ln(20)
        pdf.write(10, f"Family {name}", "C")
        pdf.add_page()
        pdf = create_report_genus_sections(sect, pdf, config, font_options)

    return pdf


def create_report_genus_sections(
    section_list: object, pdf: object, config: dict, font_options: dict
) -> object:
    """Create report genus sections.

    Filter function that splits the data frame (ds) into smaller dataframes
    based on the 'Family' column in the dataframe.

    Process:
        Creates dataframe subsections
        Sorts the new dataframes.
        Loops through each of smaller dataframes to create contents section
        and level
        Writes section title
        Passes section to the create report pages function.

    Args:
        section_list - Pandas Dataframe object
        pdf - pdf object
        config - config dict

    Returns:
        pdf - pdf object

    """
    genus = section_list["Genus"]
    genus_names = genus.value_counts().index.tolist()
    genus_names.sort()
    header_font = font_options["header_font"]
    header_font_size = font_options["header_size"]
    for name in genus_names:
        sect = section_list[section_list["Genus"] == name]
        pdf.set_font(header_font, "bi", (header_font_size / 4) * 3)
        pdf.write(10, f"Genus {name}")
        pdf.start_section(name=name, level=2)
        pdf.ln(10)
        pdf = create_report_section_pages(sect, pdf, config, font_options)

    return pdf


# Create pages
def create_report_section_pages(section, pdf, config, font_options):
    """Create report section pages.

    Takes the section passed to it. Passes section to 'create_amphibian_list'
    function to get the data transformed into a list of amphibian objects. Sorts
    the list by name. Loops through list of amphibian objects and passes them to the
    'create_report_section_page' function.

    Args:
        section - pandas dataframe object
        pdf - pdf object
        config - config dict

    Return:
        pdf - pdf object

    """
    BASE_DIR_PATH = config["dir_path"]
    DATA_DIR_PATH = os.path.join(BASE_DIR_PATH, "data")
    os.path.join(DATA_DIR_PATH, "fonts")
    IMAGES_PATH = os.path.join(DATA_DIR_PATH, "images")
    os.path.join(DATA_DIR_PATH, "location")
    (Path(os.path.dirname(os.path.realpath(__file__)))).parent
    amp_list = create_amphibian_list(section)
    amp_list = sorted(amp_list, key=lambda a: a.species)

    # Hardcoded example image will have to replace this
    amp_list[0].image_url_male = f"{ os.path.join(IMAGES_PATH ,'f1.jpg')}"
    amp_list[0].image_url_female = f"{ os.path.join(IMAGES_PATH ,'f2.jpg')}"

    report_style = "compact"

    for i in range(len(amp_list)):
        # pdf = create_report_section_page(amp, pdf)
        amp = amp_list[i]
        # Check if compact report
        if report_style == "compact":
            if i == 0 or i == 1 or i == 2:
                image_offset = 10
            else:
                image_offset = 0

            if i % 3 == 2:
                image_offset += 165
                pdf = create_report_page_compact(
                    amp, pdf, image_offset, config, font_options
                )
                pdf.add_page()
            elif i % 3 == 1:
                image_offset += 85
                pdf = create_report_page_compact(
                    amp, pdf, image_offset, config, font_options
                )
                if (i + 1) == len(amp_list):
                    pdf.add_page()
            else:
                pdf = create_report_page_compact(
                    amp, pdf, image_offset, config, font_options
                )
                if (i + 1) == len(amp_list):
                    pdf.add_page()
    return pdf


# create page
def create_report_section_page(amp, pdf, config, font_options):
    """Create report section page.

    Takes an instance of Amphibian and creates a page. Adds title.
    Adds images (insert_species_images). Adds data table (create_report_page_table).
    Then returns pdf object.

    Args:
        amp - Amphibian object
        pdf - pdf object
        config - config dict

    Return:
        pdf - pdf object

    """
    pdf.start_section(name=amp.get_short_name(), level=3)
    header_font = font_options["header_font"]
    header_font_size = font_options["header_size"]
    pdf.set_font(header_font, "", (header_font_size / 4) * 2)
    pdf.ln(20)
    pdf.write(10, amp.get_short_name())
    pdf = insert_species_images(amp, pdf, config, font_options)
    pdf = create_report_page_table(amp, pdf, config, font_options)
    pdf.add_page()

    return pdf


# add images


def insert_species_images(amp, pdf, config, font_options):
    """Insert species images.

    Takes an instance of Amphibian and pdf. Adds images (insert_species_images)
    to current pdf page. Then returns pdf object.

    FUNCTION CURRENTLY HARDCODED IMAGE VALUES

    Args:
        amp - Amphibian object
        pdf - pdf object
        config -  config dict

    Return:
        pdf - pdf object

    """
    BASE_DIR_PATH = config["dir_path"]
    DATA_DIR_PATH = os.path.join(BASE_DIR_PATH, "data")
    os.path.join(DATA_DIR_PATH, "fonts")
    IMAGES_PATH = os.path.join(DATA_DIR_PATH, "images")
    os.path.join(DATA_DIR_PATH, "location")
    (Path(os.path.dirname(os.path.realpath(__file__)))).parent
    header_font = font_options["header_font"]
    header_font_size = font_options["header_size"]
    paragraph_font = font_options["paragraph_font"]
    paragraph_font_size = font_options["paragraph_size"]
    WIDTH = 210
    pdf.ln(20)
    pdf.set_font(header_font, "", (header_font_size / 4) + 4)
    pdf.write(5, "Species Images:")
    pdf.ln(75)
    if amp.has_image_url():
        pdf.image(f"{amp.image_url_male}", x=10, y=70, w=(WIDTH / 2) - 25, h=50)
        pdf.image(
            f"{amp.image_url_female}", x=WIDTH / 2, y=70, w=(WIDTH / 2) - 25, h=50
        )
        tcell_width = 60
        tcell_height = 5
        pdf.set_font(paragraph_font, "b", paragraph_font_size)
        pdf.cell(tcell_width, tcell_height, "Male Image", align="C", border=0)
        pdf.cell(tcell_width - 20, tcell_height)
        pdf.cell(tcell_width, tcell_height, "Female Image", align="C", border=0)
    else:
        pdf.image(
            f"{os.path.join(IMAGES_PATH,'frogsil1.png')}",
            x=10,
            y=70,
            w=(WIDTH / 2) - 25,
            h=50,
        )
        pdf.image(
            f"{os.path.join(IMAGES_PATH,'frogsil2.png')}",
            x=WIDTH / 2,
            y=70,
            w=(WIDTH / 2) - 25,
            h=50,
        )
        tcell_width = 60
        tcell_height = 5
        pdf.set_font(paragraph_font, "b", paragraph_font_size)
        pdf.cell(tcell_width, tcell_height, "Missing Male Image", align="C", border=0)
        pdf.cell(tcell_width - 20, tcell_height)
        pdf.cell(tcell_width, tcell_height, "Missing Female Image", align="C", border=0)

    return pdf


# create data table
def create_report_page_table(amphibian_data, pdf, config, font_options):
    """Create report page table.

    Takes an instance of Amphibian and pdf. Adds the data in object to current pdf page
    in tabular format. Then returns pdf object.

    Args:
        amp - Amphibian object
        pdf - pdf object
        config - dict

    Return:
        pdf - pdf object

    """
    header_font = font_options["header_font"]
    header_font_size = font_options["header_size"]
    paragraph_font = font_options["paragraph_font"]
    paragraph_font_size = font_options["paragraph_size"]
    pdf.ln(20)
    pdf.set_font(header_font, "", (header_font_size / 4) + 4)
    pdf.write(5, "Species Data:")
    pdf.ln(10)
    tcell_width = 88
    tcell_height = 6

    pdf.set_font(paragraph_font, "b", paragraph_font_size - 2)

    for key, value in amphibian_data.__dict__.items():
        if key not in ["position", "image_url_male", "image_url_female"]:
            key = " ".join(key.split("_")).title()
            pdf.set_font(paragraph_font, "b", paragraph_font_size - 2)
            pdf.cell(tcell_width, tcell_height, str(key), align="L", border=1)
            pdf.set_font(paragraph_font, "", paragraph_font_size - 2)
            pdf.cell(tcell_width, tcell_height, str(value), align="L", border=1)
            pdf.ln(tcell_height)

    return pdf


def create_report_page_compact(
    amp: object, pdf, image_offset, config, font_options
) -> object:
    """Create report page compact.

    Creates a report page with a more compact style.
    Fits more entries on the page over standard version.

    Args:
        amp: Amphibian object
        pdf: Fpdf2 pdf object
        image_offset: offset values for image placement
        config: config dict

    Returns:
        pdf: Fpdf2 pdf object

    """
    header_font = font_options["header_font"]
    header_font_size = font_options["header_size"]
    font_options["paragraph_font"]
    font_options["paragraph_size"]
    pdf.start_section(name=amp.get_short_name(), level=3)
    pdf.set_font(header_font, "ib", (header_font_size / 4) + 4)
    pdf.ln(5)
    pdf.write(10, amp.get_short_name())
    pdf = insert_species_images_compact(amp, pdf, image_offset, config, font_options)
    pdf = create_report_page_table_compact(amp, pdf, config, font_options)

    return pdf


def create_report_page_table_compact(amphibian_data, pdf, config, font_options):
    """Create report page table compact.

    Takes an instance of Amphibian and pdf. Adds the data in object
    to current pdf page in tabular format. Then returns pdf object.

    Args:
        amp - Amphibian object
        pdf - pdf object
        config - config dict

    Return:
        pdf - pdf object

    """
    font_options["header_font"]
    font_options["header_size"]
    paragraph_font = font_options["paragraph_font"]
    paragraph_font_size = font_options["paragraph_size"]

    pdf.ln(10)
    lcell_width = 35
    rcell_width = 95
    tcell_height = 4.5

    pdf.set_font(paragraph_font, "b", paragraph_font_size - 2)

    for key, value in amphibian_data.__dict__.items():
        if key not in [
            "position",
            "image_url_male",
            "image_url_female",
            "order",
            "family",
            "genus",
            "species",
        ]:
            key = " ".join(key.split("_")).title()
            pdf.set_font(paragraph_font, "b", paragraph_font_size - 2)
            if key == "Iucn Category":
                key = "IUCN Category"
            if key == "Geographic Region":
                tcell_height = 3.5
                max_tcell_height = 4 + (len(value) / 60) * 3
                if max_tcell_height < 16:
                    max_tcell_height = 16
                pdf.multi_cell(
                    lcell_width,
                    tcell_height,
                    str(key),
                    align="L",
                    border=0,
                    new_x="RIGHT",
                    new_y="TOP",
                    max_line_height=max_tcell_height,
                )
                if max_tcell_height <= 16:
                    pdf.set_font(paragraph_font, "", paragraph_font_size - 2)
                else:
                    pdf.set_font(paragraph_font, "", paragraph_font_size - 3)
                pdf.multi_cell(
                    w=rcell_width,
                    h=tcell_height,
                    txt=value,
                    align="L",
                    border=0,
                    new_x="RIGHT",
                    new_y="TOP",
                    max_line_height=tcell_height,
                )
                pdf.ln(max_tcell_height)
            else:
                pdf.cell(
                    lcell_width,
                    tcell_height,
                    str(key),
                    align="L",
                    border=0,
                    new_x="RIGHT",
                    new_y="TOP",
                )
                pdf.set_font(paragraph_font, "", paragraph_font_size - 2)
                pdf.cell(rcell_width, tcell_height, str(value), align="L", border=0)
                pdf.ln(tcell_height)
            tcell_height = 4.5

    return pdf


def insert_species_images_compact(amp, pdf, image_offset, config, font_options):
    """Insert species images compact.

    Takes an instance of Amphibian and pdf. Adds images (insert_species_images)
    to current pdf page. Then returns pdf object.

    FUNCTION CURRENTLY HARDCODED IMAGE VALUES

    Args:
        amp - Amphibian object
        pdf - pdf object
        config - config dict

    Return:
        pdf - pdf object

    """
    BASE_DIR_PATH = config["dir_path"]
    DATA_DIR_PATH = os.path.join(BASE_DIR_PATH, "data")
    os.path.join(DATA_DIR_PATH, "fonts")
    IMAGES_PATH = os.path.join(DATA_DIR_PATH, "images")
    os.path.join(DATA_DIR_PATH, "location")
    (Path(os.path.dirname(os.path.realpath(__file__)))).parent
    WIDTH = 210
    header_font = font_options["header_font"]
    header_font_size = font_options["header_size"]
    font_options["paragraph_font"]
    font_options["paragraph_size"]
    pdf.set_font(header_font, "", (header_font_size / 4) + 4)
    if amp.has_image_url():
        pdf.image(
            f"{amp.image_url_male}",
            x=145,
            y=(20 + image_offset),
            w=(WIDTH / 3) - 25,
            h=30,
        )
        pdf.image(
            f"{ os.path.join(IMAGES_PATH ,'maletext.png')}",
            x=145,
            y=(50 + image_offset),
            h=5,
        )
        pdf.image(
            f"{amp.image_url_female}",
            x=145,
            y=(55 + image_offset),
            w=(WIDTH / 3) - 25,
            h=30,
        )
        pdf.image(
            f"{ os.path.join(IMAGES_PATH ,'femaleimage.png')}",
            x=145,
            y=(86 + image_offset),
            h=4,
        )
    else:
        pdf.image(
            f"{ os.path.join(IMAGES_PATH ,'frogsil1.png')}",
            x=145,
            y=(20 + image_offset),
            w=(WIDTH / 3) - 25,
            h=30,
        )
        pdf.image(
            f"{ os.path.join(IMAGES_PATH ,'maletext.png')}",
            x=145,
            y=(50 + image_offset),
            h=5,
        )
        pdf.image(
            f"{ os.path.join(IMAGES_PATH ,'frogsil2.png')}",
            x=145,
            y=(55 + image_offset),
            w=(WIDTH / 3) - 25,
            h=30,
        )
        pdf.image(
            f"{ os.path.join(IMAGES_PATH ,'femaleimage.png')}",
            x=145,
            y=(86 + image_offset),
            h=4,
        )

    return pdf


# create index
def create_report_index():
    """Create report index pages.

    Currently unimplemented.

    """


def read_data_source(file_name: str, options: dict) -> object:
    """Read data source.

    Read the data_source file and transform it into a pandas dataframe

    Args:
        file_name (str):    String path to file
        options (dict):     Dictionary with options

    Returns:
        df - Pandas dataframe object

    """
    if len(options.keys()) == 0:
        df = report_generator.read_from_db.query_db.read_from_db(options)
    elif options["--no-db"] is None:
        df = pandas.read_excel(file_name)
    else:
        df = report_generator.read_from_db.query_db.read_from_db(options)
    df["comb_name"] = df["Order"] + " " + df["Family"]

    return df


def create_amphibian_list(data_section: object) -> list:
    """Create amphibian list.

    Takes a row of data from the dataframe and extracts values and instantiates
    an instance of the AmphibianData class

    Args:
        data_section - Pandas dataframe object

    Return:
        amphibian_list - list of amphibian objects

    """
    amphibian_list = []
    for row in data_section.iterrows():
        vals = []
        for value in row:
            if isinstance(value, int):
                vals.append(value)
            else:
                vals = [*vals, *value.values]
        for i in range(len(vals)):
            if pandas.isna(vals[i]):
                vals[i] = "Unknown"
            if vals[i] == "ND":
                vals[i] = "Unknown"
        a = AmphibianData(vals)
        amphibian_list.append(a)
    return amphibian_list


def render_toc(pdf, outline):
    """Render table of contents.

    Function to render table of contents - taken from example code of
    FPDF2 documentation

    53 on first contents, 63 after

    Args:
        pdf - pdf object
        outline - outline object

    """
    pdf.ln(20)
    pdf.set_font("Helvetica", size=24)
    pdf.underline = False
    pdf.write(5, "Table of contents:")
    pdf.underline = False
    pdf.ln(20)
    pdf.set_font("Courier", size=12)

    for section in outline:
        if section.level < 3:

            link = pdf.add_link()
            pdf.set_link(link, page=section.page_number)
            text = f'{" " * section.level * 2}{section.name}'
            text += f' {"." * (60 - section.level*2 - len(section.name))} '
            text += f"{section.page_number}"
            pdf.multi_cell(
                w=pdf.epw,
                h=pdf.font_size,
                txt=text,
                new_x="LMARGIN",
                new_y="NEXT",
                align="C",
                link=link,
            )


if __name__ == "__main__":
    logger.debug(os.getcwd())
    args = sys.argv

    startTime = time.time()
    data_source = args[1]
    report_name = args[2].upper()
    report_author = args[3].upper()
    university_name = args[4].upper()
    university_school = args[5].upper()

    logger.debug(f"Creating Report: {report_name}.pdf")
    create_report(
        data_source, report_name, report_author, university_name, university_school
    )
    logger.debug(f"Report Complete: {report_name}.pdf")
    executionTime = time.time() - startTime
    logger.debug("Execution time in seconds: " + str(executionTime))
