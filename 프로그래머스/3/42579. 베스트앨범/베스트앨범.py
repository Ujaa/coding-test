from collections import defaultdict

def solution(genres, plays):
    count = defaultdict(int)
    play_by_genre = defaultdict(list)
    
    for i in range(len(plays)):
        genre = genres[i]
        play = plays[i]
        
        count[genre] += play
        play_by_genre[genre].append([i, play])
        
    sorted_count = sorted(count.keys(), key=lambda x: count[x], reverse=True)
    
    answer = []
    
    for x in sorted_count:
        sorted_play = sorted(play_by_genre[x], key=lambda x: x[1], reverse=True)[:2]
        for a in sorted_play:
            answer.append(a[0])

    return answer

