from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def table_cell_aligment():
    doc = SimpleDocTemplate("table_cell_aligment.pdf", pagesize=letter)
    story = []
    data = [
        ['col_{}'.format(x) for x in range(1, 6)],
        [str(x) for x in range(1, 6)],
        ['a', 'b', 'c', 'd', 'e'],
        ['F', 'G', 'H', 'I', 'J']
    ]

    tblstyle = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                           ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                           ('ALIGN', (0, 0), (0, -1), 'CENTER'),
                           ('VALIGN', (1, 0), (1, -1), 'MIDDLE'),
                           ('ALIGN', (2, 0), (2, -1), 'CENTER'),
                           ('VALIGN', (2, 0), (2, -1), 'MIDDLE'),
                           ('ALIGN', (-1, 0), (-1, -1), 'RIGHT'),
                           ])
    # PENAMBAHAN DI colWidth dan rowHeight dalam bentuk array
    tbl = Table(data, colWidths=[55 for x in range(5)], rowHeights=[
                45 for x in range(len(data))])
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)


if __name__ == "__main__":
    table_cell_aligment()
