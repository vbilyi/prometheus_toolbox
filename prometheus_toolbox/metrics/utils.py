from prometheus_toolbox.metrics.constants import WEB_SERVICE_METRIC_PREFIX


def with_prefix(metric_name, prefix=WEB_SERVICE_METRIC_PREFIX):
    """
    Add prefix for metric name
    """
    return '{}_{}'.format(prefix, metric_name)


def powers_of(logbase, count, lower=0, include_zero=True):
    """
    Returns a list of count powers of logbase (from logbase**lower).
    """
    if not include_zero:
        return [logbase ** i for i in range(lower, count+lower)]
    else:
        return [0] + [logbase ** i for i in range(lower, count+lower)]
