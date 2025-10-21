--- 3 - estou calculando a frequencia de alugueis disponiveis em relaçao aos dias
--- tambem estou buscando entender o preço médio dos alugueis em relaçao ao tempo, para ver se sofre de relaçao sazonal ou se há curva de tendencia 
select 
    date, 
    count(available) as frequencia,
    avg(cast(replace(replace(price, '$',''), ',', '') as real)) as price
from calendar
where available = 't'
GROUP by date