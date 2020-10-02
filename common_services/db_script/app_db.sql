--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2020-10-02 17:17:45

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
-- TOC entry 2854 (class 1262 OID 16756)
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
-- TOC entry 6 (class 2615 OID 16757)
-- Name: app_data; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA app_data;


ALTER SCHEMA app_data OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 206 (class 1259 OID 16805)
-- Name: answers; Type: TABLE; Schema: app_data; Owner: postgres
--

CREATE TABLE app_data.answers (
    id integer NOT NULL,
    value character varying NOT NULL
);


ALTER TABLE app_data.answers OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16813)
-- Name: doctors; Type: TABLE; Schema: app_data; Owner: postgres
--

CREATE TABLE app_data.doctors (
    id integer NOT NULL,
    name character varying NOT NULL,
    hospital character varying NOT NULL,
    city character varying NOT NULL,
    speciality character varying NOT NULL,
    "State" character varying NOT NULL,
    pincode integer NOT NULL,
    address character varying NOT NULL,
    latitude double precision,
    longitude double precision
);


ALTER TABLE app_data.doctors OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16797)
-- Name: questionnaire; Type: TABLE; Schema: app_data; Owner: postgres
--

CREATE TABLE app_data.questionnaire (
    id integer NOT NULL,
    question character varying NOT NULL,
    options integer[]
);


ALTER TABLE app_data.questionnaire OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16766)
-- Name: records; Type: TABLE; Schema: app_data; Owner: postgres
--

CREATE TABLE app_data.records (
    id integer NOT NULL,
    user_id character varying NOT NULL,
    file_name character varying NOT NULL,
    file bytea NOT NULL,
    description character varying NOT NULL
);


ALTER TABLE app_data.records OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16758)
-- Name: user_details; Type: TABLE; Schema: app_data; Owner: postgres
--

CREATE TABLE app_data.user_details (
    user_id character varying NOT NULL,
    password character varying NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    dob date NOT NULL,
    gender character varying NOT NULL
);


ALTER TABLE app_data.user_details OWNER TO postgres;

--
-- TOC entry 2847 (class 0 OID 16805)
-- Dependencies: 206
-- Data for Name: answers; Type: TABLE DATA; Schema: app_data; Owner: postgres
--

INSERT INTO app_data.answers (id, value) VALUES (3, 'Burns rarely');
INSERT INTO app_data.answers (id, value) VALUES (4, 'Burns moderately');
INSERT INTO app_data.answers (id, value) VALUES (5, 'Always burns ,blisters and peels');
INSERT INTO app_data.answers (id, value) VALUES (6, 'Often burns, blisters and peels');
INSERT INTO app_data.answers (id, value) VALUES (7, 'Never burns');
INSERT INTO app_data.answers (id, value) VALUES (1, 'Yes');
INSERT INTO app_data.answers (id, value) VALUES (2, 'No');
INSERT INTO app_data.answers (id, value) VALUES (8, 'Ivory white');
INSERT INTO app_data.answers (id, value) VALUES (9, 'Fair');
INSERT INTO app_data.answers (id, value) VALUES (10, 'Pale');
INSERT INTO app_data.answers (id, value) VALUES (11, 'Dark Brown');
INSERT INTO app_data.answers (id, value) VALUES (12, 'Black');


--
-- TOC entry 2848 (class 0 OID 16813)
-- Dependencies: 207
-- Data for Name: doctors; Type: TABLE DATA; Schema: app_data; Owner: postgres
--

INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1001, 'doctor1', 'Fortis Cancer Institute', 'Bengaluru', 'dermatologist', 'Karnataka', 560076, '154/9, Bannerghatta Main Road FCI Basement Floor', 12.8944, 77.5987);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1003, 'doctor3', 'Fortis Cancer Institute', 'Bengaluru', 'dermatologist', 'Karnataka', 560076, '154/9, Bannerghatta Main Road FCI Basement Floor', 12.8944, 77.5987);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1004, 'doctor4', 'Fortis Cancer Institute', 'Bengaluru', 'dermatologist', 'Karnataka', 560076, '154/9, Bannerghatta Main Road FCI Basement Floor', 12.8944, 77.5987);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1002, 'doctor2', 'Kidwai Memorial Institute of Oncology', 'Bengaluru', 'dermatologist', 'Karnataka', 560029, 'Dr M H, Marigowda Rd, Hombegowda Nagar', 12.9374, 77.598);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1005, 'doctor5', 'Kidwai Memorial Institute of Oncology', 'Bengaluru', 'dermatologist', 'Karnataka', 560029, 'Dr M H, Marigowda Rd, Hombegowda Nagar', 12.9374, 77.598);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1009, 'doctor8', 'Tata Memorial Center', 'Mumbai', 'dermatologist', 'Maharashtra', 400012, 'Dr Ernest Borges Rd, Parel East, Parel', 19.0049, 72.8432);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1010, 'doctor9', 'Tata Memorial Center', 'Mumbai', 'dermatologist', 'Maharashtra', 400012, 'Dr Ernest Borges Rd, Parel East, Parel', 19.0049, 72.8432);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1011, 'doctor10', 'Amrita Institute of Medical Science', 'Kochi', 'dermatologist', 'Kerala', 682041, 'Ponekkara, P. O', 10.0329423, 76.2935769);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1012, 'doctor12', 'Amrita Institute of Medical Science', 'Kochi', 'dermatologist', 'Kerala', 682041, 'Ponekkara, P. O', 10.0329423, 76.2935769);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1013, 'doctor13', 'Amrita Institute of Medical Science', 'Kochi', 'dermatologist', 'Kerala', 682041, 'Ponekkara, P. O', 10.0329423, 76.2935769);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1006, 'doctor6', 'Aster MIMS Hospital', 'Kozhikode', 'dermatologist', 'Kerala', 673016, 'Mini Bypass Rd, Govindapuram', 11.2458, 75.7985);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1007, 'doctor7', 'Aster MIMS Hospital', 'Kozhikode', 'dermatologist', 'Kerala', 673016, 'Mini Bypass Rd, Govindapuram', 11.2458, 75.7985);
INSERT INTO app_data.doctors (id, name, hospital, city, speciality, "State", pincode, address, latitude, longitude) VALUES (1008, 'doctor7', 'Aster MIMS Hospital', 'Kozhikode', 'dermatologist', 'Kerala', 673016, 'Mini Bypass Rd, Govindapuram', 11.2458, 75.7985);


--
-- TOC entry 2846 (class 0 OID 16797)
-- Dependencies: 205
-- Data for Name: questionnaire; Type: TABLE DATA; Schema: app_data; Owner: postgres
--

INSERT INTO app_data.questionnaire (id, question, options) VALUES (1, 'Do you wear protective clothing when you got in sunlight?', '{1,2}');
INSERT INTO app_data.questionnaire (id, question, options) VALUES (3, 'Do you use Sunscreen when you got in sunlight?', '{1,2}');
INSERT INTO app_data.questionnaire (id, question, options) VALUES (4, 'Does your work place exposes you to X-rays or chemical carcinogens?', '{1,2}');
INSERT INTO app_data.questionnaire (id, question, options) VALUES (5, 'Do you have more than 50 moles on your body?', '{1,2}');
INSERT INTO app_data.questionnaire (id, question, options) VALUES (7, 'How does your skin react to sun exposure?', '{3,4,5,6,7}');
INSERT INTO app_data.questionnaire (id, question, options) VALUES (2, 'Does you have any family history of skin cancer?', '{1,2}');
INSERT INTO app_data.questionnaire (id, question, options) VALUES (6, 'Does your skin get tanned on exposure to sun?', '{1,2}');
INSERT INTO app_data.questionnaire (id, question, options) VALUES (8, 'What is your skin tone?', '{8,9,10,11,12}');


--
-- TOC entry 2845 (class 0 OID 16766)
-- Dependencies: 204
-- Data for Name: records; Type: TABLE DATA; Schema: app_data; Owner: postgres
--



--
-- TOC entry 2844 (class 0 OID 16758)
-- Dependencies: 203
-- Data for Name: user_details; Type: TABLE DATA; Schema: app_data; Owner: postgres
--

INSERT INTO app_data.user_details (user_id, password, first_name, last_name, dob, gender) VALUES ('deepak7946@gmail.com', '12asdasd2345efsdfvsdf', 'Deepak Ram', 'K', '1994-06-17', 'M');


--
-- TOC entry 2714 (class 2606 OID 16812)
-- Name: answers answers_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.answers
    ADD CONSTRAINT answers_pkey PRIMARY KEY (id);


--
-- TOC entry 2716 (class 2606 OID 16820)
-- Name: doctors doctors_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.doctors
    ADD CONSTRAINT doctors_pkey PRIMARY KEY (id);


--
-- TOC entry 2712 (class 2606 OID 16804)
-- Name: questionnaire questionnaire_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.questionnaire
    ADD CONSTRAINT questionnaire_pkey PRIMARY KEY (id);


--
-- TOC entry 2710 (class 2606 OID 16773)
-- Name: records records_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.records
    ADD CONSTRAINT records_pkey PRIMARY KEY (id);


--
-- TOC entry 2708 (class 2606 OID 16765)
-- Name: user_details user_details_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.user_details
    ADD CONSTRAINT user_details_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2717 (class 2606 OID 16774)
-- Name: records records_user_id_fkey; Type: FK CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.records
    ADD CONSTRAINT records_user_id_fkey FOREIGN KEY (user_id) REFERENCES app_data.user_details(user_id);


-- Completed on 2020-10-02 17:17:46

--
-- PostgreSQL database dump complete
--

