# -*- coding: utf-8 -*-

import re

import pytest


@pytest.mark.sphinx('html', testroot='basic')
def test_build_png_image(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><img .*? src="_images/.*?.png" .*?/></div>', source)


@pytest.mark.sphinx('html', testroot='subdir')
def test_build_png_image_in_subdir(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'subdir' / 'index.html').text()
    assert re.search(r'<div><img .*? src="\.\./_images/.*?.png" .*?/></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_width_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :width: 224\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><a class="reference internal image-reference" href="(.*?.png)">'
                     r'<img height="97.0" src="\1" width="224.0" /></a></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_height_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :height: 97\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><a class="reference internal image-reference" href="(.*?.png)">'
                     r'<img height="97.0" src="\1" width="224.0" /></a></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_width_option_and_height_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :width: 100\n"
                                          "   :height: 200\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><a class="reference internal image-reference" href="(.*?.png)">'
                     r'<img height="200.0" src="\1" width="100.0" /></a></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_scale_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :scale: 25%\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><a class="reference internal image-reference" href="(.*?.png)">'
                     r'<img height="48.5" src="\1" width="112.0" /></a></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_width_option_and_scale_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :width: 28\n"
                                          "   :scale: 25%\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><a class="reference internal image-reference" href="(.*?.png)">'
                     r'<img height="3.03125" src="\1" width="7.0" /></a></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_align_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :align: center\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div align="center" class="align-center"><img .*? /></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_align_option_and_width_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :align: center\n"
                                          "   :width: 224\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div align="center" class="align-center">'
                     r'<a class="reference internal image-reference" href="(.*?.png)">'
                     r'<img height="97.0" src="\1" width="224.0" /></a></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_name_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :name: target\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><img .*? id="target" src=".*?" .*? /></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_name_option_and_width_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :name: target\n"
                                          "   :width: 224\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><a class="reference internal image-reference" href="(.*?.png)">'
                     r'<img height="97.0" id="target" src="\1" width="224.0" /></a></div>',
                     source)


@pytest.mark.sphinx('html', testroot='basic')
def test_href_and_scale_option_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :scale: 50%\n"
                                          "\n"
                                          "   A -> B;\n"
                                          "   A [href = 'http://blockdiag.com/'];\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><a class="reference internal image-reference" href="(.*?.png)">'
                     r'<map name="(map_\d+)">'
                     r'<area shape="rect" coords="32.0,20.0,96.0,40.0" '
                     r'href="http://blockdiag.com/"></map>'
                     r'<img .*? src="\1" usemap="#\2" .*?/></a></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_reftarget_in_href_on_png1(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. _target:\n"
                                          "\n"
                                          "heading2\n"
                                          "---------\n"
                                          "\n"
                                          ".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n"
                                          "   A [href = ':ref:`target`'];\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><map name="(map_\d+)">'
                     r'<area shape="rect" coords="64.0,40.0,192.0,80.0" href="#target"></map>'
                     r'<img .*? src=".*?.png" usemap="#\1" .*?/></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_reftarget_in_href_on_png2(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. _hello world:\n"
                                          "\n"
                                          "heading2\n"
                                          "---------\n"
                                          "\n"
                                          ".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n"
                                          "   A [href = ':ref:`hello world`'];\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search(r'<div><map name="(map_\d+)">'
                     r'<area shape="rect" coords="64.0,40.0,192.0,80.0" href="#hello-world">'
                     r'</map><img .*? src=".*?.png" usemap="#\1" .*?/></div>', source)


@pytest.mark.sphinx('html', testroot='basic')
def test_missing_reftarget_in_href_on_png(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n"
                                          "   A [href = ':ref:`unknown_target`'];\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><img .*? src=".*?.png" .*?/></div>', source)
    assert 'undefined label: unknown_target' in warning.getvalue()


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_build_svg_image(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><svg .*?>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_width_option_on_svg(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :width: 224\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><svg height="97.0" viewBox="0 0 448 194" width="224.0" .*?>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_height_option_on_svg(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :height: 97\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><svg height="97.0" viewBox="0 0 448 194" width="224.0" .*?>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_width_option_and_height_option_on_svg(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :width: 100\n"
                                          "   :height: 200\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><svg height="200.0" viewBox="0 0 448 194" width="100.0" .*?>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_scale_option_on_svg(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :scale: 25%\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><svg height="48.5" viewBox="0 0 448 194" width="112.0" .*?>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_width_option_and_scale_option_on_svg(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :width: 28\n"
                                          "   :scale: 25%\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><svg height="3.03125" viewBox="0 0 448 194" width="7.0" .*?>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_align_option_on_svg(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :align: center\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div align="center" class="align-center"><svg .*?>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_name_option_on_svg(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "   :name: target\n"
                                          "\n"
                                          "   A -> B;\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<div><span id="target"></span><svg .*?>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_reftarget_in_href_on_svg1(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. _target:\n"
                                          "\n"
                                          "heading2\n"
                                          "---------\n"
                                          "\n"
                                          ".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n"
                                          "   A [href = ':ref:`target`'];\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<a xlink:href="#target">\\n\\s*<rect .*?>\\n\\s*</a>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_reftarget_in_href_on_svg2(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. _hello world:\n"
                                          "\n"
                                          "heading2\n"
                                          "---------\n"
                                          "\n"
                                          ".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n"
                                          "   A [href = ':ref:`hello world`'];\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<a xlink:href="#hello-world">\\n\\s*<rect .*?>\\n\\s*</a>', source)


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_missing_reftarget_in_href_on_svg(app, status, warning):
    (app.srcdir / 'index.rst').write_text(".. seqdiag::\n"
                                          "\n"
                                          "   A -> B;\n"
                                          "   A [href = ':ref:`unknown_target`'];\n")
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<a xlink:href="#hello-world">\\n\\s*<rect .*?>\\n\\s*</a>', source) is None
    assert 'undefined label: unknown_target' in warning.getvalue()


@pytest.mark.sphinx('html', testroot='basic', confoverrides={'seqdiag_html_image_format': 'SVG'})
def test_autoclass_should_not_effect_to_other_diagram(app, status, warning):
    text = ("This testcase checks that autoclass plugin is unloaded correctly "
            "(and it does not effect to other diagram).\n"
            "\n"
            "    .. seqdiag::\n"
            "\n"
            "       plugin autoclass;\n"
            "       class foo [color = red];\n"
            "       A_foo;\n"
            "\n"
            "    .. seqdiag::\n"
            "\n"
            "       class foo [color = red];\n"
            "       A_foo;\n")
    (app.srcdir / 'index.rst').write_text(text)
    app.build()
    source = (app.outdir / 'index.html').text()
    assert re.search('<text[^>]+>A_foo</text>', source)  # 2nd diagram has a node labeled 'A_foo'.
