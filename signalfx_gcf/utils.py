import os
import warnings

from .version import name, version

fields = {}

def get_fields():
    # TODO: use a loop
    runtime_env = os.environ.get('FUNCTION_REGION')
    if runtime_env is not None:
        fields['gcp_region'] = runtime_env
    runtime_env = os.environ.get('GCP_PROJECT')
    if runtime_env is not None:
        fields['gcp_project_id'] = runtime_env
    runtime_env = os.environ.get('FUNCTION_NAME')
    if runtime_env is not None:
        fields['gcp_function_name'] = runtime_env
    runtime_env = os.environ.get('X_GOOGLE_FUNCTION_VERSION')
    if runtime_env is not None:
        fields['gcp_function_version'] = runtime_env
    return fields.copy()


def get_metrics_url():
    url = os.environ.get('SIGNALFX_INGEST_ENDPOINT')
    if url:
        warnings.warn('SIGNALFX_INGEST_ENDPOINT is deprecated, use SIGNALFX_METRICS_URL instead.', DeprecationWarning)
    else:
        url = os.environ.get('SIGNALFX_METRICS_URL')

    if not url:
        url = os.environ.get('SIGNALFX_ENDPOINT_URL', 'https://pops.signalfx.com')

    return url


def get_tracing_url():
    url = os.environ.get('SIGNALFX_TRACING_URL')

    if not url:
        url = os.environ.get('SIGNALFX_ENDPOINT_URL')

        if url:
            # if the common endpoint url is used, we need to append the trace path
            url = url + '/v1/trace'
        else:
            url = 'https://ingest.signalfx.com/v1/trace'

    return url


def get_access_token():
    token = os.environ.get('SIGNALFX_ACCESS_TOKEN')
    if not token:
        warnings.warn('SIGNALFX_AUTH_TOKEN is deprecated, use SIGNALFX_ACCESS_TOKEN instead.', DeprecationWarning)
        token = os.environ.get('SIGNALFX_AUTH_TOKEN')

    return token
