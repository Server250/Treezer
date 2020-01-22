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

	# if tag.group(10) exists, there is child data
	if (tag.group(10)):
		contentData = tag.group(10)
		while (contentData): # While there is data left to process in the contents
			#print("Content data: " + contentData)
			nextTag=parseTags(contentData)
			children.append(nextTag)
			
			# If tag didn't start at start of contents, there is text there which won't be caught by the regex
			tagStartPos = nextTag.parseData["blockPos"][0]
			if (tagStartPos > 0):
				children.insert(len(children)-1,contentData[:tagStartPos])				
			
			# If the tag didn't end at the end of the contents, everything left over must be parsed
			tagEndPos = nextTag.parseData["blockPos"][1]
			if (tagEndPos < len(contentData)):
				contentData = contentData[tagEndPos:]
			else:
				contentData = ""

		#print("NO MORE CONTENT DATA")

	return Element(tag.group(2),children,properties,(len(content),tag.span()))

if __name__=="__main__":
	print("Treezer running.")

	testData="<html><a><span>abcdef<p></p>teflon<q></q></span></a><b/></html>"
	
	print("Test data: " + testData)
	parseTags(testData).log()

	print("Treezer completed.")
