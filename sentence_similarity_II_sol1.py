class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """

        if len(words1) != len(words2):
            return False
        
        def find(word, word_to_color):
            if word in word_to_color:
                return word_to_color[word]
            else:
                return -1

        def union(word1, word2, word_to_color, color_to_words):
            color1 = word_to_color[word1]
            color2 = word_to_color[word2]
            list1 = color_to_words[color1]
            list2 = color_to_words[color2]
            for word in list2:
                word_to_color[word] = color1
                list1.append(word)
            del color_to_words[color2]
        
        word_to_color = dict()
        color_to_words = dict()
        max_index = 0

        for pair in pairs:
            word1 = pair[0]
            word2 = pair[1]
            color1 = find(word1, word_to_color)
            color2 = find(word2, word_to_color)
            if color1 == -1 and color2 == -1: #if both don't exist in dict 
                word_to_color[word1] = max_index
                word_to_color[word2] = max_index
                color_to_words[max_index] = list()
                color_to_words[max_index].append(word1)
                color_to_words[max_index].append(word2)
                max_index += 1
            elif color1 == -1:
                word_to_color[word1] = color2
                color_to_words[color2].append(word1)
            elif color2 == -1:
                word_to_color[word2] = color1
                color_to_words[color1].append(word2)
            else:
                union(word1, word2, word_to_color, color_to_words)

        print word_to_color
        print color_to_words
        colors1 = set()
        colors2 = set()
        for word in words1:
            colors1.add(find(word, word_to_color))
        for word in words2:
            colors2.add(find(word, word_to_color))
        result = True
        for color in colors1:
            result = result and (color in colors2)
        return result

def stringToStringArray(input):
    return json.loads(input)

def stringToString2dArray(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            words1 = stringToStringArray(line)
            line = lines.next()
            words2 = stringToStringArray(line)
            line = lines.next()
            pairs = stringToString2dArray(line)
            
            ret = Solution().areSentencesSimilarTwo(words1, words2, pairs)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()