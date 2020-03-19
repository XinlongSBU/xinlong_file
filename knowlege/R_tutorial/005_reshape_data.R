# Reshaping Data

# transpose
y<-matrix(1:20, nrow=5,ncol=4)
t(y)

# creat a dataframe
a <- c(1,1,2,2)
b <- c(1,2,1,2)
d <- c(5,3,6,2)
e <- c(6,5,1,4)
mydata <- data.frame(a,b,d,e)
names(mydata) <- c("id","time","x1","x2") # variable names

library(reshape)
# you "melt" data so that each row is a unique id-variable combination
mdata <- melt(mydata, id=c("id","time"))

# cast the melted data
# cast(data, formula, function) 
subjmeans <- cast(mdata, id~variable, mean)
timemeans <- cast(mdata, time~variable, mean)
