from .signalfx_serverless_common import common

from . import utils
from .version import name, version

def __init():
    fields = utils.get_fields()
    common.configure('gcf', fields)

# backwards compatibility
def wrapper(*args, **kwargs):
    return common.wrapper(*args, **kwargs)


def emits_metrics(*args, **kwargs):
    return common.emits_metrics(*args, **kwargs)


def is_traced(*args, **kwargs):
    return common.is_traced(*args, **kwargs)


# less convenient method
def send_metric(counters=[], gauges=[]):
    common.send_metric(counters, gauges)


# convenience method
def send_counter(metric_name, metric_value=1, dimensions={}):
    common.send_counter(metric_name, metric_value, dimensions)


# convenience method
def send_gauge(metric_name, metric_value, dimensions={}):
    common.send_gauge(metric_name, metric_value, dimensions)

