BEGIN isolation level serializable;
INSERT INTO media(name, media_type)
VALUES ('Hestebøffer 3', 'Movie');
COMMIT;

BEGIN;
INSERT INTO media(name, media_type)
VALUES ('Hestebøffer 4', 'Movie');
ROLLBACK;
