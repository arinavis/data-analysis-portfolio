-- Task nr. 1
/*/ Write a query that will return all customers (Customer) from the country Canada. /*/

SELECT FirstName, LastName, Country
FROM Customer
WHERE Country = 'Canada';

-- Task nr. 2
/*/ Find all tracks (Track) of the Rock genre. /*/

SELECT *
FROM Genre;

SELECT Name, GenreId
FROM Genre
WHERE Name = 'Rock';

-- Task nr. 3
/*/ Calculate the total sales amount (Total) for each country. /*/

SELECT *
FROM Invoice;

SELECT BillingCountry
FROM Invoice
GROUP BY BillingCountry;

SELECT BillingCountry, SUM(Total) AS TotalSales
FROM Invoice 
GROUP BY BillingCountry
ORDER By TotalSales DESC;

-- Task nr. 4
/*/ Display a list of albums (Album) and their corresponding artists (Artist). /*/

SELECT * 
FROM Album;

SELECT * 
FROM Artist;

SELECT al.Title AS AlbumTitle, ar.Name AS ArtistName
FROM Album al
JOIN Artist ar ON al.ArtistId = ar.ArtistId;

-- Task nr. 5
/*/ Find tracks that are not included in any playlist (Playlist). /*/

SELECT * 
FROM Track;

SELECT * 
FROM PlaylistTrack;

SELECT TrackId
FROM PlaylistTrack
WHERE PlaylistId IS NULL;


SELECT t.Name AS TrackName
FROM Track t
LEFT JOIN PlaylistTrack pt ON t.TrackId = pt.TrackId
WHERE pt.PlaylistId IS NULL;