--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2020-09-13 21:12:28

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE app_login;
--
-- TOC entry 2820 (class 1262 OID 16730)
-- Name: app_login; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE app_login WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';


ALTER DATABASE app_login OWNER TO postgres;

\connect app_login

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16739)
-- Name: user_registration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_registration (
    user_id character varying NOT NULL,
    password character varying NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    dob date NOT NULL,
    gender character varying
);


ALTER TABLE public.user_registration OWNER TO postgres;

--
-- TOC entry 2814 (class 0 OID 16739)
-- Dependencies: 202
-- Data for Name: user_registration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_registration (user_id, password, first_name, last_name, dob, gender) FROM stdin;
\.


--
-- TOC entry 2687 (class 2606 OID 16746)
-- Name: user_registration user_registration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_registration
    ADD CONSTRAINT user_registration_pkey PRIMARY KEY (user_id);


-- Completed on 2020-09-13 21:12:28

--
-- PostgreSQL database dump complete
--

