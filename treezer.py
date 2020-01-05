import re

class Element:

	def __init__(self,name,children):
		self.name=name
		self.children=[]
		self.properties=[]
		self.content=""
		#print("Element created: " + self.name)
		
def parseTags(content):

	if ((not content) or (content == "")):
		return

	# TODO: Self-closing tags

	# Matches: open tag, a word, spaces, as many attributes (making sure quotes match)	
	openTagRe = re.compile(r'<(\w+)(\s(\w+(=(?P<quote>\"|\').*(?P=quote)?))?)*>', re.IGNORECASE)
	openTag = re.search(openTagRe,content)	
	
	# find closing tag for new tag
	closeTagRe = re.compile(r'<\/('+openTag.group(1)+')>', re.IGNORECASE)
	closeTag = re.search(closeTagRe,content)	
	#print("Open tag: " + openTag.group(0))
	#print("Close tag: " + closeTag.group(0))		

	internalContent = content[openTag.span()[1]:closeTag.span()[0]]	
	return Element(openTag.group(1),parseTags(internalContent))

if __name__=="__main__":
	print("Treezer running.")
	print("Root tag: " + parseTags("<html><body><img><a></a></img><img></img></body></html>").name)
	print("Treezer completed.")
