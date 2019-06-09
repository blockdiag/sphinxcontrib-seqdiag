# -*- coding: utf-8 -*-

import sys
from unittest.mock import patch

import pytest


@pytest.mark.sphinx(testroot='basic', srcdir='parse_error')
def test_parse_error(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   { A -> B;\n")
    app.build()
    assert 'got unexpected token:' in warning.getvalue()


@pytest.mark.sphinx(testroot='basic', confoverrides=dict(seqdiag_html_image_format='JPG'))
def test_unknown_format_error(app, status, warning):
    app.build()
    assert 'unknown format: JPG' in warning.getvalue()


@pytest.mark.sphinx(testroot='basic', confoverrides=dict(seqdiag_html_image_format='PDF'))
def test_reportlab_not_found_error(app, status, warning):
    try:
        # unload reportlab and make loading it impossible
        sys.modules.pop('reportlab', None)
        path = sys.path
        sys.path = []

        app.build()
        assert 'Could not output PDF format. Install reportlab.' in warning.getvalue()
    finally:
        sys.path = path


@pytest.mark.sphinx(testroot='basic')
def test_rendering_error(app, status, warning):
    with patch("seqdiag.utils.rst.nodes.seqdiag.processor.drawer.DiagramDraw") as DiagramDraw:
        DiagramDraw.side_effect = RuntimeError("UNKNOWN ERROR!")
        app.build()
        assert 'UNKNOWN ERROR!' in warning.getvalue()
