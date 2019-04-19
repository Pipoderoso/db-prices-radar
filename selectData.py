import json
import os

# IBNR
ids = {
    "8000191":  "Karlsruhe",
    "8011160":  "Berlin" 
}

file = 'data.json'
exists = os.path.isfile(file)

if exists:
    with open('data.json') as f:
        data = [json.loads(line) for line in f]
    
    # Get number of unique routes
    routes = set([item["route"]["origin"] + "_" + item["route"]["destination"] for item in data])
    priceCalendars = [dict(route=x, price=[], time=[]) for x in routes]
    
    requestDate = data[0]["requestDate"].split(".")[0]
    for i, item in enumerate(data):
        for calendar in priceCalendars:
            if(calendar["route"] == item["route"]["origin"] + "_" + item["route"]["destination"]):
                if(not item["data"]):
                    continue          
                minPricedItem = min(item["data"], key=lambda x:x['price']["amount"]) # Returns the item with lowest price
                calendar["price"].append(minPricedItem["price"]["amount"])       
                calendar["time"].append(minPricedItem["legs"][0]["departure"].split(".")[0])
    
     
    # for calendar in priceCalendars:
    #     if(len(calendar["price"]) != len(calendar["time"])):  
    #         with open('priceCalendar.txt', 'w') as outfile:  
    #             outfile.write("ERROR: prices list do not match times list")       
    
    with open("priceCalendar.txt", "w") as outfile:
        outfile.write("Request Date: {}\n\n\n".format(requestDate))
        for item in priceCalendars:
            origin = ids[item["route"].split("_")[0]]
            destination = ids[item["route"].split("_")[1]]
            routeName = "From:\t{}\nTo:  \t{}\n\n".format(origin, destination)
            
            outfile.write(routeName)         
            header = "{:^24}{:^6}\n".format("Date", "Price")
            outfile.write(header)      
            template = "{:^24}{:^6}\n"
            for i in range(len(item["price"])):
                outfile.write(template.format(item["time"][i], item["price"][i]))
            outfile.write("\n{}\n\n".format(30*'-'))
        
else:
    with open('priceCalendar.txt', 'w') as outfile:  
        outfile.write("ERROR: data.json Not found")
