import re
import unicodedata

from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha
    characters, and converts spaces to hyphens.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s+-]', '', value).strip().lower())
    return mark_safe(re.sub('[-\s]+', '-', value))

slugify = stringfilter(slugify)
