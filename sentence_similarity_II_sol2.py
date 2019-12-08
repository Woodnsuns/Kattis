class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        word_dict1 = set()
        word_dict2 = set()
        for word in words1:
            word_dict1.add(word)
        for word in words2:
            word_dict2.add(word)

        def dfs(word1, word2, graph):
            stack = []
            if word1 == word2:
                return True
            if word1 not in graph:
                return False
            list1 = graph[word1]
            visited = set()
            for word in list1:
                stack.append(word)
            while stack != []:
                next_word = stack.pop()
                if next_word in visited:
                    continue
                else:
                    visited.add(next_word)
                if next_word == word2:
                    return True
                for word in graph[next_word]:
                    if word not in visited:
                        stack.append(word)
            return False

        if len(words1) != len(words2):
            return False
        
        graph = dict()

        for pair in pairs:
            word1 = pair[0]
            word2 = pair[1]
            if word1 not in graph:
                graph[word1] = list()
            if word2 not in graph:
                graph[word2] = list()
            graph[word1].append(word2)
            graph[word2].append(word1)
            #print ("word1: {}, word2:{}".format(word1, word2))
        
        result = True
        for i in range(len(words1)):
            result = result and dfs(words1[i], words2[i], graph)
        return result
