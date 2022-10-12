import os
import boto3

repo = os.environ.get('REPO_NAME')
registry = os.environ.get('ACCOUNT_ID')
region = os.environ.get('REGION')

client = boto3.client('ecr', region_name=region)


def get_image(version: str):
    return client.batch_get_image(
        registryId=registry,
        repositoryName=repo,
        imageIds=[
            {
                'imageTag': version
            }
        ]
    )['images'][0]


def update_image_tag(image, tag):
    client.put_image(
        registryId=registry,
        repositoryName=repo,
        imageManifest=image['imageManifest'],
        imageTag=tag
    )


def handler(event, context):
    print(f'Received event" {event}')
    version = event['Version']
    tag = event['Tag']

    # get image with the version specified
    image = get_image(version)
    # apply the tag specified to that version
    update_image_tag(image, tag)

    print(f'Successfully tagged version {version} with tag: {tag}')
