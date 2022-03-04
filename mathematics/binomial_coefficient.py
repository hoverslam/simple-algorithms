# ----------
# Calculate the binomial coefficient for n choose k.
# https://en.wikipedia.org/wiki/Binomial_coefficient
# ----------

def binomial_coefficient(n, k):
    if (k == 0) or (n == k):
        return 1
    else:
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)


if __name__ == "__main__":
    print("Chances of winning 'Lotto 6 aus 45': {}".format(binomial_coefficient(45, 6)))