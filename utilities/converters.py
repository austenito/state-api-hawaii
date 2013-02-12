from werkzeug.routing import BaseConverter

# http://stackoverflow.com/questions/5870188/does-flask-support-regular-expressions-in-its-url-routing
# TODO: Need to investigate, but works for now (ryankanno) <Tue Feb 12 07:36:23 2013> 
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]
