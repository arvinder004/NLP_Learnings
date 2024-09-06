import csv

# Museum data for Tamil Nadu with Google Maps latitude and longitude
museum_data = [
    {
        'Museum Name': 'Government Museum',
        'City': 'Chennai',
        'Address': 'Pantheon Rd, Egmore, Chennai, Tamil Nadu 600008',
        'Opening Hours': '9:30 AM - 5:00 PM',
        'Entry Fee': '₹15 (Indian), ₹250 (Foreigner)',
        'Phone Number': '044-28193238',
        'Email': 'gmc@tn.gov.in',
        'Website': 'https://www.governmentmuseumchennai.com/',
        'Latitude': 13.0735,
        'Longitude': 80.2605,
        'Type of Museum': 'History, Archaeology',
        'Year Established': 1851,
        'Popular Exhibits': 'Bronze Gallery, Amaravati Art',
        'Nearest Landmark': 'Near Egmore Railway Station'
    },
    {
        'Museum Name': 'DakshinaChitra',
        'City': 'Chennai',
        'Address': 'East Coast Road, Muttukadu, Tamil Nadu 603104',
        'Opening Hours': '10:00 AM - 6:00 PM',
        'Entry Fee': '₹100',
        'Phone Number': '044-27472603',
        'Email': 'info@dakshinachitra.net',
        'Website': 'https://www.dakshinachitra.net/',
        'Latitude': 12.7957,
        'Longitude': 80.2498,
        'Type of Museum': 'Cultural, Heritage',
        'Year Established': 1996,
        'Popular Exhibits': 'South Indian Heritage Village',
        'Nearest Landmark': 'Near Muttukadu Lake'
    },
    {
        'Museum Name': 'Gandhi Memorial Museum',
        'City': 'Madurai',
        'Address': 'Tamukkam Rd, Madurai, Tamil Nadu 625020',
        'Opening Hours': '10:00 AM - 1:00 PM, 2:00 PM - 5:45 PM',
        'Entry Fee': 'Free',
        'Phone Number': '0452-2531060',
        'Email': 'gmm@tn.gov.in',
        'Website': 'https://gandhimuseum.org/',
        'Latitude': 9.9296,
        'Longitude': 78.1217,
        'Type of Museum': 'History',
        'Year Established': 1959,
        'Popular Exhibits': 'Mahatma Gandhi Artifacts',
        'Nearest Landmark': 'Near Tamukkam Grounds'
    },
    {
        'Museum Name': 'Fort St. George Museum',
        'City': 'Chennai',
        'Address': 'Rajaji Salai, Chennai, Tamil Nadu 600009',
        'Opening Hours': '9:00 AM - 5:00 PM',
        'Entry Fee': '₹5',
        'Phone Number': '044-25671127',
        'Email': 'fortmuseum@tn.gov.in',
        'Website': 'https://www.tnmuseum.com/fort-st-george-museum',
        'Latitude': 13.0809,
        'Longitude': 80.2891,
        'Type of Museum': 'History, Colonial Era',
        'Year Established': 1948,
        'Popular Exhibits': 'Colonial Era Artifacts',
        'Nearest Landmark': 'Near Fort St. George'
    },
    {
        'Museum Name': 'Chennai Rail Museum',
        'City': 'Chennai',
        'Address': '2A, ICF Colony, Ayanavaram, Chennai, Tamil Nadu 600038',
        'Opening Hours': '10:00 AM - 5:00 PM',
        'Entry Fee': '₹40',
        'Phone Number': '044-26144249',
        'Email': 'crm@tn.gov.in',
        'Website': 'https://www.chennairailmuseum.in/',
        'Latitude': 13.1041,
        'Longitude': 80.2197,
        'Type of Museum': 'Railways',
        'Year Established': 2002,
        'Popular Exhibits': 'Vintage Locomotives, Heritage Trains',
        'Nearest Landmark': 'Near Integral Coach Factory'
    },
    {
        'Museum Name': 'Government Museum, Pudukkottai',
        'City': 'Pudukkottai',
        'Address': 'Thirukokarnam, Pudukkottai, Tamil Nadu 622001',
        'Opening Hours': '9:00 AM - 5:00 PM',
        'Entry Fee': '₹5',
        'Phone Number': '04322-222220',
        'Email': 'pdkmuseum@tn.gov.in',
        'Website': 'https://www.tnmuseum.com/pudukottai-museum',
        'Latitude': 10.3797,
        'Longitude': 78.8206,
        'Type of Museum': 'History, Archaeology',
        'Year Established': 1910,
        'Popular Exhibits': 'Artifacts from Early Historic Period',
        'Nearest Landmark': 'Near Thirukokarnam Temple'
    }
]

# Write data to CSV
with open('museums_tamil_nadu.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Museum Name', 'City', 'Address', 'Opening Hours', 'Entry Fee', 'Phone Number', 'Email', 'Website', 'Latitude', 'Longitude', 'Type of Museum', 'Year Established', 'Popular Exhibits', 'Nearest Landmark']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for museum in museum_data:
        writer.writerow(museum)

print("Museum data has been written to 'museums_tamil_nadu.csv'.")
