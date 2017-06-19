// mychart.js
define(['d3', 'wq/pandas', 'wq/chart'], function(d3, pandas, chart) {

// Unpivoted data (single-row header)
d3.csv("/data/2010.csv", render);

// Pivoted data (multi-row header)
pandas.get('/data/2010.csv', render);

function render(error, data) {
    d3.select('svg')
       .selectAll('rect')
       .data(data)
       // ...
}

});
