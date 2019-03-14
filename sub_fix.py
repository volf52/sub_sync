# /usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument(
    "-d",
    "--directory",
    action="store",
    dest="root_dir",
    help="The directory with files (Default = current dir)",
)
parser.add_argument(
    "-v",
    "--vid-ext",
    action="store",
    dest="vid_ext",
    help="The extension for video files. (Default = mp4)",
    default="mp4",
)
parser.add_argument(
    "-s",
    "--sub-ext",
    action="store",
    dest="sub_ext",
    help="The extension for sub files. (Default = srt)",
    default="srt",
)
parser.add_argument(
    "-r",
    "--reverse",
    action="store_true",
    dest="rev",
    help="Rename files using sub names instead of vid file names",
)

args = parser.parse_args()

files = os.listdir(args.root_dir)
vid_files = [x for x in files if x.endswith(args.vid_ext)]
sub_files = [x for x in files if x.endswith(args.sub_ext)]

if args.rev:
    old_names = vid_files[:]
    new_names = [os.path.splitext(x)[0] + "." + args.vid_ext for x in sub_files]
else:
    old_names = sub_files[:]
    new_names = [os.path.splitext(x)[0] + "." + args.sub_ext for x in vid_files]

for old, new in zip(old_names, new_names):
    old = os.path.join(args.root_dir, old)
    new = os.path.join(args.root_dir, new)
    os.rename(old, new)

print("Done...")
