/* this file contains a single entry for each field to ensure testing of the DB and will wipe all five collections upon running */
/* DELETE FROM main_app_client;
DELETE FROM main_app_motorcycle;
DELETE FROM main_app_part
DELETE FROM main_app_record
DELETE FROM main_app_tech */

/* Motorcycles */

INSERT INTO main_app_motorcycle(make,model,dom,vin,mileage,img,created_at,color,owner_id) 
    VALUES
        ('Ducati', '748s', '06/2002', 'ZDM1SB3R92B011742', 31788, 'https://i.imgur.com/aJwyI3s.jpg', '1984-09-22T05:19:05.939Z','grey',1 );

INSERT INTO main_app_motorcycle(make,model,dom,vin,mileage,img,created_at,color,owner_id) 
    VALUES
        ('Ducati', '749d', '05/2005', 'ZDM1UB3S35B009583', 17845, 'https://i.imgur.com/QDbvPiO.jpg', '1988-09-27T05:19:05.939Z','red',4 );

INSERT INTO main_app_motorcycle(make,model,dom,vin,mileage,img,created_at,color,owner_id) 
    VALUES
        ('Ducati', '750 Super Sport', '07/1992', 'DM750SCSXNB001025', 33495, 'https://i.imgur.com/jG6QziK.jpg', '1990-09-27T05:19:05.939Z','red',3 );

/* Records */

INSERT INTO main_app_record(mileage, description, created_at, motorcycle_id, tech_id, part_id)
    VALUES
        (18000, 'major serivce including valve adjustment', '2019-11-30T05:19:05.939Z', 3, 2,4 );

/* Parts */

INSERT INTO main_app_part(part_number, description)
    VALUES
        ("0", "Use this number if no parts where used in this repair" );