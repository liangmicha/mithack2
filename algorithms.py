# these are not actually algorithms.

ALL_DATA = [
]


john_doe_xrays = [
	{
		'time_string': '03 22 2014',
		'tags': ['xray'],
		'image_url': 'static/img/xray1.jpg',
	}, 
	{
		'time_string': '08 23 2014',
		'tags': ['xray'],
		'image_url': 'static/img/xray2.jpg',
	}, 
	{
		'time_string': '09 20 2014',
		'tags': ['xray'],
		'image_url': 'static/img/xray3.jpg',
	}, 
	{
		'time_string': '11 24 2014',
		'tags': ['xray'],
		'image_url': 'static/img/xray4.jpg',
	}, 
	{
		'time_string': '12 03 2014',
		'tags': ['xray'],
		'image_url': 'static/img/xray5.jpg',
	},
	{
		'time_string': '02 24 2015',
		'tags': ['xray'],
		'image_url': 'static/img/xray6.jpg',
	}
]

prescriptions = [
	{
		'time_string': '03 22 2014',
		'tags': ['prescription', 'Pubar clinic'],
		'image_url': 'static/img/p1.jpg',
	},
	{
		'time_string': '03 22 2014',
		'tags': ['prescription', 'drug store'],
		'image_url': 'static/img/p2.jpg',
	},
	{
		'time_string': '03 22 2014',
		'tags': ['prescription', 'antibiotics'],
		'image_url': 'static/img/p3.jpg',
	},
	{
		'time_string': '03 22 2014',
		'tags': ['prescription', 'clinic'],
		'image_url': 'static/img/p4.jpg',
	},
	{
		'time_string': '03 22 2014',
		'tags': ['prescription', 'fever'],
		'image_url': 'static/img/p5.jpg',
	},
	{
		'time_string': '03 22 2014',
		'tags': ['prescription', 'hand'],
		'image_url': 'static/img/p6.jpg',
	},
]


def get_patient_data_json(query_string):
	if True:
		return prescriptions
	if query_string == "john doe xrays before April":
		return john_doe_xrays
	if query_string == "Sanjit before March 2015 prescriptions":
		return prescriptions
	if query_string == "Kumar m. lab tests":
		return lab_tests


