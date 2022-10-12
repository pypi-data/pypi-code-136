import argparse
from pyspark.sql import SparkSession

def run():
    parser = argparse.ArgumentParser(description='Stage data for fast ingest.')
    parser.add_argument('--compression_format', required=False)
    parser.add_argument('--data_format', required=False)
    parser.add_argument('--sql_query', required=False)
    parser.add_argument('--stage_destination_uri', required=False)

    parser.add_argument('--csv_delimiter', required=False, default="\x1e")
    parser.add_argument('--csv_null_value', required=False, default='_SISU_NULL')

    # For GCP Cloud Storage.
    parser.add_argument('--service_account_private_key_id', required=False)
    parser.add_argument('--service_account_email', required=False)
    parser.add_argument('--service_account_private_key', required=False)

    # For AWS S3.
    parser.add_argument('--access_key_id', required=False)
    parser.add_argument('--secret_access_key', required=False)

    args = parser.parse_args()

    spark = SparkSession.builder.getOrCreate()

    url = args.stage_destination_uri

    # AWS S3.
    if url.startswith("s3://"):
        if not url.startswith("s3://"):
            raise ValueError(f"invalid S3 url: {url}")
        if not (args.access_key_id and args.secret_access_key):
            raise ValueError("access_key_id and secret_access_key must be defined for S3 stage")

        url = f"s3a://{args.access_key_id}:{args.secret_access_key}@{url[5:]}"

    # GCP Cloud Storage.
    elif url.startswith("gs://"):
        if args.service_account_private_key_id and \
                args.service_account_private_key and \
                args.service_account_email:
            # Set service account authentication information from parameters.
            spark.conf.set("fs.gs.auth.service.account.private.key.id", args.service_account_private_key_id)
            spark.conf.set("fs.gs.auth.service.account.email", args.service_account_email)
            spark.conf.set("fs.gs.auth.service.account.private.key", args.service_account_private_key)
        else:
            # If service account information is not specified, assume that the Databricks Compute Engine 
            # instance has the appropriate credentials for accessing this bucket[1].
            #
            # [1]: https://github.com/GoogleCloudDataproc/hadoop-connectors/blob/master/gcs/CONFIGURATION.md#authentication
            spark.conf.set("fs.gs.auth.type", "COMPUTE_ENGINE")

    else:
        raise ValueError(f"unsupported stage destination url: {url}")

    df = spark.sql(f"""{args.sql_query}""")
    df.write \
        .format(args.data_format) \
        .option("compression", args.compression_format) \
        .option("delimiter", args.csv_delimiter) \
        .option("nullValue", args.csv_null_value) \
        .mode("overwrite") \
        .save(url)
