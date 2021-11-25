/* this file contains a single entry for each field to ensure testing of the DB and will wipe all five collections upon running */
/* DELETE FROM main_app_client;
DELETE FROM main_app_motorcycle;
DELETE FROM main_app_part
DELETE FROM main_app_record
DELETE FROM main_app_tech */

INSERT INTO main_app_motorcycle(make,model,dom,vin,mileage,img,created_at,color,owner_id) 
    VALUES
        ('Ducati', '748s', '06/2002', 'ZDM1SB3R92B011742', 31788, 'https://i.imgur.com/aJwyI3s.jpg', '1984-09-22T05:19:05.939Z','grey',1 );


