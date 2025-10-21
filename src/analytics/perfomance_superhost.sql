-- 1 - irei investigar se a performance do host é uma caracteristica para preços maiores
WITH tb_taxa_ocupacao as (
    select 
        listing_id as id,
        available, 
        sum(case when available = 'f' then 1 else 0 end) *1.0 /count(*) as taxa
    from calendar
),

tb_superhost as (
    select 
        id,
        avg(review_scores_rating) as taxa_media_review_scores_rating, 
        reviews_per_month,
        count(*) as total_listings,
        host_is_superhost
    from listings
    where  host_is_superhost is not null
    GROUP by host_is_superhost
    ORDER by taxa_media_review_scores_rating DESC

)

SELECT 
* 
from tb_taxa_ocupacao as t1
JOIN tb_superhost as t2 
on t1.id = t2.id

