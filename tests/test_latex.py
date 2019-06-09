# -*- coding: utf-8 -*-

import os
import re

import pytest

seqdiag_fontpath = '/usr/share/fonts/truetype/ipafont/ipagp.ttf'


@pytest.mark.sphinx('latex', testroot='basic')
def test_build_png_image(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'\\sphinxincludegraphics{{seqdiag-.*?}.png}', source)


@pytest.mark.skipif(not os.path.exists(seqdiag_fontpath), reason="TrueType font not found")
@pytest.mark.sphinx('latex', testroot='basic',
                    confoverrides={
                        'seqdiag_latex_image_format': 'PDF',
                        'seqdiag_fontpath': seqdiag_fontpath,
                    })
def test_build_pdf_image1(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'\\sphinxincludegraphics{{seqdiag-.*?}.pdf}', source)


@pytest.mark.skipif(not os.path.exists(seqdiag_fontpath), reason="TrueType font not found")
@pytest.mark.sphinx('latex', testroot='basic',
                    confoverrides={
                        'seqdiag_tex_image_format': 'PDF',
                        'seqdiag_fontpath': seqdiag_fontpath,
                    })
def test_build_pdf_image2(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'\\sphinxincludegraphics{{seqdiag-.*?}.pdf}', source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_width_option(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :width: 3cm\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'\\sphinxincludegraphics\[width=3cm\]{{seqdiag-.*?}.png}', source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_height_option(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :height: 4cm\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'\\sphinxincludegraphics\[height=4cm\]{{seqdiag-.*?}.png}', source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_scale_option(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :scale: 50%\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'\\sphinxincludegraphics\[scale=0.5\]{{seqdiag-.*?}.png}', source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_align_option_left(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :align: left\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'{\\sphinxincludegraphics{{seqdiag-.*?}.png}\\hspace\*{\\fill}}', source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_align_option_center(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :align: center\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'{\\hspace\*{\\fill}\\sphinxincludegraphics{{seqdiag-.*?}.png}\\hspace\*{\\fill}}', source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_align_option_right(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :align: right\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'{\\hspace\*{\\fill}\\sphinxincludegraphics{{seqdiag-.*?}.png}}', source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_caption_option(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :caption: hello world\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()

    figure = re.compile(r'\\begin{figure}\[htbp\].\\centering.\\capstart.*?'
                        r'\\sphinxincludegraphics{{seqdiag-.*?}.png}.'
                        r'\\caption{hello world}.*\\end{figure}', re.DOTALL)
    assert re.search(figure, source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_caption_option_and_align_option(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :align: left\n"
                                          "   :caption: hello world\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'test.tex').text()

    figure = re.compile(r'\\begin{wrapfigure}{l}{0pt}.'
                        r'\\centering.'
                        r'\\noindent\\sphinxincludegraphics{{seqdiag-.*?}.png}.'
                        r'\\caption{hello world}.*\\end{wrapfigure}', re.DOTALL)
    assert re.search(figure, source)


@pytest.mark.sphinx('latex', testroot='basic')
def test_href(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n"
                                          "   A [href=\":href:`target`\"];\n")
    app.build()
    source = (app.outdir / 'test.tex').text()
    assert re.search(r'\\sphinxincludegraphics{{seqdiag-.*?}.png}', source)
