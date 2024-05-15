console.log("I'm Here");


function plotlyPlot(x, y, domElement) {

    var data = [{
        x: x,
        y: y,
    }];

    // var layout = {
    //     // margin: {
    //     //     t: 0
    //     // },
    //     xaxis: {
    //         range: [-0.01, 1.1]
    //     },
    //     yaxis: {
    //         range: [0, 0.11],
    //         //scaleratio: 0.01,
    //         domain: [0, 0.5],
    //         //scaleratio: 0.1,
    //     }
    // };

    Plotly.newPlot(
        domElement,
        data,
        //layout
    );


    // Plotly.plot(
    //     document.getElementById(domElement),
    //     [
    //         {
    //             x: x,
    //             y: y
    //         }
    //     ],
    //     {
    //         margin: { t: 0 }
    //     },

    // );
}