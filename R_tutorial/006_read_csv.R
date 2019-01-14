# To read a csv file 
mydata <- read.table("/Users/sailor/Desktop/R_tutorial/BicycleWeather.csv", header=TRUE, sep=",")

# You can also access the directory of the csv file and read it as follows:
# To get the current directory (in Mac OS X)
getwd()
# Output should be "/Users/sailor" in my labtop (my username is "sailor")

# To set a new working directory: /Users/sailor/Desktop/R_tutorial 
setwd("/Users/sailor/Desktop/R_tutorial")
# Then check the current working directory
getwd()
# Outupt should be "/Users/sailor/Desktop/R_tutorial"

# to read a csv file in the current directory
mydata <- read.table("BicycleWeather.csv", header=TRUE, sep=",")

# list the variables (name of each column) in mydata
names(mydata)

# list the structure of mydata
str(mydata)

# dimensions of mydata (number of rows and number of columns)
dim(mydata)

# class of an mydata (numeric, matrix, data.frame, etc)
class(mydata)

# print mydata 
mydata

# print first 10 rows of mydata
head(mydata, n=10)

# print last 5 rows of mydata
tail(mydata, n=5)

# output one of the column data of mydata
mydata$DATE

# length of mydata$DATE
length(mydata$DATE)
