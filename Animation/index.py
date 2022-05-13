from distutils.log import debug
import os
import json
import urllib
from pickle import TRUE
import codecs
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path =os.path.join(os.path.dirname(__file__),'main.html')
        self.response.out.write(template.render(path,template_values))

    def post(self):
        name = self.request.get('id')
        url = "https://ghibliapi.herokuapp.com/films/"+name
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        print(data)
        title = data["title"]
        template_values = {
            "title": title
        } 
        path = os.path.join(os.path.dirname(__file__), 'result.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([("/",MainPage)],debug = True)