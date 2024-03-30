% Here are gas cost measurements of MultiSigWallet smart contract
% deployment on the Ethereum blockchain depening on the owner count

%% Data
owner_count = [1:20];
gas_cost = [965877
1011800 
1057723
1103646
1149569
1195492
1241415
1287338
1333237
1379160
1425083
1471006
1516929
1562852
1608775
1654698
1700621
1746544
1792467
1838390
];


%% Graphical results
figure(1)
plot(owner_count, gas_cost, 'bo-'), grid minor
xlim([1, 20]), xticks(1:20)
% xlim([0.5, 20.5])

title('Vied? l?guma izvietošanas g?zes pat?ri?š atkar?b? no l?guma ?pašnieku skaita')
xlabel('?pašnieku skaits')
ylabel('G?zes pat?ri?š')