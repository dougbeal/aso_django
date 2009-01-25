import os, sys, re

current = os.getcwd()

from os.path import join, getsize

directories = []
root = ""
for root, directories, files in os.walk( current ):
    break

is_dot = re.compile( "\..*" )
def not_dot_dir(dir): return None == is_dot.match( dir )


add_to_path = filter(not_dot_dir, directories)


for directory in add_to_path:
    sys.path += [ os.path.join( root, directory ) ]

