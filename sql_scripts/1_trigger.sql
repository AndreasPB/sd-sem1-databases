CREATE TRIGGER media_update_after
    AFTER UPDATE
    ON media
    FOR EACH ROW
EXECUTE FUNCTION create_media_func()

