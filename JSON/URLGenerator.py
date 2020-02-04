# Creator: Yupei Liu
# liu00222@umn.edu
# On Nov. 6, 2019

# This function is only used to generate the URLs for UMedia: https://umedia.lib.umn.edu/

def generateURL(filters, keys, keyword):

    # header
    url = "https://umedia.lib.umn.edu/search.json?"
    
    # search by filter
    for i in range(len(filters)):
        if not i:
            url += "facets%5B" + filters[i] + "%5D%5B%5D=" + keys[i]
        
        else: 
            url += "&facets%5B" + filters[i] + "%5D%5B%5D=" + keys[i]
    
    # connector between filters and keyword
    if len(filters):
        url += "&"
    
    # search by keyword
    if keyword: 
        url += "sort=&q=" + keyword
        
    return url



def wrapper():
    print(generateURL(["creator_ss", "types"], ["Detroit Publishing Co.", "Still Image"], "1147. P.Z.-Flüelen"))

    print(" ")

    print(generateURL([], [], "Digitizing Immigrant Letters"))



wrapper()
