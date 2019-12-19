from django.shortcuts import render


#  this is views file


def home(request):
    #  http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=818F4FE0-A27E-4E0F-889A-0DC3E6D3C289
    global category_description, category_color
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_requests = requests.get(
             "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=818F4FE0-A27E-4E0F-889A-0DC3E6D3C289")


        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = 'Error...'

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50)Air Quality is considered satisfactory, and airpollution posses little or no " \
                                   "risk. "
            category_color = "good"
        elif api[0]['Category']['Name'] == 'Moderate':
            category_description = "Air quality is Moderate"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
            category_description = "Air quality is Unhealthy for Sensitive Groups"
            category_color = "usg"
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_description = "Air quality is Unhealthy"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            category_description = "Air quality is Very Unhealthy"
            category_color = "veryUnhealthy"
        elif api[0]['Category']['Name'] == 'Hazardous':
            category_description = "Air quality is Hazardous"
            category_color = "hazardous"

        context = {
            'api': api,
            'category_description': category_description,
            'category_color': category_color
        }
        return render(request, 'home.html', context)


    else:
        api_requests = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=818F4FE0-A27E-4E0F-889A-0DC3E6D3C289")

        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = 'Error...'

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50)Air Quality is considered satisfactory, and airpollution posses little or no " \
                                   "risk. "
            category_color = "good"
        elif api[0]['Category']['Name'] == 'Moderate':
            category_description = "Air quality is Moderate"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
            category_description = "Air quality is Unhealthy for Sensitive Groups"
            category_color = "usg"
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_description = "Air quality is Unhealthy"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            category_description = "Air quality is Very Unhealthy"
            category_color = "veryUnhealthy"
        elif api[0]['Category']['Name'] == 'Hazardous':
            category_description = "Air quality is Hazardous"
            category_color = "hazardous"

        context = {
            'api': api,
            'category_description': category_description,
            'category_color': category_color
        }
        return render(request, 'home.html', context)


def about(request):
    global movie
    import json
    import requests
    api_requests = requests.get(
        "https://api.themoviedb.org/3/movie/{movie_id}?api_key=4db4edb62145a51111a9b772bc190bb3&language=en-US")
    try:
        movie = json.loads(api_requests.content)
    except Exception as e:
        api = 'Error...'
    return render(request, 'about.html', {'movie': movie})
