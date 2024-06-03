from django import forms
from .utils import year_validator, mileage_validator

marks = (("BMW", 'BMW'), ("Indian", 'Indian'), ("Harley-Davidson", 'Harley-Davidson'), ("Ducati", 'Ducati'),
         ("Honda", 'Honda'), ("Kawasaki", 'Kawasaki'), ("KTM", 'KTM'), ("Suzuki", 'Suzuki'), ("Yamaha", 'Yamaha'))

models = {'Kawasaki': (('250 TR', '250 TR'),
  ('BJ250 Estrella', 'BJ250 Estrella'),
  ('D-tracker 250', 'D-tracker 250'),
  ('EL125 Eliminator', 'EL125 Eliminator'),
  ('EL250 Eliminator', 'EL250 Eliminator'),
  ('EN400 Vulcan', 'EN400 Vulcan'),
  ('EN500 Vulcan', 'EN500 Vulcan'),
  ('EN650 Vulcan S', 'EN650 Vulcan S'),
  ('ER-4f (Ninja 400R)', 'ER-4f (Ninja 400R)'),
  ('ER-4n', 'ER-4n'),
  ('ER-5', 'ER-5'),
  ('ER-6f (Ninja 650R)', 'ER-6f (Ninja 650R)'),
  ('ER-6n', 'ER-6n'),
  ('EX-4', 'EX-4'),
  ('GPX 250', 'GPX 250'),
  ('GPZ 1000', 'GPZ 1000'),
  ('GPZ 400', 'GPZ 400'),
  ('GPZ 500', 'GPZ 500'),
  ('GTR 1000 (ZG1000 Concours)', 'GTR 1000 (ZG1000 Concours)'),
  ('GTR 1400 (Concours 14)', 'GTR 1400 (Concours 14)'),
  ('KDX 125', 'KDX 125'),
  ('KDX 200', 'KDX 200'),
  ('KDX 220', 'KDX 220'),
  ('KDX 250', 'KDX 250'),
  ('KL 250', 'KL 250'),
  ('KLE 250', 'KLE 250'),
  ('KLE 400', 'KLE 400'),
  ('KLE 500', 'KLE 500'),
  ('KLR 250', 'KLR 250'),
  ('KLR 650', 'KLR 650'),
  ('KLX 110', 'KLX 110'),
  ('KLX 125', 'KLX 125'),
  ('KLX 150', 'KLX 150'),
  ('KLX 230', 'KLX 230'),
  ('KLX 250', 'KLX 250'),
  ('KLX 450', 'KLX 450'),
  ('KSR 110', 'KSR 110'),
  ('KX 250', 'KX 250'),
  ('KX 450', 'KX 450'),
  ('KX 65', 'KX 65'),
  ('KX 85', 'KX 85'),
  ('Ninja 1000', 'Ninja 1000'),
  ('Ninja 1000 SX (2020-н.в.)', 'Ninja 1000 SX (2020-н.в.)'),
  ('Ninja 250R', 'Ninja 250R'),
  ('Ninja 250SL', 'Ninja 250SL'),
  ('Ninja 300', 'Ninja 300'),
  ('Ninja 400', 'Ninja 400'),
  ('Ninja 650', 'Ninja 650'),
  ('Ninja H2 SX', 'Ninja H2 SX'),
  ('VN1500 Vulcan', 'VN1500 Vulcan'),
  ('VN1600 Vulcan', 'VN1600 Vulcan'),
  ('VN1700 Vulcan', 'VN1700 Vulcan'),
  ('VN2000 Vulcan', 'VN2000 Vulcan'),
  ('VN400 Vulcan', 'VN400 Vulcan'),
  ('VN800 Vulcan', 'VN800 Vulcan'),
  ('VN900 Vulcan', 'VN900 Vulcan'),
  ('Versys 1000', 'Versys 1000'),
  ('Versys 650', 'Versys 650'),
  ('Versys-X 300', 'Versys-X 300'),
  ('W 400', 'W 400'),
  ('W 650', 'W 650'),
  ('W 800', 'W 800'),
  ('Z 1000', 'Z 1000'),
  ('Z 1000SX', 'Z 1000SX'),
  ('Z 125', 'Z 125'),
  ('Z 250', 'Z 250'),
  ('Z 250 SL', 'Z 250 SL'),
  ('Z 300', 'Z 300'),
  ('Z 400', 'Z 400'),
  ('Z 650', 'Z 650'),
  ('Z 650RS', 'Z 650RS'),
  ('Z 750', 'Z 750'),
  ('Z 800', 'Z 800'),
  ('Z 900', 'Z 900'),
  ('Z 900RS', 'Z 900RS'),
  ('Z H2', 'Z H2'),
  ('ZG1200 Voyager', 'ZG1200 Voyager'),
  ('ZL1000 Eliminator', 'ZL1000 Eliminator'),
  ('ZR 1100 Zephyr', 'ZR 1100 Zephyr'),
  ('ZR 400 Zephyr', 'ZR 400 Zephyr'),
  ('ZR 550 Zephyr', 'ZR 550 Zephyr'),
  ('ZR 750 Zephyr', 'ZR 750 Zephyr'),
  ('ZR-7', 'ZR-7'),
  ('ZRX 1100', 'ZRX 1100'),
  ('ZRX 1200', 'ZRX 1200'),
  ('ZX-10 Ninja', 'ZX-10 Ninja'),
  ('ZX-12 Ninja', 'ZX-12 Ninja'),
  ('ZX-6 Ninja', 'ZX-6 Ninja'),
  ('ZX-9 Ninja', 'ZX-9 Ninja'),
  ('ZX1400C', 'ZX1400C'),
  ('ZXR 250', 'ZXR 250'),
  ('ZXR 400', 'ZXR 400'),
  ('ZZR 1100', 'ZZR 1100'),
  ('ZZR 1200', 'ZZR 1200'),
  ('ZZR 1400', 'ZZR 1400'),
  ('ZZR 250', 'ZZR 250'),
  ('ZZR 400', 'ZZR 400'),
  ('ZZR 600', 'ZZR 600')),
 'Yamaha': (('BT1100 Bulldog', 'BT1100 Bulldog'),
  ('DT125', 'DT125'),
  ('DT230 Lanza', 'DT230 Lanza'),
  ('FJR1300', 'FJR1300'),
  ('FZ1', 'FZ1'),
  ('FZ16', 'FZ16'),
  ('FZ25 Fazer', 'FZ25 Fazer'),
  ('FZ400', 'FZ400'),
  ('FZ6', 'FZ6'),
  ('FZ8', 'FZ8'),
  ('FZR1000', 'FZR1000'),
  ('FZS1000 Fazer', 'FZS1000 Fazer'),
  ('FZS600 Fazer', 'FZS600 Fazer'),
  ('FZX750', 'FZX750'),
  ('GTS1000', 'GTS1000'),
  ('MR50', 'MR50'),
  ('MT-01', 'MT-01'),
  ('MT-03', 'MT-03'),
  ('MT-07 (FZ-07)', 'MT-07 (FZ-07)'),
  ('MT-09 (FZ-09)', 'MT-09 (FZ-09)'),
  ('MT-09 Tracer (FJ-09)', 'MT-09 Tracer (FJ-09)'),
  ('MT-10', 'MT-10'),
  ('MT-25', 'MT-25'),
  ('Niken', 'Niken'),
  ('PW50/PW80', 'PW50/PW80'),
  ('SCR950', 'SCR950'),
  ('SR400', 'SR400'),
  ('SR500', 'SR500'),
  ('SRX400', 'SRX400'),
  ('SRX600', 'SRX600'),
  ('TDM850', 'TDM850'),
  ('TDM900', 'TDM900'),
  ('TT-R110', 'TT-R110'),
  ('TT-R125', 'TT-R125'),
  ('TT-R250', 'TT-R250'),
  ('TT250R', 'TT250R'),
  ('TW200', 'TW200'),
  ('TW225', 'TW225'),
  ('TZR250', 'TZR250'),
  ('Tenere 700', 'Tenere 700'),
  ('Tracer 700', 'Tracer 700'),
  ('VMAX 1200', 'VMAX 1200'),
  ('VMAX 1700', 'VMAX 1700'),
  ('WR250F', 'WR250F'),
  ('WR250R', 'WR250R'),
  ('WR250X', 'WR250X'),
  ('WR400F', 'WR400F'),
  ('WR426F', 'WR426F'),
  ('WR450F', 'WR450F'),
  ('XG250 Tricker', 'XG250 Tricker'),
  ('XJ6 (FZ6R)', 'XJ6 (FZ6R)'),
  ('XJ600', 'XJ600'),
  ('XJ900', 'XJ900'),
  ('XJR1200', 'XJR1200'),
  ('XJR1300', 'XJR1300'),
  ('XJR400', 'XJR400'),
  ('XS1100', 'XS1100'),
  ('XSR700', 'XSR700'),
  ('XSR900', 'XSR900'),
  ('XT1200Z Super Tenere', 'XT1200Z Super Tenere'),
  ('XT225 Serow', 'XT225 Serow'),
  ('XT250 Serow', 'XT250 Serow'),
  ('XT250X', 'XT250X'),
  ('XT400', 'XT400'),
  ('XT600', 'XT600'),
  ('XT660R', 'XT660R'),
  ('XT660X', 'XT660X'),
  ('XT660Z Tenere', 'XT660Z Tenere'),
  ('XTZ660 Tenere', 'XTZ660 Tenere'),
  ('XTZ750 Super Tenere', 'XTZ750 Super Tenere'),
  ('XV 1600 Wild Star', 'XV 1600 Wild Star'),
  ('XV 1700 Warrior', 'XV 1700 Warrior'),
  ('XV 1700A Road Star', 'XV 1700A Road Star'),
  ('XV 1900', 'XV 1900'),
  ('XV1100 Virago', 'XV1100 Virago'),
  ('XV400 Virago', 'XV400 Virago'),
  ('XV535 Virago', 'XV535 Virago'),
  ('XV750 Virago', 'XV750 Virago'),
  ('XV950 Bolt', 'XV950 Bolt'),
  ('XVS1100', 'XVS1100'),
  ('XVS1300', 'XVS1300'),
  ('XVS400 Drag Star', 'XVS400 Drag Star'),
  ('XVS650', 'XVS650'),
  ('XVS950', 'XVS950'),
  ('XVZ 1300', 'XVZ 1300'),
  ('YBR125', 'YBR125'),
  ('YBR250', 'YBR250'),
  ('YS125 Fazer', 'YS125 Fazer'),
  ('YS250 Fazer', 'YS250 Fazer'),
  ('YZ125', 'YZ125'),
  ('YZ250', 'YZ250'),
  ('YZ250F', 'YZ250F'),
  ('YZ450F', 'YZ450F'),
  ('YZ65', 'YZ65'),
  ('YZ85', 'YZ85'),
  ('YZF-R1', 'YZF-R1'),
  ('YZF-R125', 'YZF-R125'),
  ('YZF-R15', 'YZF-R15'),
  ('YZF-R25', 'YZF-R25'),
  ('YZF-R3', 'YZF-R3'),
  ('YZF-R6', 'YZF-R6'),
  ('YZF-R7', 'YZF-R7'),
  ('YZF1000R Thunderace', 'YZF1000R Thunderace'),
  ('YZF600R Thundercat', 'YZF600R Thundercat'),
  ('YZF750', 'YZF750')),
 'Suzuki': (('250 SB', '250 SB'),
  ('B-King', 'B-King'),
  ('Bandit GSF 1200', 'Bandit GSF 1200'),
  ('Bandit GSF 1250', 'Bandit GSF 1250'),
  ('Bandit GSF 250', 'Bandit GSF 250'),
  ('Bandit GSF 400', 'Bandit GSF 400'),
  ('Bandit GSF 600', 'Bandit GSF 600'),
  ('Bandit GSF 650', 'Bandit GSF 650'),
  ('Boulevard 400', 'Boulevard 400'),
  ('Boulevard C109R', 'Boulevard C109R'),
  ('Boulevard C50', 'Boulevard C50'),
  ('Boulevard C90', 'Boulevard C90'),
  ('Boulevard M109R', 'Boulevard M109R'),
  ('Boulevard M50', 'Boulevard M50'),
  ('Boulevard M90', 'Boulevard M90'),
  ('Boulevard S50', 'Boulevard S50'),
  ('DF 200', 'DF 200'),
  ('DR 250', 'DR 250'),
  ('DR 650 R/RS', 'DR 650 R/RS'),
  ('DR 650 SE', 'DR 650 SE'),
  ('DR 800 Big', 'DR 800 Big'),
  ('DR-Z 400', 'DR-Z 400'),
  ('DR-Z 400 SM', 'DR-Z 400 SM'),
  ('DR-Z 70', 'DR-Z 70'),
  ('Desperado VZ400', 'Desperado VZ400'),
  ('Djebel 200 (DR 200 SE)', 'Djebel 200 (DR 200 SE)'),
  ('Djebel 250', 'Djebel 250'),
  ('GN 125', 'GN 125'),
  ('GS 500', 'GS 500'),
  ('GS 750', 'GS 750'),
  ('GS 850', 'GS 850'),
  ('GSR 400', 'GSR 400'),
  ('GSR 600', 'GSR 600'),
  ('GSR 750', 'GSR 750'),
  ('GSX 1100', 'GSX 1100'),
  ('GSX 1200 Inazuma', 'GSX 1200 Inazuma'),
  ('GSX 1250 FA', 'GSX 1250 FA'),
  ('GSX 1300 R Hayabusa', 'GSX 1300 R Hayabusa'),
  ('GSX 1400', 'GSX 1400'),
  ('GSX 250', 'GSX 250'),
  ('GSX 400 Inazuma', 'GSX 400 Inazuma'),
  ('GSX 400F Katana', 'GSX 400F Katana'),
  ('GSX 600F Katana', 'GSX 600F Katana'),
  ('GSX 650F', 'GSX 650F'),
  ('GSX 750F Katana', 'GSX 750F Katana'),
  ('GSX-8S', 'GSX-8S'),
  ('GSX-R 1000', 'GSX-R 1000'),
  ('GSX-R 1100', 'GSX-R 1100'),
  ('GSX-R 125', 'GSX-R 125'),
  ('GSX-R 250', 'GSX-R 250'),
  ('GSX-R 400', 'GSX-R 400'),
  ('GSX-R 600', 'GSX-R 600'),
  ('GSX-R 750', 'GSX-R 750'),
  ('GSX-S 1000', 'GSX-S 1000'),
  ('GSX-S 1000 F', 'GSX-S 1000 F'),
  ('GSX-S 1000 GT', 'GSX-S 1000 GT'),
  ('GSX-S 1000S Katana', 'GSX-S 1000S Katana'),
  ('GSX-S 750', 'GSX-S 750'),
  ('GW 250 (GSR 250)', 'GW 250 (GSR 250)'),
  ('Gixxer 150', 'Gixxer 150'),
  ('Goose 350', 'Goose 350'),
  ('Grasstracker TU 250G', 'Grasstracker TU 250G'),
  ('Intruder C800 (VL 800)', 'Intruder C800 (VL 800)'),
  ('Intruder M1800R (VZR 1800)', 'Intruder M1800R (VZR 1800)'),
  ('Intruder M800 (VZ 800)', 'Intruder M800 (VZ 800)'),
  ('Intruder VL 1500 LC', 'Intruder VL 1500 LC'),
  ('Intruder VL 400 Classic', 'Intruder VL 400 Classic'),
  ('Intruder VS 1400', 'Intruder VS 1400'),
  ('Intruder VS 400', 'Intruder VS 400'),
  ('Intruder VS 750', 'Intruder VS 750'),
  ('Intruder VS 800', 'Intruder VS 800'),
  ('Marauder VZ 1600', 'Marauder VZ 1600'),
  ('Marauder VZ 800', 'Marauder VZ 800'),
  ('RF 400', 'RF 400'),
  ('RF 900', 'RF 900'),
  ('RM 125', 'RM 125'),
  ('RM-Z 250', 'RM-Z 250'),
  ('RM-Z 450', 'RM-Z 450'),
  ('RMX 250S', 'RMX 250S'),
  ('RV 200 VanVan', 'RV 200 VanVan'),
  ('RV 50', 'RV 50'),
  ('SFV 400 Gladius', 'SFV 400 Gladius'),
  ('SFV 650 Gladius', 'SFV 650 Gladius'),
  ('ST250 (TU250X)', 'ST250 (TU250X)'),
  ('SV 1000', 'SV 1000'),
  ('SV 400', 'SV 400'),
  ('SV 650', 'SV 650'),
  ('TL 1000', 'TL 1000'),
  ('TS 200R', 'TS 200R'),
  ('TS 250', 'TS 250'),
  ('V-Strom 800DE', 'V-Strom 800DE'),
  ('V-Strom DL 1000', 'V-Strom DL 1000'),
  ('V-Strom DL 1050', 'V-Strom DL 1050'),
  ('V-Strom DL 250', 'V-Strom DL 250'),
  ('V-Strom DL 650', 'V-Strom DL 650'),
  ('VX 800', 'VX 800'),
  ('Volty (TU250)', 'Volty (TU250)'),
  ('Wolf', 'Wolf')),
 'KTM': (('1050 Adventure', '1050 Adventure'),
  ('1090 Adventure R', '1090 Adventure R'),
  ('1190 Adventure', '1190 Adventure'),
  ('1190 Adventure R', '1190 Adventure R'),
  ('1190 RC8', '1190 RC8'),
  ('125 Duke', '125 Duke'),
  ('125 EXC', '125 EXC'),
  ('125 SX', '125 SX'),
  ('1290 Super Adventure', '1290 Super Adventure'),
  ('1290 Super Adventure R', '1290 Super Adventure R'),
  ('1290 Super Adventure S', '1290 Super Adventure S'),
  ('1290 Super Adventure T', '1290 Super Adventure T'),
  ('1290 Super Duke GT', '1290 Super Duke GT'),
  ('1290 Super Duke R', '1290 Super Duke R'),
  ('1290 Super Duke R Evo', '1290 Super Duke R Evo'),
  ('1390 Super Duke R', '1390 Super Duke R'),
  ('1390 Super Duke R Evo', '1390 Super Duke R Evo'),
  ('150 EXC', '150 EXC'),
  ('150 SX', '150 SX'),
  ('200 Duke', '200 Duke'),
  ('250 Adventure', '250 Adventure'),
  ('250 Duke', '250 Duke'),
  ('250 EXC', '250 EXC'),
  ('250 EXC F', '250 EXC F'),
  ('250 SX', '250 SX'),
  ('250 SX F', '250 SX F'),
  ('300 EXC', '300 EXC'),
  ('300 SX', '300 SX'),
  ('350 EXC F', '350 EXC F'),
  ('350 SX F', '350 SX F'),
  ('390 Adventure', '390 Adventure'),
  ('390 Adventure SW', '390 Adventure SW'),
  ('390 Duke', '390 Duke'),
  ('450 EXC', '450 EXC'),
  ('450 EXC F', '450 EXC F'),
  ('450 SMR', '450 SMR'),
  ('450 SX F', '450 SX F'),
  ('50 SX', '50 SX'),
  ('500 EXC F', '500 EXC F'),
  ('525 EXC', '525 EXC'),
  ('560 SMR', '560 SMR'),
  ('625 SMC', '625 SMC'),
  ('640 Adventure', '640 Adventure'),
  ('640 Duke', '640 Duke'),
  ('640 LC4 Supermoto', '640 LC4 Supermoto'),
  ('65 SX', '65 SX'),
  ('660 SMC', '660 SMC'),
  ('690 Duke', '690 Duke'),
  ('690 Duke R', '690 Duke R'),
  ('690 Enduro', '690 Enduro'),
  ('690 Enduro R', '690 Enduro R'),
  ('690 SM', '690 SM'),
  ('690 SMC', '690 SMC'),
  ('690 SMC R', '690 SMC R'),
  ('790 Adventure', '790 Adventure'),
  ('790 Adventure R', '790 Adventure R'),
  ('790 Duke', '790 Duke'),
  ('85 SX', '85 SX'),
  ('890 Adventure', '890 Adventure'),
  ('890 Adventure R', '890 Adventure R'),
  ('890 Adventure R Rally', '890 Adventure R Rally'),
  ('890 Duke', '890 Duke'),
  ('890 Duke GP', '890 Duke GP'),
  ('890 Duke R', '890 Duke R'),
  ('890 SMT', '890 SMT'),
  ('950 Adventure', '950 Adventure'),
  ('950 SM', '950 SM'),
  ('990 Adventure', '990 Adventure'),
  ('990 SM', '990 SM'),
  ('990 Super Duke', '990 Super Duke'),
  ('Freeride 250', 'Freeride 250'),
  ('Freeride 350', 'Freeride 350'),
  ('Freeride E', 'Freeride E'),
  ('RC 200', 'RC 200'),
  ('RC 390', 'RC 390')),
 'Indian': (('Challenger', 'Challenger'),
  ('Chief', 'Chief'),
  ('Chief Bomber', 'Chief Bomber'),
  ('Chief Deluxe', 'Chief Deluxe'),
  ('Chief Vintage', 'Chief Vintage'),
  ('Chieftain', 'Chieftain'),
  ('FTR 1200', 'FTR 1200'),
  ('Pursuit', 'Pursuit'),
  ('Roadmaster', 'Roadmaster'),
  ('Scout', 'Scout'),
  ('Scout Sixty', 'Scout Sixty'),
  ('Springfield', 'Springfield')),
 'Honda': (('400X', '400X'),
  ('AX-1', 'AX-1'),
  ('Africa Twin CRF 1000L/1100L', 'Africa Twin CRF 1000L/1100L'),
  ('Ape 50', 'Ape 50'),
  ('Bros', 'Bros'),
  ('CB 1000', 'CB 1000'),
  ('CB 1000R', 'CB 1000R'),
  ('CB 1100', 'CB 1100'),
  ('CB 125', 'CB 125'),
  ('CB 1300', 'CB 1300'),
  ('CB 190X (Wuyang)', 'CB 190X (Wuyang)'),
  ('CB 200X', 'CB 200X'),
  ('CB 223S', 'CB 223S'),
  ('CB 250F (Hornet)', 'CB 250F (Hornet)'),
  ('CB 300F', 'CB 300F'),
  ('CB 300R', 'CB 300R'),
  ('CB 350', 'CB 350'),
  ('CB 350RS', 'CB 350RS'),
  ('CB 400 Super Four', 'CB 400 Super Four'),
  ('CB 400F', 'CB 400F'),
  ('CB 400SS', 'CB 400SS'),
  ('CB 500', 'CB 500'),
  ('CB 500F', 'CB 500F'),
  ('CB 500X', 'CB 500X'),
  ('CB 550', 'CB 550'),
  ('CB 600F (Hornet)', 'CB 600F (Hornet)'),
  ('CB 600S', 'CB 600S'),
  ('CB 650F', 'CB 650F'),
  ('CB 650R', 'CB 650R'),
  ('CB 650SC Nighthawk', 'CB 650SC Nighthawk'),
  ('CB 750', 'CB 750'),
  ('CB 900 Custom', 'CB 900 Custom'),
  ('CB 900F (Hornet)', 'CB 900F (Hornet)'),
  ('CB-1', 'CB-1'),
  ('CBF 1000', 'CBF 1000'),
  ('CBF 125T', 'CBF 125T'),
  ('CBF 150R', 'CBF 150R'),
  ('CBF 190R', 'CBF 190R'),
  ('CBF 500', 'CBF 500'),
  ('CBF 600', 'CBF 600'),
  ('CBR 1000 RR/RA Fireblade', 'CBR 1000 RR/RA Fireblade'),
  ('CBR 1000F', 'CBR 1000F'),
  ('CBR 1100 XX Blackbird', 'CBR 1100 XX Blackbird'),
  ('CBR 125R', 'CBR 125R'),
  ('CBR 150R', 'CBR 150R'),
  ('CBR 250R', 'CBR 250R'),
  ('CBR 300R', 'CBR 300R'),
  ('CBR 400R', 'CBR 400R'),
  ('CBR 400RR', 'CBR 400RR'),
  ('CBR 500 R', 'CBR 500 R'),
  ('CBR 600F', 'CBR 600F'),
  ('CBR 600RR', 'CBR 600RR'),
  ('CBR 650F', 'CBR 650F'),
  ('CBR 650R', 'CBR 650R'),
  ('CBR 900RR Fireblade', 'CBR 900RR Fireblade'),
  ('CBR 919RR Fireblade', 'CBR 919RR Fireblade'),
  ('CBR 929RR Fireblade', 'CBR 929RR Fireblade'),
  ('CBR 954RR Fireblade', 'CBR 954RR Fireblade'),
  ('CBX 125', 'CBX 125'),
  ('CBX 250', 'CBX 250'),
  ('CD 125', 'CD 125'),
  ('CL 300', 'CL 300'),
  ('CL 400', 'CL 400'),
  ('CL 500', 'CL 500'),
  ('CMX 1100 Rebel', 'CMX 1100 Rebel'),
  ('CR 125R', 'CR 125R'),
  ('CR 250R', 'CR 250R'),
  ('CR 85R', 'CR 85R'),
  ('CRF 125', 'CRF 125'),
  ('CRF 190L', 'CRF 190L'),
  ('CRF 230', 'CRF 230'),
  ('CRF 250 Rally', 'CRF 250 Rally'),
  ('CRF 250F', 'CRF 250F'),
  ('CRF 250L', 'CRF 250L'),
  ('CRF 250M', 'CRF 250M'),
  ('CRF 250R', 'CRF 250R'),
  ('CRF 250X', 'CRF 250X'),
  ('CRF 300 Rally', 'CRF 300 Rally'),
  ('CRF 300L', 'CRF 300L'),
  ('CRF 450R', 'CRF 450R'),
  ('CRF 450RX', 'CRF 450RX'),
  ('CRF 450X', 'CRF 450X'),
  ('CTX 1300', 'CTX 1300'),
  ('CTX 700', 'CTX 700'),
  ('CX', 'CX'),
  ('DN-01', 'DN-01'),
  ('FMX 650', 'FMX 650'),
  ('FTR 223', 'FTR 223'),
  ('GB 250 Clubman', 'GB 250 Clubman'),
  ('GB 350S', 'GB 350S'),
  ('GB 400', 'GB 400'),
  ('GL 1100', 'GL 1100'),
  ('GL 1200', 'GL 1200'),
  ('GL 1500', 'GL 1500'),
  ('GL 1800', 'GL 1800'),
  ('GL 500', 'GL 500'),
  ('Hawk 11', 'Hawk 11'),
  ('Jazz', 'Jazz'),
  ('MSX125 Grom', 'MSX125 Grom'),
  ('Magna', 'Magna'),
  ('NC 700S', 'NC 700S'),
  ('NC 700X', 'NC 700X'),
  ('NC 750S', 'NC 750S'),
  ('NC 750X', 'NC 750X'),
  ('NM4', 'NM4'),
  ('NSR', 'NSR'),
  ('NT1100', 'NT1100'),
  ('NT650V Deauville', 'NT650V Deauville'),
  ('NT700V Deauville', 'NT700V Deauville'),
  ('NTV 650', 'NTV 650'),
  ('NV', 'NV'),
  ('NX', 'NX'),
  ('Navi', 'Navi'),
  ('PC 800', 'PC 800'),
  ('RVF 400', 'RVF 400'),
  ('Rebel 250', 'Rebel 250'),
  ('Rebel 300', 'Rebel 300'),
  ('Rebel 500', 'Rebel 500'),
  ('SL', 'SL'),
  ('ST 1100', 'ST 1100'),
  ('ST 1300', 'ST 1300'),
  ('Shadow 150', 'Shadow 150'),
  ('Shadow 400', 'Shadow 400'),
  ('Shadow 750', 'Shadow 750'),
  ('Solo', 'Solo'),
  ('Steed 400', 'Steed 400'),
  ('Steed 600', 'Steed 600'),
  ('TLM', 'TLM'),
  ('Transalp 400', 'Transalp 400'),
  ('Transalp 600', 'Transalp 600'),
  ('Transalp 650', 'Transalp 650'),
  ('Unicorn', 'Unicorn'),
  ('VF 750', 'VF 750'),
  ('VFR 1200', 'VFR 1200'),
  ('VFR 1200 X Crosstourer', 'VFR 1200 X Crosstourer'),
  ('VFR 400', 'VFR 400'),
  ('VFR 750', 'VFR 750'),
  ('VFR 800', 'VFR 800'),
  ('VFR 800X Crossrunner', 'VFR 800X Crossrunner'),
  ('VRX 400', 'VRX 400'),
  ('VT 1100', 'VT 1100'),
  ('VT 1300CR Stateline', 'VT 1300CR Stateline'),
  ('VT 1300CS Sabre', 'VT 1300CS Sabre'),
  ('VT 1300CT Interstate', 'VT 1300CT Interstate'),
  ('VT 1300CX Fury', 'VT 1300CX Fury'),
  ('VT 400', 'VT 400'),
  ('VT 600', 'VT 600'),
  ('VT 750', 'VT 750'),
  ('VTR 1000', 'VTR 1000'),
  ('VTR 250', 'VTR 250'),
  ('VTX 1300', 'VTX 1300'),
  ('VTX 1800', 'VTX 1800'),
  ('VTZ', 'VTZ'),
  ('Valkyrie 1500', 'Valkyrie 1500'),
  ('Valkyrie 1800', 'Valkyrie 1800'),
  ('X11', 'X11'),
  ('X4', 'X4'),
  ('XL 250', 'XL 250'),
  ('XL1000V Varadero', 'XL1000V Varadero'),
  ('XL700V Transalp', 'XL700V Transalp'),
  ('XL750 Transalp', 'XL750 Transalp'),
  ('XLR', 'XLR'),
  ('XR 100', 'XR 100'),
  ('XR 125', 'XR 125'),
  ('XR 190', 'XR 190'),
  ('XR 230', 'XR 230'),
  ('XR 250', 'XR 250'),
  ('XR 400', 'XR 400'),
  ('XR 50', 'XR 50'),
  ('XR 600', 'XR 600'),
  ('XR 650R', 'XR 650R'),
  ('XRV 750 Africa Twin', 'XRV 750 Africa Twin'),
  ('Z50', 'Z50')),
 'Ducati': (('1098', '1098'),
  ('1198', '1198'),
  ('1199 Panigale', '1199 Panigale'),
  ('1299 Panigale', '1299 Panigale'),
  ('749', '749'),
  ('848', '848'),
  ('899 Panigale', '899 Panigale'),
  ('959 Panigale', '959 Panigale'),
  ('996', '996'),
  ('DesertX', 'DesertX'),
  ('Diavel', 'Diavel'),
  ('Diavel Carbon', 'Diavel Carbon'),
  ('Diavel V4', 'Diavel V4'),
  ('HyperMotard', 'HyperMotard'),
  ('HyperStrada', 'HyperStrada'),
  ('Monster (2021-н.в.)', 'Monster (2021-н.в.)'),
  ('Monster 1000', 'Monster 1000'),
  ('Monster 1100', 'Monster 1100'),
  ('Monster 1200', 'Monster 1200'),
  ('Monster 400', 'Monster 400'),
  ('Monster 600', 'Monster 600'),
  ('Monster 696', 'Monster 696'),
  ('Monster 750', 'Monster 750'),
  ('Monster 796', 'Monster 796'),
  ('Monster 797', 'Monster 797'),
  ('Monster 800', 'Monster 800'),
  ('Monster 821', 'Monster 821'),
  ('Monster 900', 'Monster 900'),
  ('Monster S2R', 'Monster S2R'),
  ('Monster S4', 'Monster S4'),
  ('Multistrada 1000', 'Multistrada 1000'),
  ('Multistrada 1100', 'Multistrada 1100'),
  ('Multistrada 1200', 'Multistrada 1200'),
  ('Multistrada 1260', 'Multistrada 1260'),
  ('Multistrada 620', 'Multistrada 620'),
  ('Multistrada 950', 'Multistrada 950'),
  ('Multistrada V4', 'Multistrada V4'),
  ('Panigale S', 'Panigale S'),
  ('Panigale V2', 'Panigale V2'),
  ('Panigale V4', 'Panigale V4'),
  ('ST', 'ST'),
  ('Scrambler', 'Scrambler'),
  ('Scrambler 1100', 'Scrambler 1100'),
  ('SportClassic', 'SportClassic'),
  ('Streetfighter', 'Streetfighter'),
  ('Streetfighter V2', 'Streetfighter V2'),
  ('Streetfighter V4', 'Streetfighter V4'),
  ('SuperSport', 'SuperSport'),
  ('XDiavel', 'XDiavel')),
 'Bmw': (('F 650', 'F 650'),
  ('F 650 CS', 'F 650 CS'),
  ('F 650 GS', 'F 650 GS'),
  ('F 650 ST', 'F 650 ST'),
  ('F 700 GS', 'F 700 GS'),
  ('F 750 GS', 'F 750 GS'),
  ('F 800 GS', 'F 800 GS'),
  ('F 800 GT', 'F 800 GT'),
  ('F 800 R', 'F 800 R'),
  ('F 800 S', 'F 800 S'),
  ('F 800 ST', 'F 800 ST'),
  ('F 850 GS', 'F 850 GS'),
  ('F 850 GS Adventure', 'F 850 GS Adventure'),
  ('F 900 R', 'F 900 R'),
  ('F 900 XR', 'F 900 XR'),
  ('G 310 GS', 'G 310 GS'),
  ('G 310 R', 'G 310 R'),
  ('G 450 X', 'G 450 X'),
  ('G 650 GS', 'G 650 GS'),
  ('G 650 X', 'G 650 X'),
  ('HP2', 'HP2'),
  ('HP4', 'HP4'),
  ('K 1', 'K 1'),
  ('K 100', 'K 100'),
  ('K 100 LT', 'K 100 LT'),
  ('K 100 RS', 'K 100 RS'),
  ('K 100 RT', 'K 100 RT'),
  ('K 1100 LT', 'K 1100 LT'),
  ('K 1100 RS', 'K 1100 RS'),
  ('K 1200 GT', 'K 1200 GT'),
  ('K 1200 LT', 'K 1200 LT'),
  ('K 1200 R', 'K 1200 R'),
  ('K 1200 RS', 'K 1200 RS'),
  ('K 1200 S', 'K 1200 S'),
  ('K 1300 GT', 'K 1300 GT'),
  ('K 1300 R', 'K 1300 R'),
  ('K 1300 S', 'K 1300 S'),
  ('K 1600 B', 'K 1600 B'),
  ('K 1600 GA', 'K 1600 GA'),
  ('K 1600 GT', 'K 1600 GT'),
  ('K 1600 GTL', 'K 1600 GTL'),
  ('K 75 S', 'K 75 S'),
  ('M 1000 R', 'M 1000 R'),
  ('M 1000 RR', 'M 1000 RR'),
  ('R 100', 'R 100'),
  ('R 100 RT', 'R 100 RT'),
  ('R 1100 GS', 'R 1100 GS'),
  ('R 1100 R', 'R 1100 R'),
  ('R 1100 RS', 'R 1100 RS'),
  ('R 1100 RT', 'R 1100 RT'),
  ('R 1100 S', 'R 1100 S'),
  ('R 1150 GS', 'R 1150 GS'),
  ('R 1150 R', 'R 1150 R'),
  ('R 1150 RS', 'R 1150 RS'),
  ('R 1150 RT', 'R 1150 RT'),
  ('R 12', 'R 12'),
  ('R 1200 C', 'R 1200 C'),
  ('R 1200 CL', 'R 1200 CL'),
  ('R 1200 GS', 'R 1200 GS'),
  ('R 1200 GS Adventure', 'R 1200 GS Adventure'),
  ('R 1200 R', 'R 1200 R'),
  ('R 1200 RS', 'R 1200 RS'),
  ('R 1200 RT', 'R 1200 RT'),
  ('R 1200 S', 'R 1200 S'),
  ('R 1200 ST', 'R 1200 ST'),
  ('R 1250 GS', 'R 1250 GS'),
  ('R 1250 GS Adventure', 'R 1250 GS Adventure'),
  ('R 1250 R', 'R 1250 R'),
  ('R 1250 RS', 'R 1250 RS'),
  ('R 1250 RT', 'R 1250 RT'),
  ('R 1300 GS', 'R 1300 GS'),
  ('R 18', 'R 18'),
  ('R 18 B', 'R 18 B'),
  ('R 18 Classic', 'R 18 Classic'),
  ('R 18 Transcontinental', 'R 18 Transcontinental'),
  ('R 60', 'R 60'),
  ('R 71', 'R 71'),
  ('R 75', 'R 75'),
  ('R 80', 'R 80'),
  ('R 80 G/S', 'R 80 G/S'),
  ('R 850 R', 'R 850 R'),
  ('R 850 RT', 'R 850 RT'),
  ('R 90 S', 'R 90 S'),
  ('R Nine T', 'R Nine T'),
  ('R Nine T Pure', 'R Nine T Pure'),
  ('R Nine T Racer', 'R Nine T Racer'),
  ('R Nine T Scrambler', 'R Nine T Scrambler'),
  ('R Nine T Urban G/S', 'R Nine T Urban G/S'),
  ('S 1000 R', 'S 1000 R'),
  ('S 1000 RR', 'S 1000 RR'),
  ('S 1000 XR', 'S 1000 XR')),
 'Harley-Davidson': (
  ('Blackline', 'Blackline'),
  ('Breakout', 'Breakout'),
  ('CVO', 'CVO'),
  ('CVO Limited', 'CVO Limited'),
  ('CVO Pan America', 'CVO Pan America'),
  ('CVO Pro Street Breakout', 'CVO Pro Street Breakout'),
  ('CVO Road Glide', 'CVO Road Glide'),
  ('CVO Road Glide Limited', 'CVO Road Glide Limited'),
  ('CVO Road Glide ST', 'CVO Road Glide ST'),
  ('CVO Street Glide', 'CVO Street Glide'),
  ('CVO Tri Glide', 'CVO Tri Glide'),
  ('Cross Bones', 'Cross Bones'),
  ('Dyna Convertible', 'Dyna Convertible'),
  ('Dyna Glide Custom', 'Dyna Glide Custom'),
  ('Dyna Low Rider', 'Dyna Low Rider'),
  ('Dyna Super Glide', 'Dyna Super Glide'),
  ('Dyna Switchback', 'Dyna Switchback'),
  ('Dyna Wide Glide', 'Dyna Wide Glide'),
  ('Electra Glide', 'Electra Glide'),
  ('Electra Glide Revival', 'Electra Glide Revival'),
  ('FXDR 114', 'FXDR 114'),
  ('Fat Bob', 'Fat Bob'),
  ('Fat Boy', 'Fat Boy'),
  ('Forty-Eight', 'Forty-Eight'),
  ('Freewheeler', 'Freewheeler'),
  ('Heritage', 'Heritage'),
  ('LiveWire', 'LiveWire'),
  ('Low Rider', 'Low Rider'),
  ('Low Rider ST', 'Low Rider ST'),
  ('Night Rod', 'Night Rod'),
  ('Nightster', 'Nightster'),
  ('Pan America', 'Pan America'),
  ('Pan America Special', 'Pan America Special'),
  ('Road Glide', 'Road Glide'),
  ('Road Glide Limited', 'Road Glide Limited'),
  ('Road Glide ST', 'Road Glide ST'),
  ('Road Glide Special', 'Road Glide Special'),
  ('Road King', 'Road King'),
  ('Rocker C', 'Rocker C'),
  ('Softail Custom', 'Softail Custom'),
  ('Softail Deluxe', 'Softail Deluxe'),
  ('Softail Deuce', 'Softail Deuce'),
  ('Softail Slim', 'Softail Slim'),
  ('Softail Standard', 'Softail Standard'),
  ('Sport Glide', 'Sport Glide'),
  ('Sportster 1000', 'Sportster 1000'),
  ('Sportster 1200', 'Sportster 1200'),
  ('Sportster 883', 'Sportster 883'),
  ('Sportster S', 'Sportster S'),
  ('Springer Softail', 'Springer Softail'),
  ('Street 500', 'Street 500'),
  ('Street 750', 'Street 750'),
  ('Street Bob', 'Street Bob'),
  ('Street Glide', 'Street Glide'),
  ('Street Glide ST', 'Street Glide ST'),
  ('Street Glide Special', 'Street Glide Special'),
  ('Street Rod', 'Street Rod'),
  ('Sturgis', 'Sturgis'),
  ('Super Glide', 'Super Glide'),
  ('Tour Glide', 'Tour Glide'),
  ('Tri Glide', 'Tri Glide'),
  ('Ultra Limited', 'Ultra Limited'),
  ('V-Rod', 'V-Rod'),
  ('V-Rod Muscle', 'V-Rod Muscle'),
  ('WL', 'WL'),
  ('XR1200', 'XR1200'))}

class MarkForm(forms.Form):
    mark = forms.ChoiceField(widget=forms.RadioSelect, choices = marks, label='Марка')


class MotoPriceForm(forms.Form):     
    model = forms.ChoiceField(label='Модель')
    vollume = forms.IntegerField(label='Объём двигателя', help_text='см³ Необязательное поле', required=False)
    power = forms.IntegerField(label='Мощность двигателя', help_text='л.с. Необязательное поле', required=False)
    mileage = forms.IntegerField(label='Пробег', help_text='км', validators=(mileage_validator,))
    year = forms.IntegerField(label='Год выпуска', validators=(year_validator,))
    
    def __init__(self, *args, **kwargs):
        self.mark = kwargs.pop('mark', None).title()
        super(MotoPriceForm, self).__init__(*args, **kwargs)
        self.fields['model'].choices = models.get(self.mark, [])