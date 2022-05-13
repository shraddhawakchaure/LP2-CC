import webapp2
import os
import json
import urllib

from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html') 
        return self.response.out.write(template.render(path,template_values))

    def post(self):
        university = self.request.get('zipCode')
        if not university.isalpha() :
            template_values = {
                "error":"Incorrect name"
            }
            path = os.path.join(os.path.dirname(__file__),'index.html')
            return self.response.out.write(template.render(path,template_values))

        base_url="http://universities.hipolabs.com/search?name="
        url = base_url + university 
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        print(data)
        template_values = {
            "web_page": data[0]['web_pages'] or "not available",
            "country":data[0]['country'] or "not available",
            "domain":data[0]['domains'] or "not available",
            "name":data[0]["name"] or "not available",
        }
        path = os.path.join(os.path.dirname(__file__), 'result.html')
        self.response.out.write(template.render(path, template_values))    

app = webapp2.WSGIApplication([('/',MainPage),],debug=True)