from google.cloud import monitoring_v3
import time

# for multiple projects, feed in a list of project names and use folder/org level IAM role for perm
key_path = 'C:/Dev/bq/BI_Team-be18049eb10f.json'   # File containing GCP key
project_name = "bi-team-189611"

# my_client = monitoring_v3.MetricServiceClient.from_service_account_file(key_path)

def create_client():
    try:
        client = monitoring_v3.MetricServiceClient.from_service_account_file(key_path)
        interval = monitoring_v3.types.TimeInterval()
        now = time.time()
        interval.end_time.seconds = int(now)
        interval.end_time.nanos = int((now - interval.end_time.seconds) * 10 ** 9)
        interval.start_time.seconds = int(now - 60 * 60 * 24)
        interval.start_time.nanos = interval.end_time.nanos
        return (client, interval)
    except Exception as e:
        raise ("Error occurred creating the client: {}".format(e))


# retrieves quota for services currently in use, otherwise returns null (assume 0 for building comparison vs limits)
def get_quota_current_usage(client, project_name, interval):
    results = client.list_time_series(
        project_name,
        'metric.type = "serviceruntime.googleapis.com/quota/allocation/usage"',
        interval, monitoring_v3.enums.ListTimeSeriesRequest.TimeSeriesView.FULL
    )
    results_list = list(results)
    return (results_list)


def get_quota_current_limit(client, project_name, interval):
    results = client.list_time_series(
        project_name,
        'metric.type = "serviceruntime.googleapis.com/quota/limit"', interval,
        monitoring_v3.enums.ListTimeSeriesRequest.TimeSeriesView.FULL
    )
    results_list = list(results)
    return (results_list)


"""
    example structure

    metric {
        labels {
            key: "quota_metric"
            value: "compute.googleapis.com/cpus"
        }
        type: "serviceruntime.googleapis.com/quota/allocation/usage"
    }
    resource {
        type: "consumer_quota"
        labels {
            key: "location"
            value: "eu"
        }
        labels {
            key: "project_id"
            value: "payment-non-prod"
        }
        labels {
            key: "service"
            value: "compute.googleapis.com"
        }
    }
    metric_kind: GAUGE
    value_type: INT64
    points {
        interval {
            start_time {
                seconds: 1597111200
            }
            end_time {
                seconds: 1597111200
            }
        }
        value {
            int64_value: 1
        }
    }
    """


# if we want to filter by service eg. "compute" for GCE. We can also selectively extract specific values such as:
# i.metric.labels["quota_metric"] for quota names
# i.resource.labels["project_id"] for project IDs
# i.resource.labels["location"] for location
# i.points.value for quota numbers in int64 format
def quota_filter(service_name, results_list):
    results_filtered = [
        i
        for i in results_list if service_name in i.metric.labels["quota_metric"]
    ]
    return (results_filtered)


def quota_view(results_filtered):
    quotaViewJson = {}
    quotaViewList = []
    for result in results_filtered:
        quotaViewJson.update(dict(result.resource.labels))
        quotaViewJson.update(dict(result.metric.labels))
        for val in result.points:
            quotaViewJson.update({'value': val.value.int64_value})
        quotaViewList.append(quotaViewJson)
    return (quotaViewList)


def main(project_name):
    try:
        client, interval = create_client()
        project_name = client.project_path(project_name)
        # current_quota_usage = get_quota_current_usage(
        #     client, project_name, interval
        # )
        current_quota_limit = get_quota_current_limit(
            client, project_name, interval
        )

        # Optional filter
        # current_quota_usage_filtered = quota_filter(
        #     "compute", current_quota_usage
        # )
        current_quota_limit_filtered = quota_filter(
            "compute", current_quota_limit
        )
        # Customising view
        # current_quota_usage_view = quota_view(current_quota_usage_filtered)
        current_quota_limit_view = quota_view(current_quota_limit_filtered)

        # print("+++++++++++++")
        # print("CURRENT QUOTA USAGE")
        # print("+++++++++++++")
        # print("")
        # print(
        #     current_quota_usage_view
        # )  # merge or use data with current_quota_limit_view
        print("+++++++++++++")
        print("CURRENT QUOTA LIMIT")
        print("+++++++++++++")
        print("")
        print(current_quota_limit_view)

    except Exception as e:
        print('Error')
        #raise ("Error occurred getting Quota data: {}".format(e))


if __name__ == '__main__':
    main(project_name)
