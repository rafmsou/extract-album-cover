import argparse
from mutagen import mp4

def save_artwork(image, path):
  with open(path, 'wb') as img:
   img.write(image)

def get_artwork(filename):
  try:
    file = mp4.MP4(filename)
    albumtitle = file.tags['\xa9alb'][0] if len(file.tags['\xa9alb']) > 0 else 'album'
    imagepath = '{}/{}.png'.format(filename[0:filename.rfind('/')], albumtitle)

    if len(file.tags['covr']) > 0:
      artwork = file.tags['covr'][0]
      save_artwork(artwork, imagepath)
  except FileNotFoundError:
    print('The specified file was not found.')


parser = argparse.ArgumentParser(description='Saves embedded artwork (ID3Tag) from a music file.')
parser.add_argument('filename', metavar='filename', help='The song\'s filename.')
args = parser.parse_args()
get_artwork(args.filename)
