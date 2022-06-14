/*
able: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write an SQL query to report all the duplicate emails.

Return the result table in any order.
*/

# Write your MySQL query statement below
DELETE p2 
FROM Person p1 INNER JOIN Person p2
ON p1.email = p2.email
WHERE p1.id < p2.id
