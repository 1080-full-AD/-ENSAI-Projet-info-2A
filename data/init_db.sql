DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;

--------------------------------------------------------------
-- Utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.utilisateur CASCADE ;
CREATE TABLE projet.utilisateur (
    id_utilisateur serial PRIMARY KEY,
    mot_de_passe text NOT NULL,
    pseudo text NOT NULL
    age integer
);


--------------------------------------------------------------
-- Avis
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.avis;

CREATE TABLE projet.avis (
    id_avis SERIAL PRIMARY KEY,
    id_utilisateur integer REFERENCES projet.utilisateur(id_utilisateur),
    texte text,
    note integer
);


--------------------------------------------------------------
-- Mangas
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.manga  CASCADE ;

CREATE TABLE projet.manga (
    id_manga serial PRIMARY KEY,
    titre_manga text NOT NULL,
    synopsis text,
    status text,
    nb_volumes integer,
    nb_chapitres integer,
    auteurs text
);


-- Comme on va creer des pokemon en forcant les id_pokemon
-- il faut maj a la main la valeur de la sequence de la PK
ALTER SEQUENCE projet.manga_id_manga_seq RESTART WITH 899;


--------------------------------------------------------------
-- Collection
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.collection CASCADE;

CREATE TABLE projet.collection (
    titre_collec text UNIQUE NOT NULL,
    id_utilisateur integer REFERENCES projet.utilisateur(id_utilisateur),
    type_collec text NOT NULL,
    PRIMARY KEY (type_collec, id_utilisateur,titre_collec)
);

--------------------------------------------------------------
-- Collection Physique
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.collection_physique CASCADE;

CREATE TABLE projet.collection_physique (
    id_utilisateur integer REFERENCES projet.utilisateur(id_utilisateur),
    titre_collec text REFERENCES projet.collection(titre_collec),
    num_dernier integer,
    num_manquants integer,
    status text,
    PRIMARY KEY (id_utilisateur,titre_collec)
);

--------------------------------------------------------------
-- Collection Virtuelle
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.collection_virtuelle CASCADE;

CREATE TABLE projet.collection_virtuelle (
    id_utilisateur integer REFERENCES projet.utilisateur(id_utilisateur),
    titre_collec text REFERENCES projet.collection(titre_collec),
    description text,
    PRIMARY KEY (id_utilisateur,titre_collec)
);


--------------------------------------------------------------
-- Liaison entre les collections et les mangas
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.collection_manga CASCADE;

CREATE TABLE projet.collection_manga (
    id_manga integer REFERENCES projet.manga(id_manga),
    id_utilisateur integer REFERENCES projet.utilisateur(id_utilisateur),
    titre_collec text REFERENCES projet.collection(titre_collec),
    PRIMARY KEY (id_manga, id_utilisateur,titre_collec)
);