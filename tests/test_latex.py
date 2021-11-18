# -*- coding: utf-8 -*-

import os
import re
from sphinx_testing import with_app

import unittest

CR = '\r?\n'

seqdiag_fontpath = '/usr/share/fonts/truetype/ipafont/ipagp.ttf'
with_png_app = with_app(srcdir='tests/docs/basic',
                        buildername='latex',
                        write_docstring=True,
                        confoverrides={
                            'latex_documents': [('index', 'test.tex', '', 'test', 'manual')],
                        })
with_pdf_app = with_app(srcdir='tests/docs/basic',
                        buildername='latex',
                        write_docstring=True,
                        confoverrides={
                            'seqdiag_latex_image_format': 'PDF',
                            'latex_documents': [('index', 'test.tex', '', 'test', 'manual')],
                            'seqdiag_fontpath': seqdiag_fontpath,
                        })
with_oldpdf_app = with_app(srcdir='tests/docs/basic',
                           buildername='latex',
                           write_docstring=True,
                           confoverrides={
                               'seqdiag_tex_image_format': 'PDF',
                               'latex_documents': [('index', 'test.tex', '', 'test', 'manual')],
                               'seqdiag_fontpath': seqdiag_fontpath,
                           })


class TestSphinxcontribSeqdiagLatex(unittest.TestCase):
    @with_png_app
    def test_build_png_image(self, app, status, warning):
        """
        .. seqdiag::

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, r'\\sphinxincludegraphics{{seqdiag-.*?}.png}')

    @unittest.skipUnless(os.path.exists(seqdiag_fontpath), "TrueType font not found")
    @with_pdf_app
    def test_build_pdf_image1(self, app, status, warning):
        """
        .. seqdiag::

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, r'\\sphinxincludegraphics{seqdiag-.*?.pdf}')

    @unittest.skipUnless(os.path.exists(seqdiag_fontpath), "TrueType font not found")
    @with_oldpdf_app
    def test_build_pdf_image2(self, app, status, warning):
        """
        .. seqdiag::

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, r'\\sphinxincludegraphics{{seqdiag-.*?}.pdf}')

    @with_png_app
    def test_width_option(self, app, status, warning):
        """
        .. seqdiag::
           :width: 3cm

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, r'\\sphinxincludegraphics\[width=3cm\]{{seqdiag-.*?}.png}')

    @with_png_app
    def test_height_option(self, app, status, warning):
        """
        .. seqdiag::
           :height: 4cm

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, r'\\sphinxincludegraphics\[height=4cm\]{{seqdiag-.*?}.png}')

    @with_png_app
    def test_scale_option(self, app, status, warning):
        """
        .. seqdiag::
           :scale: 50%

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, r'\\sphinxincludegraphics\[scale=0.5\]{{seqdiag-.*?}.png}')

    @with_png_app
    def test_align_option_left(self, app, status, warning):
        """
        .. seqdiag::
           :align: left

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, (r'{\\sphinxincludegraphics{{seqdiag-.*?}.png}'
                                  r'\\hspace\*{\\fill}}'))

    @with_png_app
    def test_align_option_center(self, app, status, warning):
        """
        .. seqdiag::
           :align: center

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, (r'{\\hspace\*{\\fill}'
                                  r'\\sphinxincludegraphics{{seqdiag-.*?}.png}'
                                  r'\\hspace\*{\\fill}}'))

    @with_png_app
    def test_align_option_right(self, app, status, warning):
        """
        .. seqdiag::
           :align: right

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, (r'{\\hspace\*{\\fill}'
                                  r'\\sphinxincludegraphics{{seqdiag-.*?}.png}}'))

    @with_png_app
    def test_caption_option(self, app, status, warning):
        """
        .. seqdiag::
           :caption: hello world

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')

        figure = re.compile((r'\\begin{figure}\[htbp\]' + CR +
                             r'\\centering' + CR +
                             r'\\capstart' + CR + CR +
                             r'\\noindent\\sphinxincludegraphics{{seqdiag-.*?}.png}' + CR +
                             r'\\caption{hello world}\\label{\\detokenize{index:id1}}\\end{figure}'),
                            re.DOTALL)
        self.assertRegex(source, figure)

    @with_png_app
    def test_caption_option_and_align_option(self, app, status, warning):
        """
        .. seqdiag::
           :align: left
           :caption: hello world

           A -> B;
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')

        figure = re.compile((r'\\begin{wrapfigure}{l}{0pt}' + CR +
                             r'\\centering' + CR +
                             r'\\noindent\\sphinxincludegraphics{{seqdiag-.*?}.png}' + CR +
                             r'\\caption{hello world}\\label{\\detokenize{index:id1}}\\end{wrapfigure}'),
                            re.DOTALL)
        self.assertRegex(source, figure)

    @with_png_app
    def test_href(self, app, status, warning):
        """
        .. seqdiag::

           A -> B;
           A [href=":ref:`target`"];
        """
        app.builder.build_all()
        source = (app.outdir / 'test.tex').read_text(encoding='utf-8')
        self.assertRegex(source, r'\\sphinxincludegraphics{{seqdiag-.*?}.png}')
