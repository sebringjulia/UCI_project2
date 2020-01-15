// create the cesium container
Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyMjA1MzYwYi1iMDhjLTQwNzQtOTI3Yi0wYWNjNjhjNjUyYWIiLCJpZCI6MjAxMzMsInNjb3BlcyI6WyJhc3IiLCJnYyJdLCJpYXQiOjE1NzY4MTY5OTN9.iMx-a5aN6VEYfdlN8cfPbJEq6nB-16q1qnRELDpbsOE';
var viewer = new Cesium.Viewer('cesiumContainer', {
// imageryProvider : new Cesium.TileMapServiceImageryProvider({
//     url : Cesium.buildModuleUrl('Assets/Textures/NaturalEarthII')
// }),
// baseLayerPicker: false,
// geocoder: false,
animation: false,
timeline: false
});

function buildGlobe(data,countriesSel, yearSel) {
    var countriesBorders = "http://raw.githubusercontent.com/sebringjulia/UCI_project2/master/geojson/countries.geo.json";
    // Create a new GeoJSON data source and add it to the list.
    var dataSource = new Cesium.GeoJsonDataSource();
    viewer.dataSources.add(dataSource);
    // Load the document into the data source and then set custom graphics
    dataSource.load(countriesBorders,{
            fill: Cesium.Color.PINK
        }).then(function() {
        // Get the array of entities
        var entities = dataSource.entities.values;
        for (var i = 0; i < entities.length; i++) {
            //For each entity
            var entity = entities[i];
            var name = entity.name;
            // update selected country
            if (name == countriesSel) {
                // var data = d3.json(`/Countryfilter/${countriesSel}`).then((data) => {
                //     var yearHappiness = data[0]["Happiness Score"];
                //
                // });
                console.log(`You selected ${countriesSel} for ${yearSel}`);
                entity.polygon.extrudedHeight = 1000000;
                entity.polygon.fill = true;
            }
        }
    }).otherwise(function(error) {
        //Display any errors encountered while loading.
        window.alert(error);
    });
}

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
    console.log(`/Filter/${year}/${country}`)
    d3.json(`/Filter/${year}/${country}`).then((data) => {
        console.log(data)
        drawScatter(data)
        drawTable(data)
        drawGauge(data)
        buildGlobe(data,country,year)
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