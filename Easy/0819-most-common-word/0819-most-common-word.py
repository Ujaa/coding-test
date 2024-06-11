class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # lowercase
        paragraph = paragraph.lower()

        # 특수문자 제거
        paragraph = re.sub("[^\w\s]", " ", paragraph)
    
        # 공백 기준 split
        words = paragraph.split()

        # 단어 등장 회수 별로 카운트
        word_count = defaultdict(lambda: 0)
        for word in words:
            if word not in banned:
                word_count[word] += 1
        
        return max(word_count, key=word_count.get)