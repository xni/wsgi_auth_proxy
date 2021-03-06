#!/usr/bin/env python

"""
This is a simple runner to perform local tests or if you want
this functionality, but don't want to install Apache server.
"""

from cherrypy import wsgiserver

import main


def test_wrapper(environ, start_response):
    environ['ADFS_PERSONID'] = '0'
    environ['ADFS_LOGIN'] = 'Tester'
    environ['ADFS_EMAIL'] = 'xni@github.com'
    environ['ADFS_FULLNAME'] = 'Konstantin Nikitin'
    for chunk in main.application(environ, start_response):
        yield chunk


if __name__ == '__main__':
    server = wsgiserver.CherryPyWSGIServer(
        ('0.0.0.0', 8070), test_wrapper)
    server.start()
    