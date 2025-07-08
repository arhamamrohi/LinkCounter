# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from flask import Flask,request, render_template
import urlscraper

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    

    return render_template("home.html")

@app.route('/List',methods=['POST'])
def count_links():
        print(request.form['url'])
        url = request.form['url']
        #res = "Post  Request Url is  "+url
        urllist = urlscraper.scraplinks(url)
        
        urllistset= set(urllist)
        urllist= list(urllistset)
        
        #return urllist
        print(urllist)
        return render_template("list.html",website =url,urllist = urllist)
    


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
