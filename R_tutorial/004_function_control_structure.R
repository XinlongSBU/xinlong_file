# Function and Control Structures

# define a function to transpose a matrix
mytrans <- function(x) { 
  if (!is.matrix(x)) {      # if x is not a matrix
    warning("argument is not a matrix: returning NA")
    return(NA_real_)
  }
  y <- matrix(1, nrow=ncol(x), ncol=nrow(x)) 
  for (i in 1:nrow(x)) {    # nrow(x) the number or rows in matrix x
    for (j in 1:ncol(x)) {  # ncol(x) the number or columns in matrix x
      y[j,i] <- x[i,j] 
    }
  }
  return(y)
}

# try it
z <- matrix(1:10, nrow=5, ncol=2)
tz <- mytrans(z)
