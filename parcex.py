#!/usr/bin/env python3
"""
parcer extracts content from warc files.

USAGE:
    ./parcer.py WARC-FILE

WARC-FILE must be a warc file that conforms to:
    http://bibnum.bnf.fr/WARC/WARC_ISO_28500_version1_latestdraft.pdf
"""
import os
import sys


class WarcFileEx(object):
    """
    a warc file to web
    representation object
    """
    def __init__(self, source_file):
        """
        init values
        """
        self.source_file = source_file
        self.response_block = False
        self.line_counter = 0
        self.index_counter = 0

    def reset_init(self):
        """
        return init values
        """
        self.response_block = False
        self.line_counter = 0

    def parse_content(self):
        """
        """
        with open(self.source_file, "rb") as fd:
            warc_version = fd.readline()
            for line in fd:
                if line.lower().startswith(b"warc-type: response"):
                    self.response_block = True
                if line.lower().startswith(b"warc-target-uri") and self.response_block:
                    _full_path = line.decode("utf-8").split(":", 1)[1].strip()
                    _file_name = os.path.basename(_full_path)
                if line == b"\r\n" and self.response_block and self.line_counter < 2:
                    self.line_counter += 1
                if self.response_block and self.line_counter == 2:
                    if not os.path.exists(_full_path):
                        try:
                            os.makedirs(os.path.dirname(_full_path))
                        except OSError:
                            pass
                    if _file_name == "":
                        print("info: Empty filename. Assuming some index.html file. Using: "
                              "index.html." + str(self.index_counter))
                        _file_name = "index.html" + "." + str(self.index_counter)
                        self.index_counter += 1

                    if line == warc_version:
                        self.reset_init()
                    else:
                        if line == b"\r\n":
                            pass
                        else:
                            fd = open(os.path.dirname(_full_path) + "/" +_file_name, "ab")
                            fd.write(line)
                            fd.close()


def main():
    """
    the main function is executed 
    when parcer.py is executed.
    """
    source_file = sys.argv[1]
    warc_file = WarcFileEx(source_file)
    warc_file.parse_content()

if __name__ == '__main__':
    main()
