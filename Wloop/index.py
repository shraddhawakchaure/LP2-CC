import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        i=10
        while i>0:
            self.response.write("Disha<br>")
            i = i-1 

app = webapp2.WSGIApplication([('/',MainPage),],debug=True)