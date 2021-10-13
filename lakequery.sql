SELECT description
       , count(*) 
  FROM orderslake 
 WHERE country='France' AND 
       year='2019' AND 
       month='02' 
 GROUP BY description