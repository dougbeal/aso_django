import os, sys, re

current = __file__

from os.path import join, getsize

directories = []
root = ""
for root, directories, files in os.walk( os.path.dirname( current ) ):
    break

is_dot = re.compile( "\..*" )
def not_dot_dir(dir): return None == is_dot.match( dir )


add_to_path = filter(not_dot_dir, directories)


for directory in add_to_path:
    sys.path += [ os.path.join( root, directory ) ]

print current
print add_to_path
