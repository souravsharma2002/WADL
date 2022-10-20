import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template
///

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        number = self.request.get('zipCode')
        table_var = int(number)
        responseString = ""
        for i in range(1, 11):
            table = "{} * {} = {}".format(table_var, i, table_var*i)
            responseString = responseString + "<h4>{}</h4>".format(table)
        self.response.out.write(responseString)
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)



///


