WITH tb_allColumns AS (
    SELECT 
        id,
        tempoHost,
        is_location_exact, 
        property_type, 
        room_type,
        bed_type, 
        accommodates,
        bathrooms,
        bedrooms,
        beds, 
        weekly_price,
        monthly_price,
        security_deposit,
        cleaning_fee,
        guests_included,
        extra_people,
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
        binTempo, 
        FAIXA_RATING,
        price
    FROM HostLifeCycle
),


tb_dummies AS (
    SELECT 
        id,
        CASE
            WHEN is_location_exact = 't' THEN 1
            WHEN is_location_exact = 'f' THEN 0
        END AS is_location_exact,

        CASE
            WHEN property_type = 'Apartment' THEN 0
            WHEN property_type = 'House' THEN 1
            WHEN property_type = 'Condominium' THEN 2
            WHEN property_type = 'Cabin' THEN 3
            WHEN property_type = 'Bungalow' THEN 4
            WHEN property_type = 'Camper/RV' THEN 5
            WHEN property_type = 'Townhouse' THEN 6
            WHEN property_type = 'Loft' THEN 7
            WHEN property_type = 'Boat' THEN 8 
            WHEN property_type = 'Bed & Breakfast' THEN 9
            WHEN property_type = 'Other' THEN 10
            WHEN property_type = 'Dorm' THEN 11
            WHEN property_type = 'Yurt' THEN 12
        END AS property_type,

        CASE 
            WHEN room_type = 'Entire home/apt' THEN 0
            WHEN room_type = 'Private room' THEN 1
            WHEN room_type = 'Shared room' THEN 2
        END AS room_type,

        CASE
            WHEN bed_type = 'Real Bed' THEN 0
            WHEN bed_type = 'Futon' THEN 1
            WHEN bed_type = 'Pull-out Sofa' THEN 2
            WHEN bed_type = 'Airbed' THEN 3
            WHEN bed_type = 'Couch' THEN 4
        END AS bed_type,

        CASE
            WHEN has_availability = 't' THEN 1
            ELSE 0
        END AS has_availability,

        CASE
            WHEN binTempo = 'host_antigo' THEN 0
            WHEN binTempo = 'host_medio' THEN 1
            WHEN binTempo = 'host_novo' THEN 2
        END AS binTempo,

        CASE 
            WHEN FAIXA_RATING = 'RATING_OTIMO' THEN 0
            WHEN FAIXA_RATING = 'RATING_OK' THEN 1
            WHEN FAIXA_RATING = 'RATING_BOM' THEN 2
        END AS FAIXA_RATING
    FROM tb_allColumns
),

tb_numFeatures AS (
    SELECT 
        id,
        tempoHost,
        accommodates,
        bathrooms,
        bedrooms,
        beds,
        ROUND((accommodates / NULLIF(bedrooms,0)),2) AS accommodates_per_bedroom,
        ROUND((beds / NULLIF(bedrooms,0)),2) AS beds_per_bedroom,
        ROUND((bathrooms / NULLIF(bedrooms,0)),2) AS bathrooms_per_bedroom,
        ROUND((accommodates / NULLIF(beds,0)),2) AS accommodates_per_bed,
        ROUND((beds / NULLIF(accommodates,0)),2) AS beds_per_accommodate,
        weekly_price, 
        monthly_price, 
        security_deposit,
        cleaning_fee, 
        guests_included,
        extra_people, 
        minimum_nights,
        maximum_nights, 
        number_of_reviews,
        review_scores_rating,
        reviews_per_month,
        availability_30,
        availability_60,
        availability_90,
        availability_365,
        ROUND((availability_30 + availability_60 + availability_90 + availability_365)/4, 2) AS mean_availability,
        ROUND((number_of_reviews / NULLIF(tempoHost,0)),2) AS review_per_year,

        price
    FROM tb_allColumns
)

SELECT 
    t1.id,
    t1.is_location_exact,
    t1.property_type,
    t1.room_type,
    t1.bed_type,
    t1.has_availability,
    t1.binTempo,
    t1.FAIXA_RATING,
    t2.tempoHost,
    t2.accommodates,
    t2.bathrooms,
    t2.bedrooms,
    t2.beds,
    t2.accommodates_per_bedroom,
    t2.beds_per_bedroom,
    t2.bathrooms_per_bedroom,
    t2.accommodates_per_bed,
    t2.beds_per_accommodate,
    t2.weekly_price,
    t2.monthly_price,
    t2.security_deposit,
    t2.cleaning_fee,
    t2.guests_included,
    t2.extra_people,
    t2.minimum_nights,
    t2.maximum_nights,
    t2.number_of_reviews,
    t2.review_scores_rating,
    t2.reviews_per_month,
    t2.availability_30,
    t2.availability_60,
    t2.availability_90,
    t2.availability_365,
    t2.mean_availability,
    t2.review_per_year,
    t2.price
FROM tb_dummies AS t1
LEFT JOIN tb_numFeatures AS t2
ON t1.id = t2.id;
