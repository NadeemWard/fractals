// fetch("./data/10_triangles_scale_1-5_depth_3.json")
// .then(response => {
//    return response.json();
// })
// .then(data => console.log(data));

// import data from '../../data/'
// //require.js
// const data = require('../data/10_triangles_scale_1-5_depth_3.json');
// console.log(data);

// define(function (require) {
//     var data = require('../../data/10_triangles_scale_1-5_depth_3.json');
//     console.log(data);
// }

// )

// import * as data from '../../data/10_triangles_scale_1-5_depth_3.json'
// const {name} = data;
// console.log(name);

TESTER = document.getElementById('tester');

Plotly.plot( TESTER, [{
    x: data.x,
    y: data.y 
    }], 
    { 
        margin: { t: 0 } // important for scaling the diagram to look right
    }, 
    {
        showSendToCloud:true
    },
    {
        sliders: [{
          pad: {t: 30},
          currentvalue: {
            xanchor: 'right',
            prefix: 'color: ',
            font: {
              color: '#888',
              size: 20
            }
          },
          steps: [{
            label: 'red',
            method: 'restyle',
            args: ['line.color', 'red']
          }, {
            label: 'green',
            method: 'restyle',
            args: ['line.color', 'green']
          }, {
            label: 'blue',
            method: 'restyle',
            args: ['line.color', 'blue']
          }]
        }]
      });
console.log("here")

Plotly.newPlot('tester', [{
        x: data.x,
        y: data.y 
      }],
      {
        sliders: [{
          
          steps: [{
            label: 'first',
            method: 'restyle',
            args: ['x', data2.x, 'y', data2.y]
          }, {
            label: 'second',
            method: 'restyle',
            args: ['x', data.x, 'y', data.y]
          }, ]
        }]
      });
/* Current Plotly.js version */
console.log( Plotly.BUILD );