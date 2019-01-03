# Sorting and Merging Data

# sorting examples using the mtcars dataset
attach(mtcars)

# sort by mpg (ascending) 
newdata1 <- mtcars[order(mpg),] 
# sort by mpg and cyl
newdata2 <- mtcars[order(mpg, cyl),]
#sort by mpg (ascending) and cyl (descending)
newdata3 <- mtcars[order(mpg, -cyl),] 

# define dataframe
authors <- data.frame(
  ## I(*) : use character columns of names to get sensible sort order
  surname = I(c("Tukey", "Venables", "Tierney", "Ripley", "McNeil")),
  nationality = c("US", "Australia", "US", "UK", "Australia"),
  deceased = c("yes", rep("no", 4)))
authorN <- within(authors, { name <- surname; rm(surname) })
books <- data.frame(
  name = I(c("Tukey", "Venables", "Tierney",
             "Ripley", "Ripley", "McNeil", "R Core")),
  title = c("Exploratory Data Analysis",
            "Modern Applied Statistics ...",
            "LISP-STAT",
            "Spatial Statistics", "Stochastic Simulation",
            "Interactive Data Analysis",
            "An Introduction to R"),
  other.author = c(NA, "Ripley", NA, NA, NA, NA,
                   "Venables & Smith"))

# Merge authorN and books
m0 <- merge(authorN, books)
m1 <- merge(authors, books, by.x = "surname", by.y = "name")
