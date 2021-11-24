# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person Left Join Address
ON Person.personId = Address.personId
