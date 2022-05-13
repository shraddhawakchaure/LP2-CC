import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        t1 = 0
        t2 = 1
        s1 = t1+t2
        self.response.write(str(t1)+"<br>")
        self.response.write(str(t2)+"<br>")
        for i in range(6):
            self.response.write(str(s1)+"<br>")
            t1 = t2
            t2 = s1
            s1 = t1+t2

app = webapp2.WSGIApplication([('/',MainPage),],debug=True)