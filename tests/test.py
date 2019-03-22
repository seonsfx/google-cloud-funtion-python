import signalfx_gcf


@signalfx_gcf.wrapper
def handler(event, context):
    print(context.function_name)
    print(context.function_version)
    print(event["abc"])
    signalfx_gcf.send_gauge('application_performance', 100)
    return "result"
