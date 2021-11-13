## Description: Rake Routes File parser 
## Splint3r7 | Security Researcher
## Github: https://github.com/Splint3r7
######################

import sys
import argparse

parser = argparse.ArgumentParser(description="Fetching Routes from the Rake route output")

parser.add_argument('-r','--rakeroutes',
                            help = "rake routes file",
                            type = str,
                            required = False)


args = parser.parse_args()

f = open (args.rakeroutes, "r")

def clean(strr):

	a = strr.split("(")
	b = a[0]
	c = b.split(":")
	z = c[0]

	return z

def routes():

	routes = []
	for i in f:
		i = i.strip()
		x = i.split(" ")
		for z in x:
			z = z.strip()
			if z.startswith("/"):
				a = clean(z)
				routes.append(a)

	return routes

if __name__ == "__main__":

	arr = routes()
	arr_sort = list(dict.fromkeys(arr))
	for x in arr_sort:
		print(x)
