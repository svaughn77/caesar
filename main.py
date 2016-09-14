#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#





import webapp2
from caesar import encrypt


page_header = """
<!DOCTYPE html>
<html>
<head>
<title>Formation</title>
</head>
<body>
    <h1>Encryption</h1>
"""

page_footer = """
</body>
</html>
"""


#class Welcome(BaseHandler2):
#    def get(self):
#        username = self.request.get('username')
#        if valid_username(username);
#            self.render('welcome.html', username = username)  * welcom to welcome
#        else:
#            self.redirect('/unit2/signup')


class MainHandler(webapp2.RequestHandler):
    def get(self):


#     self.response.write('Hello world!')
        edit_header_txt = "<h2>Enter text then enter rotation amount below the text</h2>"
        add_form_txt = """
        <form method="post" action="/formation">
        <textarea name="text"
                   style="height: 100px; width: 400px;"></textarea>
                    <br>
        <input type="number" name="rotation"
            style="height: 40px; width: 100px;"/>
           <br>

        <input type="submit" value="Submit"/>
        </form>
        """


#COde below works...testing line above
        response = page_header + edit_header_txt + add_form_txt  + page_footer
        self.response.write(response)

class Encrypt(webapp2.RequestHandler):
    def post(self):
        #
        #textarea = encrypt
        #response = page_header + edit_header + add_form + textarea + page_footer
        # answer = encrypt("text","rotation")
        # response = page_header + answer
        #
        # encrypt = self.request.get("answer")
        # self.response.write(encrypt)

        text = self.request.get("text")
        rotation = self.request.get("rotation")
        answer = encrypt(text, int(rotation))
        self.response.write(answer)
#        responses = page_header + edit_header_txt + add_form_txt + answer + page_footer
#        self.response.write(responses)

#app = webapp2.WSGIApplication([
 #  ('/', MainHandler)
#], debug=True)

#app = webapp2.WSGIApplication([('/unit2/rot13', Rot13),
app = webapp2.WSGIApplication([
('/', MainHandler),
('/formation', Encrypt)
],
debug = True)
#                               ('/unit2/signup', Signup),
#                               ('/unit2/welcome', Welcome)],









#answer = encrypt("Hello, Zach!", 2)
#print(answer)
