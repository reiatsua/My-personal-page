from django import template

register = template.Library()

@register.filter
def to_ordered_list(value):
    """Convert newline-separated text to ordered list"""
    if not value:
        return ""
    lines = value.strip().split('\n')
    items = [f"<li>{line.strip()}</li>" for line in lines if line.strip()]
    return f"<ol>{''.join(items)}</ol>"

@register.filter
def to_unordered_list(value):
    """Convert newline-separated text to unordered list"""
    if not value:
        return ""
    lines = value.strip().split('\n')
    items = [f"<li>{line.strip()}</li>" for line in lines if line.strip()]
    return f"<ul>{''.join(items)}</ul>"

@register.filter
def colorize_words(value):
    """Color each word with a different color (excluding yellow and white)"""
    if not value:
        return ""
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9', '#F8B195', '#A9DFBF']
    words = value.split()
    colored_words = []
    for i, word in enumerate(words):
        color = colors[i % len(colors)]
        colored_words.append(f'<span style="color: {color}; font-weight: 600;">{word}</span>')
    return ' '.join(colored_words)
