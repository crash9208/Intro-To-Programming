Tournament Results

Project Specification

Develop a database schema to store details of a games matches between players.
Then write a Python module to rank the players and pair them up in matches in a tournament.

Files

tournament.py

Contains the implementation for the Swiss tournament

tournament.sql

Contains the SQL queries to create the database, tables and views

tournament_test.py

Contains the test cases for tournament.py


Instructions

1.Start Vagrant
  Open Terminal or cmd and browse to the vagrant folder
  Type vagrant up
  SSH in to the vagrant VM

  2.Change to the correct folder
    Type cd /vagrant/tournament
    Open PSQL and run the tournament.sql
    type psql
    copy the contents of tournament.sql and paste in to the terminal window
    type \q to quit out of PSQL

    3.Run the tests
      In the terminal type python tournament_test.py


Expected Outcome

1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
