class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 로그를 제외하고 뒤 문자열을 확인해 letter-log인지 digit-log인지 확인
        letter_logs = []
        number_logs = []

        for log in logs:
            log_content = log.split()[-1]
            if log_content.isalpha():
                letter_logs.append(log)
            if log_content.isdigit(): 
                number_logs.append(log)

        # letter-logs를 사전순으로 정렬
        letter_logs = sorted(letter_logs, key=lambda log:(log.split(" ", 1)[1], log.split(" ", 1)[0]))
        
        # digit-log 추가
        return letter_logs + number_logs
        