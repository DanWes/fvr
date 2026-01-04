import ezdxf
import ezdxf.addons.drawing
import ezdxf.addons.drawing.svg
import ezdxf.addons.drawing.properties

# dxfattribs={'color': 1}
# color
# 0: white
# 1: red
# 2: yellow
# 3: green
# 4: cyan
# 5: blue
# 6: magenta
# 7: white (as 0 - on dark background, black on light background)
# 8: gray
# 9: light-gray
#
# 10 - 19 shades of red (10 red same as 1)
# ...
# 240 - 249 shades of red (slightly blue shift)
# 250 - 255 shades of gray
# see https://ezdxf.mozman.at/docs/concepts/aci.html#aci

class doc:
  """
  contour scale and dimension scale

  to create a line in dimension scale = (x, y)/sc*sd
  """

  # scale
  _sd = 1/1  # scale dimension
  _sc = 1/1  # scale countour

  def __init__(self, setup=True, scale=1, sc=1, sd=1):
    """
    Args:
      scale: scale line and font size of contour and dimensions
      sc: scale contour
      sd: scale dimension position
    """
    self.doc = ezdxf.new(dxfversion='AC1032', setup=setup)
    self.msp = self.doc.modelspace()
    layercon = self.doc.layers.add("con")
    layercon.color = 0
    layercon.dxf.lineweight = 75
    layerdim = self.doc.layers.add("dim")
    layerdim.color = 6
    layerdim.dxf.lineweight = 35
    # dimstyle = self.doc.dimstyles.add("dim")
    # dimstyle.set_text_align(valign='center', vshift=1)
    # dimstyle.set_dimline_format(color=6)
    # dimstyle.set_extline_format(color=6)
    self.sc = self._sc*sc*scale
    self.sd = self._sd*sd*scale
    #self.sd = self._sd*sd*scale/sc
    #self.sd = sc/(self._sd*sd)*scale
    self.dims = []
    self._dimstyle()

  def _dimstyle(self):
    self.dimstyle = {
      'dimtxsty': 'Standard',
      # text
      'dimtxt': 0.35,  # 0.35mm line weight
      'dimclrt': 6,    # text color ## set via layer
      # arrow
      'dimtsz': 0,     # set tick size to 0 to enable arrow usage
      'dimasz': 0.35,  # arrow size in drawing units
      'dimblk': ezdxf.ARROWS.closed_filled,  # arrows
      # dimension line
      'dimclrd': 6,    # color ## set via layer
      'dimlwd': 35,    # 0.35mm line weight
      # extension line
      'dimclre': 6,    # color ## set via layer
      'dimlwe': 35,    # 0.35mm line weight
      'dimexe': 0.15,  # length above dimension line
      'dimex0': 0.10,  # offset from measurement point
      'dimlfac': 1/self.sc,  # scale factor for dimension measurements.
      #'dimlfac': 100*self._sdc*self.sd,
    }

  def line(
      self, p1, p2, color=None, lineweight=None, linetype='CONTINUOUS',
      layer=None, dxfattribs=None, shift=(0, 0)):
    """
    Args:
      p1: (x, y)
      p2: (x, y)
      color: defaults to 0
      lineweight: defaults to 75, corresponds to a 0.75 mm linewidth (conversion 1/100).
      linetype: 'DASHED2'
      leyer: e.g. 'con' for contour, 'dim' dimension
    """
    _dxfattribs={'layer': 'con', 'linetype': linetype}
    if layer is not None: _dxfattribs.update({'layer': layer})
    if color is not None: _dxfattribs.update({'color': color})
    if lineweight is not None: _dxfattribs.update({'lineweight': lineweight})
    if dxfattribs is not None:
      _dxfattribs = dxfattribs
    p1 = ((p1[0]+shift[0])*self.sc, (p1[1]+shift[1])*self.sc)
    p2 = ((p2[0]+shift[0])*self.sc, (p2[1]+shift[1])*self.sc)
    self.msp.add_line(p1, p2, dxfattribs=_dxfattribs)

  def polyline(
      self, pts, close=False, color=None, lineweight=None, linetype='CONTINUOUS',
      layer=None, dxfattribs=None, shift=(0, 0)):
    """
    Args:
      pts: [(x1, y1), (x2, y2), ...]
    """
    _dxfattribs={'layer': 'con', 'linetype': linetype}
    if layer is not None: _dxfattribs.update({'layer': layer})
    if color is not None: _dxfattribs.update({'color': color})
    if lineweight is not None: _dxfattribs.update({'lineweight': lineweight})
    if dxfattribs is not None:
      _dxfattribs = dxfattribs
    pts = [((x+shift[0])*self.sc, (y+shift[1])*self.sc) for x, y in pts]
    self.msp.add_lwpolyline(pts, close=close, dxfattribs=_dxfattribs)

  def circle(
      self, pt, radius, color=None, lineweight=None, linetype='CONTINUOUS',
      layer=None, dxfattribs=None):
    """
    Args:
      pt: (x, y)
      radius:
    """
    _dxfattribs={'layer': 'con', 'linetype': linetype}
    if layer is not None: _dxfattribs.update({'layer': layer})
    if color is not None: _dxfattribs.update({'color': color})
    if lineweight is not None: _dxfattribs.update({'lineweight': lineweight})
    if dxfattribs is not None:
      _dxfattribs = dxfattribs
    pt = [i*self.sc for i in pt]
    radius *= self.sc
    self.msp.add_circle(pt, radius=radius, dxfattribs=_dxfattribs)

  def linear_dim(self, base, p1, p2, text, dim_shift=None):
    """
    Args:
      base: (x, y) location of the dimension line in contour scale.
        Use dim_shift to be able to scale contour only and not the dimension.
      p1: (x, y) 1st measurement point
      p2: (x, y) 2nd measurement point
      dim_shift: shift (dx, dy), in dimension scale not contour scale
    """
    _dxfattribs={'layer': 'dim'}
    base = [i*self.sc for i in base]
    p1, p2 = [i*self.sc for i in p1], [i*self.sc for i in p2]
    if dim_shift is not None:
      dim_shift = [i*self.sd for i in dim_shift]
      base = ((base[0]+dim_shift[0]), (base[1]+dim_shift[1]))
    dim = self.msp.add_linear_dim(base=base, p1=p1, p2=p2, text=text,
      # dimstyle="EZDXF",  # default dimension style
      # dimstyle="dim",
      override=self.dimstyle,
      dxfattribs=_dxfattribs,
    )
    self.dims.append(dim)
    # dim.render() below when fetching the rendering

  def aligned_dim(
      self, p1, p2, distance, text, text_rotation=None, text_shifth=0,
      text_shiftv=0, arrow1=None, arrow2=None):
    """
    Args:
      p1: (x, y) 1st measurement point
      p2: (x, y) 2nd measurement point
      distance: NOTE! in dimension scale not contour scale
      text:
      text_rotation: global rotation in in degree
      text_shifth: shift parallel to the dimension line
      text_shiftv: shift perpendicular to the dimension line
      arrow1: 'DOTSMALL'
      arrow2: 'DOTSMALL'
    """
    _dxfattribs = {'layer': 'dim'}
    if text_rotation is not None: _dxfattribs.update({'text_rotation': text_rotation})
    p1, p2 = [i*self.sc for i in p1], [i*self.sc for i in p2]
    # distance  # not distance, this is in dimension scale
    distance *= self.sd
    text_shifth *= self.sd
    text_shiftv *= self.sd
    dim = self.msp.add_aligned_dim(
      p1=p1, p2=p2, distance=distance, text=text, override=self.dimstyle,
      dxfattribs=_dxfattribs)
    dim.shift_text(dh=text_shifth, dv=text_shiftv)
    if arrow1 is not None:
      dim.set_arrows(blk1=arrow1)
    if arrow2 is not None:
      dim.set_arrows(blk2=arrow2)
    self.dims.append(dim)
    # dim.render() below when fetching the rendering

  def leader(
      self, pts=(0, 0), layer=None):
    """
    Args:
      pts: [(x1, y1), (x2, y2), ...]
      distance: NOTE! in dimension scale not contour scale
      text:
      text_rotation: global rotation in in degree
      text_shifth: shift parallel to the dimension line
      text_shiftv: shift perpendicular to the dimension line
      arrow1: 'DOTSMALL'
      arrow2: 'DOTSMALL'
    """
    _dxfattribs = {'layer': 'dim'}
    pts = [((x)*self.sc, (y)*self.sc) for x, y in pts]
    dim = self.msp.add_leader(
      vertices=pts, override=self.dimstyle,
      dxfattribs=_dxfattribs)

  def text(
      self, text, pt=(0, 0), height=0.35, rotation=0, layer=None):
    """
    Args:
      p1: (x, y) 1st measurement point
      p2: (x, y) 2nd measurement point
      distance: NOTE! in dimension scale not contour scale
      text:
      text_rotation: global rotation in in degree
      text_shifth: shift parallel to the dimension line
      text_shiftv: shift perpendicular to the dimension line
      arrow1: 'DOTSMALL'
      arrow2: 'DOTSMALL'
    """
    _dxfattribs = {'layer': ''}
    if layer is not None: _dxfattribs.update({'layer': layer})
    pt = [i*self.sc for i in pt]
    dim = self.msp.add_text(
      text=text, height=height, rotation=rotation, dxfattribs=_dxfattribs)
    # set position and alignment
    dim.set_placement(
      pt,
      # align=ezdxf.enums.TextEntityAlignment.MIDDLE_CENTER,
      # align=ezdxf.enums.TextEntityAlignment.MIDDLE_LEFT,
      align=ezdxf.enums.TextEntityAlignment.LEFT,
    )

  def render_dims(self):
    # Necessary second step to create the BLOCK entity with the dimension geometry.
    # Additional processing of the DIMENSION entity could happen between adding
    # the entity and the rendering call.
    [dim.render() for dim in self.dims]

  def save_dxf(self, filename="output.dxf"):
    self.render_dims()
    self.doc.saveas(filename)

  def export_svg_string(self, background="#21283000"):
    self.render_dims()
    doc = self.doc
    msp = self.msp
    context = ezdxf.addons.drawing.RenderContext(doc)
    backend = ezdxf.addons.drawing.svg.SVGBackend()
    layoutprops = ezdxf.addons.drawing.properties.LayoutProperties.from_layout(msp)
    layoutprops.set_colors(background)  # set background, transparent "#21283000", default "#212830"
    frontend = ezdxf.addons.drawing.Frontend(context, backend)
    frontend.draw_layout(msp, layout_properties=layoutprops)
    # page size
    # page = ezdxf.addons.drawing.layout.Page(
    #   210, 297, units=ezdxf.addons.drawing.layout.Units.mm,
    #   margins=ezdxf.addons.drawing.layout.Margins.all(20))
    # svg_string = backend.get_string(page)
    # autodetect page size
    page = ezdxf.addons.drawing.layout.Page(
      0, 0, units=ezdxf.addons.drawing.layout.Units.mm,
      margins=ezdxf.addons.drawing.layout.Margins.all(2))
    svg_string = backend.get_string(
      page, settings=ezdxf.addons.drawing.layout.Settings(scale=20/1, fit_page=False))
    return svg_string

  def export_svg(self, filename="output.svg"):
    doc = self.doc
    svg_string = export_svg_string(doc)
    with open(filename, "wt", encoding="utf8") as fh:
      fh.write(svg_string)

if __name__ == '__main__':
  dd = doc()
  # detects the bounding box for any Iterable[DXFEntity]
  bounding_box = ezdxf.bbox.extents(dd.modelspace())
  print(bounding_box)
  print('\n'.join([f"{i}" for i in dir(dd.doc)]))
