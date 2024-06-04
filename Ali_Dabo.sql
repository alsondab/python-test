#Table pour stocker les utilisateurs
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);


#Table pour stocker les alarmes
CREATE TABLE Alarms (
    alarm_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT REFERENCES Users(user_id),
    alarm_time TIME NOT NULL,
    alarm_description VARCHAR(255),
    is_enabled BOOLEAN NOT NULL
);

#example d'insertion d'un utilisateur 
INSERTE INTO User (user_id, username, password_hash)
VALUES (1, 'alson_dab', 'hashed_password');

#example d'insertion d'une alarm
INSERT INTO Alarm (alarm_id, alarm_time, alarm_description, is_enabled)
VALUES (1,'8:00','reuinion_importante', TRUE);

#Selection d'alarm activer pour un utilisateur specifique
SELECT * FROM Alarm WHERE user id =1 AND is_nabled=TRUE