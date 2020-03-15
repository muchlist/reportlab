from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle)
from reportlab.lib import colors


def table_cell_spanning():
    doc = SimpleDocTemplate("table_cell_spaning.pdf", pagesize=letter)
    story = []

    data = [
        ['col_{}'.format(x) for x in range(1, 6)],
        [str(x) for x in range(1, 6)],
        ['bottom\nleft', 'b', 'c', 'd', 'e']
    ]

    # (SPAN, (begincol, beginrow), (endcol, endrow))
    tblstyle = TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('SPAN', (0, -1), (1, -1))
    ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)

    story.append(tbl)
    doc.build(story)


if __name__ == "__main__":
    table_cell_spanning()
