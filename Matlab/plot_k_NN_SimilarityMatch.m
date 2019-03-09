% Similarty plotting..
% We could plot the similarities between Postgres-v1, Postgres-v2, MongoDB

function plot_k_NN_SimilarityMatch(matchPercentages, kValues)


% Plot the results

fh = figure;
hold on
        
labelSize = 36;
x_labelSize = 12;

tickSize = 32;
markerSize = 24;
lineWidth = 3;
axisWidth = 4;
axisSize = 30;
outlierSize = 8;

color = [0 0 0];

color_outlier = [0.4 0.4 0.4];

% BOXPLOT - Both Percentile and STSS Models
bp = boxplot(matchPercentages, 'Color', color, 'labelverbosity', 'major', 'outliersize', outlierSize);


ylabel('M a t c h  P e r c e n t a g e', 'FontSize', labelSize);
xlabel('\it{k}', 'Interpreter', 'Tex', 'FontSize', labelSize+8, 'FontName', 'Times New Roman');

set(gca, 'XTickLabel', kValues,'xtick',[1:size(kValues,2)])

set(gca, 'YGrid','on', 'GridLineStyle', '--');

set(gcf,'units','normalized','outerposition',[0 0 1 1]); %frames the figure into the computer screen - not a complete maximize, but works fine -when opening the figure, it opens as big scale (but not maximized)


set(gca, 'XTickLabel', kValues);


        set(fh, 'color', 'white'); % sets the color to white 
        set(gca, 'Box', 'off'); % here gca means get current axis 
        set(gca, 'FontSize', tickSize);
        set(gca,'LineWidth',lineWidth);
        
        
        yLims = get(gca, 'YLim');
        maxY = yLims(2);

% Increase the width of the box plot
set(findobj(gca,'type','line'),'linew',2)

% Color the outliers
color_outlier = [0.2 0.2 0.2];
h = findobj(gcf,'tag','Outliers');
for iH = 1:length(h)
    h(iH).MarkerEdgeColor = color_outlier;
end

