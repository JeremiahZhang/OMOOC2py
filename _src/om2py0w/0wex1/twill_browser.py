from twill import get_browser
b = get_browser()

b.go("http://www.python.org/")
b.showforms()

# To talk to the Web browser directly, call the get_browser function: