class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
 
        # 첫 번째 문자열 부터 전체 문자열을 순회하면서 전체 문자열 중에 같은 문자를 찾기
        for index, letter in enumerate(s):
            iterate = re.finditer(f'{letter}', s)
            
            # 동일한 문자 찾아 해당 문자를 기준으로 reverse 해보기
            for i in iterate:
                string = s[index : i.start() + 1]
                if string == string[::-1] and len(longest) < len(string): # palindromic이고 length가 가장 길면 저장
                    longest = string

        return longest

