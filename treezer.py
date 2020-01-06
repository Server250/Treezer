import re

#TODO: DEAL WITH EOLs IT'S PROBABLY VERY EASY

class Element:

	def __init__(self,name,children,properties):
		self.name=name
		self.children=children
		self.properties=[]
		#print("Element created: " + self.name)

	def log(self,indent=0):
		print(("\t"*indent) + "Element type: " + self.name)
		for e in self.children:
			if (type(e) is str):
				print (("\t"*(indent+1)) + "Element contents: " + e)
			else:
				e.log(indent+1)		

def parseTags(content):

	# Matches: open tag, a word, spaces, as many attributes (making sure quotes match)	
	tagRe = re.compile(r'<(?P<tname>\w+)(\s(\w+(=(?P<quote>\"|\').*(?P=quote)?))?)*((\/>)|(>(.*)(<\/(?P=tname)>)))', re.IGNORECASE)
	tag = re.search(tagRe,content)
	
	# if contents aren't a tag, return the text
	if (tag==None):
		return content

	# extract properties
	properties=[]
	
	children=[]
	# if tag.group(9) exists, there is child data
	if (tag.group(9)):
		#print("HAS CONTENTS")
		for e in re.findall(tagRe,tag.group(9)):
			#print("HAS CONTENTS")
			# PARSE ALL OF THEse hot mamas
		
	return Element(tag.group(1),children,properties)

if __name__=="__main__":
	print("Treezer running.")
	parseTags("<html><a><span>abcdefg</span></a><b/></html>").log()
	print("Treezer completed.")
