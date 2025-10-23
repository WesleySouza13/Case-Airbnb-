WITH tb_hostLife as (
SELECT
    id, 
    host_id,
    (last_review - first_review) as tempoHost,
    city, 
    state, 
    country,
    is_location_exact,
    property_type, 
    room_type,
    bed_type,
    accommodates, 
    bathrooms,
    bedrooms,
    beds, 
    CAST(REPLACE(weekly_price,"$", "") as real)  as weekly_price,
    CAST(REPLACE(monthly_price,"$", "") as real) as monthly_price,
    CAST(REPLACE(security_deposit,"$", "") as real) as security_deposit,
    cast(REPLACE(cleaning_fee, "$", "") as real) as cleaning_fee,
    guests_included,
    CAST(REPLACE(extra_people,"$", "") as real) as extra_people,
    minimum_nights,
    maximum_nights,
    has_availability,
    number_of_reviews,
    review_scores_rating,
    reviews_per_month,
    availability_30,
    availability_60,
    availability_90,
    availability_365,
    CAST(REPLACE(price, "$", "") as real) as price
from listings

),

tb_faixas as (
SELECT *,
CASE
    when tempoHost = 1 THEN 'host_novo'
    WHEN tempoHost > 1 AND tempoHost <= 3 THEN 'host_medio'
    else 'host_antigo'
end as binTempo,
CASE
WHEN review_scores_rating <=80 THEN 'RATING_OK'
WHEN review_scores_rating > 81 AND review_scores_rating < 90 THEN 'RATING_BOM'
    ELSE 'RATING_OTIMO'
END AS FAIXA_RATING

FROM tb_hostLife
)

SELECT
* 
FROM tb_faixas
