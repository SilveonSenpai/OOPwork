class TextElement:
    def render(self):
        raise NotImplementedError("Render method must be implemented.")

class Paragraph(TextElement):
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"{self.text}\n"

class Header(TextElement):
    def __init__(self, text, level=1):
        self.text = text
        self.level = level

    def render(self):
        return f"{'#' * self.level} {self.text}\n"

class MarkdownRenderer:
    @staticmethod
    def render(elements):
        return "\n".join(element.render() for element in elements)
