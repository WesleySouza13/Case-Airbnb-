select 
    date, 
    count(available) as frequencia,
    avg(cast(replace(replace(price, '$',''), ',', '') as real)) as price
from calendar
where available = 't'
GROUP by date