from app.requests_roistat import *
from app.xlsx_write import *
from app.config import *
import json


def main():
    api = API
    url = 'https://cloud.roistat.com/api/v1/project/analytics/data'
    project_id = ID_PROJECTS['id_gotour']
    #Источник
    dimensions = ["marker_level_1"]
    # Визиты, Заявки, Продажи, Прибыль, Расходы, ROI
    metrics = ["visits", "leads", "sales", "profit", "marketing_cost", "roi"]
    period_from = "2023-03-01T00:00:00+0300"
    period_to = "2023-03-31T23:59:59+0300"

    response = post_request(url, api, project_id, period_from, period_to, metrics, dimensions)
    if response.ok:
        json_data = json.loads(response.text)
        data = json_data['data']
        data = data[0]['items']
        write_to_xls(metrics, data)

if __name__ == '__main__':
    main()

