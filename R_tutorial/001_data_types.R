# Data Types

# Vectors
a <- c(1,2,5.3,6,-2,4) # numeric vector
b <- c("one","two","three") # character vector
c <- c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE) #logical vector

# Refer to elements of a vector using subscripts.
a[c(2,4)] # 2nd and 4th elements of vector

# Matrices
y<-matrix(1:20, nrow=5,ncol=4)  # generates 5 x 4 numeric matrix 

# another example
cells <- c(1,26,24,68)
rnames <- c("R1", "R2")
cnames <- c("C1", "C2") 
mymatrix <- matrix(cells, nrow=2, ncol=2, byrow=TRUE,
                   dimnames=list(rnames, cnames))
# Identify rows, columns or elements using subscripts.
y[,4] # 4th column of matrix
y[3,] # 3rd row of matrix 
y[2:4,1:3] # rows 2,3,4 of columns 1,2,3

# Data Frames
d <- c(1,2,3,4)
e <- c("red", "white", "red", NA)
f <- c(TRUE,TRUE,TRUE,FALSE)
mydata <- data.frame(d,e,f)
names(mydata) <- c("ID","Color","Passed") # variable names

mydata[2:3] # columns 2,3of data frame
mydata[c("ID","Passed")] # columns ID and Passed from data frame
mydata$ID # variable ID in the data frame

# List
# example of a list with 4 components - 
# a string, a numeric vector, a matrix, and a scaler 
w <- list(name="Fred", mynumbers=a, mymatrix=y, age=5.3)

w[[2]] # 2nd component of the list
w[["age"]] # component named age in list

# Factors
# variable gender with 20 "male" entries and 
# 30 "female" entries 
gender <- c(rep("male",20), rep("female", 30)) 
gender <- factor(gender) 
summary(gender)

# Useful Functions
length(a) # number of elements or components
str(mydata)    # structure of an object 
class(y)  # class or type of an object
names(mydata)  # names

c(a,b)       # combine objects into a vector
cbind(a, b) # combine objects as columns
rbind(a, b) # combine objects as rows 
