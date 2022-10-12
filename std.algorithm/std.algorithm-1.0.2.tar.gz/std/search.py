
# https://www.inf.fh-flensburg.de/lang/algorithmen/pattern/sundayen.htm
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
# https://www.jianshu.com/p/2594d312cefd
def sunday(haystack, needle):
    
    needelLength = len(needle)
    
    haystackLength = len(haystack)
    
    dic = {v:needelLength - k for k, v in enumerate(needle)}
    
    end = needelLength
    
    while end <= haystackLength:
        begin = end - needelLength
        if haystack[begin:end] == needle:
            return begin

        if end >= haystackLength:
            return -1

        offset = dic.get(haystack[end])
        if not offset:
            offset = needelLength + 1
        
        end += offset

    return -1
    
