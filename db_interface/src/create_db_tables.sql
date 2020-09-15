CREATE TABLE persona (
	id serial NOT NULL,
	name VARCHAR(255) NOT NULL,
	language_id integer NOT NULL,
	geographic_zone_id integer NOT NULL,
	category_id integer NOT NULL,
	source_id integer NOT NULL UNIQUE,
	CONSTRAINT persona_pk PRIMARY KEY (id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE language_identification (
	id serial NOT NULL,
	primar VARCHAR(255) NOT NULL,
	secondary VARCHAR(255) NOT NULL,
	tertiary VARCHAR(255) NOT NULL,
	quaternary VARCHAR(255) NOT NULL,
	CONSTRAINT language_identification_pk PRIMARY KEY (id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE work_birth_zone (
	id serial NOT NULL,
	work_id integer NOT NULL UNIQUE,
	birth_id integer NOT NULL UNIQUE,
	CONSTRAINT work_birth_zone_pk PRIMARY KEY (id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE category (
	id serial NOT NULL,
	category VARCHAR(255) NOT NULL UNIQUE,
	CONSTRAINT category_pk PRIMARY KEY (id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE description_zone (
	id integer NOT NULL,
	continent VARCHAR(255) NOT NULL,
	country VARCHAR(255) NOT NULL,
	state VARCHAR(255) NOT NULL,
	CONSTRAINT description_zone_pk PRIMARY KEY (id)
) WITH (
  OIDS=FALSE
);

CREATE TABLE source (
	id serial NOT NULL,
	search_engine VARCHAR(255) NOT NULL,
	link VARCHAR(255) NOT NULL,
	CONSTRAINT source_pk PRIMARY KEY (id)
) WITH (
  OIDS=FALSE
);

ALTER TABLE persona ADD CONSTRAINT persona_fk0 FOREIGN KEY (language_id) REFERENCES language_identification
    (id);
ALTER TABLE persona ADD CONSTRAINT persona_fk1 FOREIGN KEY (geographic_zone_id) REFERENCES work_birth_zone(id);
ALTER TABLE persona ADD CONSTRAINT persona_fk2 FOREIGN KEY (category_id) REFERENCES category(id);
ALTER TABLE persona ADD CONSTRAINT persona_fk3 FOREIGN KEY (source_id) REFERENCES source(id);

ALTER TABLE work_birth_zone ADD CONSTRAINT work_birth_zone_fk0 FOREIGN KEY (work_id) REFERENCES description_zone
    (id);
ALTER TABLE work_birth_zone ADD CONSTRAINT work_birth_zone_fk1 FOREIGN KEY (birth_id) REFERENCES
    description_zone(id);

