from django.http import HttpResponseRedirect
from fpdf import FPDF

from main.models import FirstFormModel

"""
Redéfinition du header et du footer 
"""


class PDF(FPDF):
    def header(self):
        # Logo
        self.image("/portail_web_chu/report/static/report/logo.jpg", 10, 5, 33)
        # helvetica bold 15
        self.set_font('helvetica', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(60, 10, 'Recherche Clinique', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # helvetica italic 8
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


"""
Permet de modifier la valeur de is_valid pour un string
Sinon renvoi la valeur en string
"""


def handle_value(value):
    if value == "True":
        return "Validé"
    elif value == "False":
        return "Non validé"
    else:
        return value


def create_report(request, recherche_id):
    try:
        recherche = FirstFormModel.objects.get(id=recherche_id)
    except FirstFormModel.DoesNotExist:
        return HttpResponseRedirect("/liste_recherche")

    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Times', 'B', 12)
    for key, value in recherche:
        pdf.cell(200, 10, str(key) + ": " + handle_value(value), 0, 1, "C")
    pdf.output('tempPDF/Recherche_' + str(recherche.id) + '.pdf')

    return HttpResponseRedirect("/")  # TODO Changer la direction
