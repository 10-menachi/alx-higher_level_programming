-- This script  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
USE hbtn_0d_tvshows;
SELECT tv_shows.title, genres.name
FROM tv_shows
JOIN genres ON tv_shows.genre_id = genres.id
ORDER BY tv_shows.title ASC;