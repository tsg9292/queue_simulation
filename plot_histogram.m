function plot_histogram(lam, mu, n, T)
	Xt=csvread('output.csv');
	figure
	h=histogram(Xt);
	title(['Histogram of 1000 trials of Xt with \lambda = ' num2str(lam) ' and \mu = ' num2str(mu) '.']);
	xlabel(['Xt (# of people in the queue at time ' num2str(T) ')']);
	ylabel('frequency');
	saveas(h,'hist','png');
	close
	exit