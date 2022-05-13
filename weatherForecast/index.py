import os
import json
from re import template
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__),"index.html")
        self.response.out.write(template.render(path,template_values))

    def post(self):
        lon = self.request.get('lon')
        lat = self.request.get('lat')
        if not lon.isalpha() and not lat.isalpha() and abs(float(lat))<=90 and abs(float(lon))<=180:
            url="https://api.open-meteo.com/v1/forecast?latitude="+lat+"&longitude="+lon+"&hourly=temperature_2m&daily=temperature_2m_max&current_weather=true&timezone=America%2FNew_York&past_days=1"
            data = urllib.urlopen(url).read()
            data = json.loads(data)
            print(data)
            template_values = {
                "longitude": data['longitude'] or "not available",
                "latitude": data["latitude"] or "not available",
                "time": data['current_weather']['time'] or "not available",
                "windspeed": data['current_weather']['windspeed'] or "not available",
                "winddirection": data['current_weather']["winddirection"] or "not available",
                "temp": data["current_weather"]["temperature"] or "not available"
            }
            path = os.path.join(os.path.dirname(__file__), 'result.html')
            self.response.out.write(template.render(path, template_values))

        else:
            template_values = {
                "error" : "Invalid Data"
            }
            path = os.path.join(os.path.dirname(__file__), 'error.html')
            self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([("/",MainPage)],debug = True)