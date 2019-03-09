% This function plots the boxplot of runtimes for three different k-NN
% queries:
% 1. Postgres - insertion of a point: this idea is similar to MongoDB
% 2. Postgres - using two tables and calculating pair-wise distance between all points.
% 3. MongoDB

% Each of the query results are provided through a txt file with a size of k*n
% k: different k values (e.g. 5, 10, 100 etc.)
% n: number of randomly generated points

% fileNames is a cell array of runtimes for [1]: Postgres - insertion of a point, [2]: Postgres - two tables, [3]: MongoDB
function plot_k_NN_RunTimes(all, labels)


% Plot the results
        
labelSize = 36;
x_labelSize = 12;

tickSize = 32;
markerSize = 24;
lineWidth = 3;
axisWidth = 4;
axisSize = 30;
outlierSize = 4;

% we'll have three different lines
f1 = ':^k';
f2 = ':*k';
f3 = '-ok';



fh = figure;
hold on

plot(all(1,:), f1, 'LineWidth', lineWidth, 'MarkerSize', markerSize)
plot(all(2,:), f2, 'LineWidth', lineWidth, 'MarkerSize', markerSize)
plot(all(3,:), f3, 'LineWidth', lineWidth, 'MarkerSize', markerSize)



        ylabel('R u n  T i m e  ( s e c o n d s )', 'FontSize', labelSize);
        xlabel('\it{k}', 'FontSize', labelSize+8, 'FontName', 'Times New Roman');
        %xlabel('k', 'FontSize', labelSize+8, 'FontName', 'Times New Roman');


        set(gca, 'YGrid','on', 'GridLineStyle', '--');

        set(gcf,'units','normalized','outerposition',[0 0 1 1]); %frames the figure into the computer screen - not a complete maximize, but works fine -when opening the figure, it opens as big scale (but not maximized)

        % Set the NRC Detection Models
        
        
        
        % set(gca, 'XTickLabel', labels); --> Causes repeating tick labels
        % Solution: https://www.mathworks.com/matlabcentral/answers/215143-how-to-remove-repeated-xtick-values
        set(gca, 'XTickLabel', labels,'xtick',[1:size(labels,2)])
        
        % Tick label rotation: https://www.mathworks.com/matlabcentral/answers/231538-how-to-rotate-x-tick-label
        %set(gca,'XTickLabelRotation',20)

        set(fh, 'color', 'white'); % sets the color to white 
        set(gca, 'Box', 'off'); % here gca means get current axis 
        set(gca, 'FontSize', tickSize);
        set(gca,'LineWidth',lineWidth);
        
        %set(gca, 'XLim', [0.9 max(positions)+ increment])
        
        yLims = get(gca, 'YLim');
        maxY = yLims(2);
        
        legend('Postgres-v1', 'Postgres-v2', 'MongoDB');

       




