import argparse
from mutagen import mp3,mp4

def get_file(filename):
  extension = filename[filename.rfind('.'):len(filename)]
  
  if extension == '.mp3':
    return mp3.MP3(filename), 'mp3'
  if extension == '.mp4' or extension == '.m4a':
    return mp4.MP4(filename), 'mp4'
    
def get_album_title(file, type):
  if type == 'mp3':
    return file.tags['TALB'][0]
  if type == 'mp4':
    return file.tags['\xa9alb'][0]
  return 'album-not-found'

def get_albuma_artwork(file, type):
  try:
    if type == 'mp3':
      return file.tags['APIC:'].data
    if type == 'mp4':
      return file.tags['covr'][0]
    return None
  except:
    print('Album artwork was not found in the file.')
    exit(1)
    
def save_artwork(image, path):
  with open(path, 'wb') as img:
   img.write(image)

def get_artwork(filename):
  try:
    file, type = get_file(filename)
    albumtitle = get_album_title(file, type)
    imagepath = '{}/{}.png'.format(filename[0:filename.rfind('/')], albumtitle)
    artwork = get_albuma_artwork(file, type)
    save_artwork(artwork, imagepath)
  except FileNotFoundError:
    print('The specified file was not found.')

    
parser = argparse.ArgumentParser(description='Saves embedded artwork (from ID3 or Mp4Tag) from a music file.')
parser.add_argument('filename', metavar='filename', help='The song\'s filename.')
args = parser.parse_args()
get_artwork(args.filename)
