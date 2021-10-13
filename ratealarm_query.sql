-- Author: Udemy Instructor 
CREATE OR REPLACE STREAM "ALARM_STREAM" (order_count INTEGER);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
    INSERT INTO "ALARM_STREAM"
        SELECT STREAM order_count
        FROM (
            SELECT STREAM COUNT(*) OVER TEN_SECOND_SLIDING_WINDOW AS order_count
            FROM "SOURCE_SQL_STREAM_001"
            WINDOW TEN_SECOND_SLIDING_WINDOW AS (RANGE INTERVAL '10' SECOND PRECEDING)
        )
        WHERE order_count >= 10;

CREATE OR REPLACE STREAM TRIGGER_COUNT_STREAM(
    order_count INTEGER,
    trigger_count INTEGER);
    
CREATE OR REPLACE PUMP trigger_count_pump AS INSERT INTO TRIGGER_COUNT_STREAM
SELECT STREAM order_count, trigger_count
FROM (
    SELECT STREAM order_count, COUNT(*) OVER W1 as trigger_count
    FROM "ALARM_STREAM"
    WINDOW W1 AS (RANGE INTERVAL '1' MINUTE PRECEDING)
)
WHERE trigger_count >= 1;