from app.requests_roistat import *
from app.config import *

def main():
    api = API
    url = 'https://cloud.roistat.com/api/v1/project/analytics/data/export/excel'
    project_id = ID_PROJECTS['id_gotour']
    #Источник
    dimensions = ["marker_level_1"]
    # Визиты, Заявки, Продажи, Прибыль, Расходы, ROI
    metrics = ["visits", "leads", "sales", "profit", "marketing_cost", "roi"]
    period_from = "2023-03-01T00:00:00+0300"
    period_to = "2023-03-31T23:59:59+0300"

    response = post_request(url, api, project_id, period_from, period_to, metrics, dimensions)
    if response.ok:
        with open("data.xls", 'wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    main()

