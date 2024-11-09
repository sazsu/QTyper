--
-- File generated with SQLiteStudio v3.4.4 on Sat Nov 9 17:31:06 2024
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Data
CREATE TABLE IF NOT EXISTS Data (
    wpm      INTEGER NOT NULL,
    accuracy REAL
);


-- Table: Languages
DROP TABLE IF EXISTS Languages;

CREATE TABLE IF NOT EXISTS Languages (
    id       INTEGER PRIMARY KEY AUTOINCREMENT
                     UNIQUE
                     NOT NULL,
    language TEXT    NOT NULL
                     UNIQUE
);

INSERT INTO Languages (
                          id,
                          language
                      )
                      VALUES (
                          1,
                          'english'
                      );

INSERT INTO Languages (
                          id,
                          language
                      )
                      VALUES (
                          2,
                          'russian'
                      );


-- Table: Modes
DROP TABLE IF EXISTS Modes;

CREATE TABLE IF NOT EXISTS Modes (
    id   INTEGER PRIMARY KEY AUTOINCREMENT
                 UNIQUE
                 NOT NULL,
    mode INTEGER UNIQUE
                 NOT NULL
);

INSERT INTO Modes (
                      id,
                      mode
                  )
                  VALUES (
                      1,
                      15
                  );

INSERT INTO Modes (
                      id,
                      mode
                  )
                  VALUES (
                      2,
                      30
                  );

INSERT INTO Modes (
                      id,
                      mode
                  )
                  VALUES (
                      3,
                      60
                  );

INSERT INTO Modes (
                      id,
                      mode
                  )
                  VALUES (
                      4,
                      120
                  );


-- Table: Settings
CREATE TABLE IF NOT EXISTS Settings (
    mode            INTEGER REFERENCES Modes (id) 
                            NOT NULL,
    language        INTEGER REFERENCES Languages (id) 
                            NOT NULL,
    interface_color INTEGER NOT NULL
);

INSERT INTO Settings (
                         mode,
                         language,
                         interface_color
                     )
                     SELECT 1, 1, 1
                     WHERE NOT EXISTS (SELECT 1 FROM Settings);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
