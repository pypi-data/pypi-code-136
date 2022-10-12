import omicidx.geo.parser as op
import omicidx.biosample
import click
import json
import sys
from datetime import date


@click.group()
def cli():
    pass


@cli.group("biosample")
def biosample():
    pass


@biosample.command("downloadxml")
def biosample_download():
    """Download the biosample_set.xml.gz file"""
    omicidx.biosample.download_biosample()


@biosample.command("xml2json")
@click.option(
    "--infile",
    help="compose file to work with",
    type=click.File("r"),
    default=sys.stdin,
)
def biosample_to_json(infile: click.File):
    """Convert the biosample xml file to json"""
    bp = omicidx.biosample.BioSampleParser(infile)
    print(infile.name)
    for rec in bp:
        print(rec.as_json())


@cli.command()
@click.option("--gse", help="A single GSE accession")
def gse_to_json(gse):
    print(op.gse_to_json(gse))


@cli.command()
@click.argument("etype", type=click.Choice(["GSE", "GPL", "GSM"]), default="GSE")
@click.option(
    "--date-start", type=click.DateTime(formats=["%Y-%m-%d"]), default=str(date.today())
)
@click.option(
    "--date-end", type=click.DateTime(formats=["%Y-%m-%d"]), default=str(date.today())
)
def bulk_gse_to_json(date_start: date, date_end: date, etype: str = "GSE"):
    date_formatter = lambda x: x.strftime("%Y/%m/%d")
    term = f"{date_formatter(date_start)}:{date_formatter(date_end)}[PDAT] AND {etype}[ETYP]"
    op.bulk_gse_to_json(term, sys.stdout)


@cli.command()
@click.option("--term", help='something like "2019/01/28:2019/02/28[PDAT]"')
@click.option("--outfile", help="output file name, default is stdout")
def gse_accessions(term, outfile="/dev/stdout"):
    op.gse_accessions(term, outfile)


if __name__ == "__main__":
    cli()
