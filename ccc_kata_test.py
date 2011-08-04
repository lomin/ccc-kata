#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    An integration test for the ccc-kata.

    :copyright: (c) 2011 by it-agile GmbH
    :license: BSD, see LICENSE for more details.
"""

import sys
import uuid
import socket
from random import Random

LOCALHOST = 'localhost'

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

functions = {add: 'ADD', subtract: 'SUBTRACT', multiply: 'MULTIPLY'}

def create_client(port):
    addr = (LOCALHOST, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return addr, client

def create_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((LOCALHOST, port))
    return server

def get_function(index):
    return functions.keys()[index]

def create_new_message(function, id, args):
    message = [functions[function]]
    message.append(id)
    for arg in args:
        message.append(str(arg))
    message = u':'.join(message)
    return message

def create_new_args(number_of_args):
    args = []
    for j in xrange(0, number_of_args):
        arg = random.randint(1, 200)
        args.append(arg)
    return args

def create_expected_response(function, id, args):
    result = reduce(function, args)
    return u':'.join([id, str(result)])

if __name__ == '__main__':
    client_addr, client = create_client(int(sys.argv[1]))
    server = create_server(int(sys.argv[2]))
    random = Random()
    random.seed()
    ok = True
    for i in xrange(0, 3):
        function = get_function(random.randint(0, 2))
        args = create_new_args(random.randint(2, 5))
        id = uuid.uuid4().hex
        message = create_new_message(function, id, args)
        print 'send: <%s>' % message
        expected = create_expected_response(function, id, args)
        print 'expected: <%s>' % expected
        client.sendto(message, client_addr)
        response = server.recv(4096)
        print 'received: <%s>' % (response)
        if response != expected:
            ok = False

    client.sendto(u'__SHUTDOWN__', client_addr)
    if ok:
        print 'successful!'
    else:
        print 'unsuccessful!'
