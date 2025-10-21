--- 4 - irei investigar cliente antigos têm melhor desempenho e se merecem incentivos

with tb_tempoHost as (select 
    id,
    host_since, 
    (last_scraped - host_since) as tempoHost,
    review_scores_rating,
    cast(REPLACE(price, '$', '') as real) as price$, 
    (last_review - first_review) as diferencaUltimoReview
from listings
where host_since is not null -- para nao retornar valores de tempo nulos
)

SELECT 
*, 
CASE
    when tempoHost = 1 THEN 'host_novo'
    WHEN tempoHost > 1 AND tempoHost <= 3 THEN 'host_medio'
    else 'host_antigo'
end as binTempo
from tb_tempoHost;
