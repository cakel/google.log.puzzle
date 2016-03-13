### google.log.puzzle
Alternative solution for Google Python Class' logpuzzle Solution. Problem and resources is located at [Google's Python Class](https://developers.google.com/edu/python/)

### Requirement
* python 2.x (tested with Python 2.7.11/Windows 7 x64)

### Change from reference solution
Images reside at Google server which uses HTTPS. So reference solution doesn't work with urllib's _urlretrieve()_ or _urlopen()_ showing below error  message
```
urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed 
```
This code changes to urllib2 and add dummy cerification which could communicate using HTTPS

### Usage
```
logpuzzle.py [--todir dir] logfile (animal_code.google.com|place_code.google.com)
```
Log file includes *animal_code.google.com* and *place_code.google.com*. Result images/html are archived as their name with zip extension.
if *--todir* is omitted, only shows result URL.

### License
CC Attribution: the images used in this puzzle were made available by their owners under the [Creative Commons Attribution 2.5 license](http://creativecommons.org/licenses/by/2.5/), which generously encourages remixes of the content such as this one. The animal image is from the user zappowbang at flickr and the place image is from the user booleansplit at flickr.
