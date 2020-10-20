 CREATE TABLE "newscontent" (
	"id" serial,
	"persona_id" integer NOT NULL,
	"title" VARCHAR(255),
	"media" VARCHAR(255),
	"date" VARCHAR(255),
	"desc" TEXT,
	"link" TEXT,
	"content_txt" TEXT,
	"source_search" VARCHAR(255),
	CONSTRAINT "newscontent_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "language"
(
    "id"         serial NOT NULL,
    "primar"     VARCHAR(255),
    "secondary"  VARCHAR(255),
    "tertiary"   VARCHAR(255),
    "quaternary" VARCHAR(255),
    CONSTRAINT "language_pk" PRIMARY KEY ("id")
) WITH (
      OIDS= FALSE
    );

CREATE TABLE "persona"
(
    "id"                 serial NOT NULL,
    "first_name"         VARCHAR(255),
    "middle_name"        VARCHAR(255),
    "last_name"          VARCHAR(255),
    "language_id"        integer,
    "geographic_zone_id" integer,
    "category_id"        integer,
    CONSTRAINT "persona_pk" PRIMARY KEY ("id")
) WITH (
      OIDS= FALSE
    );

CREATE TABLE "category"
(
    "id"       serial NOT NULL,
    "category" VARCHAR(255) UNIQUE,
    CONSTRAINT "category_pk" PRIMARY KEY ("id")
) WITH (
      OIDS= FALSE
    );

CREATE TABLE "geographic_zone"
(
    "id"        integer NOT NULL,
    "state" VARCHAR(255),
    "country"   VARCHAR(255),
    "continent"     VARCHAR(255),
    CONSTRAINT "geographic_zone_pk" PRIMARY KEY ("id")
) WITH (
      OIDS= FALSE
    );

ALTER TABLE "persona"
    ADD CONSTRAINT "persona_fk0" FOREIGN KEY ("id") REFERENCES "newscontent" ("persona_id");
ALTER TABLE "persona"
    ADD CONSTRAINT "persona_fk1" FOREIGN KEY ("language_id") REFERENCES "language" ("id");
ALTER TABLE "persona"
    ADD CONSTRAINT "persona_fk2" FOREIGN KEY ("geographic_zone_id") REFERENCES "geographic_zone" ("id");
ALTER TABLE "persona"
    ADD CONSTRAINT "persona_fk3" FOREIGN KEY ("category_id") REFERENCES "category" ("id");


