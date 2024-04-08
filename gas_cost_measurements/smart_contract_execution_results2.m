clear all, clc, format compact
%% Note
% Here are gas cost measurements of MultiSigWallet smart contract
% execution on the Ethereum blockchain 
% depening on the deposit count for with 1 needed signature for each


%% Data
% for every transaction 80009 extra gas
% signature cost increases as the transaction cost increases

% for deposit count 1,2,3...10
gas_cost1 = [
114209 + 66761
194218 + 125299
274227 + 186544
354236 + 250496
434245 + 317155
514254 + 386521
594263 + 458594
674272 + 533374
754281 + 610861
834290 + 691055
]

deposit_count1 = [1:length(gas_cost1)];

% for deposit count 10,30,40...100
gas_cost2 = [
834290 + 691055
1634380 + 1641880
2434470 + 2863405
3234560 + 4355630
4034650 + 6118555
4834740 + 8152180
5634830 + 10456505
6434920 + 13031530
7235010 + 15877255
8035100 + 18993680
];
deposit_count2 = [10:10:100];

%% Graphical results
figure(1)
plot(deposit_count1, gas_cost1, 'bo-', 'LineWidth', 1.5), grid minor
% xlim([1, length(gas_cost1)]), xticks(1:length(gas_cost1))
% xlim([0.5, 20.5])
hold on
plot(deposit_count2, gas_cost2, 'bo-', 'LineWidth', 1.5)
hold off


title('Vied? l?guma izpildes g?zes pat?ri?š atkar?b? no parakstu skaita vienai transakcijai')
xlabel('Parakst?mo depoz?tu skaits')
ylabel('G?zes pat?ri?š')