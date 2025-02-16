-- 코드를 입력하세요
SELECT 
    I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, 
    ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_REVIEW R
JOIN REST_INFO I
ON R.REST_ID = I.REST_ID
WHERE I.ADDRESS LIKE '서울%'
GROUP BY I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS
ORDER BY SCORE DESC, FAVORITES DESC

