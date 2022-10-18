import os
# UID of the pipeline in torch
pipeline_uid = "torch.test"
# Name of the pipeline in torch
pipeline_name = "Integration test pipeline"
job_uid = "test_job"


# setup these 3 env vars in your environment.
# torch_credentials = {
#     'url': os.getenv('TORCH_CATALOG_URL', 'https://torch.acceldata.local:5443/torch'),
#     'access_key': os.getenv('TORCH_ACCESS_KEY', 'P04IM8FNQRUCRTU'),
#     'secret_key': os.getenv('TORCH_SECRET_KEY', 'E6LL9YUPMG4BDTJHT2VZD75HW0B8E5')
# }

torch_credentials = {
    'url': os.getenv('TORCH_CATALOG_URL', 'https://acceldata.dev.10.90.3.89.nip.io/torch'),
    'access_key': os.getenv('TORCH_ACCESS_KEY', '21DK0CVJUAE0LET'),
    'secret_key': os.getenv('TORCH_SECRET_KEY', '1PT5E06TLCHKGELZCOEC7LLOCPYHJO')
}