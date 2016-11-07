from __future__ import print_function

import morepath
import argparse
from dectate.tool import parse_app_class

# XXX how to deal with authorization? passing a header is cumbersome.
# we could display the permission of the response


def why_tool(app_class):
    """Command-line query tool to see what code handles Morepath response.

    usage: morepath_why

    param app_class: the root :class:`App` subclass to query by default.
    """
    parser = argparse.ArgumentParser(description="Query Morepath paths")
    parser.add_argument('path', help="Path to request.")
    parser.add_argument('--app', help="Dotted name for App subclass.",
                        type=parse_app_class)
    parser.add_argument('-r', '--request_method',
                        default='GET',
                        help='Request method such as GET, POST, PUT, DELETE.')
    parser.add_argument('-f', '--file', help='File with request body data.')
    parser.add_argument('-b', '--body', help='Request body data.')
    parser.add_argument('-H', '--header',
                        help='Request header ("Foo-header: Blah")',
                        action='append')

    args, filters = parser.parse_known_args()

    if args.app:
        app_class = args.app

    app = app_class()

    if args.body is not None:
        body = args.body
    elif args.file is not None:
        with open(args.file, 'rb') as f:
            body = f.read()
    else:
        body = None
    if args.headers:
        headers = {}
        for header in args.headers:
            key, value = header.split(':', 1)
            headers[key] = value
    else:
        headers = None
    request = morepath.Request.blank(args.path,
                                     method=args.request_method.upper(),
                                     headers=headers,
                                     body=body,
                                     app=app)

