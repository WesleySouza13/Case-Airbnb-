-- 5 - Quais fatores mais influenciam uma boa avaliação?
-- irei selecionar algumas variaveis para fazer um estudo de correlaçao (nao causa) 
select 
    room_type, 
    beds,
    bed_type,
    bathrooms,
    bedrooms,
    accommodates,
    review_scores_rating, 
    cleaning_fee as taxa_de_limpeza,
    host_is_superhost
from listings