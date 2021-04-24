def groupStrings( strings):
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    result = {}
    for word in strings:
        if len(word) not in result:
            result[len(word)]=[word]
        else:
            result[len(word)].append(word)
    return result.values()

print(groupStrings(strings = ["abc","bcd","acef","xyz","az","ba","a","z"]))