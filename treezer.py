import re

#TODO: DEAL WITH EOLs IT'S PROBABLY VERY EASY

class Element:

	def __init__(self,name,children,properties,pdata):
		self.name=name
		self.children=children
		self.properties=[]
		self.parseData={"blockSize":pdata[0],"blockPos":pdata[1]} # pdata is data gathered by and used in the parsing process
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
	tagRe = re.compile(r'(<(?P<tname>\w+))(\s(\w+(=(?P<quote>\"|\').*(?P=quote)?))?)*((\/>)|(>(.*)(<\/(?P=tname)>)))', re.IGNORECASE)
	tag = re.search(tagRe,content)
	
	# if contents aren't a tag, return the text
	if (tag==None):
		return content

	# extract properties
	properties=[]
	
	children=[]

	# TODO: CHECK IF MATCH LENGTH IS EXACTLY THAT OF THE DATA, ELSE EVERYTHING BEFORE AND AFTER MUST BE CHECKED
	# if tag.group(10) exists, there is child data
	if (tag.group(10)):
		contentData = tag.group(10)
		while (contentData): # While there is data left to process in the contents
			nextTag=parseTags(contentData)
			children.append(nextTag)
			
			contentData = "" # prevent infinite looping

	return Element(tag.group(2),children,properties,(len(content),0))

if __name__=="__main__":
	print("Treezer running.")
	parseTags("<html><a><span>abcdefg</span></a><b/></html>").log()

	print("Treezer completed.")
