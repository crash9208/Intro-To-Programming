-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop tournament database if it exists
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;


--colummns: player_id,player_name
CREATE TABLE player(
  player_id serial PRIMARY KEY,
  player_name text
);


--colummns: match_id,winner,loser
CREATE TABLE matches (
  match_id serial PRIMARY KEY,
  winner INTEGER,
  loser INTEGER,
  FOREIGN KEY(winner) REFERENCES player(player_id),
  FOREIGN KEY(loser) REFERENCES player(player_id)
);


--colummns: player_id,player_name,number_of_wins, number_of_matches
CREATE VIEW standings AS
SELECT player.player_id as player_id, player.player_name,
(SELECT count(*) FROM matches WHERE matches.winner = player.player_id) as number_of_wins,
(SELECT count(*) FROM matches WHERE player.player_id in (winner, loser)) as number_of_matches
FROM player
GROUP BY player.player_id
ORDER BY number_of_wins DESC;
