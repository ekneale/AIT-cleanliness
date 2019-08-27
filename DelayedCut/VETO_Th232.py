from statistics import mean
Ac228 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Pb212 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Bi212 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Tl208 = [0.00133407, 0.000792644, 0.00102596, 0.00109752, 0.00125088, 0.000549623, 0.000937134, 0.000781189, 0.000548977, 0.00101365, 0.000705053, 0.00148926, 0.000393825, 0.000711238, 0.000707492, 0.000549063, 0.00109520, 0.000551746, 0.00117288, 0.000311721, 0.000932401, 0.000314218, 0.00110046, 0.000861326, 0.000553710, 0.000549537, 0.00100979, 0.000630965, 0.000392188, 0.000630666, 0.000470736, 0.000552399, 0.000949067, 0.000233973, 0.000632511, 0.000314367, 0.000870942, 0.000790014, 0.000470995, 0.000705219]
print('Delayed cut for VETO for Th232 chain')
print('Ac228 = %.5e' % mean(Ac228))
print('Bi212 = %.5e' % mean(Bi212))
print('Pb212 = %.5e' % mean(Pb212))
print('Tl208 = %.5e' % mean(Tl208))
