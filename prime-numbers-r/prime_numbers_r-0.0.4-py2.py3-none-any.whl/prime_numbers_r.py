from rpy2.robjects import r

def print_prime_numbers(last_number):
  """
  Print prime numbers count between 1 and n, both numers included.
  
  Parameters
  ----------
  last_number : int
  """
  if type(last_number) is int:
    n_string = str(last_number)
    msg1 = (f'''n <-{n_string}
    primes <- c(2,3)
      i <- 4
      k <- 3
    while (i <= n) {{
        primes[k]<-i
        for (j in 2:(i%/%2)) {{
        if(i%%j == 0){{
          primes <- primes[-length(primes)]
          k <- k-1
          break
          }}
        }}
        i <- i+1
        k <- k+1
      }}
      print(primes)''')
    r(msg1)
  else:
    print("You should use int Numbers")


