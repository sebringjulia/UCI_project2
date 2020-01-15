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
    // viewer.dataSources.removeAll()
    countriesBorders = "http://raw.githubusercontent.com/sebringjulia/UCI_project2/master/geojson/countries.geo.json";
    // Create a new GeoJSON data source and add it to the list.
    var dataSource = new Cesium.GeoJsonDataSource();
    viewer.dataSources.add(dataSource);
    // Load the document into the data source and then set custom graphics
    dataSource.load(countriesBorders,{
            fill: Cesium.Color.PINK
        }).then(function() {
        // Get the array of entities
        var entities = dataSource.entities.values;

        var colorHash = {};

        for (var i = 0; i < entities.length; i++) {
            for (var j= 0; j < data.length; j++) {
                //For each entity
                var entity = entities[i];
                var name = entity.name;
                // update selected country
                if (name == data[j]['Country']) {
                    // var data = d3.json(`/Countryfilter/${countriesSel}`).then((data) => {
                    //     var yearHappiness = data[0]["Happiness Score"];
                    //
                    // });
                    entity.polygon.fill = true;

                    if (data[j]['Happiness Score']<2){
                        entity.polygon.material = Cesium.Color.DARKGREY
                    } 
                    else if (data[j]['Happiness Score']>2 && data[j]['Happiness Score']<4){
                        entity.polygon.material = Cesium.Color.DARKORANGE
                    }
                    else if (data[j]['Happiness Score']>4 && data[j]['Happiness Score']<6){
                        entity.polygon.material = Cesium.Color.GOLDROD
                    }
                    else if (data[j]['Happiness Score']>6 && data[j]['Happiness Score']<8){
                        entity.polygon.material = Cesium.Color.GOLD
                    }
                    else if (data[j]['Happiness Score']>8 && data[j]['Happiness Score']<10){
                        entity.polygon.material = Cesium.Color.YELLOW
                    }
                    else {

                    };

                    console.log(`You selected ${countriesSel} for ${yearSel}`);
                    entity.polygon.extrudedHeight = data[j]['Happiness Score']*100000;

            }
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
    buildVisuals(year,country)
}

init();