# Media tools

> `Media tools` is a combination of a lot of tools. I wanted to make it so that it
> would be the solution for all media tasks, if not all at least most of
> them. For example, conversion between media files, cut parts of files (make ringtones), make
> gifs, etc. For these tasks I am going to use the `ffmpeg` tool with Python. I also
> want to make a light weight gui for it.

Usage
-----

```
usage: media_tools [-h] [-v] [-cut Start Stop] [-mp3] source

Media Tools

positional arguments:
  source           source file

optional arguments:
  -h, --help       show this help message and exit
  -v, --version    show program's version number and exit
  -cut Start Stop  Cut mp3 files
  -mp3             Convert to mp3
```

TODO
----

`Media tools` is a work in progress, so any ideas and patches are appreciated.

* [x] Convert any media to mp3
* [x] Cut part of mp3 file

Contributing
------------

Feel free to improve `Media tools`. All kinds of pull-requests are welcome.

LICENSE
------

`Media tools` is licensed under 
[GPL3](https://github.com/nagracks/media_tools/blob/master/LICENSE)

