CREATE VIEW user_media_view AS
    SELECT u.id as user_id,
           u.username as user_username,
           m.id as media_id,
           m.name as media_name
    FROM public.user u
        JOIN user_media um on u.id = um.user_id
        JOIN media m on m.id = um.media_id
