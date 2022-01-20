CREATE PROCEDURE create_media(type varchar, media_name varchar)
    LANGUAGE SQL
AS
$$
INSERT INTO media(name, media_type)
VALUES (media_name, type)
$$;
