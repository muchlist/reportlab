from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def simple_table_with_style():
    doc = SimpleDocTemplate("simple_table_with_style.pdf", pagesize=letter)
    story = []
    data = [
        ['col_{}'.format(x) for x in range(1, 6)],
        [str(x) for x in range(1, 6)],
        ['a', 'b', 'c', 'dadasdadasd', 'e']
    ]

    # format atribute , range awal (colomn, row), range akhir -1 dari belakang, value
    # format lain ALIGMENT dengan value LEFT, RIGHT, CENTER, DECIMAL
    # FONT, FONTSIZE, LEFTPADDING, BOTTOMPADDING, VALIGN
    tblstyle = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.red),
                           ('TEXTCOLOR', (0, 1), (-1, 1), colors.blue)])

    tbl = Table(data)
    tbl.setStyle(tblstyle)

    story.append(tbl)
    doc.build(story)


if __name__ == "__main__":
    simple_table_with_style()
