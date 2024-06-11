class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase로 만들기
        s_lower = s.lower()

        # 정규식으로 letter or number인 문자만 필터링
        s_regex = re.sub("[^a-z0-9]", "", s_lower)

        # 문자열 뒤집어서 비교하기
        return s_regex == s_regex[::-1]