--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2020-09-17 00:42:17

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

DROP DATABASE app_db;
--
-- TOC entry 2847 (class 1262 OID 16756)
-- Name: app_db; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE app_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';


ALTER DATABASE app_db OWNER TO postgres;

\connect app_db

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

--
-- TOC entry 9 (class 2615 OID 16779)
-- Name: questionaire_data; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA questionaire_data;


ALTER SCHEMA questionaire_data OWNER TO postgres;

--
-- TOC entry 6 (class 2615 OID 16757)
-- Name: user_data; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA user_data;


ALTER SCHEMA user_data OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 16788)
-- Name: answers; Type: TABLE; Schema: questionaire_data; Owner: postgres
--

CREATE TABLE questionaire_data.answers (
    id integer NOT NULL,
    value character varying NOT NULL
);


ALTER TABLE questionaire_data.answers OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16780)
-- Name: questions; Type: TABLE; Schema: questionaire_data; Owner: postgres
--

CREATE TABLE questionaire_data.questions (
    id integer NOT NULL,
    question character varying NOT NULL,
    options integer[] NOT NULL
);


ALTER TABLE questionaire_data.questions OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16766)
-- Name: records; Type: TABLE; Schema: user_data; Owner: postgres
--

CREATE TABLE user_data.records (
    id integer NOT NULL,
    user_id character varying NOT NULL,
    file_name character varying NOT NULL,
    file bytea NOT NULL
);


ALTER TABLE user_data.records OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16758)
-- Name: user_details; Type: TABLE; Schema: user_data; Owner: postgres
--

CREATE TABLE user_data.user_details (
    user_id character varying NOT NULL,
    password character varying NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    dob date NOT NULL,
    gender character varying NOT NULL
);


ALTER TABLE user_data.user_details OWNER TO postgres;

--
-- TOC entry 2841 (class 0 OID 16788)
-- Dependencies: 207
-- Data for Name: answers; Type: TABLE DATA; Schema: questionaire_data; Owner: postgres
--

INSERT INTO questionaire_data.answers (id, value) VALUES (1, 'outdoors');
INSERT INTO questionaire_data.answers (id, value) VALUES (2, 'indoors');
INSERT INTO questionaire_data.answers (id, value) VALUES (3, 'mix of outdoor and indoor');
INSERT INTO questionaire_data.answers (id, value) VALUES (4, 'low');
INSERT INTO questionaire_data.answers (id, value) VALUES (5, 'medium');
INSERT INTO questionaire_data.answers (id, value) VALUES (6, 'high');
INSERT INTO questionaire_data.answers (id, value) VALUES (7, 'yes');
INSERT INTO questionaire_data.answers (id, value) VALUES (8, 'no');


--
-- TOC entry 2840 (class 0 OID 16780)
-- Dependencies: 206
-- Data for Name: questions; Type: TABLE DATA; Schema: questionaire_data; Owner: postgres
--

INSERT INTO questionaire_data.questions (id, question, options) VALUES (1, 'work environment?', '{1,2,3}');
INSERT INTO questionaire_data.questions (id, question, options) VALUES (2, 'Exposure to sun?', '{4,5,6}');
INSERT INTO questionaire_data.questions (id, question, options) VALUES (3, 'Exposure to heat?', '{4,5,6}');
INSERT INTO questionaire_data.questions (id, question, options) VALUES (4, 'Had cancer earlier?', '{7,8}');
INSERT INTO questionaire_data.questions (id, question, options) VALUES (5, 'Anyone in family has cancer?', '{7,8}');


--
-- TOC entry 2839 (class 0 OID 16766)
-- Dependencies: 205
-- Data for Name: records; Type: TABLE DATA; Schema: user_data; Owner: postgres
--



--
-- TOC entry 2838 (class 0 OID 16758)
-- Dependencies: 204
-- Data for Name: user_details; Type: TABLE DATA; Schema: user_data; Owner: postgres
--



--
-- TOC entry 2710 (class 2606 OID 16795)
-- Name: answers answers_pkey; Type: CONSTRAINT; Schema: questionaire_data; Owner: postgres
--

ALTER TABLE ONLY questionaire_data.answers
    ADD CONSTRAINT answers_pkey PRIMARY KEY (id);


--
-- TOC entry 2708 (class 2606 OID 16787)
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: questionaire_data; Owner: postgres
--

ALTER TABLE ONLY questionaire_data.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


--
-- TOC entry 2706 (class 2606 OID 16773)
-- Name: records records_pkey; Type: CONSTRAINT; Schema: user_data; Owner: postgres
--

ALTER TABLE ONLY user_data.records
    ADD CONSTRAINT records_pkey PRIMARY KEY (id);


--
-- TOC entry 2704 (class 2606 OID 16765)
-- Name: user_details user_details_pkey; Type: CONSTRAINT; Schema: user_data; Owner: postgres
--

ALTER TABLE ONLY user_data.user_details
    ADD CONSTRAINT user_details_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2711 (class 2606 OID 16774)
-- Name: records records_user_id_fkey; Type: FK CONSTRAINT; Schema: user_data; Owner: postgres
--

ALTER TABLE ONLY user_data.records
    ADD CONSTRAINT records_user_id_fkey FOREIGN KEY (user_id) REFERENCES user_data.user_details(user_id);


-- Completed on 2020-09-17 00:42:17

--
-- PostgreSQL database dump complete
--

