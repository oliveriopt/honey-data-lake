CREATE TABLE "Persona" (
	"id" serial NOT NULL,
	"name" VARCHAR(255) NOT NULL,
	"language_id" integer NOT NULL,
	"geographic_zone_id" integer NOT NULL,
	"category_id" integer NOT NULL,
	"source_id" integer NOT NULL UNIQUE,
	CONSTRAINT "Persona_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "LanguageIdentification" (
	"id" serial NOT NULL,
	"primary" VARCHAR(255) NOT NULL,
	"secondary" VARCHAR(255) NOT NULL,
	"tertiary" VARCHAR(255) NOT NULL,
	"quaternary" VARCHAR(255) NOT NULL,
	CONSTRAINT "LanguageIdentification_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "WorkBirthZone" (
	"id" serial NOT NULL,
	"work_id" integer NOT NULL UNIQUE,
	"birth_id" integer NOT NULL UNIQUE,
	CONSTRAINT "WorkBirthZone_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "Category" (
	"id" serial NOT NULL,
	"category" VARCHAR(255) NOT NULL UNIQUE,
	CONSTRAINT "Category_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "DescriptionZone" (
	"id" integer NOT NULL,
	"continent" VARCHAR(255) NOT NULL,
	"country" VARCHAR(255) NOT NULL,
	"state" VARCHAR(255) NOT NULL,
	CONSTRAINT "DescriptionZone_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "Source" (
	"id" serial NOT NULL,
	"search_engine" VARCHAR(255) NOT NULL,
	"link" VARCHAR(255) NOT NULL,
	CONSTRAINT "Source_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "Persona" ADD CONSTRAINT "Persona_fk0" FOREIGN KEY ("language_id") REFERENCES "LanguageIdentification"("id");
ALTER TABLE "Persona" ADD CONSTRAINT "Persona_fk1" FOREIGN KEY ("geographic_zone_id") REFERENCES "WorkBirthZone"("id");
ALTER TABLE "Persona" ADD CONSTRAINT "Persona_fk2" FOREIGN KEY ("category_id") REFERENCES "Category"("id");
ALTER TABLE "Persona" ADD CONSTRAINT "Persona_fk3" FOREIGN KEY ("source_id") REFERENCES "Source"("id");

ALTER TABLE "WorkBirthZone" ADD CONSTRAINT "WorkBirthZone_fk0" FOREIGN KEY ("work_id") REFERENCES "DescriptionZone"("id");
ALTER TABLE "WorkBirthZone" ADD CONSTRAINT "WorkBirthZone_fk1" FOREIGN KEY ("birth_id") REFERENCES "DescriptionZone"("id");



