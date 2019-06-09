# -*- coding: utf-8 -*-

import pytest


@pytest.mark.sphinx('html', testroot='basic')
def test_build_html(app, status, warning):
    app.builder.build_all()


@pytest.mark.sphinx('singlehtml', testroot='basic')
def test_build_singlehtml(app, status, warning):
    app.builder.build_all()


@pytest.mark.sphinx('latex', testroot='basic')
def test_build_latex(app, status, warning):
    app.builder.build_all()


@pytest.mark.sphinx('epub', testroot='basic')
def test_build_epub(app, status, warning):
    app.builder.build_all()


@pytest.mark.sphinx('json', testroot='basic')
def test_build_json(app, status, warning):
    app.builder.build_all()
