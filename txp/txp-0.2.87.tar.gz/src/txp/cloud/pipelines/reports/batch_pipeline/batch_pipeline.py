import argparse
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from google.cloud import firestore, bigquery
from txp.common.utils import firestore_utils, reports_utils
from txp.common.config import settings
from txp.cloud.pipelines.reports.batch_pipeline import steps as ts
import datetime
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

BIGQUERY_TABLE = "PROJECT_ID:DATASET_NAME.TABLE_NAME"
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../../../../common/credentials/pub_sub_to_bigquery_credentials.json"


def get_all_sections(dataset, start_time, end_time):
    dataset = dataset.replace(":", ".")
    start_datetime = datetime.datetime.strptime(start_time, settings.time.datetime_zoned_format)
    end_datetime = datetime.datetime.strptime(end_time, settings.time.datetime_zoned_format)
    firestore_db = firestore.Client()
    bigquery_db = bigquery.Client()
    all_tenants = firestore_utils.get_all_tenants_from_firestore(firestore_db)
    for tenant_doc in all_tenants:
        if "reports" in tenant_doc:
            for report_id in tenant_doc["reports"]:
                sections = reports_utils.get_report_sections(firestore_db, bigquery_db,
                                                             f"{dataset}.sections",
                                                             tenant_doc["tenant_id"], report_id, start_datetime,
                                                             end_datetime)
                if sections is None:
                    continue
                logging.info(f'On start date: {start_datetime} and end date: {end_datetime} '
                             f'for {tenant_doc["tenant_id"]} on report {report_id} there are {len(sections)} sections')
                yield tenant_doc["tenant_id"], report_id, sections
    firestore_db.close()
    bigquery_db.close()


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reports_dataset", help="Bigquery sections dataset name")
    parser.add_argument("--start_datetime",
                        help="Start for report time interval, reports are going to be generated from "
                             "[start_time, end_time]")
    parser.add_argument("--end_datetime", help="End for report time interval, reports are going to be generated from "
                                               "[start_time, end_time]")
    parser.add_argument("--reports_bucket_name", help="Google cloud storage final destination for report pdf files")
    parser.add_argument("--notifications_user", help="Username for auth with notification service", default="")
    parser.add_argument("--notifications_password", help="Password for auth with notification service", default="")
    parser.add_argument("--notifications_url", help="Notifications service url", default="")

    known_args, pipeline_args = parser.parse_known_args()

    pipeline_options = PipelineOptions(pipeline_args)

    with beam.Pipeline(options=pipeline_options) as p:
        (
                p
                | "GetAllSections" >> beam.Create(get_all_sections(known_args.reports_dataset,
                                                                   known_args.start_datetime,
                                                                   known_args.end_datetime))
                | "BuildPdf" >> beam.ParDo(ts.BuildPdf())
                | "StorePdf" >> beam.ParDo(ts.StorePdf(), known_args.reports_bucket_name)
                | "Notify" >> beam.ParDo(ts.NotifyPdfCreation(), known_args.reports_bucket_name,
                                         known_args.notifications_url,
                                         known_args.notifications_user,
                                         known_args.notifications_password)
        )


if __name__ == "__main__":
    run()
