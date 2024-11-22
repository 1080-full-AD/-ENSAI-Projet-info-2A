DROP SCHEMA IF EXISTS test CASCADE;
CREATE SCHEMA test;

--------------------------------------------------------------
-- Utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS test.utilisateur CASCADE ;
CREATE TABLE test.utilisateur (
    id_utilisateur serial PRIMARY KEY,
    mot_de_passe text NOT NULL,
    pseudo text NOT NULL,
    age integer,
    is_admin boolean
);

ALTER SEQUENCE test.utilisateur_id_utilisateur_seq RESTART WITH 3;

--------------------------------------------------------------
-- Mangas
--------------------------------------------------------------

DROP TABLE IF EXISTS test.manga  CASCADE ;

CREATE TABLE test.manga (
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

DROP TABLE IF EXISTS test.avis;

CREATE TABLE test.avis (
    id_utilisateur INTEGER,
    id_manga INTEGER,
    texte text,
    note integer,
    PRIMARY KEY (id_manga, id_utilisateur),
    FOREIGN KEY (id_manga)  REFERENCES test.manga(id_manga),
    FOREIGN KEY (id_utilisateur)  REFERENCES test.utilisateur(id_utilisateur) ON DELETE CASCADE
);

--------------------------------------------------------------
-- Collection
--------------------------------------------------------------

DROP TABLE IF EXISTS test.collection CASCADE;

CREATE TABLE test.collection (
    titre_collec text UNIQUE NOT NULL,
    id_utilisateur integer REFERENCES test.utilisateur(id_utilisateur),
    description text,
    PRIMARY KEY (id_utilisateur,titre_collec)
);

--------------------------------------------------------------
-- Mangathèque
--------------------------------------------------------------

DROP TABLE IF EXISTS test.mangatheque CASCADE;

CREATE TABLE test.mangatheque (
    id_utilisateur integer REFERENCES test.utilisateur(id_utilisateur),
    id_manga integer REFERENCES test.manga(id_manga),
    num_dernier integer,
    num_manquants JSON,
    status text,
    PRIMARY KEY (id_utilisateur,id_manga)
);

--------------------------------------------------------------
-- Liaison entre les collections et les mangas
--------------------------------------------------------------

DROP TABLE IF EXISTS test.collection_manga CASCADE;

CREATE TABLE test.collection_manga (
    id_manga integer REFERENCES test.manga(id_manga),
    id_utilisateur integer REFERENCES test.utilisateur(id_utilisateur),
    titre_collec text REFERENCES test.collection(titre_collec),
    PRIMARY KEY (id_manga, id_utilisateur,titre_collec)
);