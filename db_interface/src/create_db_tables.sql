CREATE TABLE "NewsContent" (
	"id" serial,
	"search_query_id" integer,
	"title" VARCHAR(255),
	"content_txt" TEXT NOT NULL,
	"path_img" TEXT NOT NULL,
	"link_news" TEXT NOT NULL,
	CONSTRAINT "NewsContent_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "language" (
	"id" serial NOT NULL,
	"primar" VARCHAR(255),
	"secondary" VARCHAR(255),
	"tertiary" VARCHAR(255),
	"quaternary" VARCHAR(255),
	CONSTRAINT "language_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "SentimentBasics" (
	"id" serial NOT NULL,
	"news_content_id" integer NOT NULL,
	"language_id" integer NOT NULL,
	"text" integer NOT NULL,
	"number_chars" integer NOT NULL,
	"sent_nrc" integer NOT NULL,
	"sent_vader" integer NOT NULL,
	"tag" TEXT NOT NULL,
	CONSTRAINT "SentimentBasics_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "persona" (
	"id" serial NOT NULL,
	"first_name" VARCHAR(255),
	"middle_name" VARCHAR(255),
	"last_name" VARCHAR(255),
	"language_id" integer,
	"geographic_zone_id" integer,
	"category_id" integer,
	"source_id" integer,
	CONSTRAINT "persona_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "category" (
	"id" serial NOT NULL,
	"category" VARCHAR(255) UNIQUE,
	CONSTRAINT "category_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "geographic_zone" (
	"id" integer NOT NULL,
	"continent" VARCHAR(255),
	"country" VARCHAR(255),
	"state" VARCHAR(255),
	CONSTRAINT "geographic_zone_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "source" (
	"id" serial NOT NULL,
	"search_engine" VARCHAR(255),
	"search_query_id" VARCHAR(255),
	CONSTRAINT "source_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "NewsContent" ADD CONSTRAINT "NewsContent_fk0" FOREIGN KEY ("search_query_id") REFERENCES ""("");


ALTER TABLE "SentimentBasics" ADD CONSTRAINT "SentimentBasics_fk0" FOREIGN KEY ("news_content_id") REFERENCES "NewsContent"("id");
ALTER TABLE "SentimentBasics" ADD CONSTRAINT "SentimentBasics_fk1" FOREIGN KEY ("language_id") REFERENCES "language"("id");

ALTER TABLE "persona" ADD CONSTRAINT "persona_fk0" FOREIGN KEY ("language_id") REFERENCES "language"("id");
ALTER TABLE "persona" ADD CONSTRAINT "persona_fk1" FOREIGN KEY ("geographic_zone_id") REFERENCES "geographic_zone"("id");
ALTER TABLE "persona" ADD CONSTRAINT "persona_fk2" FOREIGN KEY ("category_id") REFERENCES "category"("id");
ALTER TABLE "persona" ADD CONSTRAINT "persona_fk3" FOREIGN KEY ("source_id") REFERENCES "source"("id");



ALTER TABLE "source" ADD CONSTRAINT "source_fk0" FOREIGN KEY ("search_query_id") REFERENCES "NewsContent"("search_query_id");
