# -*- coding: UTF-8 -*-
import os.path

from zope.interface import implementer

from plone.memoize import ram
from plone.i18n.normalizer.interfaces import INormalizer
from plone.i18n.normalizer.base import baseNormalize
#from plone.i18n.normalizer.base import mapUnicode


# Chinese character mapping
pinyin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'pinyin.db')


@ram.cache(lambda *args: args)
def PinyinDict():
    mapping = {}
    for line in open(pinyin_path):
        k, v = line.split('\t')
        mapping[int(k, base=16)] = v.split()[0][:-1].lower()
    return mapping
mapping = PinyinDict()


def mapUnicode(text, mapping=()):
    """
    This method is used for replacement of special characters found in a
    mapping before baseNormalize is applied.
    """
    res = []
    word = u''
    for ch in text:
        ordinal = ord(ch)
        # split english word
        if ordinal < 128:
            word += ch
            continue
        elif word and not word.isspace():
            res.append(word.strip())
            word = u''

        if ordinal in mapping:
            # try to apply custom mappings
            res.append(mapping.get(ordinal).strip())
        else:
            # else leave untouched
            res.append(ch)
    else:
        if word and not word.isspace():
            res.append(word.strip())
    # always apply base normalization
    return baseNormalize(u'-'.join(res))


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
        return mapUnicode(text, mapping=mapping)

normalizer = Normalizer()
