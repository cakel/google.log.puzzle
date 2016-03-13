#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib2
import ssl

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  return_list = []

  try:
    f = open(filename, 'rU')
    for readline in f.xreadlines():
      match = re.search(r'[a-z-_]+\.jpg', readline)
      if match and match.group() != 'no_picture.jpg':   # no_picture.jpg doesn't exist in google server
        url = 'https://developers.google.com/edu/python/images/puzzle/' + match.group()
        # print '{0}'.format(url)
        return_list.append(url)

  except IOError, e:
    print 'IOError {0!s}'.format(e.message)

  # remove duplicate
  return_list = list(set(return_list))

  # /edu/languages/google-python-class/images/puzzle/p-bjab-bbih.jpg => bbih
  return sorted(return_list, key=lambda x: (map(str, re.findall(r'([a-z]+).jpg', x)), x))

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  imgcount = 0
  context = ssl._create_unverified_context()    # for https retrieving

  if os.path.isdir(dest_dir) == False:
      os.mkdir(dest_dir)

  for img_url in img_urls:
    print 'Try to retrieving {0!s}'.format(img_url),

    try:
        url_file = urllib2.Request(img_url)
        download_file = urllib2.urlopen(url_file, context=context)
        save_as = 'img' + '{:03d}'.format(imgcount) + '.jpg'
        save_as_fullpath = os.path.join(dest_dir, save_as)
        write_file = open(save_as_fullpath, 'wb')
        write_file.write(download_file.read())
        print 'Saved as {0} OK'.format(save_as)
        imgcount += 1
    except IOError, e:
        print 'Error' + e.message

  write_file.close()

  # Craft index.html by creating img###.jpg
  body = ''
  head = '''
<html>
<body>
'''
  for img_index in range(imgcount):
      body = body + '<img src="img{:03d}.jpg">'.format(img_index)

  bottom = '''
</body>
</html>
'''

  write_file = open(os.path.join(dest_dir,'index.html'), 'w')
  write_file.write(head + body + bottom)
  write_file.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  # next step
  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
