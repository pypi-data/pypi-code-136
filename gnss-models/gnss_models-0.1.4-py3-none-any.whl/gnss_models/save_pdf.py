import utils
import os
from fpdf import FPDF


def save(results):
    pdf = FPDF()
    filename = 'gnss-model-satellite' + results['sat'] + '.pdf'
    filepath = os.path.join(results['save'], filename)

    pdf.add_page()
    generation = 'Model generated on GNSS Satellite {}'.format(results['sat'])
    pdf.set_font("helvetica", size=14)
    pdf.cell(200, 10, txt=generation, ln=1, align="C")
    pdf.ln(0)
    pdf.cell(200, 10, txt='With {}.csv'.format(results['analysis_filename']), ln=1, align="C")
    pdf.ln(10)
    pdf.set_font("helvetica", size=11)

    piece_str = 'X = x % p_value and p_value = 0.997176 day.'
    pdf.cell(200, 10, txt=piece_str, ln=1, align="C")

    for piece in results['str_model'][1:]:
        y_str = '{} * X^3 + {} * X^2 + {} * X + {}'.format(utils.parse_str(piece['a']), utils.parse_str(piece['b']),
                                                           utils.parse_str(piece['c']), utils.parse_str(piece['d']))
        str_model = 'X in [{}, {}]: f(X) = {}'.format(piece['x_min'], piece['x_max'], y_str)
        pdf.cell(200, 10, txt=str_model, ln=1, align="C")

    analysis_image, evaluation_image, other_images = utils.get_images(results['save'])

    pdf.ln(5)
    analysis_text = 'Satellite {}, {}'.format(results['sat'], results['analysis_filename'])
    pdf.cell(200, 10, txt=analysis_text, ln=1, align="C")
    pdf.image(analysis_image, w=4 * pdf.epw / 5, x=pdf.epw / 7.5)

    if len(results['other_filenames']) > 0:
        pdf.ln(5)
        application = 'Model applied to the following files ' + ', '.join(results['other_filenames'])
        pdf.cell(200, 10, txt=application, ln=1, align="C")
        pdf.ln(2)

        for i in range(len(other_images)):
            top = pdf.y
            if i % 2 == 0:
                pdf.image(other_images[i], w=pdf.epw / 2 - 5, y=top)
            else:
                pdf.image(other_images[i], w=pdf.epw / 2 - 5, x=pdf.epw / 2 + 5, y=top)
                if i < len(other_images) - 1:
                    pdf.ln(45)

    pdf.add_page()
    pdf.set_font("helvetica", size=14)
    evaluation = 'Model evaluation for satellite ' + results['sat'] + ': '
    pdf.cell(200, 10, txt=evaluation, ln=1, align="C")
    pdf.ln(10)
    pdf.set_font("helvetica", size=11)

    for evl in results['evaluation']:
        pdf.cell(200, 10, txt=evl, ln=1, align="C")
        pdf.ln(1)

    pdf.image(evaluation_image, w=2 * pdf.epw / 3, x=pdf.epw / 4.5)

    utils.remove_files(results['save'])
    pdf.output(filepath)
