class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = list(map(lambda str: {
            self.get_identifier(collections.Counter(list(str))): str}, strs))

        merged_dict = collections.defaultdict(list)

        for count in counts:
            for key, value in count.items():
                merged_dict[key].append(value)

        return list(merged_dict.values())

    def get_identifier(self, items):
            a = ""
            for x, v in sorted(items.most_common(), key=lambda item: item[0]):
                a = a + str(x) + str(v)
            return a