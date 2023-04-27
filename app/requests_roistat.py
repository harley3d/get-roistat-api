import requests

def post_request(url, api, project_id, period_from, period_to, metrics, dimensions):
    headers = {
        'Content-type': 'application/json',
        'Api-key': api,
    }
    params = {
        'project': project_id,
    }
    json_data = {
        "dimensions": dimensions,
        "metrics": metrics,
        "period": {
            "from": period_from,
            "to": period_to
        },
    }
    response = requests.post(url, params=params, headers=headers, json=json_data)
    return response