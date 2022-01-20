CREATE VIEW user_media_view AS
SELECT u.username as user_username,
       c.name     as country_name,
       m.name     as media_name
FROM public.user u
         JOIN country c on u.country_id = c.id
         JOIN user_media um on u.id = um.user_id
         JOIN media m on m.id = um.media_id
