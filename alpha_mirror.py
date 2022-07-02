def alpha_mirror(n):
    o=""
    key = { 'a':'z','b':'y','c':'x','d':'e','e':'v','f':'g','g':'t','h':'s','i':'r',
            'j':'k','k':'l','l':'m','m':'n','n':'m','o':'l','p':'q',
            'q':'r','r':'i','s':'h','t':'u','u':'v','v':'w','w':'x','x':'y','y':'b','z':'a',
                # UPPER
            'A':'Z','B':'C','C':'D','D':'E','E':'F','F':'G','G':'H','H':'I','I':'J','J':'K','K':'L','L':'M',
            'M': 'N','N':'O','O':'P','P':'Q','Q':'R','R':'S','S':'T','T':'U','U':'V','V':'W','W':'X','X':'Y',
            'Y': 'Z','Z':'A'}
    for x in n:
        v = x in key.keys()
        if v == True:
            o += (key[x])
        else:
            o += x
    return o

#RUN
# OK = alpha_mirror("")
# print(OK)
