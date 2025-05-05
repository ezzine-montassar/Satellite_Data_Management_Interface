# create_db.py
import sqlite3

# Connexion (ou création) à la base de données
conn = sqlite3.connect('DB_Project.db')
cursor = conn.cursor()

# Création de la table Agences_Spatiales
cursor.execute('''
CREATE TABLE Agences_Spatiales (
    agence_id INT PRIMARY KEY,
    nom VARCHAR(100),
    pays VARCHAR(100)
);
''')

# Création de la table Satellites
cursor.execute('''
CREATE TABLE Satellites (
    satellite_id INT PRIMARY KEY,
    parent_id INT NULL,
    agence_id INT NOT NULL,
    type_orbite VARCHAR(50)CHECK (type_orbite IN ('LEO', 'MEO', 'GEO')),
    statut VARCHAR(50) CHECK (statut IN ('Opérationnel', 'Inactif', 'Défaillant')),
    FOREIGN KEY (parent_id) REFERENCES Satellites(satellite_id),
    FOREIGN KEY (agence_id) REFERENCES Agences_Spatiales(agence_id)
);
''')

# Création de la table Instrument_Embarqués
cursor.execute('''
CREATE TABLE Instrument_Embarqués (
    instrument_id INT PRIMARY KEY,
    satellite_id INT NOT NULL,
    type VARCHAR(50),
    resolution VARCHAR(50),
    statut VARCHAR(20),
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id)
);
''')

# Création de la table Anomalie
cursor.execute('''
CREATE TABLE Anomalie (
    anomalie_id INT PRIMARY KEY,
    satellite_id INT NOT NULL,
    instrument_id INT,
    type VARCHAR(50),
    description VARCHAR2(1000),
    date_détection DATE,
    statut VARCHAR(20),
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id),
    FOREIGN KEY (instrument_id) REFERENCES Instrument_Embarqués(instrument_id)
);
''')


# Création de la table Missions
cursor.execute('''
CREATE TABLE Missions (
    mission_id INT PRIMARY KEY,
    satellite_id INT,
    type_donnée VARCHAR(100),
    date_début DATE,
    date_fin DATE,
    priorité INT,
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id)
);
''')


# Création de la table Données_Satellites
cursor.execute('''
CREATE TABLE Données_Satellites (
    donnée_id INT PRIMARY KEY,
    mission_id INT,
    nom_fichier VARCHAR(255),
    chemin_stockage VARCHAR(500),
    date_ajout DATE,
    FOREIGN KEY (mission_id) REFERENCES Missions(mission_id)
);
''')

# Création de la table Zones
cursor.execute('''
CREATE TABLE Zones (
    zone_id INT PRIMARY KEY,
    nom VARCHAR(100),
    pays VARCHAR(100),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6)
);
''')


# Création de la table Observation
cursor.execute('''
CREATE TABLE Observation (
    satellite_id INT,
    zone_id INT,
    PRIMARY KEY (satellite_id, zone_id),
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id),
    FOREIGN KEY (zone_id) REFERENCES Zones(zone_id)
);
''')


# Création de la table Stations_terrestres
cursor.execute('''
CREATE TABLE Stations_terrestres (
    station_id INT PRIMARY KEY,
    nom VARCHAR(100),
    pays VARCHAR(100)
);
''')


# Création de la table Communication
cursor.execute('''
CREATE TABLE Communication (
    satellite_id INT,
    station_id INT,
    PRIMARY KEY (satellite_id, station_id),
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id),
    FOREIGN KEY (station_id) REFERENCES Stations_terrestres(station_id)
);
''')


# Création de la table Sat_Telecom_Navigation
cursor.execute('''
CREATE TABLE Sat_Telecom_Navigation (
    satellite_id INT PRIMARY KEY,
    bande_frequence VARCHAR(50),
    capacite_transmission VARCHAR(50),
    precision_localisation VARCHAR(50),
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id)
);
''')


# Création de la table Observation_De_Donnees
cursor.execute('''
CREATE TABLE Observation_De_Donnees (
    satellite_id INT PRIMARY KEY,
    resolution_spectrale VARCHAR(50),
    frequence_passage VARCHAR(50),
    type_image VARCHAR(50),
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id)
);
''')


# Création de la table Sat_Recherche
cursor.execute('''
CREATE TABLE Sat_Recherche (
    satellite_id INT PRIMARY KEY,
    domaine_recherche VARCHAR(100),
    type_instrumentation VARCHAR(100),
    precision_mesure VARCHAR(50),
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id)
);
''')

# Création de la table Sat_Militaire
cursor.execute('''
CREATE TABLE Sat_Militaire (
    satellite_id INT PRIMARY KEY,
    niveau_securite VARCHAR(50),
    cryptage VARCHAR(50),
    type_mission_militaire VARCHAR(100),
    FOREIGN KEY (satellite_id) REFERENCES Satellites(satellite_id)
);
''')




# Commit et fermeture
conn.commit()
conn.close()
