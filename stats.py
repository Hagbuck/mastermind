import csv, xlsxwriter

from model import Board

class Stats():
    def __init__(self, b):
        self.file = 'stats.xlsx'
        self.data = []
        self.max_row = b.max_row

    def register_data(self, board):
        self.data.append({
                "solution" : str(board.solution), 
                "win" : board.is_win(),
                "moves" : len(board.rows),
            })

    def save_file(self):
        workbook = xlsxwriter.Workbook(self.file)
        worksheet = workbook.add_worksheet()

        # Formats
        header_format = workbook.add_format({'bold' : True})
        loose_format = workbook.add_format({'bg_color' : 'red'})
        win_format = workbook.add_format()

        # Charts
        column_chart = workbook.add_chart({'type': 'column'})

        if len(self.data) > 0:
            # Write Header
            row, col, max_co = 0, 0, 0
            for key in self.data[0]:
                worksheet.write(row, col, key, header_format)
                col += 1
            max_col = col

            # Write datas
            row += 1
            for i in range(0, len(self.data)):
                col = 0
                cell_format = loose_format if self.data[i]["win"] == False else win_format
                    
                for key in self.data[i]:
                    worksheet.write(row, col, self.data[i][key], cell_format)
                    col += 1
                row += 1

            # Create table stats
            row = 0
            col = max_col + 2
            worksheet.write(row, col, "Average", header_format)
            worksheet.write_formula(row + 1, col, "AVERAGE(C:C)")

            col += 1
            for i in range(0, self.max_row):
                worksheet.write(row, col + i, i+1, header_format)
                worksheet.write_formula(row + 1, col + i, "COUNTIF(C:C, {})".format(i+1))

            # Create chart
            column_chart.add_series({
                "name" : "Moves",
                # "categories" : "=Sheet1!$G$1:$L$1",
                # "values" : "=Sheet1!$G$2:$L$2",
                "categories" : ["Sheet1", 0, col, 0, col + self.max_row],
                "values" : ["Sheet1", 1, col, 1, col + self.max_row],
            })
            worksheet.insert_chart(4, col - 1, column_chart)

        workbook.close()

    def __str__(self):
        return "{} Games".format(len(self.data))