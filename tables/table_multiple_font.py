from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def table_multi_font():
    doc = SimpleDocTemplate("table_multi_font.pdf", pagesize=letter)
    story = []
    data = [
        ['col_{}'.format(x) for x in range(1, 6)],
        [str(x) for x in range(1, 6)],
        ['a', 'b', 'c', 'd', 'e']
    ]

    # Jangan gunakan style font dan fontsize terpisah
    tblstyle = TableStyle([('FONT', (0, 0), (-1, 0), 'Times-Roman'),
                           ('FONT', (0, 1), (-1, 1), 'Helvetica', 24),
                           ('FONT', (0, 2), (-1, 2), 'Courier', 12)])

    tbl = Table(data)
    tbl.setStyle(tblstyle)

    story.append(tbl)
    doc.build(story)


if __name__ == "__main__":
    table_multi_font()
