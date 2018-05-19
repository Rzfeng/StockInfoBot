import sys; sys.path.insert(0, 'lib') # this line is necessary for the rest
import os                             # of the imports to work!

import web
import stockBot

from jinja2 import Environment, FileSystemLoader
from datetime import datetime

###########################################################################################
##########################DO NOT DELETE ANYTHING ABOVE THIS LINE!##########################
###########################################################################################


# WARNING: DO NOT CHANGE THIS METHOD
#Will explain what's going on later
def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(autoescape=True,
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            extensions=extensions,
            )
    jinja_env.globals.update(globals)

    web.header('Content-Type','text/html; charset=utf-8', unique=True)

    return jinja_env.get_template(template_name).render(context)




#####################OUR CODE STARTS HERE#####################

urls = ('/selectStock', 'select_stock',
        # first parameter => URL, second parameter => class name
        '/', 'select_stock',
        '', 'select_stock'
        )


class select_stock:
    # Another GET request, this time to the URL '/selectStock'
    def GET(self):
        return render_template('select_stock.html')

    # A POST request
    #
    # You can fetch the parameters passed to the URL
    # by calling `web.input()' for **both** POST requests
    # and GET requests
    def POST(self):
        post_params = web.input()
        curTicker = post_params['enterstock']
        #update_message = 'Stock to search is %s' % (curTicker)
        info = stockBot.searchStock(curTicker)
        update_message = info
        return render_template('select_stock.html', message = info)



###########################################################################################
########################## TRY NOT TO CHANGE ANYTHING BELOW ###############################
###########################################################################################

if __name__ == '__main__':
    web.internalerror = web.debugerror
    app = web.application(urls, globals())
    app.run()
