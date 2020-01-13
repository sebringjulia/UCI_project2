

// define source data
// // var countries = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson";
// var countries =  "../../geojson/countries.geo.json";
// // var geojson = "/geojson/simplestyles.geojson";
// // var topojson = "/topojson/us-states.topo.json";
// // console.log({{country_coord}})
// // create the cesium container
// // Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyMjA1MzYwYi1iMDhjLTQwNzQtOTI3Yi0wYWNjNjhjNjUyYWIiLCJpZCI6MjAxMzMsInNjb3BlcyI6WyJhc3IiLCJnYyJdLCJpYXQiOjE1NzY4MTY5OTN9.iMx-a5aN6VEYfdlN8cfPbJEq6nB-16q1qnRELDpbsOE';

// // var viewer = new Cesium.Viewer('cesiumContainer', {

// // });

// // load country boundaries
// // var dataSource = Cesium.GeoJsonDataSource.load(countries);

// // simple load
// // viewer.dataSources.add(Cesium.GeoJsonDataSource.load(topojson, {
// //     stroke: Cesium.Color.HOTPINK,
// //     fill: Cesium.Color.PINK.withAlpha(0.5),
// //     strokeWidth: 5
// // }));

// // custom style
// // Seed the random number generator for repeatable results.
// // Sandcastle.addToolbarButton('Custom styling', function() {
//     Cesium.Math.setRandomNumberSeed(0);

//     // Create a new GeoJSON data source and add it to the list.
//     var dataSource = new Cesium.GeoJsonDataSource();
//     viewer.dataSources.add(dataSource);

//     // console.log(viewer.dataSources);
//     // console.log(dataSource);

//     // Load the document into the data source and then set custom graphics
//     dataSource.load(countries).then(function() {
//         //Get the array of entities
//         var entities = dataSource.entities.values;

//         var colorHash = {};
//         // for (var i = 0; i < 1; i++) { // replace with entities.length to go though all entities
//         for (var i = 0; i < entities.length; i++) { // replace with entities.length to go though all entities
//             //For each entity, create a random color based on the state name.
//             //Some states have multiple entities, so we store the color in a
//             //hash so that we use the same color for the entire state.
//             var entity = entities[i];
//             var name = entity.name;
//             var color = colorHash[name];

//             if (!color) {
//                 color = Cesium.Color.fromRandom({
//                     alpha : 1
//                 });
//                 colorHash[name] = color;
//             }
//             // console.log(colorHash);

//             // console.log(entity.polygon.material.color);
            
//             // Set the polygon material to our random color.
//             // entity.polygon.material = Cesium.ColorMaterialProperty.fromColor(color);
//             // entity.polygon.material.color = color;

//             //Set the polygon material to our random color.
//             entity.polygon.fill = true;
//             entity.polygon.material = color;

//             //Remove the outlines.
//             // entity.polygon.outline = false;

//             //Extrude the polygon based on the state's population.  Each entity
//             //stores the properties for the GeoJSON feature it was created from
//             //Since the population is a huge number, we divide by 50.
//             // entity.polygon.extrudedHeight = 25;
//             // entity.polygon.extrudedHeight = entity.properties.Population / 50.0;

//             // learning by messing with california or USA
//             // if (name == "California") {
//             if (name == "United States of America") {
//                 entity.polygon.extrudedHeight = 1000000;
//                 entity.polygon.fill = true;
//                 console.log("---------");
//                 console.log(entity);
//                 console.log(name);
//                 console.log("---------");
//             }

//             // Print some info for debugging
//             if (i === entities.length-1) {
//                 console.log("---------");
//                 console.log(`last entity @ i = ${i}`);
//                 console.log(entity);
//                 console.log(name);
//                 console.log("---------");
//                 console.log(colorHash);
//             }
//         }
//     }).otherwise(function(error){
//         //Display any errors encountered while loading.
//         window.alert(error);
//     });
// });


//Reset the scene when switching demos.
// Sandcastle.reset = function() {
//   viewer.dataSources.removeAll();
//
//   //Set the camera to a US centered tilted view.
//   viewer.camera.lookAt(Cesium.Cartesian3.fromDegrees(-98, 15.0, 5000000),
//       Cesium.Cartesian3.fromDegrees(-98, 40.0, 0), Cesium.Cartesian3.UNIT_Z);
// };

function country_dropdown() {
    
    var country_selector = d3.select("#selDatasetThree");

    d3.json("/countryNames").then((countryNames)=>{
        countryNames.forEach((country)=>{
            country_selector
                .append("option")
                .text(country)
                .property("value",country);
        });
    }); 
}

function year_dropdown() {

    var year_selector = d3.select("#selDatasetTwo");

    d3.json("/Year").then((Years) => {
        Years.forEach((year)=> {
            year_selector
                .append("option")
                .text(year)
                .property("value",year);
        });
    });
}

function init() {
    //Grabs a reference to the dropdown select element
    country_dropdown();
    year_dropdown();
    year = '2015';
    country = 'All';
    buildVisuals(year,country);    
}

function buildVisuals(year,country) {
    d3.json(`/Filter/${year}/${country}`).then((data)=> {
        drawScatter(data)
        drawTable(data)
    // =================================================================
    // Place functions for visuals
    //  Make sure you path your visual in the index.html
	// =================================================================
    })
}

function optionChanged(new_value,category) {
    if (category === 'country') {
        var year = document.getElementById("selDatasetTwo").value;
        var country = new_value;
    }
    else {
        var country = document.getElementById("selDatasetThree").value;
        var year = new_value;
    }
    buildVisuals(year,country);
}


init();