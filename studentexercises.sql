CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName   TEXT NOT NULL,
    LastName	TEXT NOT NULL,
    SlackHandle TEXT NOT NULL UNIQUE,
    CohortId	INTEGER,
    FOREIGN KEY (CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Instructor (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName   TEXT NOT NULL,
    LastName	TEXT NOT NULL,
    SlackHandle	TEXT NOT NULL UNIQUE,
    CohortId	INTEGER,
    Specialty	TEXT,
    FOREIGN KEY (CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE,
    ExLanguage	TEXT NOT NULL
);

CREATE TABLE StudentExercises (
	Id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StudentId	INTEGER,
	ExerciseId	INTEGER,
	FOREIGN KEY (StudentId) REFERENCES Student(Id),
	FOREIGN KEY (ExerciseId) REFERENCES Exercise(Id)
);

-- use the insert into sql statement to create...
-- 3 cohorts
INSERT INTO Cohort (Name)
VALUES ('Day Cohort 39');

INSERT INTO Cohort (Id, Name) 
VALUES (NULL, 'Day Cohort 40');

INSERT INTO Cohort
VALUES (NULL, 'Day Cohort 38');

SELECT * FROM Cohort;
-- 5 exercises
INSERT INTO Exercise (Name, ExLanguage)
VALUES ('Kandy Korner', 'JavaScript');

INSERT INTO Exercise (Name, ExLanguage)
VALUES ('Daily Journal', 'JavaScript');

INSERT INTO Exercise (Name, ExLanguage)
VALUES ('Student Exercises', 'Python');

INSERT INTO Exercise (Name, ExLanguage)
VALUES ('Fizz Buzz', 'JavaScript');

INSERT INTO Exercise (Name, ExLanguage)
VALUES ('Flexbox', 'CSS');

SELECT * FROM Exercise;
-- 3 instructors
INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty)
VALUES ('Andy', 'Collins', 'Andy Collins', 3, '');

INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty)
VALUES ('Steve', 'Brownlee', 'Steve Brownlee', 1, 'Theatrical Powerpoints');

INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty)
VALUES ('Bryan', 'Nilsen', 'Bryan Nilsen', 2, 'High Fives');

SELECT * FROM Instructor;
-- 7 students
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES ('Katie', 'Wohl', 'Katie Wohl', 3);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES ('Cooper', 'Nichols', 'Cooper Nichols', 3);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES ('Roxanne', 'Nasraty', 'Roxanne Nasraty', 2);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES ('Sophia', 'Law', 'Sophia Law', 2);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES ('Crystal', 'Elsey', 'Crystal Elsey', 1);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES ('Derek', 'Buckley', 'Derek Buckley', 1);

INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
VALUES ('Alyssa', 'Nycum', 'Alyssa Nycum', 3);

SELECT * FROM Student;
-- assign 2 exercises to each student
INSERT INTO StudentExercises (StudentId, ExerciseId)
VALUES (1, 1);

INSERT INTO StudentExercises (StudentId, ExerciseId)
VALUES (3, 2);