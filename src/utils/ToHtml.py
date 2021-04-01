class ToHtml
    _color_template = Template(
        open("../templates/color.html").read()
    )

    _index_template = Template(
        open("../templates/index.html").read()
    )

    @StaticMethod
    def color_to_html(color):
        return _color_template.substitute(rgb=color)

    @StaticMethod
    def create_content(*colors):
        result = ""
        for color in colors:
            result += color_to_html(color) + "\n"       
        return result

    @StaticMethod
    def create_index(colors_html):
        index_html = _index_template.substitute(content=colors_html) 
        return
