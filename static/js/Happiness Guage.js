// Guage for Project 2 by Mikayla

function buildGauge(wfreq) {
    var level = parseFloat(wfreq) * 20;
    var degrees = 180 - level;
    var radius = 0.7;
    var radians = (degrees * Math.PI) / 180;
    var x = radius * Math.cos(radians);
    var y = radius * Math.sin(radians);
  
    var mainPath = "M -.0 -0.05 L .0 0.05 L ";
    var pathX = String(x);
    var space = " ";
    var pathY = String(y);
    var pathEnd = " Z";
    var path = mainPath.concat(pathX, space, pathY, pathEnd);
  
    var data = [
      {
        type: "scatter",
        x: [0],
        y: [0],
        marker: { size: 10, color: "850000" },
        showlegend: false,
        name: "Freq",
        text: level,
        hoverinfo: "text+name"
      },
      {
        values: [50 / 5, 50 / 5, 50 / 5, 50 / 5, 50 / 5, 50],
        rotation: 90,
        text: ["8-10", "8-6", "4-6","2-4", "0-2", ""],
        textinfo: "text",
        textposition: "inside",
        marker: {
          colors: [
            "rgba(0, 105, 11, .5)",
            "rgba(0, 38, 77, .5)",
            "rgba(0, 51, 102, .5)",
            "rgba(0, 115, 230, .5)",
            "rgba(51, 153, 255, .5)",
            "rgba(204, 230, 255, 0)"
          ]
        },
        labels: ["8-10", "8-6", "4-6","2-4", "0-2", ""],
        hoverinfo: "label",
        hole: 0.7,
        type: "pie",
        showlegend: false
      }
    ];
  
    var layout = {
      shapes: [
        {
          type: "path",
          path: path,
          fillcolor: "850043",
          line: {
            color: "850000"
          }
        }
      ],
      title: "<b>Happiness</b> <br></b>Scale</b>",
      height: 600,
      width: 600,
      xaxis: {
        zeroline: false,
        showticklabels: false,
        showgrid: false,
        range: [-2, 2]
      },
      yaxis: {
        zeroline: false,
        showticklabels: false,
        showgrid: false,
        range: [-1, 1]
      }
    };
  
    var GAUGE = document.getElementById("gauge");
    Plotly.newPlot(GAUGE, data, layout);
  }

