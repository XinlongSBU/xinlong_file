# Built-in Functions

# Almost everything in R is done through functions. Here are some examples

# Numeric Functions
x <- -3.1415
y <- 25
z <- 1.414
a <- 1.898

abs(x)  # absolute value 
sqrt(y) # square root

ceiling(x)
ceiling(z)

floor(x)
floor(z)

round(z, digits=2)
round(z, digits=0)
round(a, digits=0)

signif(z, digits=1)
signif(z, digits=3)

cos(x)
xin(x)
tan(x)

log(z)    # natural logarithm
log10(z)  # common logarithm
exp(z)    # e^z


# Character Functions
c <- "abcdef" 

# Extract or replace substrings in a character vector.
substr(c, start=2, stop=4)
substr(c, 2, 4) <- "22222" 
c

# Search for pattern in character vector d.
d <- c("abcdef","abc","km")
grep("abc",d)  # the 1st and 2nd element of d both has patten "abc". So reture 1 and 2

# split the string
e <- "hello"
strsplit(e,"") # return "h" "e" "l" "l" "o"
f <- "hello,how,hi,hei"
strsplit(f,",")  # split at where there is comma

# change to upper case
g <- "hello!"
toupper(g)

# change to lower case
h <- "APPLE"
tolower(h)


# Statistical Probability Functions

# normal density function (by default mean = 0 sd = 1)
dnorm(0)
# cumulative normal probability
pnorm(100)
# normal quantile. value at the 90 percentile of normal distribution 
qnorm(0.9)
# n random normal deviates with mean m and standard deviation sd. 
rnorm(n=50, m=0,sd=1)
# binomial distribution where size is the sample size 
# and prob is the probability of a heads (pi) 
dbinom(x=40, size=100, prob=0.5)
# prob of 0 to 5 heads of fair coin out of 10 flips
pbinom(q=0:50, size=100, prob=0.5)
# prob of 5 or less heads of fair coin out of 10 flips
qbinom(p, size, prob)

x <- c(1:10)
mean(x)  # mean of object x
sd(x)    # standard deviation of object x
median(x) # median of object x
quantile(x) # quantiles where x is the numeric vector
range(x)
sum(x)
min(x)
max(x)
scale(x)


# Other Useful Functions
y <- seq(from=0 , to=10, by=2) # generate a sequence
rep(y, 2) # repeat y n=2 times
