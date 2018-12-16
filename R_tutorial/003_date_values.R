# Date Values

# use as.Date( ) to convert strings to dates 
mydates <- as.Date(c("2007-06-22", "2004-02-13"))
# number of days between 6/22/07 and 2/13/04 
days <- mydates[1] - mydates[2]

Sys.Date( ) # returns today's date. 
date() # returns the current date and time.

# print today's date
today <- Sys.Date()
format(today, format="%B %d %Y")

# convert date info in format 'mm/dd/yyyy'
strDates <- c("01/05/1965", "08/16/1975")
dates <- as.Date(strDates, "%m/%d/%Y")

# convert dates to character data
strDates <- as.character(dates)

