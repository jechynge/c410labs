#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()

print "Content-type: text/html"
print

print "<div style='margin:10;padding:10;border:1px solid blue;background-colour:lightgrey;width:50%;'>"

if(form.getvalue('name') != None):
    print "Name: %s<br /><br />" % form.getvalue('name')

if(form.getvalue('family') != None):
    print "Family: %s<br /><br />" % form.getvalue('family')
    
print "</div>"

print "<title>Test CGI</title>"

print "<form method='POST' action='/cgi/page1.py'>"

print "<h3>Name</h3>"
print "<input type='text' name='name' /><br />"

print "<h3>Family</h3>"
print "<input type='text' name='family' /><br />"

print "<h3>Age</h3>"
print "<input type='text' name='age' /><br />"

print "<h3>Favourite Hobby</h3>"
print "<input type='text' name='hobby' /><br />"

print "<input type='submit' name='submit' value='Send' />"
print "</form>"