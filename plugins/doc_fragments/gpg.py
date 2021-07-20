# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
options:
  gnupghome:
    description:
      - Directory to use for GPG
      - Uses the systems default if not set
    type: str
  gpgbinary:
    description:
      - Path to the GnuPG binary
    """
