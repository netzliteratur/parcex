#Description
parcex extracts content from warc files.

#Usage
./parcex.py WARC-FILE

WARC-FILE must be a warc file that conforms to

http://bibnum.bnf.fr/WARC/WARC_ISO_28500_version1_latestdraft.pdf

#Output
- Directory structure with the schema as root.
- The structure maps the structure of the web resource.
- Empty file names are named index.html.N, where N >= 0

#Requirements
Python 2.7/3.x

#Status
Testing
