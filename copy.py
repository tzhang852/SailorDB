mysql> select CA.country_a_name, CB.country_b_name from countrya CA left join countryb CB on CA.country_a_id = CB.country_b_id where CB.country_b_population < 80000000 limit 20;  
+--------------------------+----------------------------+
| country_a_name           | country_b_name             |
+--------------------------+----------------------------+
| Canada                   | Gambia                     |
| Palestine                | Cabo Verde                 |
| Albania                  | Sudan South                |
| Netherlands              | Lao People's Dem. Republic |
| Iraq                     | Guyana                     |
| Timor-Leste              | Malaysia                   |
| Congo                    | Micronesia                 |
| Serbia                   | Kosovo                     |
| Myanmar                  | Namibia                    |
| Armenia                  | Central African Republic   |
| Gambia                   | Cabo Verde                 |
| Armenia                  | Armenia                    |
| Barbados                 | Nigeria                    |
| Singapore                | Spain                      |
| Gabon                    | Equatorial Guinea          |
| Jamaica                  | Brunei Darussalam          |
| Turkmenistan             | Trinidad and Tobago        |
| Turkey                   | Guyana                     |
| Angola                   | Switzerland                |
| United States of America | Madagascar                 |
+--------------------------+----------------------------+
20 rows in set (0.05 sec)

mysql> select E.country_a_name, count(RM.raw_material_id) from  rawmaterial RM left join exportsto E on E.raw_material_id = RM.raw_material_id group by RM.raw_material_name limit 20;             
+----------------------------+---------------------------+
| country_a_name             | count(RM.raw_material_id) |
+----------------------------+---------------------------+
| Egypt                      |                        20 |
| Argentina                  |                        32 |
| Honduras                   |                        20 |
| Greece                     |                        24 |
| Japan                      |                        28 |
| Malaysia                   |                        16 |
| Bosnia and Herzegovina     |                        22 |
| Afghanistan                |                        22 |
| Lao People's Dem. Republic |                        28 |
| Bosnia and Herzegovina     |                        30 |
| Palestine                  |                        27 |
| Mauritania                 |                        30 |
| Serbia                     |                        31 |
| Nigeria                    |                        18 |
| Angola                     |                        33 |
| Jordan                     |                        31 |
| Austria                    |                        23 |
| Mexico                     |                        33 |
| South Africa               |                        23 |
| Sao Tome and Principe      |                        24 |
+----------------------------+---------------------------+
20 rows in set (0.08 sec)

mysql> select IM.country_b_name, IM.raw_material_name from importedby IM group by IM.transportation having IM.transportation = 'muscle car';          
+----------------+-------------------+
| country_b_name | raw_material_name |
+----------------+-------------------+
| Puerto Rico    | rocks             |
+----------------+-------------------+
1 row in set (0.01 sec)

Starting up Assignment5...
Original:  (10001, 'Canada', 24512641)
Insert New:  (10001, 'Canada', 24512641)
Insert New:  (99999, 'Canada', 24512641)
Original:  (10001, 'Canada', 24512641)
Original:  (99999, 'Canada', 24512641)
Update New:  (10001, 'Canada', 24512641)
Update New:  (99999, 'Brazil', 24512641)
Original:  (10001, 'Canada', 24512641)
Original:  (99999, 'Brazil', 24512641)
Update New:  (10001, 'United States of America', 24512641)
Update New:  (99999, 'United States of America', 24512641)