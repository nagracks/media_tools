#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "13-07-2016"
__license__   = "GPL3"
__copyright__ = "Copyright © 2016 nagracks"

import os
import subprocess
from argparse import ArgumentParser

class MediaTools(object):
    """MediaTools

    Constructor args:
    :source: str, source file name

    :methods:
    * convert_to_mp3
    * cut_it
    * convert_to_mp4
    """

    def __init__(self, source):
        self.source = source
        # Get file name and file extension
        self.fn, self.fe = os.path.splitext(source)

    def convert_to_mp3(self):
        """Convert any media file to mp3

        :returns: None
        """
        in_file = self.source
        out_file = self.fn + '.mp3'
        # ffmpeg command, converts input file to mp3
        # -b:a, audio bit rate of mp3 file set to 128kbps
        # -vn, disable video recording
        ffmpeg_cmd = ("ffmpeg -i {in_file} -b:a 128K -vn {out_file}"
                      "".format(in_file=in_file, out_file=out_file))
        subprocess.call(ffmpeg_cmd, shell=True)

    def cut_it(self, start, stop):
        """Cut from mp3 files

        :start: int, start point 
        :stop: int, stop point
        :returns: None
        """
        in_file = self.source
        out_file = self.fn + '_cutted' + '.mp3'
        ffmpeg_cmd = ("ffmpeg -ss {start} -t {stop} -i {in_f} {out_f}"
                      "".format(start=start, stop=stop, 
                                in_f=in_file, out_f=out_file))
        subprocess.call(ffmpeg_cmd, shell=True)

    def convert_to_mp4(self):
        """Convert any media file to mp4

        :returns: None
        """
        in_file = self.source
        out_file = self.fn + '.mp4'
        ffmpeg_cmd = ("ffmpeg -i {in_file} -codec copy {out_file}"
                      "".format(in_file=in_file, out_file=out_file))
        subprocess.call(ffmpeg_cmd, shell=True)


def parse_args():
    """Parse commandline args 
    :returns: args
    """
    parser = ArgumentParser(description="Media Tools")
    parser.add_argument('-v', '--version',
            action='version',
            version='%(prog)s version 0.1')

    parser.add_argument('source',
            action='store',
            help="source file")

    parser.add_argument('-cut',
            dest='cut',
            nargs=2,
            metavar=('Start', 'Stop'),
            action='store',
            help="Cut mp3 files")

    parser.add_argument('-mp3',
            dest='mp3',
            action='store_true',
            help="Convert to mp3")

    parser.add_argument('-mp4',
            dest='mp4',
            action='store_true',
            help="Convert to mp4")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    media_tools = MediaTools(args.source)

    if args.mp3:
        media_tools.convert_to_mp3()
    elif args.mp4:
        media_tools.convert_to_mp4()
    elif args.cut:
        start, stop = args.cut
        media_tools.cut_it(start, stop)
