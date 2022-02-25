# Queries used in the many-to-many demo

Fans table:
```sql
SELECT * FROM sports_fans_schema.fans;

INSERT INTO fans (first_name, last_name, email, birthdate) VALUES
("Adrian", "Barnard", "a@b.com", "1960-01-01"),
("Jane", "Doe", "j@d.com", "1980-05-05"),
("Kim", "Barnard", "k@b.com", "1975-08-15");
```

Teams table:
```sql
SELECT * FROM sports_fans_schema.teams;

INSERT INTO teams (city, nickname, mascot, sport) VALUES
("Seattle","Seahawks","Eagle","American football"),
("Milwaukee","Bucks","Buck","Basketball"),
("Manchester", "Reds", "Red", "International football");
```

Fans_and_teams table:
```sql
SELECT * FROM sports_fans_schema.fans_and_teams;

-- INSERT INTO fans_and_teams (fan_id, team_id) VALUES -- (3, 2), (3,3);
-- (1, 1), (1, 2), (3, 1);

-- Show Adrian and all his teams
SELECT * FROM fans 
LEFT JOIN fans_and_teams ON fans.id = fans_and_teams.fan_id
LEFT JOIN teams ON teams.id = fans_and_teams.team_id WHERE fans.id = 1;

-- Show all fans for the Seahawks
SELECT * FROM teams 
LEFT JOIN fans_and_teams ON teams.id = fans_and_teams.team_id
LEFT JOIN fans ON fans.id = fans_and_teams.fan_id;

-- Remove connection between Adrian and Seahawks
DELETE FROM fans_and_teams WHERE fan_id = 1 AND team_id = 1;

-- Count the number of fans for each team
SELECT teams.id, COUNT(fans.id), city, nickname FROM teams 
LEFT JOIN fans_and_teams ON teams.id = fans_and_teams.team_id
LEFT JOIN fans ON fans.id = fans_and_teams.fan_id GROUP BY teams.id;

-- Get all fans who are NOT fans of the Seahawks with a nested query
SELECT * FROM fans WHERE id NOT IN (SELECT fan_id FROM fans_and_teams WHERE team_id = 1);
```