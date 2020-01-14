function drawTable(data) {
	
	let code = data.Code,
		country = data[0]['Country'],
		economy = Math.round(data[0]['Economy (GDP per Capita)']*100)/100,
		family = Math.round(data[0]["Family"]*100)/100,
		freedom = Math.round(data[0]["Freedom"]*100)/100,
		generosity = Math.round(data[0]["Generosity"]*100)/100,
		rank = Math.round(data[0]["Happiness Rank"]*100)/100,
		score = Math.round(data[0]["Happiness Score"]*100)/100,
		health = Math.round(data[0]["Health (Life Expectancy)"]*100)/100,
		trust = Math.round(data[0]["Trust (Government Corruption)"]*100)/100,
		year = data[0]['Year'];


	var values = [
    	['Happiness Score','Happiness Rank', 
    	'Economy (GDP per Capita)','Family',
    	'Health (Life Expectancy)','Freedom',
    	'Trust (Government Corruption)','Generosity'],
		[score,rank,economy,family,health,freedom,trust,generosity],
		['A metric measured by asking the sampled people the question:\
		"How would you rate your happiness on a scale of 0 to 10 where 10 is the happiest."',
		'Rank of the country based on the Happiness Score.',
		'The extent to which GDP contributes to the calculation of the Happiness Score.',
		'The extent to which Family contributed to the calculation of the Happiness Score',
		'The extent to which Life expectancy contributed to the calculation of the Happiness Score',
		'The extent to which Freedom contributed to the calculation of the Happiness Score.',
		'The extent to which Perception of Corruption contributes to Happiness Score.',
		'The extent to which Generosity contributed to the calculation of the Happiness Score.'
		]
	]

	var data = [{
	  type: 'table',
	  columnorder: [1,2,3],
	  columnwidth: [100,100,400],

	header: {
    	values: [["Factors"],["Data"],["DESCRIPTION"]],
		align: ["center", "center","center"],
		height: 40,
	    line: {
	    	width: 1, 
	    	color: '#506784'
		    },
	    fill: {
	    	color: 'rgb(65, 130, 190)'
		    },
	    font: {
	    	family: "'Barlow Condensed' , 'sans-serif'", 
	    	size: 17, 
	    	color: "white"
		    }
		},
	  
	cells: {
		values: values,
		align: ["left", "center","left"],
		height: 50,
		width: 100,
		line: {
			color: "#506784",
			width: 1
		    },
		fill: {
			color: ['rgba(65, 130, 190, .5)', 'white']
			},
		font: {
			family: "'Barlow Condensed' , 'sans-serif'", 
			size: 15, 
		    }
		}
	}]

	var layout = {
		title: `<b> HAPPINESS DATA </b> <br>${country}<br>${year}`,
		// autosize: false,
		width: 600,
		height: 500,
		margin: {
			l: 50,
			r: 50,
			b: 100,
			t: 100,
		},
		plot_bgcolor: 'rgba(0, 0, 0, 0)',
		paper_bgcolor: 'rgba(0, 0, 0, 0)',
	}


	Plotly.newPlot('table', data,layout,{responsive: true});	

}