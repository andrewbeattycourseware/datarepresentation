import urllib.parse
query = 'Hellö Wörld@Python'
parsed =  urllib.parse.quote(query)
print(parsed)
#'Hell%C3%B6%20W%C3%B6rld%40Python'

params = {'q': 'Python URL encoding', 'as_sitesearch': 'www.urlencoder.io'}
parsedparams = urllib.parse.urlencode(params)
print(parsedparams)
#'q=Python+URL+encoding&as_sitesearch=www.urlencoder.io'