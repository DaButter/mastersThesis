clear all, clc, format compact
%% Note
% Here are gas cost measurements of MultiSigWallet smart contract
% deployment on the Ethereum blockchain depening on the owner count


%% Data
owner_count = [1:20];
gas_cost = [
960883
1006806 
1052729
1098652
1144575
1190498
1236421
1282344
1328267
1374190
1420113
1466036
1511959
1557882
1603805
1649728
1695651
1741574
1787497
1833420
];


%% Graphical results
figure(1)
plot(owner_count, gas_cost, 'bo-'), grid minor
xlim([1, 20]), xticks(1:20)
% xlim([0.5, 20.5])

title('Vied? l?guma izvietošanas g?zes pat?ri?š atkar?b? no l?guma ?pašnieku skaita')
xlabel('?pašnieku skaits')
ylabel('G?zes pat?ri?š')

% title('Vieda liguma izvietosanas gazes paterins atkariba no liguma ipasnieku skaita')
% xlabel('?pašnieku skaits')
% ylabel('G?zes pat?ri?š')