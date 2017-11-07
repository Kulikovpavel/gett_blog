from django import template


register = template.Library()


@register.inclusion_tag('tag_list_extras.html')
def tag_list(post):
    return {'tags': post.tags.all()}
