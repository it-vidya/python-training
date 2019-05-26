import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
    

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      print('startElement called for ',tag)

    # Call when a character is read
   def characters(self, content):
      print('characters called for ',self.CurrentData)
   # Call when an elements ends
   def endElement(self, tag):
      print('endElement called for ',tag)
      self.CurrentData = ""

   
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   
	# override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("movies2.xml")
   
   
   
   
   
   
   