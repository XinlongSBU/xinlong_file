# Importing Data

# From A Comma Delimited Text File
mydata <- read.table("/Users/sailor/Desktop/asro_work/xinlong_file/R_tutorial/Workbook1.csv")

# From Excel
library(xlsx)
mydata <- read.xlsx("/Users/sailor/Desktop/asro_work/xinlong_file/R_tutorial/Workbook1.xlsx", 1)

# From SPSS
library(Hmisc)    # use install.packages('Hmisc') if you don't have Hmisc package
mydata <- spss.get("/Users/sailor/Desktop/asro_work/xinlong_file/R_tutorial/Workbook1.por", 
                   use.value.labels=TRUE)