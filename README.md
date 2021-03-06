# Instructions
1. Clone this repository 
2. Create the following exrecise in `ext_info.py`.
3. Don't forget to add, commit and push your work.
4. Send your repo url to via https://hackita02.hasadna.org.il/sa/ 

# File Information By Extension (Python Standard Library Exercise)

Create a command line program that shows information about different file
types in a specified folder.  For example:

    :::bash
    $ python ext_info.py .
    png 16 2765632
    py 1 2103
    pyc 1 608
    txt 10 34042
    zip 3 4540097

    $ python ext_info.py /home/udi/music/
    m3u 12 97633
    mp3 52 83654229

In the first example the current folder was checked (by specifying `.` on the
command line as the parameter).  16 files with the "png" extension were found,
with a total size of 2765632 bytes.

Implementation notes:

 * Subfolders should be ignored.
 * "jpg" and "JPG" are considered different extensions.
 * Files with no extensions should include the '.' extension instead.
   (This also includes files ending with a dot, which is possible in linux)
 * Output should be sorted by extension using string (lexical) order.
 * When no parameter is supplied the following should be displayed:

        :::text
        usage: ext_info.py path
        displays number of files and total size of files per extension in the specified path.

 * (This exercise scope is standard library modules, and not 3rd party packages)

Recommended modules and functions:

 * [`sys.argv`](http://docs.python.org/2/library/sys.html#sys.argv)

    > The list of command line arguments passed to a Python script.
    argv[0] is the script name...

    Example:

        #!python
        import sys
        if __name__ == '__main__':
            print("I am:", sys.argv[0])
            for i, s in enumerate(sys.argv[1:]):
                print "Parameter #{}: {}".format(i+1, s)

 * [`os.listdir`](http://docs.python.org/2/library/os.html#os.listdir):

    > Return a list containing the names of the entries in the directory
    given by path...

    Example:

        :::python
        import os

        for filename in os.listdir('.'):
            print filename


 * [`os.path.join`](http://docs.python.org/2/library/os.path.html#os.path.join).
   Always use this to concatenate paths.

    > Join one or more path components intelligently...

    Windows example:

        :::python
        import os.path

        home_folder = r'c:\users\foo'
        child = r'projects'
        filename = r'pictures\baz.jpeg'

        print os.path.join(home_folder, child, filename)
        # prints: c:\users\foo\projects\pictures\baz.jpeg

    Linux example:

        :::python
        import os.path

        home_folder = '/home/foo/'
        child = 'projects'
        filename = 'pictures/baz.jpeg'

        print os.path.join(home_folder, child, filename)
        # prints: /home/foo/projects/pictures/baz.jpeg

 * And:
   [`os.path.isdir`](http://docs.python.org/2/library/os.path.html#os.path.isdir),
   [`os.path.getsize`](http://docs.python.org/2/library/os.path.html#os.path.getsize),
   and [`os.path.splitext`](http://docs.python.org/2/library/os.path.html#os.path.splitext).

 * Bonus: use [`collection.defaultdict`](http://docs.python.org/2/library/collections.html#collections.defaultdict).

    Example:

        #!python
        from collections import defaultdict

        def create_player():
            return {
                'hit points': 10,
                'money': 1000,
            }

        players = defaultdict(create_player)

        # defaultdict calls create_player on first access to players['foo'].
        # There is no need to explicitly call:
        #   players['foo'] = create_player()

        players['Aragorn']['hit points'] += 5
        players['Frodo']['hit points'] -= 1
        players['Bilbo']['money'] += 50

        for name, info in players.items():
            print name, info
