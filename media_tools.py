#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "13-07-2016"
__license__   = "MIT"
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
        self.fname, self.fext = os.path.splitext(source)

    def convert_to_mp3(self):
        """Convert any media file to mp3

        :returns: None
        """
        infile = self.source
        outfile = self.fname + '.mp3'
        # ffmpeg command to converts input file to mp3
        # -b:a: audio bit rate of mp3 file set to 128kbps
        # -vn: disable video recording
        ffmpeg_cmd = (
                "ffmpeg -i {infile} -b:a 128K -vn {outfile}".format(
                    infile=infile, outfile=outfile
                    )
                )
        subprocess.call(
                ffmpeg_cmd, shell=True, 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                )

    def cut_it(self, start, stop):
        """Cut from mp3 files

        :start: int, start point 
        :stop: int, stop point
        :returns: None
        """
        infile = self.source
        outfile = self.fname + '_cutted' + '.mp3'
        ffmpeg_cmd = (
                "ffmpeg -ss {start} -t {stop} -i {infile} {outfile}".format(
                    start=start, stop=stop, 
                    infile=infile, outfile=outfile
                    )
                )
        subprocess.call(
                ffmpeg_cmd, shell=True, 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                )

    def convert_to_mp4(self):
        """Convert any media file to mp4

        :returns: None
        """
        infile = self.source
        outfile = self.fname + '.mp4'
        ffmpeg_cmd = (
                "ffmpeg -i {infile} -codec copy {outfile}".format(
                    infile=infile, outfile=outfile
                    )
                )
        subprocess.call(
                ffmpeg_cmd, shell=True, 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                )


if __name__ == "__main__":
    # Parse commandline options with argparse
    parser = ArgumentParser(description="Media Tools")
    parser.add_argument(
            '-v', '--version',
            action='version',
            version='%(prog)s version 0.1'
            )
    parser.add_argument(
            'source',
            action='store',
            help="source file"
            )
    parser.add_argument(
            '-cut',
            nargs=2,
            metavar=('Start', 'Stop'),
            action='store',
            help="Cut mp3 files"
            )
    parser.add_argument(
            '-mp3',
            action='store_true',
            help="Convert to mp3"
            )
    parser.add_argument(
            '-mp4',
            action='store_true',
            help="Convert to mp4")
    args = parser.parse_args()

    media_tools = MediaTools(args.source)

    if args.mp3:
        media_tools.convert_to_mp3()
    elif args.mp4:
        media_tools.convert_to_mp4()
    elif args.cut:
        start, stop = args.cut
        media_tools.cut_it(start, stop)
