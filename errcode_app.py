
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Example data structures (Complete List is over 2000+ unique codes, 200+ Demo Video Links and 100+ Error Code Flowcharts)
titlepairs = {
'EON ALPHA|ALPHA|52141501SD02292|52141501SD02293|52141501SD02294|52141501SD02988|52141501SD02989|52141501SD02990|52141501SD02991|52141501SD02992|52141501SD02993|52141501SD02994|52141501SD02995|52141501SD02996|52141501SD02997|52141501SD02998|52141501SD02999|52141501SD03000|52141501SD03001|52141501SD03002|52141501SD03003|52141501SD03004|52141501SD03005|52141501SD03006|52141501SD03007|52141501SD03008|52141501SD03009|52141501SD03010|52141501SD03011|2292|2293|2294|2988|2989|2990|2991|2992|2993|2994|2995|2996|2997|2998|2999|3000|3001|3002|3003|3004|3005|3006|3007|3008|3009|3010|3011|52141501SD03267|52141501SD03268|3267|3268':'DEMO : VIDEO FOR EON ALPHA',
'RCIM|52141501SD02365|52141501SD02366|52141501SD02367|52141501SD02449|52141501SD02450|52141501SD02451|52141501SD02452|52141501SD02453|52141501SD02469|52141501SD02470|52141501SD02471|52141501SD02472|52141501SD02473|52141501SD02503|52141501SD02504|52141501SD02520|52141501SD02521|2365|2366|2367|2449|2450|2451|2452|2453|2469|2470|2471|2472|2473|2503|2504|2520|2521':'RT EON VALOR RCIM (SPIN REFRESH MECHANICAL) DEMO',
'326 HCF|326 HCI|346 HCF |346 HCI |366 HCF |366 HCI |52141501SD01847|52141501SD01854|52141501SD01855|52141501SD01856|52141501SD01857|52141501SD01858|52141501SD01859|52141501SD01860|52141501SD01861|52141501SD02439|52141501SD02440|52141501SD02441|1847|1854|1855|1856|1857|1858|1859|1860|1861|2439|2440|2441':'DEMO : RT EONVIBE OR RT EONVALOR 326/346/366 HCF/HCI  & RCF/RCI',
'SET PCB|52141501SD01515|52141501SD01516|52141501SD01552|52141501SD01553|52141501SD01680|52141501SD01690|52141501SD01718|52141501SD02094|1515|1516|1552|1553|1680|1690|1718|2094':'DEMO : SPIN - TOP DISPLAY (EON WITH DISPLAY AT TOP)',
'40101701SD00758|0886|GTC|E5':'E5 AC GSC GTC',
'BLINKS|BLINK':'PCB BLINKS',
}

linkpairs = {
'EON ALPHA|ALPHA|52141501SD02292|52141501SD02293|52141501SD02294|52141501SD02988|52141501SD02989|52141501SD02990|52141501SD02991|52141501SD02992|52141501SD02993|52141501SD02994|52141501SD02995|52141501SD02996|52141501SD02997|52141501SD02998|52141501SD02999|52141501SD03000|52141501SD03001|52141501SD03002|52141501SD03003|52141501SD03004|52141501SD03005|52141501SD03006|52141501SD03007|52141501SD03008|52141501SD03009|52141501SD03010|52141501SD03011|2292|2293|2294|2988|2989|2990|2991|2992|2993|2994|2995|2996|2997|2998|2999|3000|3001|3002|3003|3004|3005|3006|3007|3008|3009|3010|3011|52141501SD03267|52141501SD03268|3267|3268':'https://youtu.be/12iKWqmqqu8',
'RCIM|52141501SD02365|52141501SD02366|52141501SD02367|52141501SD02449|52141501SD02450|52141501SD02451|52141501SD02452|52141501SD02453|52141501SD02469|52141501SD02470|52141501SD02471|52141501SD02472|52141501SD02473|52141501SD02503|52141501SD02504|52141501SD02520|52141501SD02521|2365|2366|2367|2449|2450|2451|2452|2453|2469|2470|2471|2472|2473|2503|2504|2520|2521':'https://youtu.be/2w_DEcI6g7w',
'326 HCF|326 HCI|346 HCF |346 HCI |366 HCF |366 HCI |52141501SD01847|52141501SD01854|52141501SD01855|52141501SD01856|52141501SD01857|52141501SD01858|52141501SD01859|52141501SD01860|52141501SD01861|52141501SD02439|52141501SD02440|52141501SD02441|1847|1854|1855|1856|1857|1858|1859|1860|1861|2439|2440|2441':'https://youtu.be/4hvd3AosG5Q',
'SET PCB|52141501SD01515|52141501SD01516|52141501SD01552|52141501SD01553|52141501SD01680|52141501SD01690|52141501SD01718|52141501SD02094|1515|1516|1552|1553|1680|1690|1718|2094':'https://youtu.be/9JvQiyKUvaU',
'40101701SD00758|0886|GTC|E5':'e5_ac_gsc_gtc.png',
'BLINKS|BLINK':'blinks.png',
}

@app.route('/')
def index():
    search_query = request.args.get('search', '').lower()
    if search_query:
        filtered_titles = {key: value for key, value in titlepairs.items() if search_query in value.lower()}
    else:
        filtered_titles = titlepairs

    # Filter linkpairs to include only those keys that are present in filtered_titles
    filtered_linkpairs = {key: linkpairs[key] for key in filtered_titles if key in linkpairs}

    # Determine if each linkpair value is a URL or an image
    link_info = {}
    for key, value in filtered_linkpairs.items():
        if value.startswith('http://') or value.startswith('https://'):
            # It's a URL, not an image
            link_info[key] = {'is_url': True, 'url': value}
        else:
            # It's an image file
            link_info[key] = {'is_url': False, 'url': url_for('detail', filename=value)}

    return render_template('index.html', titles=filtered_titles, link_info=link_info, search_query=search_query)





@app.route('/detail/<filename>')
def detail(filename):

    # Find the key in linkpairs that corresponds to the filename
    key_for_filename = next((key for key, value in linkpairs.items() if value == filename), None)

    # Use the found key to get the title from titlepairs
    title = titlepairs.get(key_for_filename, "Unknown Error") if key_for_filename else "Unknown Error"

    # Generate the full path for the image file
    image_path = url_for('static', filename=f'images/{filename}')

    return render_template('detail.html', image_path=image_path, title=title)


if __name__ == '__main__':
    app.run(debug=True)

