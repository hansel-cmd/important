from django import template

register = template.Library()

@register.filter('format_title')
def format_title(title):
    if len(title) > 100:
        return title[:100] + "..."
    return title

@register.filter('format_content')
def format_content(content):
    if len(content) > 100:
        return content[:100] + "..."
    return content

@register.filter('get_previous_page')
def get_previous_page(page):
    if page == 1:
        return page
    return int(page) - 1

@register.filter('get_next_page')
def get_next_page(page, total):
    if page >= len(total):
        return page
    return int(page) + 1

@register.filter('get_color')
def get_color(key):
    category =  {
        'Lifestyle': 'text-bg-success',
        'K-pop': 'text-bg-danger',
        'Sports': 'text-bg-warning',
        'Politics': 'text-bg-info',
        'Entertainment': 'text-bg-secondary',
    }
    return category.get(key, 'text-bg-secondary')