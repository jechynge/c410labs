#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()

print "Content-type: text/html"
print

if(form.length > 37):
    print "<div style='margin:10;padding:10;border:1px solid blue;background-colour:lightgrey;width:50%;'>"
    
    if(form.getvalue('name') != None):
        print "<h4>Name: %s</h4>" % form.getvalue('name')
    
    if(form.getvalue('family') != None):
        print "<h4>Family: %s</h4>" % form.getvalue('family')
        
    if(form.getvalue('age') != None):
        print "<h4>Age: %s</h4>" % form.getvalue('age')
    
    if(form.getvalue('hobby') != None):
        print "<h4>Favourite Hobby: %s</h4>" % form.getvalue('hobby')
        
    print "</div>"

print "<title>Test CGI</title>"

print "<form method='POST' action='/cgi/page2.py'>"

print "<h3>Name</h3>"
print "<input type='text' name='name' /><br />"

print "<h3>Family</h3>"
print "<input type='text' name='family' /><br />"

print "<input type='submit' name='submit' value='Send' />"
print "</form>"