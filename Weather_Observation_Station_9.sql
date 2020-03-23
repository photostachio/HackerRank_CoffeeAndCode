# -*- coding: utf-8 -*-
"""
Weather Observation Station 9
"""

SELECT DISTINCT(CITY)
FROM STATION 
WHERE LEFT(CITY,1) 
NOT IN ('A','E','I','O','U');