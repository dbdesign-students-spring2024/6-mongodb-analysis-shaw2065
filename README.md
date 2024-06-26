# AirBnB MongoDB Analysis

## Data set details:

1. [My data set](https://data.insideairbnb.com/greece/attica/athens/2023-12-25/data/listings.csv.gz) contains detailed Airbnb listings data specifically from the region of Athens, Attica, Greece. It comes from the website, [Inside Airbnb](https://insideairbnb.com/get-the-data/).


2. The original data file was in the format of CSV.

3. First 20 rows of raw data from the original data file

    | **id**| **listing_url** | **scrape_id** | **last_scraped** | **source** | **name** | **description** | **neighborhood_overview** | **picture_url** | **host_id** | **host_url** | **host_name** | **host_since** | **host_location** | **host_about** | **host_response_time** | **host_response_rate** | **host_acceptance_rate** | **host_is_superhost** | **host_thumbnail_url** | **host_picture_url** | **host_neighbourhood** | **host_listings_count** | **host_total_listings_count** | **host_verifications** | **host_has_profile_pic** | **host_identity_verified** | **neighbourhood** | **neighbourhood_cleansed** | **neighbourhood_group_cleansed** | **latitude** | **longitude** | **property_type** | **room_type** | **accommodates** | **bathrooms** | **bathrooms_text** | **bedrooms** | **beds** | **amenities** | **price** | **minimum_nights** | **maximum_nights** | **minimum_minimum_nights** | **maximum_minimum_nights** | **minimum_maximum_nights** | **maximum_maximum_nights** | **minimum_nights_avg_ntm** | **maximum_nights_avg_ntm** | **calendar_updated** | **has_availability** | **availability_30** | **availability_60** | **availability_90** | **availability_365** | **calendar_last_scraped** | **number_of_reviews** | **number_of_reviews_ltm** | **number_of_reviews_l30d** | **first_review** | **last_review** | **review_scores_rating** | **review_scores_accuracy** | **review_scores_cleanliness** | **review_scores_checkin** | **review_scores_communication** | **review_scores_location** | **review_scores_value** | **license** | **instant_bookable** | **calculated_host_listings_count** | **calculated_host_listings_count_entire_homes** | **calculated_host_listings_count_private_rooms** | **calculated_host_listings_count_shared_rooms** | **reviews_per_month** |
    | ----------------------- | ---------------------------------------------------------------------------------------------------- | -------------- | ---------------- | --------------- | ------------------------------------------------------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------ | --------------------- | -------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ---------------------- | ------------------------ | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ----------------------- | ----------------------------- | -------------------------------- | ------------------------ | -------------------------- | ----------------- | -------------------------------- | -------------------------------- | ------------------ | ------------------ | --------------------------- | --------------- | ---------------- | ------------- | ------------------ | ------------ | -------- | ------------- | --------- | ------------------ | ------------------ | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------- | -------------------- | ------------------- | ------------------- | ------------------- | -------------------- | ------------------------- | --------------------- | ------------------------- | -------------------------- | ---------------- | --------------- | ------------------------ | -------------------------- | ----------------------------- | ------------------------- | ------------------------------- | -------------------------- | ----------------------- | ----------- | -------------------- | ---------------------------------- | ----------------------------------------------- | ------------------------------------------------ | ----------------------------------------------- | --------------------- |
    | **40042598** | [https://www.airbnb.com/rooms/40042598](https://www.airbnb.com/rooms/40042598) | 20231225075512 | 2023-12-26 | previous scrape | Rental unit in Athina · 1 bedroom · 1 bed · 1 shared bath | | | [https://a0.muscache.com/pictures/fb6d0257-52ec-43b4-b3e4-6f8cb93ab8df.jpg](https://a0.muscache.com/pictures/fb6d0257-52ec-43b4-b3e4-6f8cb93ab8df.jpg) | 158884228 | [https://www.airbnb.com/users/show/158884228](https://www.airbnb.com/users/show/158884228) | Christos | 2017-11-15 | Athens, Greece | | N/A | N/A | N/A | f | [https://a0.muscache.com/im/pictures/user/6146e0dc-7177-43ec-8f55-8b09d375b74d.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/6146e0dc-7177-43ec-8f55-8b09d375b74d.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/6146e0dc-7177-43ec-8f55-8b09d375b74d.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/6146e0dc-7177-43ec-8f55-8b09d375b74d.jpg?aki_policy=profile_x_medium) | Pedion Areos | 1 | 1 | ['email', 'phone'] | t | t | | ΠΕΔΙΟ ΑΡΕΩΣ | | 37.99443 | 23.73688 | Private room in rental unit | Private room | 2 | | 1 shared bath | | 1 | [] | $20.00 | 1 | 1125 | 1 | 1 | 1125 | 1125 | 1.0 | 1125.0 | | t | 0 | 0 | 0 | 0 | 2023-12-26 | 0 | 0 | 0 | | | | | | | | | | | f | 1 | 0 | 1 | 0 | |
    | **39069205** | [https://www.airbnb.com/rooms/39069205](https://www.airbnb.com/rooms/39069205) | 20231225075512 | 2023-12-26 | previous scrape | Rental unit in Athina · 2 bedrooms · 2 beds · 2 baths | | Is located in one of the hottest spots in Kolonaki  very close to all the hottest leisured spots of Kolonaki. | [https://a0.muscache.com/pictures/8965800b-9101-438e-8da0-7e08574a8e3b.jpg](https://a0.muscache.com/pictures/8965800b-9101-438e-8da0-7e08574a8e3b.jpg) | 299446668 | [https://www.airbnb.com/users/show/299446668](https://www.airbnb.com/users/show/299446668) | Nikos | 2019-10-02 | | | within an hour | 100% | 0% | f | [https://a0.muscache.com/im/pictures/user/62e8de54-3838-4379-9e4d-fa5943e22ae3.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/62e8de54-3838-4379-9e4d-fa5943e22ae3.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/62e8de54-3838-4379-9e4d-fa5943e22ae3.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/62e8de54-3838-4379-9e4d-fa5943e22ae3.jpg?aki_policy=profile_x_medium) | Kolonaki | 1 | 2 | ['email', 'phone'] | t | t | Athina, Greece | ΚΟΛΩΝΑΚΙ | | 37.97919 | 23.74532 | Entire rental unit | Entire home/apt | 4 | | 2 baths | | 2 | [] | $293.00 | 2 | 10 | 2 | 2 | 10 | 10 | 2.0 | 10.0 | | t | 23 | 53 | 83 | 173 | 2023-12-26 | 0 | 0 | 0 | | | | | | | | | | | f | 1 | 1 | 0 | 0 | |
    | **653274914834812593** | [https://www.airbnb.com/rooms/653274914834812593](https://www.airbnb.com/rooms/653274914834812593) | 20231225075512 | 2023-12-26 | city scrape | Condo in Athina · ★5.0 · 1 bedroom · 2 beds · 1 bath | | Η γειτονιά βρίσκεται μια ανάσα από τον Παρθενώνα,το μουσείο της Ακρόπολης  ,την Πλάκα και το ιστορικό κέντρο της Αθήνας<br /><br />The neighbourhood is locaded a breath away from the Parthenon, the Actopolis Museum, Plaka and the historic city centre | [https://a0.muscache.com/pictures/b8926124-f861-45f8-9203-917cd0d2b9f1.jpg](https://a0.muscache.com/pictures/b8926124-f861-45f8-9203-917cd0d2b9f1.jpg) | 272702874 | [https://www.airbnb.com/users/show/272702874](https://www.airbnb.com/users/show/272702874) | Costas | 2019-07-01 | Athens, Greece | | within an hour | 100% | 96% | t | [https://a0.muscache.com/im/pictures/user/User-272702874/original/cf81a259-c3f4-4a57-9798-3b96b851fa02.jpeg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/User-272702874/original/cf81a259-c3f4-4a57-9798-3b96b851fa02.jpeg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/User-272702874/original/cf81a259-c3f4-4a57-9798-3b96b851fa02.jpeg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/User-272702874/original/cf81a259-c3f4-4a57-9798-3b96b851fa02.jpeg?aki_policy=profile_x_medium) | | 1 | 1 | ['email', 'phone'] | t | t | Athina, Greece | ΚΟΥΚΑΚΙ-ΜΑΚΡΥΓΙΑΝΝΗ | | 37.966 | 23.72717 | Entire condo | Entire home/apt | 3 | | 1 bath | | 2 | [] | $60.00 | 1 | 365 | 1 | 1 | 1125 | 1125 | 1.0 | 1125.0 | | t | 23 | 53 | 83 | 263 | 2023-12-26 | 47 | 37 | 0 | 2022-07-19 | 2023-11-15 | 5.0 | 5.0 | 5.0 | 4.96 | 5.0 | 4.98 | 4.96 | 1652202 | t | 1 | 1 | 0 | 0 | 2.68 |
    | **54361219** | [https://www.airbnb.com/rooms/54361219](https://www.airbnb.com/rooms/54361219) | 20231225075512 | 2023-12-26 | city scrape | Rental unit in Athina · ★4.75 · 1 bedroom · 1 bed · 1 bath | | | [https://a0.muscache.com/pictures/miso/Hosting-54361219/original/2097f813-3e19-4708-8fca-063e7f436f9c.jpeg](https://a0.muscache.com/pictures/miso/Hosting-54361219/original/2097f813-3e19-4708-8fca-063e7f436f9c.jpeg) | 433120301 | [https://www.airbnb.com/users/show/433120301](https://www.airbnb.com/users/show/433120301) | Iordanka | 2021-11-23 | | | within an hour | 100% | 100% | f | [https://a0.muscache.com/im/pictures/user/80ddd0dd-b898-4590-a4db-dd74fa9155e8.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/80ddd0dd-b898-4590-a4db-dd74fa9155e8.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/80ddd0dd-b898-4590-a4db-dd74fa9155e8.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/80ddd0dd-b898-4590-a4db-dd74fa9155e8.jpg?aki_policy=profile_x_medium) | | 1 | 1 | ['email', 'phone'] | t | t | | ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ | | 37.97589 | 23.73275 | Entire rental unit | Entire home/apt | 2 | | 1 bath | | 1 | [] | $93.00 | 1 | 365 | 1 | 1 | 365 | 365 | 1.0 | 365.0 | | t | 16 | 43 | 67 | 335 | 2023-12-26 | 40 | 11 | 0 | 2022-03-13 | 2023-10-03 | 4.75 | 4.83 | 4.78 | 4.98 | 5.0 | 4.98 | 4.83 | 1402443 | t | 1 | 1 | 0 | 0 | 1.83 |
    | **51258073** | [https://www.airbnb.com/rooms/51258073](https://www.airbnb.com/rooms/51258073) | 20231225075512 | 2023-12-26 | city scrape | Rental unit in Athina · ★5.0 · Studio · 3 beds · 1.5 baths | | | [https://a0.muscache.com/pictures/2e0592af-8983-46d0-8ffa-0ca7457d6113.jpg](https://a0.muscache.com/pictures/2e0592af-8983-46d0-8ffa-0ca7457d6113.jpg) | 199937958 | [https://www.airbnb.com/users/show/199937958](https://www.airbnb.com/users/show/199937958) | Nick | 2018-07-04 | Athens, Greece | My name is Nick and I love travelling and meeting new people from all over the world! My guests are my priority and I strive to make them feel at home and enjoy their stay to the fullest! | within an hour | 100% | 100% | f | [https://a0.muscache.com/im/pictures/user/326228b6-683f-44b3-9585-e0f4deab27a3.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/326228b6-683f-44b3-9585-e0f4deab27a3.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/326228b6-683f-44b3-9585-e0f4deab27a3.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/326228b6-683f-44b3-9585-e0f4deab27a3.jpg?aki_policy=profile_x_medium) | Psyri | 3 | 3 | ['email', 'phone', 'work_email'] | t | t | | ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ | | 37.97922 | 23.7247 | Entire rental unit | Entire home/apt | 4 | | 1.5 baths | | 3 | [] | $119.00 | 2 | 365 | 2 | 2 | 1125 | 1125 | 2.0 | 1125.0 | | t | 14 | 14 | 14 | 218 | 2023-12-26 | 9 | 3 | 0 | 2021-08-08 | 2023-10-13 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 2160731 | f | 3 | 3 | 0 | 0 | 0.31 |
    | **986232372259000220** | [https://www.airbnb.com/rooms/986232372259000220](https://www.airbnb.com/rooms/986232372259000220) | 20231225075512 | 2023-12-25 | city scrape | Rental unit in Athina · ★5.0 · 1 bedroom · 1 bed · 1 bath | | An upcoming neighborhood full with cafeterias small shops and some big chain shops. | [https://a0.muscache.com/pictures/miso/Hosting-986232372259000220/original/7bf30c34-02d3-4997-b2a6-ca0a695a8919.jpeg](https://a0.muscache.com/pictures/miso/Hosting-986232372259000220/original/7bf30c34-02d3-4997-b2a6-ca0a695a8919.jpeg) | 220064887 | [https://www.airbnb.com/users/show/220064887](https://www.airbnb.com/users/show/220064887) | Alexandros | 2018-10-11 | Arta, Greece | Hi there!<br>We are Alex & Maria, we're both dental technicians and love to travel.<br>We used to live in Kallithea before having kids so we moved out of the apartment gave the house a full renovation and wonna try this hosting trend to meet new people, new cultures and who knows maybe one day we meet again in your bnbs!<br>Thankfully we have expanded and we are welcoming more people to our lovely apartments :)<br>We welcome guests from every racial and social background. <br>We hope you do have a nice and comfy stay in our lovely homes. | within an hour | 100% | 100% | t | [https://a0.muscache.com/im/pictures/user/d8cee7a5-1106-4e46-bc80-c01380cd0165.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/d8cee7a5-1106-4e46-bc80-c01380cd0165.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/d8cee7a5-1106-4e46-bc80-c01380cd0165.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/d8cee7a5-1106-4e46-bc80-c01380cd0165.jpg?aki_policy=profile_x_medium) | Patisia | 7 | 7 | ['email', 'phone'] | t | t | Athina, Greece | ΠΑΤΗΣΙΑ | | 38.0124488 | 23.7296833 | Entire rental unit | Entire home/apt | 3 | | 1 bath | | 1 | [] | $45.00 | 2 | 365 | 2 | 2 | 365 | 365 | 2.0 | 365.0 | | t | 24 | 54 | 84 | 84 | 2023-12-25 | 8 | 8 | 2 | 2023-09-29 | 2023-12-12 | 5.0 | 5.0 | 4.38 | 5.0 | 5.0 | 4.75 | 4.88 | 2219582 | t | 2 | 2 | 0 | 0 | 2.73 |
    | **13842245** | [https://www.airbnb.com/rooms/13842245](https://www.airbnb.com/rooms/13842245) | 20231225075512 | 2023-12-26 | city scrape | Condo in Athina · ★4.86 · 1 bedroom · 2 beds · 1 bath | | The street where the flat is located connects the Temple of Olympian Zeus and the Arch of Hadrian with the historical, fascinating and vibrant side of Plaka. The flat is just 4 min walk from the Acropolis metro station and within easy reach of the most famous sights of Athens (Acropolis and Acropolis Museum, National Gardens, Panathenaic "Kallimarmaro" Stadium, Syntagma square, Monastiraki and Thission). | [https://a0.muscache.com/pictures/54d2948c-0e26-4b96-948b-a1eb99a5035c.jpg](https://a0.muscache.com/pictures/54d2948c-0e26-4b96-948b-a1eb99a5035c.jpg) | 65341135 | [https://www.airbnb.com/users/show/65341135](https://www.airbnb.com/users/show/65341135) | Lito | 2016-04-01 | Athens, Greece | Hello! I am Lito, the host of “Plaka’s heArt”. I travel a lot myself, so I am very happy to host people from all over the world in my small flat, which I have looked after with great care. I teach Greek literature, but in my spare time I am always an eager student, taking lessons in theatre, the flute, yoga and photography. However, I never forget the small joys of life, such as a glass of wine by the sea or a meal at a small Greek taverna in the company of good friends.<br>Hello! I am Yiannis and I am helping Lito with Plaka's heArt. I really enjoy communicating with the guests before their arrival, welcoming and meeting all these people from all over the world, and offering them tips and recommendations for spending a great time in Athens. I like doing many things, but most of all I am interested in the theatre, that's why I participate in two theatrical groups, both as an actor and as a teacher. | within an hour | 100% | 100% | t | [https://a0.muscache.com/im/pictures/user/d8e0f80f-70d0-487f-8321-ddcac3d0ad2d.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/d8e0f80f-70d0-487f-8321-ddcac3d0ad2d.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/d8e0f80f-70d0-487f-8321-ddcac3d0ad2d.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/d8e0f80f-70d0-487f-8321-ddcac3d0ad2d.jpg?aki_policy=profile_x_medium) | Plaka | 1 | 1 | ['email', 'phone'] | t | t | Athina, Greece | ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ | | 37.97134 | 23.73146 | Entire condo | Entire home/apt | 3 | | 1 bath | | 2 | [] | $50.00 | 1 | 1125 | 1 | 1 | 1125 | 1125 | 1.0 | 1125.0 | | t | 0 | 0 | 0 | 0 | 2023-12-26 | 741 | 125 | 6 | 2016-07-12 | 2023-12-18 | 4.86 | 4.89 | 4.92 | 4.96 | 4.96 | 4.99 | 4.87 | 531949 | t | 1 | 1 | 0 | 0 | 8.16 |
    | **886572018411948012** | [https://www.airbnb.com/rooms/886572018411948012](https://www.airbnb.com/rooms/886572018411948012) | 20231225075512 | 2023-12-25 | city scrape | Rental unit in Athina · 1 bedroom · 4 beds · 1 bath | | | [https://a0.muscache.com/pictures/dfa4117a-7dbc-4eb2-9360-947df810ac21.jpg](https://a0.muscache.com/pictures/dfa4117a-7dbc-4eb2-9360-947df810ac21.jpg) | 317333784 | [https://www.airbnb.com/users/show/317333784](https://www.airbnb.com/users/show/317333784) | Michail | 2019-12-14 | Kissamos, Greece | former chania airport manager | within an hour | 100% | 100% | f | [https://a0.muscache.com/im/pictures/user/ec5540c2-4ff8-42b2-b3e9-4ecf47992c56.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/ec5540c2-4ff8-42b2-b3e9-4ecf47992c56.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/ec5540c2-4ff8-42b2-b3e9-4ecf47992c56.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/ec5540c2-4ff8-42b2-b3e9-4ecf47992c56.jpg?aki_policy=profile_x_medium) | | 3 | 3 | ['email', 'phone'] | t | t | | ΝΕΟΣ ΚΟΣΜΟΣ | | 37.950322295887500 | 23.722645730233900 | Entire rental unit | Entire home/apt | 4 | | 1 bath | | 4 | [] | $32.00 | 28 | 1125 | 28 | 28 | 1125 | 1125 | 28.0 | 1125.0 | | t | 22 | 52 | 82 | 357 | 2023-12-25 | 0 | 0 | 0 | | | | | | | | | | 2077390 | f | 1 | 1 | 0 | 0 | |
    | **48565349** | [https://www.airbnb.com/rooms/48565349](https://www.airbnb.com/rooms/48565349) | 20231225075512 | 2023-12-26 | city scrape | Condo in Athina · ★4.67 · 1 bedroom · 4 beds · 1 bath | | | [https://a0.muscache.com/pictures/miso/Hosting-48565349/original/7dc422db-e071-4647-a97a-62be6f500462.jpeg](https://a0.muscache.com/pictures/miso/Hosting-48565349/original/7dc422db-e071-4647-a97a-62be6f500462.jpeg) | 389089363 | [https://www.airbnb.com/users/show/389089363](https://www.airbnb.com/users/show/389089363) | ΜΙΧΟΣ Μονοπροσωπη Ικε | 2021-02-18 | | | within an hour | 100% | 100% | f | [https://a0.muscache.com/im/pictures/user/5eca7dd9-935a-4ce1-bbec-e3e75675545d.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/5eca7dd9-935a-4ce1-bbec-e3e75675545d.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/5eca7dd9-935a-4ce1-bbec-e3e75675545d.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/5eca7dd9-935a-4ce1-bbec-e3e75675545d.jpg?aki_policy=profile_x_medium) | Koukaki | 20 | 22 | ['email', 'phone', 'work_email'] | t | t | | ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ | | 37.97623 | 23.7308 | Entire condo | Entire home/apt | 4 | | 1 bath | | 4 | [] | $51.00 | 2 | 1125 | 2 | 2 | 365 | 365 | 2.0 | 365.0 | | t | 0 | 0 | 0 | 0 | 2023-12-26 | 17 | 1 | 0 | 2021-04-14 | 2023-06-12 | 4.67 | 4.72 | 4.67 | 4.61 | 4.67 | 4.61 | 4.72 | 1131148 | t | 17 | 17 | 0 | 0 | 0.52 |
    | **52818014** | [https://www.airbnb.com/rooms/52818014](https://www.airbnb.com/rooms/52818014) | 20231225075512 | 2023-12-25 | city scrape | Condo in Athina · ★4.77 · 1 bedroom · 3 beds · 1 bath | | | [https://a0.muscache.com/pictures/miso/Hosting-52818014/original/9e02a49b-3cd9-4899-b7c8-c2593dfb1fa9.jpeg](https://a0.muscache.com/pictures/miso/Hosting-52818014/original/9e02a49b-3cd9-4899-b7c8-c2593dfb1fa9.jpeg) | 427611455 | [https://www.airbnb.com/users/show/427611455](https://www.airbnb.com/users/show/427611455) | Ourania And Giorgos | 2021-10-16 | | | within an hour | 100% | 100% | t | [https://a0.muscache.com/im/pictures/user/9a489a2c-a67b-4d65-8dd5-42dbfa9544ad.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/9a489a2c-a67b-4d65-8dd5-42dbfa9544ad.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/9a489a2c-a67b-4d65-8dd5-42dbfa9544ad.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/9a489a2c-a67b-4d65-8dd5-42dbfa9544ad.jpg?aki_policy=profile_x_medium) | | 2 | 2 | ['email', 'phone'] | t | t | | ΠΑΓΚΡΑΤΙ | | 37.97268 | 23.74908 | Entire condo | Entire home/apt | 4 | | 1 bath | | 3 | [] | $47.00 | 1 | 25 | 1 | 2 | 25 | 25 | 1.0 | 25.0 | | t | 24 | 53 | 83 | 252 | 2023-12-25 | 167 | 72 | 2 | 2021-10-28 | 2023-11-29 | 4.77 | 4.74 | 4.81 | 4.91 | 4.94 | 4.83 | 4.74 | 1371227 | t | 1 | 1 | 0 | 0 | 6.35 |
    | **870196725841398447** | [https://www.airbnb.com/rooms/870196725841398447](https://www.airbnb.com/rooms/870196725841398447) | 20231225075512 | 2023-12-25 | city scrape | Rental unit in Athina · 1 bedroom · 6 beds · 2 shared baths | | | [https://a0.muscache.com/pictures/miso/Hosting-851383748637595596/original/e56ef6e8-e342-41e3-b245-a7abeb92210c.jpeg](https://a0.muscache.com/pictures/miso/Hosting-851383748637595596/original/e56ef6e8-e342-41e3-b245-a7abeb92210c.jpeg) | 33626433 | [https://www.airbnb.com/users/show/33626433](https://www.airbnb.com/users/show/33626433) | Airnite | 2015-05-18 | Athens, Greece | | within an hour | 100% | 96% | f | [https://a0.muscache.com/im/pictures/user/c0474f18-4180-4460-8635-327e5292a08b.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/c0474f18-4180-4460-8635-327e5292a08b.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/c0474f18-4180-4460-8635-327e5292a08b.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/c0474f18-4180-4460-8635-327e5292a08b.jpg?aki_policy=profile_x_medium) | | 20 | 20 | ['email', 'phone'] | t | t | | ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ-ΠΛΑΤΕΙΑ ΒΑΘΗΣ | | 37.98966143162360 | 23.728679354853400 | Shared room in rental unit | Shared room | 1 | | 2 shared baths | | 6 | [] | $20.00 | 1 | 365 | 1 | 1 | 365 | 365 | 1.0 | 365.0 | | t | 29 | 59 | 89 | 364 | 2023-12-25 | 0 | 0 | 0 | | | | | | | | | | 1126280217 | f | 20 | 2 | 3 | 15 | |
    | **1001479705609008221** | [https://www.airbnb.com/rooms/1001479705609008221](https://www.airbnb.com/rooms/1001479705609008221) | 20231225075512 | 2023-12-25 | city scrape | Rental unit in Athina · 4 bedrooms · 5 beds · 1 shared bath | | | [https://a0.muscache.com/pictures/miso/Hosting-1001479705609008221/original/9f8ccba8-afb1-4fb1-8288-3bdcc28aaa1f.jpeg](https://a0.muscache.com/pictures/miso/Hosting-1001479705609008221/original/9f8ccba8-afb1-4fb1-8288-3bdcc28aaa1f.jpeg) | 272941329 | [https://www.airbnb.com/users/show/272941329](https://www.airbnb.com/users/show/272941329) | Giannis | 2019-07-02 | Athina, Greece | | within a few hours | 95% | 90% | f | [https://a0.muscache.com/im/pictures/user/User-272941329/original/4c8f540e-3d20-412b-b5a8-a1ffd7806a4f.jpeg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/User-272941329/original/4c8f540e-3d20-412b-b5a8-a1ffd7806a4f.jpeg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/User-272941329/original/4c8f540e-3d20-412b-b5a8-a1ffd7806a4f.jpeg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/User-272941329/original/4c8f540e-3d20-412b-b5a8-a1ffd7806a4f.jpeg?aki_policy=profile_x_medium) | | 7 | 7 | ['email', 'phone'] | t | t | | ΓΚΥΖΗ | | 37.9928 | 23.74707 | Private room in rental unit | Private room | 2 | | 1 shared bath | | 5 | [] | $21.00 | 1 | 365 | 1 | 1 | 365 | 365 | 1.0 | 365.0 | | t | 29 | 59 | 89 | 269 | 2023-12-25 | 1 | 1 | 0 | 2023-10-23 | 2023-10-23 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 13237613 | f | 7 | 0 | 7 | 0 | 0.47 |
    | **22549921** | [https://www.airbnb.com/rooms/22549921](https://www.airbnb.com/rooms/22549921) | 20231225075512 | 2023-12-25 | city scrape | Condo in Athina · ★5.0 · 1 bedroom · 1 bed · 1 bath | | | [https://a0.muscache.com/pictures/261c764a-d0dd-4df2-ab01-a49a3fa92677.jpg](https://a0.muscache.com/pictures/261c764a-d0dd-4df2-ab01-a49a3fa92677.jpg) | 165640249 | [https://www.airbnb.com/users/show/165640249](https://www.airbnb.com/users/show/165640249) | Sofia | 2018-01-03 | Athens, Greece | I have lived around the world and have retired in my home country of Greece. I like art, music, and exploring different cultures. | N/A | N/A | 100% | f | [https://a0.muscache.com/im/pictures/user/e322cbd4-8914-4e79-bf16-e4259e705f7f.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/e322cbd4-8914-4e79-bf16-e4259e705f7f.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/e322cbd4-8914-4e79-bf16-e4259e705f7f.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/e322cbd4-8914-4e79-bf16-e4259e705f7f.jpg?aki_policy=profile_x_medium) | Kolonaki | 1 | 1 | ['email', 'phone'] | t | t | | ΚΟΛΩΝΑΚΙ | | 37.97947 | 23.74965 | Entire condo | Entire home/apt | 2 | | 1 bath | | 1 | [] | $60.00 | 3 | 90 | 3 | 3 | 90 | 90 | 3.0 | 90.0 | | t | 23 | 53 | 83 | 358 | 2023-12-25 | 3 | 0 | 0 | 2018-05-26 | 2019-06-16 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | | t | 1 | 1 | 0 | 0 | 0.04 |
    | **953306949213332448** | [https://www.airbnb.com/rooms/953306949213332448](https://www.airbnb.com/rooms/953306949213332448) | 20231225075512 | 2023-12-25 | city scrape | Rental unit in Athina · 1 bedroom · 1 bed · 1 bath | | | [https://a0.muscache.com/pictures/hosting/Hosting-953306949213332448/original/519ca673-029d-425a-8048-d48e3c79aa5d.jpeg](https://a0.muscache.com/pictures/hosting/Hosting-953306949213332448/original/519ca673-029d-425a-8048-d48e3c79aa5d.jpeg) | 357976509 | [https://www.airbnb.com/users/show/357976509](https://www.airbnb.com/users/show/357976509) | Γιώργος | 2020-07-23 | Greece | Hello, my name is George and I am the founder of The Property Concierge, a luxury villa and apartment management company with a focus on Mykonos and Athens, and soon expanding globally. With my wife, I am an avid traveler, and our experiences have led us to become experts in hospitality.<br>When you book with us, you'll have access to one of the best concierge services in the world. We strive to make your vacation experience as fresh and easy as a gentle breeze. | within an hour | 77% | 98% | f | [https://a0.muscache.com/im/pictures/user/d54ac3a9-2aeb-418c-95b1-c1ff2d9fb67c.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/d54ac3a9-2aeb-418c-95b1-c1ff2d9fb67c.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/d54ac3a9-2aeb-418c-95b1-c1ff2d9fb67c.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/d54ac3a9-2aeb-418c-95b1-c1ff2d9fb67c.jpg?aki_policy=profile_x_medium) | | 17 | 21 | ['email', 'phone'] | t | t | | ΑΜΠΕΛΟΚΗΠΟΙ | | 37.9832706 | 23.7535501 | Entire rental unit | Entire home/apt | 4 | | 1 bath | | 1 | [] | $56.00 | 2 | 365 | 2 | 2 | 365 | 365 | 2.0 | 365.0 | | t | 25 | 55 | 85 | 265 | 2023-12-25 | 2 | 2 | 0 | 2023-09-26 | 2023-11-09 | 5.0 | 5.0 | 4.5 | 4.5 | 5.0 | 5.0 | 5.0 | 2340702 | f | 4 | 4 | 0 | 0 | 0.66 |
    | **919666880147647194** | [https://www.airbnb.com/rooms/919666880147647194](https://www.airbnb.com/rooms/919666880147647194) | 20231225075512 | 2023-12-25 | city scrape | Rental unit in Athina · ★5.0 · 1 bedroom · 1 bed · 1 bath | | | [https://a0.muscache.com/pictures/miso/Hosting-917899314664624863/original/d04c1934-963d-4b1e-b0b1-b5f52e19755a.jpeg](https://a0.muscache.com/pictures/miso/Hosting-917899314664624863/original/d04c1934-963d-4b1e-b0b1-b5f52e19755a.jpeg) | 520997151 | [https://www.airbnb.com/users/show/520997151](https://www.airbnb.com/users/show/520997151) | Dimitris | 2023-06-20 | | | within a few hours | 100% | 73% | t | [https://a0.muscache.com/im/pictures/user/a0661e49-9ae1-47c7-8b4c-a358ba329e1c.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/a0661e49-9ae1-47c7-8b4c-a358ba329e1c.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/a0661e49-9ae1-47c7-8b4c-a358ba329e1c.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/a0661e49-9ae1-47c7-8b4c-a358ba329e1c.jpg?aki_policy=profile_x_medium) | | 3 | 5 | ['email', 'phone'] | t | t | | ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ | | 37.9863 | 23.72728 | Private room in rental unit | Private room | 2 | | 1 bath | | 1 | [] | $20.00 | 1 | 365 | 1 | 1 | 365 | 365 | 1.0 | 365.0 | | t | 30 | 59 | 89 | 179 | 2023-12-25 | 7 | 7 | 0 | 2023-07-04 | 2023-08-15 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 4.43 | 5.0 | 98765432109 | f | 3 | 0 | 3 | 0 | 1.20 |
    | **53693288** | [https://www.airbnb.com/rooms/53693288](https://www.airbnb.com/rooms/53693288) | 20231225075512 | 2023-12-25 | city scrape | Condo in Athina · ★4.36 · 1 bedroom · 1 bed · 1 bath | | | [https://a0.muscache.com/pictures/miso/Hosting-53693288/original/737c0c73-1398-40b2-b749-8aacba36acc8.jpeg](https://a0.muscache.com/pictures/miso/Hosting-53693288/original/737c0c73-1398-40b2-b749-8aacba36acc8.jpeg) | 434869524 | [https://www.airbnb.com/users/show/434869524](https://www.airbnb.com/users/show/434869524) | Yongqun | 2021-12-06 | | | within an hour | 100% | 89% | f | [https://a0.muscache.com/im/pictures/user/65e10a18-a1d1-450b-bcb9-0cbe73f4770a.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/65e10a18-a1d1-450b-bcb9-0cbe73f4770a.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/65e10a18-a1d1-450b-bcb9-0cbe73f4770a.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/65e10a18-a1d1-450b-bcb9-0cbe73f4770a.jpg?aki_policy=profile_x_medium) | | 1 | 1 | ['email', 'phone'] | t | t | | ΝΙΡΒΑΝΑ | | 38.01304 | 23.72302 | Entire condo | Entire home/apt | 3 | | 1 bath | | 1 | [] | $28.00 | 3 | 365 | 3 | 3 | 365 | 365 | 3.0 | 365.0 | | t | 14 | 44 | 74 | 349 | 2023-12-25 | 14 | 6 | 0 | 2022-01-28 | 2023-09-29 | 4.36 | 4.5 | 4.86 | 4.57 | 4.5 | 4.43 | 4.64 | 1297500 | f | 1 | 1 | 0 | 0 | 0.60 |
    | **1004298036239647295** | [https://www.airbnb.com/rooms/1004298036239647295](https://www.airbnb.com/rooms/1004298036239647295) | 20231225075512 | 2023-12-25 | city scrape | Rental unit in Athina · ★New · 1 bedroom · 1 bed · 1.5 baths | | | [https://a0.muscache.com/pictures/miso/Hosting-1004298036239647295/original/f19e7250-afd1-4e68-9938-9341887d16c4.jpeg](https://a0.muscache.com/pictures/miso/Hosting-1004298036239647295/original/f19e7250-afd1-4e68-9938-9341887d16c4.jpeg) | 408918439 | [https://www.airbnb.com/users/show/408918439](https://www.airbnb.com/users/show/408918439) | Jozef | 2021-06-24 | | | within a few hours | 86% | 75% | f | [https://a0.muscache.com/im/pictures/user/edbc745e-9082-40d2-b788-bf8f14416d6c.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/edbc745e-9082-40d2-b788-bf8f14416d6c.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/edbc745e-9082-40d2-b788-bf8f14416d6c.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/edbc745e-9082-40d2-b788-bf8f14416d6c.jpg?aki_policy=profile_x_medium) | | 8 | 14 | ['phone'] | t | t | | ΠΛΑΤΕΙΑ ΑΤΤΙΚΗΣ | | 37.99623991765500 | 23.729077410901400 | Private room in rental unit | Private room | 1 | | 1.5 baths | | 1 | [] | $27.00 | 28 | 365 | 28 | 28 | 365 | 365 | 28.0 | 365.0 | | t | 29 | 59 | 89 | 269 | 2023-12-25 | 0 | 0 | 0 | | | | | | | | | | Exempt | f | 2 | 0 | 2 | 0 | |
    | **39631513** | [https://www.airbnb.com/rooms/39631513](https://www.airbnb.com/rooms/39631513) | 20231225075512 | 2023-12-25 | city scrape | Aparthotel in Athina · 1 bedroom · 3 beds · 1 bath | | Located in the histοrical area of Athens, you have straight access to Monastiraki Metro Station (direct line to the Athens International Airport and Central Piraeus Port). Stroll around the pedestrians earby, which are part of the great shopping district in the capital and get lost among the athenian monuments that stand a breath away from this central hotel. | [https://a0.muscache.com/pictures/miso/Hosting-39631513/original/ac4f0b93-40a3-4744-a9bb-be654dbcf28a.jpeg](https://a0.muscache.com/pictures/miso/Hosting-39631513/original/ac4f0b93-40a3-4744-a9bb-be654dbcf28a.jpeg) | 303652112 | [https://www.airbnb.com/users/show/303652112](https://www.airbnb.com/users/show/303652112) | Enattica | 2019-10-21 | Athens, Greece | Handpicked furniture and urban elegance comes first in mind when talking about The Athens Green Suites. This recent renovated and high tech hotel has just come online to upgrade the hospitality experience in Athens, while introducing the real green way of accommodating thanks to it's enviromental friendly practiques.<br>The Athens Green Suites meet the needs of every single traveler through the variety of it's suite types and the wide array in their amenities' catalogue.<br>Located in the histοrical area of Athens, you have straight access to Monastiraki Metro Station (direct line to the Athens International Airport and Central Piraeus Port). Stroll around the pedestrians earby, which are part of the great shopping district in the capital and get lost among the athenian monuments that stand a breath away from this central hotel. | within an hour | 100% | 100% | f | [https://a0.muscache.com/im/pictures/user/bd49c88f-80af-43bf-9964-3a9310674d91.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/bd49c88f-80af-43bf-9964-3a9310674d91.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/bd49c88f-80af-43bf-9964-3a9310674d91.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/bd49c88f-80af-43bf-9964-3a9310674d91.jpg?aki_policy=profile_x_medium) | Plaka | 5 | 5 | ['email', 'phone'] | t | t | Athina, Greece | ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ | | 37.97755 | 23.72874 | Room in aparthotel | Entire home/apt | 3 | | 1 bath | | 3 | [] | $172.00 | 1 | 1125 | 1 | 1 | 1125 | 1125 | 1.0 | 1125.0 | | t | 22 | 52 | 79 | 308 | 2023-12-25 | 1 | 1 | 1 | 2023-12-10 | 2023-12-10 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 1152259 | f | 5 | 2 | 3 | 0 | 1 |
    | **665083132669737868** | [https://www.airbnb.com/rooms/665083132669737868](https://www.airbnb.com/rooms/665083132669737868) | 20231225075512 | 2023-12-25 | city scrape | Condo in Athina · 1 bedroom · 1 bed · 1 bath | | | [https://a0.muscache.com/pictures/miso/Hosting-665083132669737868/original/fccbbbb2-0725-4873-a635-3782b78d3e45.jpeg](https://a0.muscache.com/pictures/miso/Hosting-665083132669737868/original/fccbbbb2-0725-4873-a635-3782b78d3e45.jpeg) | 419174410 | [https://www.airbnb.com/users/show/419174410](https://www.airbnb.com/users/show/419174410) | Sylvia | 2021-08-19 | | | N/A | N/A | N/A | f | [https://a0.muscache.com/im/pictures/user/0d45709a-15f5-4ad2-9cd8-b00129e9b707.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/0d45709a-15f5-4ad2-9cd8-b00129e9b707.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/0d45709a-15f5-4ad2-9cd8-b00129e9b707.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/0d45709a-15f5-4ad2-9cd8-b00129e9b707.jpg?aki_policy=profile_x_medium) | | 2 | 2 | ['email', 'phone'] | t | t | | ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ | | 37.97444 | 23.73195 | Entire condo | Entire home/apt | 2 | | 1 bath | | 1 | [] | $90.00 | 1 | 365 | 1 | 1 | 365 | 365 | 1.0 | 365.0 | | t | 22 | 52 | 75 | 323 | 2023-12-25 | 0 | 0 | 0 | | | | | | | | | | 1658224 | t | 2 | 2 | 0 | 0 | |
    | **24716838** | [https://www.airbnb.com/rooms/24716838](https://www.airbnb.com/rooms/24716838) | 20231225075512 | 2023-12-26 | previous scrape | Rental unit in Athina · ★4.70 · 1 bedroom · 1 bed · 1 bath | | | [https://a0.muscache.com/pictures/54c10409-fb92-4618-8a8f-8558268437b6.jpg](https://a0.muscache.com/pictures/54c10409-fb92-4618-8a8f-8558268437b6.jpg) | 158101640 | [https://www.airbnb.com/users/show/158101640](https://www.airbnb.com/users/show/158101640) | Katerina | 2017-11-09 | Athens, Greece | | N/A | N/A | 0% | f | [https://a0.muscache.com/im/pictures/user/21086f84-8f63-4726-8858-cc2a79ab6232.jpg?aki_policy=profile_small](https://a0.muscache.com/im/pictures/user/21086f84-8f63-4726-8858-cc2a79ab6232.jpg?aki_policy=profile_small) | [https://a0.muscache.com/im/pictures/user/21086f84-8f63-4726-8858-cc2a79ab6232.jpg?aki_policy=profile_x_medium](https://a0.muscache.com/im/pictures/user/21086f84-8f63-4726-8858-cc2a79ab6232.jpg?aki_policy=profile_x_medium) | Ambelokipi | 2 | 2 | ['email', 'phone'] | t | f | | ΑΜΠΕΛΟΚΗΠΟΙ | | 37.99879 | 23.76088 | Entire rental unit | Entire home/apt | 2 | | 1 bath | | 1 | [] | $50.00 | 2 | 40 | 2 | 2 | 40 | 40 | 2.0 | 40.0 | | t | 0 | 0 | 0 | 0 | 2023-12-26 | 40 | 0 | 0 | 2018-08-23 | 2020-02-28 | 4.7 | 4.8 | 4.83 | 4.8 | 4.83 | 4.55 | 4.75 | | f | 1 | 1 | 0 | 0 | 0.61 |


4. In the original dataset, there are five columns that contain no values of any kind: `description`, `neighbourhood_group_cleansed`, `bathrooms`, `bedrooms`, and `calendar_updated`. Due to the dataset's size, it is necessary to remove these completely empty columns to improve data processing efficiency and readability. To achieve this, I first generate a list of indexes corresponding to the empty columns. Then, when writing the new clean CSV file, I skip these columns using the generated list. All scrubbing tasks are done with Python.
    1. generate a list of indexes corresponding to the empty columns
    ```python
    revise = []
    headers = list(data[0].keys())
    mark = True

    for i in headers:
        mark = True
        for j in range(len(data)):
            c = data[j][i]
            if len(str(c)) != 0:
                mark = False
        if mark == True:
            revise.append(headers.index(i))
    ```
    2. skip empty columns when writing the new clean CSV file
    ```python
    f1 = open(filepath1, 'r')
    f2 = open(filepath2, 'w')

    headers = list(data[0].keys())
    indexes = []
    for i in range(0,len(headers)):
        if i not in deletion:
            indexes.append(i)
    headers_ = []
    for j in indexes:
        headers_.append(headers[j])

    r = csv.reader(f1)
    w = csv.writer(f2)
    for k in r:
        w.writerow([k[i] for i in indexes])
    f2.close()
    ```

## Analysis:

1. show exactly two documents from the listings collection in any order
    - Retrieve only 2 documents.
    ```
    db.athens.find().limit(2)
    ```
    **results**
    
            {
                _id: ObjectId('660e409cb1d5d2f5d39bf58e'),
                id: 40042598,
                listing_url: 'https://www.airbnb.com/rooms/40042598',
                scrape_id: 20231225075512,
                last_scraped: 2023-12-26T00:00:00.000Z,
                source: 'previous scrape',
                name: 'Rental unit in Athina · 1 bedroom · 1 bed · 1 shared bath',
                neighborhood_overview: '',
                picture_url: 'https://a0.muscache.com/pictures/fb6d0257-52ec-43b4-b3e4-6f8cb93ab8df.jpg',
                host_id: 158884228,
                host_url: 'https://www.airbnb.com/users/show/158884228',
                host_name: 'Christos',
                host_since: 2017-11-15T00:00:00.000Z,
                host_location: 'Athens, Greece',
                host_about: '',
                host_response_time: 'N/A',
                host_response_rate: 'N/A',
                host_acceptance_rate: 'N/A',
                host_is_superhost: false,
                host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/6146e0dc-7177-43ec-8f55-8b09d375b74d.jpg?aki_policy=profile_small',
                host_picture_url: 'https://a0.muscache.com/im/pictures/user/6146e0dc-7177-43ec-8f55-8b09d375b74d.jpg?aki_policy=profile_x_medium',
                host_neighbourhood: 'Pedion Areos',
                host_listings_count: 1,
                host_total_listings_count: 1,
                host_verifications: "['email', 'phone']",
                host_has_profile_pic: true,
                host_identity_verified: true,
                neighbourhood: '',
                neighbourhood_cleansed: 'ΠΕΔΙΟ ΑΡΕΩΣ',
                latitude: 37.99443,
                longitude: 23.73688,
                property_type: 'Private room in rental unit',
                room_type: 'Private room',
                accommodates: 2,
                bathrooms_text: '1 shared bath',
                beds: 1,
                amenities: [],
                price: '$20.00',
                minimum_nights: 1,
                maximum_nights: 1125,
                minimum_minimum_nights: 1,
                maximum_minimum_nights: 1,
                minimum_maximum_nights: 1125,
                maximum_maximum_nights: 1125,
                minimum_nights_avg_ntm: 1,
                maximum_nights_avg_ntm: 1125,
                has_availability: true,
                availability_30: 0,
                availability_60: 0,
                availability_90: 0,
                availability_365: 0,
                calendar_last_scraped: 2023-12-26T00:00:00.000Z,
                number_of_reviews: 0,
                number_of_reviews_ltm: 0,
                number_of_reviews_l30d: 0,
                first_review: 1970-01-01T00:00:00.000Z,
                last_review: 1970-01-01T00:00:00.000Z,
                review_scores_rating: NaN,
                review_scores_accuracy: NaN,
                review_scores_cleanliness: NaN,
                review_scores_checkin: NaN,
                review_scores_communication: NaN,
                review_scores_location: NaN,
                review_scores_value: NaN,
                license: '',
                instant_bookable: false,
                calculated_host_listings_count: 1,
                calculated_host_listings_count_entire_homes: 0,
                calculated_host_listings_count_private_rooms: 1,
                calculated_host_listings_count_shared_rooms: 0,
                reviews_per_month: ''
            }
            {
                _id: ObjectId('660e409cb1d5d2f5d39bf58f'),
                id: 39069205,
                listing_url: 'https://www.airbnb.com/rooms/39069205',
                scrape_id: 20231225075512,
                last_scraped: 2023-12-26T00:00:00.000Z,
                source: 'previous scrape',
                name: 'Rental unit in Athina · 2 bedrooms · 2 beds · 2 baths',
                neighborhood_overview: 'Is located in one of the hottest spots in Kolonaki  very close to all the hottest leisured spots of Kolonaki.',
                picture_url: 'https://a0.muscache.com/pictures/8965800b-9101-438e-8da0-7e08574a8e3b.jpg',
                host_id: 299446668,
                host_url: 'https://www.airbnb.com/users/show/299446668',
                host_name: 'Nikos',
                host_since: 2019-10-02T00:00:00.000Z,
                host_location: '',
                host_about: '',
                host_response_time: 'within an hour',
                host_response_rate: '100%',
                host_acceptance_rate: '0%',
                host_is_superhost: false,
                host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/62e8de54-3838-4379-9e4d-fa5943e22ae3.jpg?aki_policy=profile_small',
                host_picture_url: 'https://a0.muscache.com/im/pictures/user/62e8de54-3838-4379-9e4d-fa5943e22ae3.jpg?aki_policy=profile_x_medium',
                host_neighbourhood: 'Kolonaki',
                host_listings_count: 1,
                host_total_listings_count: 2,
                host_verifications: "['email', 'phone']",
                host_has_profile_pic: true,
                host_identity_verified: true,
                neighbourhood: 'Athina, Greece',
                neighbourhood_cleansed: 'ΚΟΛΩΝΑΚΙ',
                latitude: 37.97919,
                longitude: 23.74532,
                property_type: 'Entire rental unit',
                room_type: 'Entire home/apt',
                accommodates: 4,
                bathrooms_text: '2 baths',
                beds: 2,
                amenities: [],
                price: '$293.00',
                minimum_nights: 2,
                maximum_nights: 10,
                minimum_minimum_nights: 2,
                maximum_minimum_nights: 2,
                minimum_maximum_nights: 10,
                maximum_maximum_nights: 10,
                minimum_nights_avg_ntm: 2,
                maximum_nights_avg_ntm: 10,
                has_availability: true,
                availability_30: 23,
                availability_60: 53,
                availability_90: 83,
                availability_365: 173,
                calendar_last_scraped: 2023-12-26T00:00:00.000Z,
                number_of_reviews: 0,
                number_of_reviews_ltm: 0,
                number_of_reviews_l30d: 0,
                first_review: 1970-01-01T00:00:00.000Z,
                last_review: 1970-01-01T00:00:00.000Z,
                review_scores_rating: NaN,
                review_scores_accuracy: NaN,
                review_scores_cleanliness: NaN,
                review_scores_checkin: NaN,
                review_scores_communication: NaN,
                review_scores_location: NaN,
                review_scores_value: NaN,
                license: '',
                instant_bookable: false,
                calculated_host_listings_count: 1,
                calculated_host_listings_count_entire_homes: 1,
                calculated_host_listings_count_private_rooms: 0,
                calculated_host_listings_count_shared_rooms: 0,
                reviews_per_month: ''
            }


2. show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function.
    - Retrieve 10 documents, and use pretty() to prettyprint (prettyprinting is by default in this version).

    ```
    db.athens.find().limit(10).pretty()
    ```
    **results**

            {
                _id: ObjectId('660e409cb1d5d2f5d39bf58e'),
                id: 40042598,
                listing_url: 'https://www.airbnb.com/rooms/40042598',
                scrape_id: 20231225075512,
                last_scraped: 2023-12-26T00:00:00.000Z,
                source: 'previous scrape',
                name: 'Rental unit in Athina · 1 bedroom · 1 bed · 1 shared bath',
                neighborhood_overview: '',
                picture_url: 'https://a0.muscache.com/pictures/fb6d0257-52ec-43b4-b3e4-6f8cb93ab8df.jpg',
                host_id: 158884228,
                host_url: 'https://www.airbnb.com/users/show/158884228',
                host_name: 'Christos',
                host_since: 2017-11-15T00:00:00.000Z,
                host_location: 'Athens, Greece',
                host_about: '',
                host_response_time: 'N/A',
                host_response_rate: 'N/A',
                host_acceptance_rate: 'N/A',
                host_is_superhost: false,
                host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/6146e0dc-7177-43ec-8f55-8b09d375b74d.jpg?aki_policy=profile_small',
                host_picture_url: 'https://a0.muscache.com/im/pictures/user/6146e0dc-7177-43ec-8f55-8b09d375b74d.jpg?aki_policy=profile_x_medium',
                host_neighbourhood: 'Pedion Areos',
                host_listings_count: 1,
                host_total_listings_count: 1,
                host_verifications: "['email', 'phone']",
                host_has_profile_pic: true,
                host_identity_verified: true,
                neighbourhood: '',
                neighbourhood_cleansed: 'ΠΕΔΙΟ ΑΡΕΩΣ',
                latitude: 37.99443,
                longitude: 23.73688,
                property_type: 'Private room in rental unit',
                room_type: 'Private room',
                accommodates: 2,
                bathrooms_text: '1 shared bath',
                beds: 1,
                amenities: [],
                price: '$20.00',
                minimum_nights: 1,
                maximum_nights: 1125,
                minimum_minimum_nights: 1,
                maximum_minimum_nights: 1,
                minimum_maximum_nights: 1125,
                maximum_maximum_nights: 1125,
                minimum_nights_avg_ntm: 1,
                maximum_nights_avg_ntm: 1125,
                has_availability: true,
                availability_30: 0,
                availability_60: 0,
                availability_90: 0,
                availability_365: 0,
                calendar_last_scraped: 2023-12-26T00:00:00.000Z,
                number_of_reviews: 0,
                number_of_reviews_ltm: 0,
                number_of_reviews_l30d: 0,
                first_review: 1970-01-01T00:00:00.000Z,
                last_review: 1970-01-01T00:00:00.000Z,
                review_scores_rating: NaN,
                review_scores_accuracy: NaN,
                review_scores_cleanliness: NaN,
                review_scores_checkin: NaN,
                review_scores_communication: NaN,
                review_scores_location: NaN,
                review_scores_value: NaN,
                license: '',
                instant_bookable: false,
                calculated_host_listings_count: 1,
                calculated_host_listings_count_entire_homes: 0,
                calculated_host_listings_count_private_rooms: 1,
                calculated_host_listings_count_shared_rooms: 0,
                reviews_per_month: ''
            }
            {
                _id: ObjectId('660e409cb1d5d2f5d39bf58f'),
                id: 39069205,
                listing_url: 'https://www.airbnb.com/rooms/39069205',
                scrape_id: 20231225075512,
                last_scraped: 2023-12-26T00:00:00.000Z,
                source: 'previous scrape',
                name: 'Rental unit in Athina · 2 bedrooms · 2 beds · 2 baths',
                neighborhood_overview: 'Is located in one of the hottest spots in Kolonaki  very close to all the hottest leisured spots of Kolonaki.',
                picture_url: 'https://a0.muscache.com/pictures/8965800b-9101-438e-8da0-7e08574a8e3b.jpg',
                host_id: 299446668,
                host_url: 'https://www.airbnb.com/users/show/299446668',
                host_name: 'Nikos',
                host_since: 2019-10-02T00:00:00.000Z,
                host_location: '',
                host_about: '',
                host_response_time: 'within an hour',
                host_response_rate: '100%',
                host_acceptance_rate: '0%',
                host_is_superhost: false,
                host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/62e8de54-3838-4379-9e4d-fa5943e22ae3.jpg?aki_policy=profile_small',
                host_picture_url: 'https://a0.muscache.com/im/pictures/user/62e8de54-3838-4379-9e4d-fa5943e22ae3.jpg?aki_policy=profile_x_medium',
                host_neighbourhood: 'Kolonaki',
                host_listings_count: 1,
                host_total_listings_count: 2,
                host_verifications: "['email', 'phone']",
                host_has_profile_pic: true,
                host_identity_verified: true,
                neighbourhood: 'Athina, Greece',
                neighbourhood_cleansed: 'ΚΟΛΩΝΑΚΙ',
                latitude: 37.97919,
                longitude: 23.74532,
                property_type: 'Entire rental unit',
                room_type: 'Entire home/apt',
                accommodates: 4,
                bathrooms_text: '2 baths',
                beds: 2,
                amenities: [],
                price: '$293.00',
                minimum_nights: 2,
                maximum_nights: 10,
                minimum_minimum_nights: 2,
                maximum_minimum_nights: 2,
                minimum_maximum_nights: 10,
                maximum_maximum_nights: 10,
                minimum_nights_avg_ntm: 2,
                maximum_nights_avg_ntm: 10,
                has_availability: true,
                availability_30: 23,
                availability_60: 53,
                availability_90: 83,
                availability_365: 173,
                calendar_last_scraped: 2023-12-26T00:00:00.000Z,
                number_of_reviews: 0,
                number_of_reviews_ltm: 0,
                number_of_reviews_l30d: 0,
                first_review: 1970-01-01T00:00:00.000Z,
                last_review: 1970-01-01T00:00:00.000Z,
                review_scores_rating: NaN,
                review_scores_accuracy: NaN,
                review_scores_cleanliness: NaN,
                review_scores_checkin: NaN,
                review_scores_communication: NaN,
                review_scores_location: NaN,
                review_scores_value: NaN,
                license: '',
                instant_bookable: false,
                calculated_host_listings_count: 1,
                calculated_host_listings_count_entire_homes: 1,
                calculated_host_listings_count_private_rooms: 0,
                calculated_host_listings_count_shared_rooms: 0,
                reviews_per_month: ''
            }
            {
                _id: ObjectId('660e409cb1d5d2f5d39bf590'),
                id: 653274914834812500,
                listing_url: 'https://www.airbnb.com/rooms/653274914834812593',
                scrape_id: 20231225075512,
                last_scraped: 2023-12-26T00:00:00.000Z,
                source: 'city scrape',
                name: 'Condo in Athina · ★5.0 · 1 bedroom · 2 beds · 1 bath',
                neighborhood_overview: 'Η γειτονιά βρίσκεται μια ανάσα από τον Παρθενώνα,το μουσείο της Ακρόπολης  ,την Πλάκα και το ιστορικό κέντρο της Αθήνας<br /><br />The neighbourhood is locaded a breath away from the Parthenon, the Actopolis Museum, Plaka and the historic city centre',
                picture_url: 'https://a0.muscache.com/pictures/b8926124-f861-45f8-9203-917cd0d2b9f1.jpg',
                host_id: 272702874,
                host_url: 'https://www.airbnb.com/users/show/272702874',
                host_name: 'Costas',
                host_since: 2019-07-01T00:00:00.000Z,
                host_location: 'Athens, Greece',
                host_about: '',
                host_response_time: 'within an hour',
                host_response_rate: '100%',
                host_acceptance_rate: '96%',
                host_is_superhost: true,
                host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/User-272702874/original/cf81a259-c3f4-4a57-9798-3b96b851fa02.jpeg?aki_policy=profile_small',
                host_picture_url: 'https://a0.muscache.com/im/pictures/user/User-272702874/original/cf81a259-c3f4-4a57-9798-3b96b851fa02.jpeg?aki_policy=profile_x_medium',
                host_neighbourhood: '',
                host_listings_count: 1,
                host_total_listings_count: 1,
                host_verifications: "['email', 'phone']",
                host_has_profile_pic: true,
                host_identity_verified: true,
                neighbourhood: 'Athina, Greece',
                neighbourhood_cleansed: 'ΚΟΥΚΑΚΙ-ΜΑΚΡΥΓΙΑΝΝΗ',
                latitude: 37.966,
                longitude: 23.72717,
                property_type: 'Entire condo',
                room_type: 'Entire home/apt',
                accommodates: 3,
                bathrooms_text: '1 bath',
                beds: 2,
                amenities: [],
                price: '$60.00',
                minimum_nights: 1,
                maximum_nights: 365,
                minimum_minimum_nights: 1,
                maximum_minimum_nights: 1,
                minimum_maximum_nights: 1125,
                maximum_maximum_nights: 1125,
                minimum_nights_avg_ntm: 1,
                maximum_nights_avg_ntm: 1125,
                has_availability: true,
                availability_30: 23,
                availability_60: 53,
                availability_90: 83,
                availability_365: 263,
                calendar_last_scraped: 2023-12-26T00:00:00.000Z,
                number_of_reviews: 47,
                number_of_reviews_ltm: 37,
                number_of_reviews_l30d: 0,
                first_review: 2022-07-19T00:00:00.000Z,
                last_review: 2023-11-15T00:00:00.000Z,
                review_scores_rating: 5,
                review_scores_accuracy: 5,
                review_scores_cleanliness: 5,
                review_scores_checkin: 4.96,
                review_scores_communication: 5,
                review_scores_location: 4.98,
                review_scores_value: 4.96,
                license: 1652202,
                instant_bookable: true,
                calculated_host_listings_count: 1,
                calculated_host_listings_count_entire_homes: 1,
                calculated_host_listings_count_private_rooms: 0,
                calculated_host_listings_count_shared_rooms: 0,
                reviews_per_month: 2.68
            }

3. choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts
    - Retrieve documents associated with two superhosts (`272702874` and `220064887`), guaranteed by the two criteria using the `$or` operator
    - Include only the requested fields (`name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost`) in the results, enabled by the projection that specifies the fields to be included and explicitly disables the `_id` field.

    ```
    db.athens.find({$or: [{host_id: 272702874},{host_id: 220064887}]}, { _id: 0, host_id: 1, name: 1, price: 1, neighbourhood: 1, host_name: 1, host_is_superhost: 1 })
    ```
    **results**

            {
                name: 'Condo in Athina · ★5.0 · 1 bedroom · 2 beds · 1 bath',
                host_id: 272702874,
                host_name: 'Costas',
                host_is_superhost: true,
                neighbourhood: 'Athina, Greece',
                price: '$60.00'
            }
            {
                name: 'Rental unit in Athina · ★5.0 · 1 bedroom · 1 bed · 1 bath',
                host_id: 220064887,
                host_name: 'Alexandros',
                host_is_superhost: true,
                neighbourhood: 'Athina, Greece',
                price: '$45.00'
            }
            {
                name: 'Condo in Athina · ★4.93 · 2 bedrooms · 3 beds · 1 bath',
                host_id: 220064887,
                host_name: 'Alexandros',
                host_is_superhost: true,
                price: '$53.00'
            }
    
    **insight**

    Listings by superhosts tend to have exceptionally high review scores, which is the reasons why these hosts are considered as such.

4. find all the unique host_name values
    - Finds the distinct values for `host_name` across the collection using `distinct`.

    ```
    db.athens.distinct("host_name")
    ```
    **results**

            [
                '1915 Team',
                'A',
                'A. Tony &',
                'A77',
                "AIKATERINI'S Place, ATHENS",
                'Abdelssatar',
                'Abdo',
                'Academia BnB',
                'Achilleas',
                'Acropolis Magenta',
                'Acropolis Museum',
                'Acropolis Suites And Tours',
                'Ada',
                'Adam',
                'Adam & Christina',
                'Adamantia',
                'Adelina',
                'Adelos',
                'Adi',
                'Adib',
                'Adiola',
                'Adnan',
                'Adone',
                'Adonis',
                'Adrian',
                'Adriana',
                'Adrienn',
                'Advance Helix Development',
                'Aemilia',
                'Afrodite',
                'Afroditi',
                'Agamemnon',
                'Agathi',
                'Ageliki',
                'Aggeliki',
                'Aggelos',
                'Aggie’s',
                'Agis',
                'Agni',
                'Agnieszka',
                'Ah',
                'Ahmad',
                'Aida',
                'Aikaterini',
                'Aimei',
                'Aimilios',
                'Ainta',
                'Airio',
                'Airnite',
                'Akan',
                'Akhmet',
                'Akis',
                'Akis & Marietta',
                'Akrivi',
                'Al.Ke',
                'Ala',
                'Alain',
                'Alberto',
                'Albi',
                'Alda',
                'Alejandro',
                'Aleksander',
                'Aleksandra',
                'Alessandra',
                'Alessia',
                'Alex',
                'Alexa',
                'Alexander',
                'Alexandra',
                'Alexandra L',
                'Alexandre',
                'Alexandros',
                'Alexandros & Valia',
                'Alexandros-Emmanouil',
                'Alexi',
                'Alexia',
                'Alexios',
                'Alexis',
                'Alexis And Anastasia',
                'Alfiarios',
                'Alfred',
                'Aliang',
                'Aliki',
                'Alis,Yannis,Mimis',
                'Alister',
                'Alix And Georges',
                'Alkis',
                'Alkistis',
                'Alma',
                'Almi',
                'Altanay',
                'Amalia',
                'Amanda',
                'Amantin - Panos',
                'Amelie',
                'Amid',
                'Amir',
                'Ana',
                'Ana Maria',
                'Anabel',
                ... 2473 more items
            ]

    **insight**

    Some names are not human names but rather business names or addresses, indicating that some Airbnb listings are managed by companies or organizations.

5. find all of the places that have more than 2 beds in Athens, Attika, Greece (referred to as the neighborhood field in the data file, as neighbourhood_group_cleansed contains none in this dataset), ordered by review_scores_rating descending
    - Retrieve documents meeting the two criteria simultaneously, ensuring they have more than 2 beds in Athens, Attika, Greece, using the `$and` operator and the `$gt` operator for the number of beds.
    - Include only the requested fields (`name`, `beds`, `review_scores_rating`, and `price`) in the results, enabled by the projection that specifies the fields to be included and explicitly disables the `_id` field.
    - Maintain descending order using the `sort` function, which sorts by the `review_scores_rating` field.

    ```
    db.athens.find({$and:[{beds: {$gt: 2, }},{neighbourhood: 'Athens, Greece'}]}, { _id: 0, name: 1, beds: 1, review_scores_rating: 1, price: 1 }).sort({ review_scores_rating: -1 })
    ```
    **results**

            {
                name: 'Rental unit in Athens · 1 bedroom · 6 beds · 2 shared baths',
                beds: 6,
                price: '$12.00',
                review_scores_rating: 5
            }
            {
                name: 'Rental unit in Athens · ★5.0 · 1 bedroom · 6 beds · 2 shared baths',
                beds: 6,
                price: '$12.00',
                review_scores_rating: 5
            }
            {
                name: 'Rental unit in Athens · ★5.0 · 2 bedrooms · 3 beds · 2 baths',
                beds: 3,
                price: '$171.00',
                review_scores_rating: 5
            }

    **insight**

    Through the name, one can observe how the ratio between the number of bedrooms and the number of beds significantly influences the price. For example, having 6 beds in a rental unit with only 1 bedroom indicates potentially poorer living conditions compared to 3 beds in a unit with 2 bedrooms.

6. show the number of listings per host
    - Use the `$group` stage to separate documents into groups based on the `host_id` field.
    - Then use the `$count` stage to count the documents.

    ```
    db.athens.aggregate({$group: {_id: "$host_id",count: {$count: { } }}})
    ```
    **results**

            {
                _id: 54669323,
                count: 1
            }
            {
                _id: 464172971,
                count: 1
            }
            {
                _id: 86859429,
                count: 1
            }

    **insight**

    Many hosts can only manage one Airbnb listing, while there are a few who are responsible for more than one, or even ten units. These are highly likely to be managed by companies or organizations.

7. find the average review_scores_rating per neighborhood, and only show those that are 4 or above, sorted in descending order of rating 
    - Use the `$group` stage to separate documents into groups based on the `host_id` field..
    - Utilize `$avg` to compute the average rating for each group
    - Next, use `$match` to filter out all documents in groups that have an average rating below 4.
    - Finally, use `$sort` to maintain a descending order of average ratings for each group.

    ```
    db.athens.aggregate([{$group: {_id: "$neighbourhood", avgRating: {$avg: "$review_scores_rating"}}},{$match: {avgRating: {$gte: 4}}},{$sort: {avgRating: -1}}])
    ```
   **results**

        {
            _id: 'Athina, England, Greece',
            avgRating: 5
        }
        {
            _id: 'Athens, Victoria Square, Greece',
            avgRating: 5
        }
        {
            _id: 'Athina, Kato Patisia, Greece',
            avgRating: 5
        }

    **insight**

    From the average rating and the list sorted in descending order, one can assume that the neighborhoods at the top of the list will be the most recommended places for travelers to stay in.
