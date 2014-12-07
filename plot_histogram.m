Xt=csvread('output.csv');
figure
h=histogram(Xt,'BinLimits',[0,100]);
title('Histogram of 1000 trials of Xt');
xlabel('Xt (# of people in the queue at time T)');
ylabel('frequency');
saveas(h,'hist','png')
close
exit