import argparse

from PyPDF2 import PdfReader, PdfWriter


def create_tete_beche(book1, book2, outfilename):
    with open(outfilename, "wb") as outfp:
        out = PdfWriter()
        with open(book1, "rb") as fp1:
            reader = PdfReader(fp1)
            for p in range(len(reader.pages)):
                out.add_page(reader.pages[p])
            with open(book2, "rb") as fp2:
                reader = PdfReader(fp2)
                for p in range(len(reader.pages) - 1, -1, -1):
                    out.add_page(reader.pages[p])
                    out.pages[-1].rotate(180)
                with open(outfilename, "wb") as wfp:
                    out.write(wfp)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "book1",
        help="path to first (non-reversed) book",
    )
    parser.add_argument(
        "book2",
        help="path to second (reversed) book",
    )
    parser.add_argument("merged", help="path to merged output file")
    args = parser.parse_args()
    create_tete_beche(args.book1, args.book2, args.merged)


if __name__ == "__main__":
    main()
