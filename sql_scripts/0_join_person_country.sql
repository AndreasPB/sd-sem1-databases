CREATE VIEW person_country_view AS
SELECT person.name  as person_name,
       person.job,
       country.name as country_name
FROM person
         JOIN country ON country.id = person.country_id