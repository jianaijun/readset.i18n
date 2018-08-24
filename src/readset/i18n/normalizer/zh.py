# -*- coding: UTF-8 -*-

from slugify import slugify

from plone.i18n.normalizer.base import baseNormalize
from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implementer


@implementer(INormalizer)
class Normalizer(object):
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(Normalizer, INormalizer)
      True

      >>> norm = Normalizer()
      >>> text = unicode('简繁漢字', 'utf-8')
      >>> norm.normalize(text)
      'jian-fan-han-zi'
    """

    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """
        slug = slugify(text)
        # always apply base normalization
        return baseNormalize(slug)


normalizer = Normalizer()
