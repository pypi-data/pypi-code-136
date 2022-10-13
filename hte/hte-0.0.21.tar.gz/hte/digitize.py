"""Package to extract text from historical documents. For personal use.

=======================

Written by Eirik Berger
"""


class Book:
    """Class defining informatino and methods for printed books (pdfs)."""

    def __init__(self, input_file, output_folder):
        import os

        self.input_file = input_file
        self.output_folder = output_folder

        self.bookfilename = os.path.basename(self.input_file)
        self.bookname = os.path.splitext(self.bookfilename)[0]
        self.inputdir = os.path.dirname(self.input_file)
        self.bookdir = self.output_folder

        print()
        print("Class defined for: ", self.input_file)
        print()

    # ===========

    # Create Folder Structure
    def CreateFolderStructure(self):
        """Create folder structure from main directory."""
        import os
        import shutil
        dir = os.path.join(self.bookdir, self.bookname)

        if os.path.exists(dir):
            shutil.rmtree(dir)

        os.mkdir(dir)

        # folders for a) images and b) splits
        os.mkdir(os.path.join(dir, "splits"))
        os.mkdir(os.path.join(dir, "images"))
        os.mkdir(os.path.join(dir, "text"))
        os.mkdir(os.path.join(dir, "bounding_boxes"))

        return "structure created"

    # ===========

    # Import and split pdf by page
    def PdfImport(self, page_info=True, from_page=1, to_page=10):
        """Import pdf and splits into pages, before saving.

        Args:
          road (bool): Import all pages (True) or only selected range (False).
          If False, parameters 'from_page' and 'to_page' must be specified.
        """
        from PyPDF2 import PdfFileReader
        import pdf2image
        import os
        from tqdm import tqdm

        inputpdf = PdfFileReader(open(self.input_file, "rb"), strict=False)

        if page_info:
            maxPages = inputpdf.numPages
        if not page_info:
            maxPages = to_page

        print()
        print("Number of pages:", maxPages-from_page)
        print()

        pil_images = []

        for page in tqdm(range(from_page, maxPages, 10)):
            pil_images
            pil_images.extend(
                pdf2image.convert_from_path(
                    self.input_file,
                    dpi=500,
                    first_page=page,
                    last_page=min(page + 10 - 1, maxPages),
                    thread_count=1,
                    userpw=None,
                    use_cropbox=False,
                    strict=False,
                    output_folder=os.path.join(
                        self.bookdir, self.bookname, "images"),
                    paths_only=True,
                )
            )
        return f"pdf ({self.input_file}) imported"

    # ===========

    def TesseractExtract(self, image_file):
        """Use image path and run tesseract."""
        tesseract_whitelist = 'äÄÖöÉéabcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ()/:-–—.,&0123456789" "' # pylint: disable=line-too-long.
        # tesseract_options = '--psm 6' #--oem 0

        import pandas as pd
        import pytesseract as pt
        from pytesseract import Output

        import cv2
        import os

        text = pt.image_to_data(
            image_file,
            lang=self.tesseract_language,
            output_type=Output.DICT,
            config='-c tessedit_char_whitelist=' +
            tesseract_whitelist+" "+self.tesseract_options,
        )

        if self.export_image:

            n_boxes = len(text['level'])

            for i in range(n_boxes):
                (x, y, w, h) = (text['left'][i], text['top']
                                [i], text['width'][i], text['height'][i])
                cv2.rectangle(image_file, (x, y),
                              (x + w, y + h), (0, 255, 0), 2)

            cv2.imwrite(os.path.join(self.bookdir, self.bookname,
                        "bounding_boxes", self.count + ".jpg"), image_file)

        text = pd.DataFrame.from_dict(text, orient="index")
        text = text.T
        text["conf"] = pd.to_numeric(text["conf"])
        text = text[text.conf >= 0]
        text = text.reset_index(drop=True)

        return text

    # ===========

    def ImageList(self, folder):
        """List all files in folder."""
        import pandas as pd
        import os

        image_list = os.listdir(folder)
        image_list = pd.DataFrame(image_list)
        image_list.rename(
            columns={image_list.columns[0]: "books"}, inplace=True)
        image_list['page_number'] = image_list["books"].str.extract(
            pat='-([0-9]*?).ppm($|.)')[0]
        image_list['side'] = image_list["books"].str.extract(
            pat='_side_([a-z0-9]*?).ppm')
        return image_list

    # ===========

    def SplitPage(self, image, func_name, func_output):
        """Take image of page and split in two."""
        import cv2
        import numpy as np
        from skimage.transform import probabilistic_hough_line

        img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        img = cv2.Canny(img, 130, 150, apertureSize=3)
        img = cv2.blur(img, (10, 10))

        lines = probabilistic_hough_line(
            img, threshold=5, line_length=1000, line_gap=2)

        # Finding the longest line in the middle 50 percent (25-75 percentile)

        h1, w1, c1 = img.shape

        max = 0

        for line in lines:
            temp1 = abs(line[0][1] - line[1][1])
            temp2 = abs(line[0][0] - line[1][0])
            if (
                temp1 > max
                and temp2 < 70
                and ((line[0][0] + line[1][0]) / 2) > w1*0.25
                and ((line[0][0] + line[1][0]) / 2) < w1*0.75
            ):
                max = temp1
                split_line = line

        #####

        img_main = np.array(image)
        h, w, c = img_main.shape
        split = (split_line[0][0] + split_line[1][0]) / 2

        # cut columns
        file_left = img_main[0:h, 0: int(split)]
        cv2.imwrite(func_output+"/"+func_name+"_side_left.ppm", file_left)

        file_right = img_main[0:h, int(split): w]
        cv2.imwrite(func_output+"/"+func_name+"_side_right.ppm", file_right)

    # ===========

    def SplitPages(self, image, func_name, func_output):
        """Split pages."""
        import cv2
        import numpy as np
        from skimage.transform import probabilistic_hough_line
        import pandas as pd

        img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        img = cv2.Canny(img, 130, 150, apertureSize=3)
        img = cv2.blur(img, (10, 10))
        lines = probabilistic_hough_line(
            img, threshold=5, line_length=1000, line_gap=2)

        # Finding the x longest lines that do not overlapp

        h2, w2 = img.shape

        lines_df = pd.DataFrame(
            columns=['length', 'tilt', 'xcoordinates', 'l1', 'l2', 'l3', 'l4'])
        i = 0

        for line in lines:
            temp1 = abs(line[0][1] - line[1][1])
            temp2 = abs(line[0][0] - line[1][0])
            if (
                    temp2 < 70
                    and ((line[0][0] + line[1][0]) / 2) > w2*0.25
                    and ((line[0][0] + line[1][0]) / 2) < w2*0.75
            ):
                x_split = (line[0][0] + line[1][0]) / 2
                lines_df.loc[i] = [temp1] + [temp2] + [x_split] + \
                    [line[0][0]] + [line[0][1]] + [line[1][0]] + [line[1][1]]
                i = i+1

        count = 0
        lines_df['code'] = np.nan
        missing_values = np.nan
        pixels = 25

        while (missing_values != 0):
            row_id = lines_df[pd.isnull(lines_df.code)].idxmax()
            t = lines_df.loc[[row_id[0]]]['xcoordinates']
            lines_df.loc[((lines_df.xcoordinates > int(t)-pixels) &
                          (lines_df.xcoordinates < int(t)+pixels)), 'code'] = 99
            lines_df.loc[[row_id[0]], ['code']] = count
            lines_df = lines_df[lines_df.code != 99]
            missing_values = lines_df['code'].isnull().sum()
            count = count + 1

        # print(f'          Columns identified {lines_df.shape[0]+1}')

        lines_df.loc[-1] = [0, 0, 0, 0, 0, 0, 0, 0]
        lines_df.loc[-2] = [0, 0, w2, 0, 0, 0, 0, 0]

        lines_df = lines_df.sort_values(by='xcoordinates', ascending=True)
        lines_df = lines_df.reset_index(drop=True)

        for i in range(len(lines_df)-1):
            img_split = image[0:int(h2), int(lines_df["xcoordinates"][i]): int(
                lines_df["xcoordinates"][i+1])]
            cv2.imwrite(func_output+"/"+func_name +
                        "_side_"+str(i)+".ppm", img_split)

    # ===========

    def TopBars(self, image, bottom_status="yes"):
        """TopBars."""
        import cv2
        from skimage.transform import probabilistic_hough_line

        # from PIL import Image
        # import numpy as np
        # image = np.array(Image.open('books/hordaland/images/84df49cc-233f-42de-8fad-16339922fb37-757.ppm'))

        img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        img = cv2.Canny(img, 130, 150, apertureSize=3)
        img = cv2.blur(img, (10, 10))

        h, w = img.shape

        lines = probabilistic_hough_line(
            img, threshold=5, line_length=1000, line_gap=2)

        min, max, line_len = 10000, 0, 0

        for line in lines:
            temp1 = abs(line[0][1] - line[1][1])
            temp2 = abs(line[0][0] - line[1][0])
            if temp1 < 70:
                if line[0][1] < 700 and line[1][1] < 700 and line[0][1] > 40 and line[1][1] > 40:
                    if temp2 > line_len:
                        line_len = temp2
                        min = (line[0][1] + line[1][1]) / 2
                if line[0][1] > max and (h-line[0][1]) > 150:
                    max = line[0][1]
                if line[1][1] > max and (h-line[1][1]) > 150:
                    max = line[1][1]

        min = int(min)

        if bottom_status == "yes" and max > (h-500) and max != 0:
            img_main = image[min+2:max-2, 0:w]
        else:
            img_main = image[min+2:h, 0:w]

        # img_main = Image.fromarray(img_main, 'RGB')

        return img_main

    # ===========

    def Split(self, multiple_columns=False):
        """Take images and splots by column (2)."""
        import os
        import numpy as np
        from PIL import Image
        from tqdm import tqdm

        page_list = self.ImageList(os.path.join(
            self.bookdir, self.bookname, "images")).sort_values(by=['page_number'])

        if page_list.count == 0:
            print(f"Folder for {self.bookname} is empty")
            exit
        else:
            pass

        print('')
        print('Splitting pages:')
        print('')

        # Loop over images and split
        for index, row in tqdm(page_list.iterrows(), total=page_list.shape[0]):
            # print("Splits: starting page:", row['page_number'])

            filename = os.path.join(
                self.bookdir, self.bookname, "images", row['books'])
            img = np.array(Image.open(filename))
            img = self.TopBars(img, bottom_status='no')

            try:
                if multiple_columns:
                    self.SplitPages(img, row['books'], os.path.join(
                        self.bookdir, self.bookname, "splits"))
                if not multiple_columns:
                    self.SplitPage(img, row['books'], os.path.join(
                        self.bookdir, self.bookname, "splits"))
            except:
                # print("... could not find column seperator(s) (line)")
                pass

    # ===========

    def RunOCR(self, type="splits", export_image=False, tesseract_options='--psm 3', tesseract_language='nor'):
        """run OCR"""
        import os
        import numpy as np
        from PIL import Image
        from tqdm import tqdm

        self.type = type
        self.tesseract_options = tesseract_options
        self.export_image = export_image
        self.tesseract_language = tesseract_language

        print("")
        print("Running OCR:")
        print("")
        print("tesseract settings: " + self.tesseract_options)
        print("tesseract language: " + self.tesseract_language)

        print("")

        page_list = self.ImageList(os.path.join(
            self.bookdir, self.bookname, self.type)).sort_values(by=['page_number'])

        for index, row in tqdm(page_list.iterrows(), total=page_list.shape[0]):
            self.count = row['books']

            filename = os.path.join(
                self.bookdir, self.bookname, self.type, row['books'])
            img = np.array(Image.open(filename))
            OCR_text = self.TesseractExtract(img)

            filename_out = "book_" + row['books'] + \
                "_page_" + row['page_number'] + ".csv"
            OCR_text.to_csv(os.path.join(
                self.bookdir, self.bookname, "text", filename_out), index=False)

    # ===========

    def CombineCsv(self):
        """Give folder and append all csv in it."""
        import pandas as pd
        import glob
        import os

        combined_csv = pd.DataFrame()
        extension = 'csv'

        os.chdir(os.path.join(self.bookdir, self.bookname, "text"))

        for f in glob.glob('*.{}'.format(extension)):
            df = pd.read_csv(f, index_col=False)
            df["origin_file"] = f
            combined_csv = pd.concat([combined_csv, df])
            # combined_csv = combined_csv.append(df)

        os.chdir("../../..")

        return combined_csv

    # ===========

    def OCRClean(self, text_df):
        """Take pd dataframe and run a series of regex based cleanings."""
        text = text_df.reset_index(drop=True)

        text["text"] = text["text"].str.replace(r"\s+", " ", regex=True)
        text["text"] = text["text"].str.replace(r"|", "", regex=True)
        text["text"] = text["text"].str.replace(r"=", "", regex=True)
        text["text"] = text["text"].str.replace(r"\\", "", regex=True)
        text["text"] = text["text"].str.replace(r'"', "", regex=True)
        text["text"] = text["text"].str.replace(r"«", "", regex=True)
        text["text"] = text["text"].str.replace(r"»", "", regex=True)
        text["text"] = text["text"].str.replace(r"\*", "", regex=True)
        text["text"] = text["text"].str.replace(r"%", "", regex=True)
        text["text"] = text["text"].str.replace(r"'", "", regex=True)
        text["text"] = text["text"].str.replace(r"”", "", regex=True)

        # text["text"] = text["text"].str.replace(r":", "", regex=True)
        # text["text"] = text["text"].str.replace(r"é", "e", regex=True)

        text['text'] = text['text'].str.strip()
        text = text[text.text != ""]
        text = text.reset_index(drop=True)

        return text

    # ===========

    def OCRGroupingNorway(self, df_input, from_page=None, to_page=None):
        """Group words and lines together as 'people'."""
        text = df_input.copy()

        text['page'] = text.origin_file.str.extract(r"page_(.*?).csv")
        text['side'] = text.origin_file.str.extract(r"side_(.*?).ppm")

        # Id per group...
        text["id"] = text.groupby(
            ["block_num", "par_num", "line_num", "page", "side"]).ngroup()

        # Create groups/lines...
        text["keep"] = 0

        # Loop over rows and paste together ids in a cumulative fashion
        for i in range(1, text.shape[0]):
            if text.at[i, "id"] == text.at[i - 1, "id"]:
                text.at[i, "text"] = str(
                    text.at[i - 1, "text"]) + " " + str(text.at[i, "text"])
            else:
                text.at[i - 1, "keep"] = 1

        # Always keep last observation
        text.at[int(text.shape[0] - 1), "keep"] = 1

        text = text[text.keep == 1]
        text = text.drop(['keep'], axis=1)
        text = text.reset_index(drop=True)

        # Create lines bases on commas and '-'
        length = text.shape[0]
        text["comma"] = text["text"].astype(str).str[-1]

        for i in range(length, 0, -1):
            try:
                if text.at[i, "comma"] == "," or text.at[i, "comma"] == "-":
                    text.at[i, "text"] = text.at[i, "text"] + \
                        " " + text.at[i + 1, "text"]
                    text.at[i + 1, "text"] = ""
            except:
                pass

        text = text[text.text != ""]
        text = text.drop(['comma'], axis=1)
        text = text.reset_index(drop=True)

        return text

    def OCRGroupingIndustry(self, df_input, from_page=None, to_page=None):
        """OCR grouping for 'Industri kalender'."""
        import pandas as pd

        text = df_input.copy()

        text['page'] = text.origin_file.str.extract(r"page_(.*?).csv")
        text['side'] = text.origin_file.str.extract(r"side_(.*?).ppm")

        if from_page is None:
            from_page = 0
        if to_page is None:
            to_page = text.pages.max()

        text['page'] = text['page'].astype(int)
        text = text[text['page'].astype(int).between(
            from_page, to_page, inclusive='both')]

        text = text.drop(["word_num", "block_num", "par_num", "line_num",
                         'level', 'page_num', 'left', 'width', 'conf'], axis=1)
        text = text.drop(["origin_file"], axis=1)

        # group only by vertical spaces between word/lines
        text["id"] = text.groupby(["page", "side"]).ngroup()
        text = text.reset_index()
        text = text.drop('index', axis=1)

        text['t'] = text['text'].astype(str).str[0:8]

        for i, row in text.iterrows():
            if i == text.index[-1]:
                pass
            else:
                if (text.at[i, "id"] == text.at[i+1, "id"] and int(text.at[i+1, "top"])-int(text.at[i, "top"]) < 100) or text.at[i+1, "t"] == "Akt.-kap.":
                    text.at[i+1, "text"] = str(text.at[i, "text"]) + \
                        " " + str(text.at[i+1, "text"])
                    text.at[i, "drop"] = 1

        text = text[pd.isnull(text["drop"])]
        text = text.drop(['drop'], axis=1)
        text = text.reset_index(drop=True)

        # remove rows with very little information
        text = text.sort_values(by=['page', 'side'])

        text["len"] = text["text"].str.len()
        text = text[text['len'] > 15]
        text = text.drop(['len'], axis=1)
        text = text[text['text'].str.count(r'\s+') > 2]
        text = text.reset_index(drop=True)

        text = text.drop(["top", "height", "id", "t"], axis=1)

        return text

    # ===========

    def OCRGroupingCalendar(self, df_input, from_page, to_page):
        """OCR grouping for Swedish 'Handelskalender'."""
        import pandas as pd

        text = df_input.copy()

        if from_page is None:
            from_page = 0
        if to_page is None:
            to_page = text.pages.max()

        text['page'] = text.origin_file.str.extract(r"page_(.*?).csv")
        text['page'] = text['page'].astype(int)
        text = text[text['page'].astype(int).between(
            from_page, to_page, inclusive='both')]

        # Id per group...
        text["id"] = text.groupby(["block_num", "page"]).ngroup()
        text = text.drop(["word_num", "block_num", "par_num",
                         "line_num", 'level', 'page_num', 'width', 'conf'], axis=1)
        text = text.reset_index(drop=True)

        for i, row in text.iterrows():
            if i == text.index[-1]:
                pass
            else:
                if text.at[i, "id"] == text.at[i+1, "id"]:
                    text.at[i+1, "text"] = str(text.at[i, "text"]) + \
                        " " + str(text.at[i+1, "text"])
                    if text.at[i+1, "left"] < text.at[i, "left"]:
                        text.at[i+1, "left"] = text.at[i, "left"]
                    text.at[i, "drop"] = 1

        text = text[pd.isnull(text["drop"])]
        text = text.drop(['drop'], axis=1)
        text = text.reset_index(drop=True)

        ##

        for i, row in text.iterrows():
            if i == text.index[-1]:
                pass
            else:
                if (int(text.at[i+1, "top"])-int(text.at[i, "top"]) < 45 and abs(int(text.at[i+1, "top"])-int(text.at[i, "top"])) < 100):
                    text.at[i+1, "text"] = str(text.at[i, "text"]) + " " + str(text.at[i+1, "text"])
                    text.at[i, "drop"] = 1

        text = text[pd.isnull(text["drop"])]
        text = text.drop(['drop'], axis=1)
        text = text.reset_index(drop=True)

        ###

        # remove rows with very little information
        text = text.sort_values(by=['page'])
        text["len"] = text["text"].str.len()
        text = text[text['len'] > 5]

        ###

        # text['t'] = text['text'].astype(str).str[0:3]
        text['t1'] = text['text'].str.contains(r'^[A-ZÆØÅa-zæøå][a-zæøå]{2,}')
        text['t2'] = text['text'].str.contains(r'^[0-9 ]{3,}')
        text['t31'] = text['text'].str.contains(r'^[, ]{0,2}Pn[r]{0,1} [0-9]')
        text['t32'] = text['text'].str.contains(r'^[, ]{0,2}P[n]{0,1}r [0-9]')
        text['t4'] = text['text'].str.contains(r'^\(')

        text['left'].hist(bins=20)

        text['bin'] = 0
        text.loc[text.left >= 600, 'bin'] = 1
        text.loc[text.left >= 1150, 'bin'] = 2

        text["bin_rank"] = text.groupby(
            "page")["top"].rank("dense", ascending=True)
        text = text.sort_values(
            by=[('page'), ('bin'), ('bin_rank')], ascending=True)

        text = text.reset_index(drop=True)

        for i, row in text.iterrows():
            if i == text.index[-1]:
                pass
            else:
                if text.at[i+1, 't1'] or text.at[i+1, 't2'] or text.at[i+1, 't31'] or text.at[i+1, 't32'] or text.at[i+1, 't4']:
                    text.at[i+1, "text"] = str(text.at[i, "text"]) + " " + str(text.at[i+1, "text"])
                    text.at[i, "drop"] = 1

        text = text.drop(["t1", "t2", "t31", "t32", "t4"], axis=1)

        text = text[pd.isnull(text["drop"])]
        text = text.drop(['drop'], axis=1)
        text = text.reset_index(drop=True)

        text = text.drop(["id"], axis=1)  # height, top

        return text

    # ===========

    def OCRGroupingTaxeringskalender(self, df_input, from_page=None, to_page=None):
        """Group words and lines together as 'people'."""
        import re
        text = df_input.copy()

        text['page'] = text.origin_file.str.extract(r"page_(.*?).csv")
        text['side'] = text.origin_file.str.extract(r"side_(.*?).ppm")

        # Id per group...
        text["id"] = text.groupby(
            ["line_num", "page", "side", "block_num", "par_num"]).ngroup()

        # Create groups/lines...
        text["keep"] = 0

        # Loop over rows and paste together ids in a cumulative fashion
        for i in range(1, text.shape[0]):
            if text.at[i, "id"] == text.at[i - 1, "id"]:
                text.at[i, "text"] = str(
                    text.at[i - 1, "text"]) + " " + str(text.at[i, "text"])
            else:
                text.at[i - 1, "keep"] = 1

        # Always keep last observation
        text.at[int(text.shape[0] - 1), "keep"] = 1

        text = text[text.keep == 1]
        text = text.drop(['keep'], axis=1)
        text = text.reset_index(drop=True)

        # Create lines bases on commas and '-'
        # change other strange symbols/characters
        text["text"] = text["text"].str.replace(r",,", ".,", regex=True)
        text["text"] = text["text"].str.replace(r"-—", "—", regex=True)
        text["text"] = text["text"].str.replace(r"-", "—", regex=True)
        text["text"] = text["text"].str.replace(r"—", "—", regex=True)
        text["text"] = text["text"].str.replace(r"\.—", "—", regex=True)
        text["text"] = text["text"].str.replace(r"—[ ]{0,1}—", "—", regex=True)
        text["text"] = text["text"].str.replace(r"— ,", "—", regex=True)
        text["text"] = text["text"].str.replace(r", —", "—", regex=True)

        text['text'] = text['text'].str.strip()

        length = text.shape[0]
        text["end"] = text["text"].astype(str).str[-1]

        for i in range(length-2, -1, -1):
            text.at[i, 'DUMMY'] = 2
            if (text.at[i, "end"] == ","):
                text.at[i, 'DUMMY'] = 1
            if text.at[i, "end"] == "-":
                text.at[i, 'DUMMY'] = 1
            if text.at[i, "end"] == "—" and re.search("^[0-9]{3,}$", str(text.at[i+1, "text"])):
                text.at[i, 'DUMMY'] = 1
            if re.search("^—[ ]{0,1}[0-9]{3,}$", str(text.at[i+1, "text"])):
                text.at[i, 'DUMMY'] = 1
            if re.search("[^0-9]{3,}[0-9]{3,}$", str(text.at[i, "text"])) and re.search("^[0-9]{3,}$", str(text.at[i+1, "text"])):
                text.at[i, 'DUMMY'] = 1
            if text.at[i, "page"] != text.at[i+1, "page"]:
                text.at[i, 'DUMMY'] = 0

        for i in range(length-2, -1, -1):
            if (text.at[i, "DUMMY"] == 1):
                text.at[i, "text"] = str(text.at[i, "text"]) + " " + str(text.at[i+1, "text"])
                text.at[i+1, "text"] = ""

        text = text[text.text != ""]
        text = text.drop(['end'], axis=1)
        text = text.drop(['DUMMY'], axis=1)
        text = text.reset_index(drop=True)

        return text

    # ===========

    def CombineCleanGroup(self, ocr_grouping=True, group_type=None, from_page=None, to_page=None):
        """Combine raw text from OCR, quick clean and grouping."""
        import os

        text = self.CombineCsv()
        text = self.OCRClean(text)
        if ocr_grouping:
            if group_type == "industry":
                text = self.OCRGroupingIndustry(text, from_page, to_page)
            if group_type == "calendar":
                text = self.OCRGroupingCalendar(text, from_page, to_page)
            if group_type == "norway":
                text = self.OCRGroupingNorway(text, from_page, to_page)
            if group_type == "taxeringskalender":
                text = self.OCRGroupingTaxeringskalender(text, from_page, to_page)

        text.to_csv(os.path.join(self.bookdir, self.bookname,
                    f"{self.bookname}_grouped.csv"), index=False)

        print('')

        return "Cleanup finished"

    # ===========

    def RegexClean(self, df):
        """Clean data before regex."""
        # remove/change special characters
        remove_vec = [r"|", r"=", r":", r"\\", r'"', r"«",
                      r"»", r"\*", r"%", r"”"]
        csv = df

        for i in range(len(remove_vec)):
            csv["text"] = csv["text"].str.replace(
                remove_vec[i], "", regex=True)

        # change other strange symbols/characters
        csv["text"] = csv["text"].str.replace(r",,", ".,", regex=True)
        csv["text"] = csv["text"].str.replace(r"-—", "— ", regex=True)
        csv["text"] = csv["text"].str.replace(r"-", "— ", regex=True)
        csv["text"] = csv["text"].str.replace(r"—", "— ", regex=True)
        csv["text"] = csv["text"].str.replace(r"\.—", "—", regex=True)
        csv["text"] = csv["text"].str.replace(r"——", "—", regex=True)
        csv["text"] = csv["text"].str.replace(r"— ,", "—", regex=True)
        csv["text"] = csv["text"].str.replace(r", —", "—", regex=True)

        # csv["text"] = csv["text"].str.replace(r"\. —", "—", regex=True)
        # csv["text"] = csv["text"].str.replace(r"— ", "", regex=True)
        # csv["text"] = csv["text"].str.replace(r"é", "e", regex=True)
        # csv["text"] = csv["text"].str.replace(r"\.\.", "\.", regex=True)

        csv.text = csv.text.replace(r"([0-9] 000)", "\1000", regex=True)

        # remove several spaces, and replace by one space
        csv.text = csv.text.replace(r"\s+", " ", regex=True)
        csv.text = csv.text.str.strip()

        # remove if dot at end of line
        csv.text = csv.text.replace(r"(\.)$", "", regex=True)
        csv["text"] = csv["text"].str.replace(",,", ",", regex=True)
        csv["text"] = csv["text"].str.replace(",,", ",", regex=True)

        return csv

    # ===========`

    def RegexNorway(self, df):
        """Run predefined regex on dataframe."""
        import pandas as pd
        import numpy as np
        global csv

        csv = df

        extract = csv['text'].str.extract(r"()()()()()()")
        # new = csv['text'].str.extract(r"()()()()()()")

        # Main regex system
        surname = [r"(^[—]) ", "(^[ÄÖA-ZÆØÅ][ÄÖA-ZÆØÅäöa-zæøå]*?), ", "^()"]
        firstname = [
            r"([A-ZÆØÅ][A-ZÆØÅa-zæøå\-.]*?), ",
            r"([A-ZÆØÅ][A-ZÆØÅa-zæøå\-.]*? [A-ZÆØÅ][A-ZÆØÅa-zæøå\-.]*?), ",
            r"([A-ZÆØÅ][A-ZÆØÅa-zæøå\-.]*? [A-ZÆØÅ][A-ZÆØÅa-zæøå\-.]*? [A-ZÆØÅ][A-ZÆØÅa-zæøå\-.]*?), ",
        ]

        occupation = ["([äöa-zæøå. ]+?), ", "()",
                      "([äöa-zæøå. ]+?, [äöa-zæøå. ]+?), "]
        residence = ["([ÄÖA-ZÆØÅ0][ÄÖA-ZÆØÅäöa-zæøå.0-9 /-]{0,}?), ", "()"]

        number_1 = ["([0-9OGC][0-9,.OGC]{1,}?)[,]{0,1}", "()"]
        number_2 = ["[,]{0,1}[ ]{0,1}([0-9OGC][0-9OGC,.]{1,})$"]

        comb = np.array(
            np.meshgrid(surname, firstname, occupation,
                        residence, number_1, number_2)
        ).T.reshape(-1, 6)
        comb = pd.DataFrame(comb)
        comb = comb.rename(
            columns={
                0: "surname",
                1: "firstname",
                2: "occupation",
                3: "residence",
                4: "number1",
                5: "number2",
            }
        )

        comb["loop_value"] = (
            "new = csv['text'].str.extract(r\""
            + comb["surname"]
            + comb["firstname"]
            + comb["occupation"]
            + comb["residence"]
            + comb["number1"]
            + comb["number2"]
            + '")'
        )

        for i in range(len(comb)):
            # print(comb["loop_value"][i])
            exec(comb["loop_value"][i], globals())
            extract.update(new, overwrite=True)

        extract = extract.join(csv, how='outer')

        del csv
        extract = extract.drop(['Unnamed: 0', 'level', 'page_num', 'par_num',
                               'line_num', 'word_num', 'width', 'conf'],
                               axis=1, errors='ignore')

        return extract

    # ===========

    def RegexHistorical(self, df):
        """Run predefined regex on dataframe."""
        import pandas as pd
        import numpy as np
        global csv

        csv = df

        extract = csv['text'].str.extract(r"()()()()()()")
        # new = csv['text'].str.extract(r"()()()()()()")

        # Main regex system
        surname = [
            r'(^[—]) ', '(^[—] [A-ZÆØÅ][a-zæøå]*?)[,]{0,1} ', r'(^[A-ZÆØÅ][a-zæøå]*?)[,]{0,1} ']
        firstname = [r'([A-ZÆØÅ][A-ZÆØÅa-zæøå \-\.]*?)[,]{0,1} ']

        occupation = [r'([a-zæøå ]+)\.*?', r'(\.*?)']
        residence = [r'()']

        number_1 = [r'([0-9][0-9,.]{1,}?)[ ]{0,1}—[ ]{0,1}', '()']
        number_2 = [r'([0-9][0-9,.]{1,})$']

        comb = np.array(
            np.meshgrid(surname, firstname, occupation,
                        residence, number_1, number_2)
        ).T.reshape(-1, 6)
        comb = pd.DataFrame(comb)
        comb = comb.rename(
            columns={
                0: "surname",
                1: "firstname",
                2: "occupation",
                3: "residence",
                4: "number1",
                5: "number2",
            }
        )

        comb["loop_value"] = (
            "new = csv['text'].str.extract(r\""
            + comb["surname"]
            + comb["firstname"]
            + comb["occupation"]
            + comb["residence"]
            + comb["number1"]
            + comb["number2"]
            + '")'
        )

        for i in range(len(comb)):
            # print(comb["loop_value"][i])
            exec(comb["loop_value"][i], globals())
            extract.update(new, overwrite=True)

        extract = extract.join(csv, how='outer')

        del csv
        extract = extract.drop(['Unnamed: 0', 'level', 'page_num', 'par_num',
                               'line_num', 'word_num', 'width', 'conf'],
                               axis=1, errors='ignore')
        extract = extract.assign(book=self.bookname)

        return extract

    # ===========

    def RegexIndustry(self, df_input):
        """Regex."""
        import numpy as np

        # get firm names
        text = df_input.replace(r'^\s*$', np.nan, regex=True)

        text['firm_name'] = text.text.str.extract(r"^(AB.{1,}?),")[0]
        text['firm_name'] = text.firm_name.fillna(
            text.text.str.extract(r"^(.*?AB\..*?),")[0])
        text['firm_name'] = text.firm_name.fillna(
            text.text.str.extract(r"^(.*?)\. Se ")[0])

        text['firm_suggested'] = text.text.str.extract(r"^([A-ZÆØÅ].+?),")[0]

        # new, get other information
        text['workers'] = text.text.str.extract(
            r"Arb[.]{0,1}[- ]{0,1}antal ([0-9,]+)[. ]{0,1}")[0]
        text['workers'] = text.workers.fillna(
            text.text.str.extract(r"Antal anställda ([0-9]+)[. ]")[0])
        text['workers'] = text.workers.fillna(
            text.text.str.extract(r"-antal ([0-9]+)[. ]")[0])

        text['equity'] = text.text.str.extract(
            r"Akt[.]{0,1}[- ]{0,1}kap[.]{0,1} ([0-9,]+)")[0]

        text['established'] = text.text.str.extract(
            r" etabl\. ([0-9]{4})\.")[0]
        text['established'] = text.established.fillna(
            text.text.str.extract(r"grundat ([0-9]{4})\.")[0])
        text['established'] = text.established.fillna(
            text.text.str.extract(r"grundades ([0-9]{4})\.")[0])
        text['established'] = text.established.fillna(
            text.text.str.extract(r"bolag ([0-9]{4})\.")[0])

        text['prod_value'] = text.text.str.extract(
            r"Omsättn\.- värde pr år ([0-9,]+?) kr")[0]
        text['prod_value'] = text.prod_value.fillna(
            text.text.str.extract(r"Tillv\.- värde pr år ([0-9,]+?) kr")[0])
        text['prod_value'] = text.prod_value.fillna(
            text.text.str.extract(r" pr år ([0-9,]+?) kr")[0])

        text['phone'] = text.text.str.extract(r"Telefon ([0-9]+?)\.")[0]
        text['postgiro'] = text.text.str.extract(r"Postgiro ([0-9]+?)\.")[0]

        # remove extra spaces and commas in numbers
        for i in text[["prod_value", "phone", "postgiro", "equity", "workers"]]:
            text[i] = text[i].str.replace("[ ,]{1}", "", regex=True)

        return text

    # ===========

    def RegexCalendar(self, df_input):
        """Regex."""
        import numpy as np

        text = df_input.copy()

        # get firm names
        text = df_input.replace(r'^\s*$', np.nan, regex=True)

        text['firm_name'] = text.text.str.extract(
            r"^(.{2,30}) Pn[r]{0,1} [0-9 ]+")[0]
        text['firm_name'] = text.firm_name.fillna(
            text.text.str.extract(r"^([A-ZÆØÅÄÖÉ&.,\-\— ]+? AB ) ")[0])
        text['firm_name'] = text.firm_name.fillna(
            text.text.str.extract(r"^([A-ZÆØÅÄÖÉ&.,\-\— ,\(\)]+) ")[0])

        # new, get other information
        text['pnr'] = text.text.str.extract(r" Pn[r]{0,1} ([0-9 ]+) ")[0]

        text['place'] = text.text.str.extract(
            r" Pn[r]{0,1} [0-9 ]+ ([A-ZÆØÅÄÖÉ][A-ZÆØÅa-zæøåäÄÖöÉé0-9,. ]{,57}?)[,. ]* Box ")[0]
        text['place'] = text.place.fillna(text.text.str.extract(
            r" Pn[r]{0,1} [0-9 ]+ ([A-ZÆØÅÄÖÉ][A-ZÆØÅa-zæøåäÄÖöÉé0-9,. ]{,57}?)[,. ]* Tel ")[0])

        text['box'] = text.text.str.extract(r" Box ([0-9]{,4}).")[0]
        text['phone'] = text.text.str.extract(r" Tel ([0-9 ]*).")[0]

        text['bankgiro'] = text.text.str.extract(r" Bankgiro ([0-9 ]*)")[0]
        text['postgiro'] = text.text.str.extract(r" Postgiro ([0-9 ]*)")[0]
        text['telex'] = text.text.str.extract(r" Telex ([0-9 ]*)")[0]

        text['employees'] = text.text.str.extract(
            r" Antal anställda ([0-9 ]*)")[0]
        text['equity'] = text.text.str.extract(r" Aktiekapital ([0-9 ]*)")[0]
        text['established'] = text.text.str.extract(
            r" Etableringsår ([0-9]{4})")[0]
        text['revenue'] = text.text.str.extract(r" Arsomsättning ([0-9 ]*)")[0]

        text['operations'] = text.text.str.extract(
            r" Verksamhet ([A-ZÆØÅa-zæøåäÄÖöÉé,. ]*) [A-ZÆØÅÄÖÉ][A-ZÆØÅa-zæøåäÄÖöÉé0-9,. ]+ [0-9]+")[0]

        # remove extra spaces
        for i in text[["bankgiro", "postgiro", "telex", "pnr", "phone", "revenue", "equity", "box"]]:
            text[i] = text[i].str.replace("[ ,]{1}", "", regex=True)

        return text

    # ===========

    def RegexTaxeringskalender(self, df):
        """Run predefined regex on dataframe."""
        global csv

        csv = df.copy()
        csv["text"] = csv["text"].str.replace(r"([0-9]{3,}) [a-zøå]$", "\\1", regex=True)

        extract = csv['text'].str.extract(r"^(.*?) ([a-zæøåäö., —]{3,})[ ]*([A-ZÆØÅÄÖ]{0,1}[^0-9]*?)([0-9]*)[—\- ]{1,3}([0-9]*)$")
        extract = extract.rename(columns={"0": "name",
                                          "1": "occupation",
                                          "2": "residence",
                                          "3": "income",
                                          "4": "wealth"})
        extract = extract.join(csv, how='outer')

        del csv
        extract = extract.drop(['Unnamed: 0', 'level', 'page_num', 'par_num',
                                'line_num', 'word_num', 'width', 'conf',
                                'text_part'],
                               axis=1, errors='ignore')

        return extract

    # ===========

    def RegexStructure(self, regex_type):
        """Structure text using customized regex."""
        import os
        import pandas as pd

        df = pd.read_csv(os.path.join(
            self.bookdir, self.bookname, f"{self.bookname}_grouped.csv"),)

        df = self.RegexClean(df)
        if regex_type == "industry":
            df = self.RegexIndustry(df)
        if regex_type == "calendar":
            df = self.RegexCalendar(df)
        if regex_type == "norway":
            df = self.RegexNorway(df)
        if regex_type == "historical":
            df = self.RegexHistorical(df)
        if regex_type == "taxeringskalender":
            df = self.RegexTaxeringskalender(df)

        df = df.drop(['Unnamed: 0', 'left', 'top', 'height', 'origin_file',
                     'len', 't', 'bin_rank'], axis=1, errors='ignore')

        df.to_csv(os.path.join(self.bookdir, self.bookname,
                  f"{self.bookname}_regex.csv"))

        print('')

        return "Done!"

    # ===========s

    def Message(self, string):
        """Print message."""
        print("")
        print(string)

    # ===========

    def Main(self, regex_type, group_type, from_page, to_page):
        """Run full process."""
        self.Message("Creating folder structure...")
        self.CreateFolderStructure()

        self.Message("Importing pdf...")
        self.PdfImport()

        self.Message("Splitting images...")
        self.Split()

        self.Message("Running OCR...")
        self.RunOCR()

        self.Message("Combining pages, cleaning them and grouping lines...")
        self.CombineCleanGroup(
            group_type=None, from_page=from_page, to_page=to_page)

        self.Message("Running regex structure...")
        self.RegexStructure(regex_type)

        return "function successfully completed"

###############################################################################
###############################################################################
###############################################################################
###############################################################################
