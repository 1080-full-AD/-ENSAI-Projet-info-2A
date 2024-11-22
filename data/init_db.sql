DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;

--------------------------------------------------------------
-- Utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.utilisateur CASCADE ;
CREATE TABLE projet.utilisateur (
    id_utilisateur serial PRIMARY KEY,
    mot_de_passe text NOT NULL,
    pseudo text NOT NULL,
    age integer,
    is_admin boolean
);

ALTER SEQUENCE projet.utilisateur_id_utilisateur_seq RESTART WITH 3;

--------------------------------------------------------------
-- Mangas
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.manga  CASCADE ;

CREATE TABLE projet.manga (
    id_manga serial PRIMARY KEY,
    titre_manga text NOT NULL,
    synopsis text,
    auteurs text,
    nb_volumes integer,
    nb_chapitres integer
);


--------------------------------------------------------------
-- Avis
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.avis;

CREATE TABLE projet.avis (
    id_utilisateur INTEGER,
    id_manga INTEGER,
    texte text,
    note integer,
    PRIMARY KEY (id_manga, id_utilisateur),
    FOREIGN KEY (id_manga)  REFERENCES projet.manga(id_manga),
    FOREIGN KEY (id_utilisateur)  REFERENCES projet.utilisateur(id_utilisateur) ON DELETE CASCADE
);

--------------------------------------------------------------
-- Collection
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.collection CASCADE;

CREATE TABLE projet.collection (
    titre_collec text UNIQUE NOT NULL,
    id_utilisateur integer REFERENCES projet.utilisateur(id_utilisateur),
    description text,
    PRIMARY KEY (id_utilisateur,titre_collec)
);

--------------------------------------------------------------
-- Mangathèque
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.mangatheque CASCADE;

CREATE TABLE projet.mangatheque (
    id_utilisateur integer REFERENCES projet.utilisateur(id_utilisateur),
    id_manga integer REFERENCES projet.manga(id_manga),
    num_dernier integer,
    num_manquants JSON,
    status text,
    PRIMARY KEY (id_utilisateur,id_manga)
);

--------------------------------------------------------------
-- Liaison entre les collections et les mangas
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.collection_manga CASCADE;

CREATE TABLE projet.collection_manga (
    id_manga integer REFERENCES projet.manga(id_manga),
    id_utilisateur integer REFERENCES projet.utilisateur(id_utilisateur),
    titre_collec text REFERENCES projet.collection(titre_collec) ON UPDATE CASCADE,
    PRIMARY KEY (id_manga, id_utilisateur,titre_collec)
);
