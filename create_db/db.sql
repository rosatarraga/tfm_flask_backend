-- public.logs definition

-- Drop table

-- DROP TABLE public.logs;

CREATE TABLE public.logs (
	id serial4 NOT NULL,
	email varchar NOT NULL,
	"date" date NOT NULL
);