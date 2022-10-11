"""Report Generator.

A tool to create pdf reports from excel (.xlsx) spreadsheet.

Example:

    report-generator
    report-generator --gui
    report-generator --cli [--order_taxon_name='Anura'] [--GeoGraphicRegion='China'] --output 'Report Aura China'
    report-generator --cli --Clutch=5 --Clutch=10

Usage:
    report-generator
    report-generator --gui
    report-generator --new
    report-generator --no-db
    report-generator --output <filename>
    report-generator --cli [--order_taxon_name=<ordname>]
                    [--Family=<famname>]
                    [--Genus=<genname>]
                    [--Species=specname]
                    [--SVLMx=<sm>]...
                    [--SVLMMx=<smm>]...
                    [--SVLFMx=<smf>]...
                    [--ClutchMin=<cmn>]...
                    [--ClutchMax=<cmx]...
                    [--Clutch=<ca>]...
                    [--ParityMode=<pmd>]...
                    [--EggDiameter=<ed>]...
                    [--Longevity=<lmn>]...
                    [--NestingSite=<nsd>]
                    [--MicroHabitat=<mhn>]
                    [--Activity=<ak>]
                    [--GeographicRegion=<gr>]
                    [--IUCN=<iucn>]
                    [--PopTrend=<pt>]


Options:
    -h --help               Show this screen.
    --version               Show version.
    --gui                   Use GUI
    --cli                   Use CLI
    --new                   Create new report project
    --no-db                 Do not check for db settings
                            instead supply string values to create project
                            works directly from Excel(.xlsx) file.
    -o --output             The output filename/location of the report
    [--order_taxon_name]    The order name of species.
    [--Family]              The Family name of species.
    [--Genus]               The genus name of species.
    [--Species]             The latin species name of species
    [--SVLMx]...            Body Size max. For range call twice.
    [--SVLMMx]...           Body size max for male. For range call twice.
    [--SVLFMx]...           Body size max for female.For range call twice.
    [--ClutchMin]...        Minimum clutch size. For range call twice.
    [--ClutchMax]...        Maximum clutch size. For range call twice.
    [--Clutch]...           Average clutch size. For range call twice.
    [--ParityMode]...       Parity Mode of species. Can be called multiple times.
    [--EggDiameter]...      Diameter of species egg. For range call twice.
    [--Longevity]...        Longevity of species. For range call twice.
    [--NestingSite]...      Nesting sites of species. Can be called multiple times.
    [--MicroHabitat]...     Microhabitat of species. Can be called multiple times.
    [--Activity]...         Activity of species. Can be called multiple times.
    [--GeographicRegion]    Geographic region species can be found in.
    [--IUCN]                IUCN type. For more detailed information check documentation.
    [--PopTrend]            Population Trend.
"""


from docopt import docopt
from loguru import logger

import report_generator.report_generator_cli.main
import report_generator.report_generator_gui.main


def main():
    """Driver function.

    Main function for application. Takes no arguments currently.
    """

    arguments = docopt(__doc__, version="Report Generator 1.0")
    # check if gui option selected
    # print(arguments)
    if arguments["--cli"] is True:
        logger.info("Report Generator CLI")
        report_generator.report_generator_cli.main.main(arguments)
    else:
        report_generator.report_generator_gui.main.main()


if __name__ == "__main__":
    main()
