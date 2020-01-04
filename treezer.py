import re

class Element:

	def __init__(self,name):
		self.name=name;
		print("Element created: " + self.name)
		
def parseTags(content):

	# Matches: open tag, a word, spaces, as many attributes (making sure quotes match)	
	openTagRe = re.compile(r'<(\w+)(\s(\w+(=(?P<quote>\"|\').*(?P=quote)?))?)*>')
	openTag = re.search(openTagRe,content)	

	# find closing tag for new tag
	closeTagRe = re.compile(r'<\/('+openTag.group(1)+')>')
	closeTag = re.search(closeTagRe,content)	
	print("Open tag: " + openTag.group(0))
	print("Close tag: " + closeTag.group(0))	
	# run parsetags on all internal content	

if __name__=="__main__":
	print("Treezer running.")
	parseTags("<body></body>")
