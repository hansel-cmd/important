"""
singledispatch is useful if you want to dynamically run a specific code
depending on a specific variable type. Although it can be done using if-else
and/or dictionary mapping, it is best to use singledispatch.

Example 1:

if x == 'HOME':
    // do this
elif x == 'LIVING ROOM':
    // do this
elif fx == 'KITCHEN':
    // do this

Example 2:

places = {
    'HOME': lambda: // do this,
    'LIVING ROOM': lambda: // do this,
    'KITCHEN': lambda: // do this,
}

Example 3:

@singledispatch
def do_this(args):
    // raise exception or anything you do in an else block

@do_this.register(str):
    // code here...

@do_this.register(int):
    // code here...

@do_this.register(bool):
    // code here...


"""


from functools import singledispatch

class Shape:

    def __init__(self, *, stroke_color=None, fill_color=None, stroke_width=None):
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.fill_color = fill_color

    def attrs(self):
        attr_list = [
            '{key}="{value}"'.format(key = k, value = v)
            for k, v in { 
                "stroke": self.stroke_color,
                "stroke-width": self.stroke_width,
                "fill": self.fill_color
            }.items()
            if v is not None
        ]
        return ' '.join(attr_list)
    

class Rectangle(Shape):

    def __init__(self, p, width, height, **kwargs):
        super().__init__(**kwargs)
        self.p = p
        self.width = width
        self.height = height

    
class Circle(Shape):

    def __init__(self, center, radius, **kwargs):
        super().__init__(**kwargs)
        self.center = center
        self.radius = radius
  

class Polygon(Shape):

    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = points


class Group:

    def __init__(self, shapes):
        self.shapes = shapes

    
def make_svg_document(min_x, min_y, max_x, max_y, shapes):
    """Make an SVG document from a collection of shapes."""
    return (
        '<svg viewBox="{min_x} {min_y} {width} {height}" xmnls="https://www.w3.org/2000/svg'
        '\n{shapes}\n'
        '</svg>'.format(
            min_x = min_x,
            min_y = min_y,
            width = max_x - min_x,
            height = max_y - min_y,
            shapes="\n".join(draw(shape) for shape in shapes)
        )
    )

@singledispatch
def draw(shape):
    raise TypeError(f"Cant draw shape {shape!r}")

@draw.register(Rectangle)
def _(shape):
        return (
            f'<rect '
            f'x="{shape.p[0]}" '
            f'y="{shape.p[1]}" '
            f'width="{shape.width}"'
            f'height="{shape.height}"'
            f'{shape.attrs()} />'
        )

@draw.register(Circle)
def _(shape):
        return (
            f'<circle '
            f'cx="{shape.center[0]}" '
            f'cy="{shape.center[1]}" '
            f'r="{shape.radius}"'
            f'{shape.attrs()} />'
        )

@draw.register(Polygon)
def _(shape):
        points = " ".join(f"{p[0]} {p[1]}" for p in shape.points)
        return f'<polygon points="{points}" {shape.attrs()} />'

@draw.register(Group)
def _(group):
        return (
            '<g>\n{}\n</g>'.format(
                "\n".join(draw(shape) for shape in group.shapes)
            )
        )


circle = Circle((0, 2), 10)
print(make_svg_document(100, 75, 100, 75, [circle]))