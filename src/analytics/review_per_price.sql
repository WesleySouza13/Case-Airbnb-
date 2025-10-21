-- 2 - vou investigar se o score de reviews impatam no preço do imovel 
select 
    review_scores_rating,
    avg(cast(replace(replace(price, '$',''), ',', '') as real)) as preco_medio
from listings
where review_scores_rating > 80.0 and price is not null
GROUP by review_scores_rating