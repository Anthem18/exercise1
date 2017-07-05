import jinja2
import os
import webapp2 # webapp2 is a module that you import




jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))




class MainHandler(webapp2.RequestHandler): # This is the handler class
    def get(self):
        #this is where you reference your HTML file
        template = jinja_environment.get_template('templates/today.html')
        self.response.out.write(template.render())

    def post(self):
        template=jinja_environment.get_template('templates/hello.html')
        template_variables = {
            'name1':self.request.get("name1"),
            'noun1':self.request.get("noun1"),
            'verb1':self.request.get("verb1"),

        }
        self.response.out.write(template.render(template_variables))



app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True) # creates a WSGIApplication and assigns it to the variable app.
