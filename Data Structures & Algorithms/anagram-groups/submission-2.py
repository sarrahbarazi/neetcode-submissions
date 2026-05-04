class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #go through the strings, sort each word and save it as a key in the dict

        #word= "act" 
        #sorted = act
        # is it in dict? no, so add to dict and move on
        # {act: act}

        #word = "pots":
        #sorted = "opst"
        # is it in dict? no, so add to dict and move on
        # {act: act, opst: pots}

        #word = tops
        #sorted = opts
        # is it in dict? yes! so add word to key
        # {act: act, opst: pots, tops}

        #word = cat
        #sorted = act
        # is it in dict? yes! so add word to key
        # {act: act,cat opst: pots, tops}

        #word = stop
        #sorted = opst
        # is it in dict? yes! so add word to key
        # {act: act,cat opst: pots, tops, stop}

        #final map: {act: act,cat opst: pots, tops, stop aht: hat}
        #now that we have the map we can return list of values grouped by key
        hashmap = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        return list(hashmap.values())



