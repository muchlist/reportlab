from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,  Spacer
from reportlab.lib import colors


def table_alternating():
    doc = SimpleDocTemplate("alternating_table_color.pdf", pagesize=letter)
    story = []
    data = [
        ['col_{}'.format(x) for x in range(1, 6)],
        [str(x) for x in range(1, 6)],
        ['a', 'b', 'c', 'd', 'e'],
        ['F', 'G', 'H', 'I', 'J']]

    # Saat menccoba menggabungkan warna row dan col , yang row akan tidak terapply
    tblstyle = TableStyle(
        [('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.grey, colors.white])])
    # tblstyle = TableStyle([('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.green, colors.red]),
    #                        ('COLBACKGROUNDS', (0, 0), (-1, -1), [colors.red, colors.blue, colors.green])])
    tbl = Table(data)
    tbl.setStyle(tblstyle)

    story.append(tbl)

    story.append(Spacer(0, 24))

    tbl = Table(data, style=[('GRID', (0, 0), (-1, -1), 0.5, colors.blue)])
    story.append(tbl)

    doc.build(story)


if __name__ == "__main__":
    table_alternating()
