function plot_mean_vincenty( means,labels )

% Plot the results
        
labelSize = 36;
x_labelSize = 12;

tickSize = 30;
markerSize = 24;
lineWidth = 3;
axisWidth = 4;
axisSize = 30;
outlierSize = 6;



fh = figure;
hold on

numTicks = size(labels, 2); % determines the number of ticks.

% Rearrange the data - so that one Postgres and the next is MongoDB
m=1;
for i=1:numTicks
    data(:, m) = means(:, i);
    data(:, m+1) = means(:, i+numTicks);
    m = m+2;
end

means = data;

% Take the natural log to have better visualisation
%data = log(data);
%data = log10(data);

% Ticks would be positioned in between the positions.
startPos = 1;
increment = 0.1;

m=1;
for i=1:numTicks
    positions(m) = startPos;
    positions(m+1) = startPos + increment;
    labelPositions(i) = startPos + increment/2; 
    startPos = startPos + increment*3; 
    m= m+2;
end


colors = [50/288 102/288 144/288;
          96/288 177/288 80/288];

color_outlier = [0.4 0.4 0.4];

% Postgres & MongoDB colours
      
colors = repmat(colors, numTicks, 1);

% BOXPLOT - Both Percentile and STSS Models
bp = boxplot(data, 'positions', positions, 'Color', colors, 'labelverbosity', 'minor', 'outliersize', outlierSize);
        
 % Set the line width
        set(bp,{'linew'},{lineWidth})
        

        
          % Setting the color of the MEDIAN
        %set(findobj(gcf,'Tag','Median'), 'LineWidth',3);
        
        h = findobj(gcf,'tag','Outliers');
        for iH = 1:length(h)
            h(iH).MarkerEdgeColor = color_outlier;
        end
        %set(findobj(gcf,'Tag','Outlier'), 'Color', color_outlier);
        
        %set(findobj(gca,'Type','text'),'VerticalAlignment','top')

        ylabel('V i n c e n t y  M e a n  ( M e t e r )', 'FontSize', labelSize);
        xlabel('\it{k}', 'Interpreter', 'Tex', 'FontSize', labelSize+8, 'FontName', 'Times New Roman');


        set(gca, 'YGrid','on', 'GridLineStyle', '--');

        set(gcf,'units','normalized','outerposition',[0 0 1 1]); %frames the figure into the computer screen - not a complete maximize, but works fine -when opening the figure, it opens as big scale (but not maximized)

        % Set the NRC Detection Models
        set(gca, 'XTick', labelPositions)
        set(gca, 'XTickLabel', labels);
        % Tick label rotation: https://www.mathworks.com/matlabcentral/answers/231538-how-to-rotate-x-tick-label
        %set(gca,'XTickLabelRotation',20)

        set(fh, 'color', 'white'); % sets the color to white 
        set(gca, 'Box', 'off'); % here gca means get current axis 
        set(gca, 'FontSize', tickSize);
        set(gca,'LineWidth',lineWidth);
        
        set(gca, 'XLim', [0.9 max(positions)+ increment])
        
        yLims = get(gca, 'YLim');
        maxY = yLims(2);

        % Legend
        % Manual legend insertion:
        %https://stackoverflow.com/questions/33474206/add-custom-legend-without-any-relation-to-the-graph
        h = zeros(2, 1);
        h(1) = plot(2,2,'-', 'Color', colors(1,:), 'visible', 'off');
        h(2) = plot(2,2,'-', 'Color', colors(2,:),  'visible', 'off');
        % Adjustment of line thickness in the legend
        % https://www.mathworks.com/matlabcentral/answers/328791-how-do-i-change-the-linewidth-and-the-fontsize-in-a-legend
        [hleg, hobj, hout, mout] = legend(h, 'P o s t g r e s - v 2','M o n g o D B');
        %set(hobj,'linewidth',lineWidth+2);
        
        
        % Both works:  legend(h, 'Postgres','MongoDB'); OR legend('Postgres','MongoDB');
        reduceWhiteSpace();

end



