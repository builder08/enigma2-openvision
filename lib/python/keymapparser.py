# This module is a placeholder / redirector to allow old code and plugins
# to continue to function until such time that they are updated to use the
# newer modules and methods.

from ActionMap import loadKeymap, parseKeymap, removeKeymap as removeKeymapNew


class KeymapError(Exception):
	def __init__(self, message):
		self.msg = message

	def __str__(self):
		return self.msg


def parseKeys(context, filename, actionmap, device, keys):
	return parseKeymap(filename, context, actionmap, device, keys)


def readKeymap(filename):
	return loadKeymap(filename)


def removeKeymap(filename):
	return removeKeymapNew(filename)
