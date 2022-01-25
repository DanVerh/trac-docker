# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2021 Edgewall Software
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at https://trac.edgewall.org/wiki/TracLicense.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at https://trac.edgewall.org/log/.

import unittest

import trac.tests.wikisyntax
import trac.ticket.tests.wikisyntax
import trac.versioncontrol.web_ui.tests.wikisyntax
import trac.web.tests.wikisyntax
import trac.wiki.tests.macros
import trac.wiki.tests.wikisyntax
import trac.wiki.tests.formatter

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(trac.tests.wikisyntax.test_suite())
    suite.addTest(trac.ticket.tests.wikisyntax.test_suite())
    suite.addTest(trac.versioncontrol.web_ui.tests.wikisyntax.test_suite())
    suite.addTest(trac.web.tests.wikisyntax.test_suite())
    suite.addTest(trac.wiki.tests.macros.test_suite())
    suite.addTest(trac.wiki.tests.wikisyntax.test_suite())
    suite.addTest(trac.wiki.tests.formatter.test_suite())
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
