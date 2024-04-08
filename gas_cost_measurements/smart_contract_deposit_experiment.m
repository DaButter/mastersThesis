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
];

deposit_count1 = 1:length(gas_cost1);

% for deposit count 20,30,40...100
gas_cost2 = [
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

deposit_count2 = 20:10:100;

% Append NaN to gas_cost1 and gas_cost2
gas_cost1 = [gas_cost1, NaN];
gas_cost2 = [NaN, gas_cost2];

% Plot the gas costs
figure;
plot(deposit_count1, gas_cost1, 'bo-', 'LineWidth', 1.5);
hold on;
plot(deposit_count2, gas_cost2, 'ro-', 'LineWidth', 1.5);
hold off;

% Add labels and legend
xlabel('Deposit Count');
ylabel('Gas Cost');
title('Gas Cost vs. Deposit Count');
legend('1-10 Deposits', '20-100 Deposits', 'Location', 'best');
grid minor;
