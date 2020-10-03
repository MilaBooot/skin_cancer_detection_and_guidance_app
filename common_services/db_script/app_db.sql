--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2020-10-03 13:03:45

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
-- TOC entry 2862 (class 1262 OID 16756)
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
-- TOC entry 208 (class 1259 OID 25006)
-- Name: cancer_types; Type: TABLE; Schema: app_data; Owner: postgres
--

CREATE TABLE app_data.cancer_types (
    type character varying NOT NULL,
    description character varying NOT NULL,
    symptoms character varying[] NOT NULL,
    risk_factors character varying[] NOT NULL,
    link character varying NOT NULL,
    name character varying
);


ALTER TABLE app_data.cancer_types OWNER TO postgres;

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
    description character varying NOT NULL,
    file bytea NOT NULL
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
-- TOC entry 2854 (class 0 OID 16805)
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
-- TOC entry 2856 (class 0 OID 25006)
-- Dependencies: 208
-- Data for Name: cancer_types; Type: TABLE DATA; Schema: app_data; Owner: postgres
--

INSERT INTO app_data.cancer_types (type, description, symptoms, risk_factors, link, name) VALUES ('actinicKeratosis', 'An actinic keratosis (ak-TIN-ik ker-uh-TOE-sis) is a rough, scaly patch on your skin that develops from years of exposure to the sun. It''s most found on your face, lips, ears, back of your hands, forearms, scalp or neck. These patches take years to develop, usually first appearing in people over 40.', '{Rough,"dry or scaly patch of skin","usually less than 1 inch (2.5 centimeters) in diameter","Flat to slightly raised patch or bump on the top layer of skin","Color as varied as pink","red or brown","Itching or burning in the affected area"}', '{"Are older than 40","Live in a sunny place","Have a history of frequent or intense sun exposure or sunburn","Have red or blond hair","and blue or light-colored eyes","Tend to freckle or burn when exposed to sunlight","Have a weak immune system as a result of chemotherapy",leukemia,"AIDS or organ transplant medications"}', 'https://www.mayoclinic.org/diseases-conditions/actinic-keratosis/symptoms-causes/syc-20354969', 'Actinic Keratosis');
INSERT INTO app_data.cancer_types (type, description, symptoms, risk_factors, link, name) VALUES ('basalCellCarcinoma', 'Basal cell carcinoma is a type of skin cancer. It begins in the basal cells  a type of cell within the skin that produces new skin cells as old ones die off. It often appears as a slightly transparent bump on the skin, though it can take other forms. This occurs most often on areas of the skin that are exposed to the sun, such as your head and neck.
Most basal cell carcinomas are thought to be caused by long-term exposure to ultraviolet (UV) radiation from sunlight. Avoiding the sun and using sunscreen may help protect against basal cell carcinoma.', '{"A pearly white","skin-colored or pink bump that is translucent","meaning you can see a bit through the surface Flat to slightly raised patch or bump on the top layer of skin","A brown","black or blue lesion — or a lesion with dark spots Itching or burning in the affected area","A flat",scaly,"reddish patch with a raised edge is more common on the back or chest"}', '{"Chronic sun exposure. A lot of time spent in the sun","Radiation therapy to treat acne or other skin conditions may increase the risk of basal cell carcinoma at previous treatment sites on the skin","Fair skin- Risk is higher among people who freckle or burn easily or who have very light skin","red or blond hair","or light-colored eyes"}', 'https://www.mayoclinic.org/diseases-conditions/basal-cell-carcinoma/symptoms-causes/syc-20354187', 'Basal Cell Carcinoma');
INSERT INTO app_data.cancer_types (type, description, symptoms, risk_factors, link, name) VALUES ('dermatofibromas', 'Dermatofibromas are harmless growths within the skin that usually have a small diameter. They can vary in color, and the color may change over the years.
Dermatofibromas are firm to the touch. They are very dense, and many people say they feel like a small stone underneath or raised above the skin. Most dermatofibromas are painless.
Some people experience itching or irritation at the site of the growth, as well as tenderness. Dermatofibromas may also be called benign fibrous histiocytomas.', '{"Appearance – a round bump that is mostly under the skin","Size – the normal range is about the size of the tip of a ballpoint pen to a pea","and it usually remains stable","Color – may be pink",red,gray,"light brown or purple in varying degrees","and may change over time","Location –Found on the legs","but sometimes on the arms",trunk,"and less common elsewhere on the body","Additional symptoms – usually harmless and painless","but occasionally may be itchy",tender,painful,"or feel inflamed"}', '{"They may be caused by an adverse reaction to a small injury","such as a bug bite",splinter,"or puncture wound","Age may be another risk factor","as the growths appear mostly in adults. People with suppressed immune systems may be more likely to experience dermatofibromas"}', 'https://www.medicalnewstoday.com/articles/318870#what-is-a-dermatofibroma', 'Dermatofibromas');
INSERT INTO app_data.cancer_types (type, description, symptoms, risk_factors, link, name) VALUES ('melanoma', 'Melanoma, the most serious type of skin cancer, develops in the cells (melanocytes) that produce melanin — the pigment that gives your skin its color. It can also form in your eyes and, rarely, inside your body, such as in your nose or throat.
The exact cause of all melanomas isn''t clear, but exposure to ultraviolet (UV) radiation from sunlight or tanning lamps and beds increases your risk of developing melanoma. Limiting your exposure to UV radiation can help reduce your risk of melanoma.
The risk of melanoma seems to be increasing in people under 40, especially women. Knowing the warning signs of skin cancer can help ensure that cancerous changes are detected and treated before the cancer has spread. Melanoma can be treated successfully if it is detected early.', '{"A change in an existing mole","The development of a new pigmented or unusual-looking growth on your skin"}', '{"Fair skin","A history of sunburn","Excessive ultraviolet (UV) light exposure","Living closer to the equator or at a higher elevation","Having many moles or unusual moles"}', 'https://www.mayoclinic.org/diseases-conditions/melanoma/symptoms-causes/syc-20374884', 'Melanoma');
INSERT INTO app_data.cancer_types (type, description, symptoms, risk_factors, link, name) VALUES ('nevus', 'Moles are a common type of skin growth. They often appear as small, dark brown spots and are caused by clusters of pigmented cells. Moles generally appear during childhood and adolescence. Most people have 10 to 40 moles, some of which may change in appearance or fade away over time.
Most moles are harmless. Rarely, they become cancerous. Monitoring moles and other pigmented patches is an important step in detecting skin cancer, especially malignant melanoma.', '{"Color and texture. Moles can be brown",tan,black,red,"blue or pink. They can be smooth",wrinkled,"flat or raised. They may have hair growing from them","Shape - Most moles are oval or round","Size - Moles are usually less than 1/4 inch (about 6 millimeters) in diameter"}', '{"Being born with large moles","Having unusual moles","Having a personal or family history of melanoma"}', 'https://www.mayoclinic.org/diseases-conditions/moles/symptoms-causes/syc-20375200', 'Nevus');
INSERT INTO app_data.cancer_types (type, description, symptoms, risk_factors, link, name) VALUES ('benignKeratosis', 'A seborrheic keratosis (seb-o-REE-ik ker-uh-TOE-sis) is a common noncancerous skin growth. People tend to get more of them as they get older.
Seborrheic keratoses are usually brown, black or light tan. The growths look waxy, scaly and slightly raised. They usually appear on the head, neck, chest or back.
Seborrheic keratoses are harmless and not contagious. They don''t need treatment, but you may decide to have them removed if they become irritated by clothing or you don''t like how they look.', '{"Ranges in color from light tan to brown or black","Is round or oval shaped","Has a characteristic pasted on look","Is flat or slightly raised with a scaly surface","Ranges in size from very small to more than 1 inch (2.5 centimeters) across","May itch"}', '{"You''re generally more likely to develop seborrheic keratoses if you''re over age 50","You''re also more likely to have them if you have a family history of the condition"}', 'https://www.mayoclinic.org/diseases-conditions/seborrheic-keratosis/symptoms-causes/syc-20353878', 'Benign Keratosis');


--
-- TOC entry 2855 (class 0 OID 16813)
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
-- TOC entry 2853 (class 0 OID 16797)
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
-- TOC entry 2852 (class 0 OID 16766)
-- Dependencies: 204
-- Data for Name: records; Type: TABLE DATA; Schema: app_data; Owner: postgres
--



--
-- TOC entry 2851 (class 0 OID 16758)
-- Dependencies: 203
-- Data for Name: user_details; Type: TABLE DATA; Schema: app_data; Owner: postgres
--



--
-- TOC entry 2719 (class 2606 OID 16812)
-- Name: answers answers_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.answers
    ADD CONSTRAINT answers_pkey PRIMARY KEY (id);


--
-- TOC entry 2723 (class 2606 OID 25013)
-- Name: cancer_types cancer_types_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.cancer_types
    ADD CONSTRAINT cancer_types_pkey PRIMARY KEY (type);


--
-- TOC entry 2721 (class 2606 OID 16820)
-- Name: doctors doctors_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.doctors
    ADD CONSTRAINT doctors_pkey PRIMARY KEY (id);


--
-- TOC entry 2717 (class 2606 OID 16804)
-- Name: questionnaire questionnaire_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.questionnaire
    ADD CONSTRAINT questionnaire_pkey PRIMARY KEY (id);


--
-- TOC entry 2715 (class 2606 OID 16773)
-- Name: records records_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.records
    ADD CONSTRAINT records_pkey PRIMARY KEY (id);


--
-- TOC entry 2713 (class 2606 OID 16765)
-- Name: user_details user_details_pkey; Type: CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.user_details
    ADD CONSTRAINT user_details_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2724 (class 2606 OID 16774)
-- Name: records records_user_id_fkey; Type: FK CONSTRAINT; Schema: app_data; Owner: postgres
--

ALTER TABLE ONLY app_data.records
    ADD CONSTRAINT records_user_id_fkey FOREIGN KEY (user_id) REFERENCES app_data.user_details(user_id);


-- Completed on 2020-10-03 13:03:46

--
-- PostgreSQL database dump complete
--

