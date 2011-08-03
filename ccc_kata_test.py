#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    An integration test for the ccc-kata.

    :copyright: (c) 2011 by it-agile GmbH
    :license: BSD, see LICENSE for more details.
"""

import sys
from socket import *
from random import Random

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

functions = {'ADD': add, 'SUBTRACT': subtract, 'MULTIPLY': multiply}

if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_addr = ('127.0.0.1', int(sys.argv[1]))
    own_socket = socket(AF_INET, SOCK_DGRAM)
    own_socket.bind(('127.0.0.1', int(sys.argv[2])))
    print 'waiting for client name...'
    client_name = own_socket.recv(4096)
    print 'client name: <%s>' % (client_name)
    random = Random()
    random.seed()
    ok = True
    for i in xrange(0, 3):
        key, function = functions.items()[random.randint(0,2)]
        message = [key]
        args = []
        number_of_args = random.randint(2,5)
        for j in xrange(0, number_of_args):
            arg = random.randint(1, 200)
            message.append(str(arg))
            args.append(arg)
        message = ':'.join(message)
        result = reduce(function, args)
        expected = ':'.join([client_name, str(result)])
        print message
        print 'expected: <%s>' % (expected)
        server_socket.sendto(message, server_addr)
        response = own_socket.recv(4096)
        print 'received: <%s>' % (response)
        if response != expected:
            ok = False

    server_socket.sendto(u'__SHUTDOWN__', server_addr)
    if ok:
        print 'successful!'
    else:
        print 'unsuccessful!'
