from SearchApp import SearchTerm


queryString = "compute these vectors exactly"

searchResult= SearchTerm(queryString)
print("Search result")
print("size = ",len(searchResult))
print("output : max 10 records ,  list of list -> [  [Title-page, web-address, star-time, content], [], []   ]")

for result in searchResult:
    print("{} \n".format(result))