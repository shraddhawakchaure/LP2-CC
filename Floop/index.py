import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(5):
            self.response.write("Disha<br>")

app = webapp2.WSGIApplication([('/',MainPage),],debug=True)