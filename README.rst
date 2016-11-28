more.whytool: find out what code was responsible for generating a response
==========================================================================

``more.whytool`` lets you create a tool that tells you what view code
was responsible for handling a request.

To create such a tool you do the following, for instance in the
``main.py`` of your project::

  from more.whytool import why_tool
  from .someplace import SomeApp

  def my_why_tool():
      SomeApp.commit()
      why_tool(SomeApp)

where ``SomeApp`` is the application you want to query, typically the
root application of your project.

Now you need to hook it up in ``setup.py`` to you can have the tool
available::

    entry_points={
        'console_scripts': [
            'morewhytool = myproject.main:my_why_tool',
        ]
    },

After you install your project, you should now have a ``morewhytool``
tool available. You can give it requests::

  $ morewhytool /some/path

It tells you:

* What path directive handled the request.

* What view directive handled the request.
