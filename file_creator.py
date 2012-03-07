import subprocess
import os
import random
import string

def random_string( char_min, char_max ):
  return "".join( random.sample( string.letters + string.digits,random.randrange( char_min, char_max)) )


path = raw_input( "Enter directory name (default '/srv/ftp/'): " )

if ( not path ):
  path = '/srv/ftp/'

num = -1
while ( num < 1 or num > 1000 ):
  num = input( "Number of files to generate on every level( upper limit 1000 ): " )
dir_depth = -1
while ( dir_depth < 1 or dir_depth > 5 ):
  dir_depth = input( "How many levels of directories you want (upper limit 5 ): ")
dir_num = -1
while ( dir_num < 1 or dir_num > 10 ):
  dir_num = input( "How many diretories per level ( upper limit 10 ): ")


def generate( num, dir_level, dir_num, path ):
  if ( dir_level < 1 ):
    return
  
  for i in range ( num ):
    name = random_string( 4, 13 )
    ext  = random_string( 1, 3 )
    subprocess.call( ['touch', path + name + '.' + ext] )

  if ( dir_level < 2 ):
    return

  for i in range ( dir_num ):
    name = random_string( 7, 10 )
    subprocess.call( ['mkdir', path + name ] )
    generate( num, dir_level - 1, dir_num,  path + name + '/' )

generate( num, dir_depth, dir_num,  path )
