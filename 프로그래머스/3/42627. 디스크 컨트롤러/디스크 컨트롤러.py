import heapq

def solution(jobs):
    jobs = sorted([(r, w, i) for i, (r, w) in enumerate(jobs)])  # 요청 시각 기준 정렬
    heap = []
    time, i, total = 0, 0, 0
    n = len(jobs)
    
    while i < n or heap:
        # 현재 시간까지 들어온 작업들을 힙에 추가
        while i < n and jobs[i][0] <= time:
            r, w, idx = jobs[i]
            heapq.heappush(heap, (w, r, idx))  # 우선순위: 소요시간 → 요청시각 → 작업번호
            i += 1
        
        if heap:
            w, r, idx = heapq.heappop(heap)
            time += w
            total += time - r  # 반환 시간 = 완료 시각 - 요청 시각
        else:
            # 실행 가능한 작업이 없으면 time을 다음 작업 도착 시점으로 점프
            time = jobs[i][0]
    
    return total // n
