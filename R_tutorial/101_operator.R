# Operators

# Use the assignment operator <- to create new variables.

x1 <- 2
x2 <- 5
sum <- x1+x2
product <- x1*x2
y <- c(1:10)
z <- TRUE

# there is other operators such as logical operators
y1 <- y[y>8]
y2 <- y[(y>8) | (y<5)]   # the element in y which is > 8 or < 5
y3 <- y[(y>3) & (y<=7)]  # the element in y which is > 3 or <= 7
y4 <- y[(y!=1)]          # the element in y which is not equal to 1
y5 <- y[(y==1)]          # the element in y which is equal to 1
z1 <- !z                 # Not z

# y>8 returns a logical vector
l <- y>8
