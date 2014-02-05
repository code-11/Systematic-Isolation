from HTMLParser import HTMLParser
import urllib2



# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
        #print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        pass
        #print "Encountered an end tag :", tag
    def handle_data(self, data):
        data=data.strip()
        if data=="Change 3D viewing mode":
            self.record=True
        if (len(data)<100) and (data!="") and (self.record==True):
            self.playlist.append(data)
    def get_source(self, website):
        return urllib2.urlopen(website).read()
    def post_processing(self):
        self.playlist.pop(0)
        self.playlist.pop(0)
        self.playlist.insert(0,"1")
        self.playlist.pop(-1)
        self.playlist.pop(-1)
        self.playlist.pop(-1)
        self.playlist.pop(-1)
        self.playlist.pop(-1)
        self.refined_playlist=[]
        
        for el in self.playlist:
            if not el.isdigit():
                if not el.lower().startswith("by"):
                    self.refined_playlist.append(el)        
    def write_to_file(self,output_name="playlist"):
        self.output_file=open(output_name+".txt","w")
        for item in self.refined_playlist:
            print>>self.output_file, item
    def extract(self, website):
        self.playlist=[]
        self.record=False
        self.feed(self.get_source(website))
        self.post_processing()
        self.write_to_file()
        # print self.refined_playlist



# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
response=parser.extract("YOUR PLAYLIST URL HERE")
# response = urllib2.urlopen()
# page_source = response.read()
#print response