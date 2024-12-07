from text import Header, Paragraph, MarkdownRenderer

def render_character(character):
    """Генерує текстове представлення персонажа у форматі Markdown."""
    elements = [
        Header(f"Character: {character.name}", level=1),
        Paragraph(f"Health: {character.health}"),
        Paragraph(f"Armor: {character.armor}"),
        Paragraph(f"Attack: {character.attack}"),
    ]
    return MarkdownRenderer.render(elements)
