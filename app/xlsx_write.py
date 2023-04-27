import xlsxwriter

def write_to_xls(titles, data,filename='data.xlsx'):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'Источник')
    cell_row = 0
    cell_col = 1
    for caption in titles:
        worksheet.write(cell_row, cell_col, caption)
        cell_col += 1
    cell_row = 1
    cell_col = 0
    for row in data:
        source_name = row['dimensions']['marker_level_1']['title']
        worksheet.write(cell_row, cell_col, source_name)
        metrics = row['metrics']
        cell_col = 1
        for index in metrics:
            metric_name = index["metric_name"];
            if metric_name == 'visitCount':
                continue
            metric_value = index["value"];
            worksheet.write(cell_row, cell_col, metric_value)
            cell_col += 1
        cell_col = 0
        cell_row += 1
    workbook.close()