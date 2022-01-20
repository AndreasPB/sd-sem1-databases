CREATE OR REPLACE FUNCTION create_media_func() RETURNS TRIGGER
    LANGUAGE plpgsql
AS
$$
BEGIN
    INSERT INTO media(name, media_type)
    VALUES ('Hestebøffer', 'Movie');
    RETURN NULL;
END;
$$
