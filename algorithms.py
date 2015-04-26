# these are not actually algorithms.

ALL_DATA = [
]


results_prescription = [
	{
		'time_string': '03 22 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img1.jpg',
	}, 
	{
		'time_string': '03 23 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img2.jpg',
	}, 
	{
		'time_string': '03 24 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img3.jpg',
	}, 
]

results_xray = [
	{
		'time_string': '03 22 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img1.jpg',
	}, 
	{
		'time_string': '03 23 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img2.jpg',
	}, 
	{
		'time_string': '03 24 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img3.jpg',
	}, 
]

results_vitals = [
	{
		'time_string': '03 22 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img1.jpg',
	}, 
	{
		'time_string': '03 23 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img2.jpg',
	}, 
	{
		'time_string': '03 24 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img3.jpg',
	}, 
]


results_notes = [
	{
		'time_string': '03 22 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img1.jpg',
	}, 
	{
		'time_string': '03 23 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img2.jpg',
	}, 
	{
		'time_string': '03 24 2014',
		'tags': ['Xray', 'March', 'pain'],
		'image_url': 'static/img/img3.jpg',
	}, 
]

all_results = [results_prescription, results_xray,  results_vitals, results_notes]


def get_patient_data_json(query_string):
	return_arguments = []
	for results_type in all_results:
		results = []
		for result in results_type:
			good_result = True
			for token in query_string.split(' '):
				if not token in result['tags']:
					good_result = False
					break
			if good_result:
				results.append(result)
		return_arguments.append(results)
	return return_arguments[0], return_arguments[1], return_arguments[2], return_arguments[3]

