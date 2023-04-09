# python-selenium-clicker-function
A function designed to make clicking links in your selenium script a bit simpler

link_click('TYPE', "XpathHere", description)

Use your driver object to .get a URL
driver.get('https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiA_M21wIn-AhX6mWoFHXadA1EQPAgJ')

The python-selenium-click-function takes 3 arguments:
XPATH - Specify wether using Xpath, ID, Class etc
"//a[@aria-label='Gmail (opens a new tab)']" - replace this with your Xpath (the link you want clicked)
'gmail button' - Description of the oject you want to click

EXAMPLE USE:
link_click('XPATH', "//a[@aria-label='Gmail (opens a new tab)']", 'gmail button')
