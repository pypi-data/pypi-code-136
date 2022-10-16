from rpy2.robjects import r
r('''
prime_nums <- function(n) {
    if(n >= 2){
        x = seq(2, n)
        prime_nums = c()
        for (i in seq(2, n)) {
            if (any(x == i)) {
            prime_nums = c(prime_nums, i)
            x = c(x[(x %% i) != 0], i)
        }
        }
        print(prime_nums)
        }
        else 
        {
        stop("Input number should be at least 2.")
        }
        }
   
# Function call
prime_nums(20)
''')