import argparse
from mutagen import mp4


parser = argparse.ArgumentParser(description='Saves embedded artwork (ID3Tag) from a music file.')
parser.add_argument('filename', metavar='filename', help='The song\'s filename.')

args = parser.parse_args()

try:
  file = mp4.MP4(args.filename)
  album_title = file.tags['\xa9alb'][0] if len(file.tags['\xa9alb']) > 0 else 'album'
  
  if len(file.tags['covr']) > 0:
    artwork = file.tags['covr'][0]
    save_artwork(artwork, album_title)
except FileNotFoundError:
  print('The specified file was not found.')
   
   
def save_artwork(image, name):
  with open(name +'.jpg', 'wb') as img:
   img.write(artwork)
