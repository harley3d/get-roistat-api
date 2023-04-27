from app.requests_roistat import *
from app.config import *
import json


def main():
    api = API
    url = 'https://cloud.roistat.com/api/v1/project/analytics/metrics-new'
    project_id = ID_PROJECTS['id_gotour']

    response = getListOfAvailableMetrics(url, api, project_id)
    if response.ok:
        json_data = json.loads(response.text)
        print(json_data)

if __name__ == '__main__':
    main()