# top true snow overall as based on the following data source: https://www.zrankings.com/ski-resorts/snow for ski areas in western north america(all that matters)
#use no sql to store this data, each as a document 
# if this is just for ski area crawler, make it a separate entity for storing ski area data to crawl, on a frontend db using something fast, cut down on connections
top_ski_areas = [
        {"state": "utah", "ski_areas":[{"domain_name": "https://alta.com/", "snow_data_url": "conditions/daily-mountain-report/snow-report#snow-report"}]}, #alta = 12/24hr/base data in inches/cm/ base is mid moutain
        {"state":"wyoming", "ski_areas":[{"domain_name": "https://www.grandtarghee.com/", "snow_data_url": "the-mountain/snow-report"}]}, # targhee = 24/48/72hr/base data in inches the-mountain/snow-report/
        {"state": "new_mexico", "ski_areas":[{"domain_name":"https://www.skitaos.com/","snow_data_url": "ski-ride/cams-conditions"}]}, # taos 24hr/base both in inches
        {"state":"colorado", "ski_areas":[{"domain_name":"https://wolfcreekski.com/", "snow_data_url": "snow-report-page"}]}, #wolf creek has 24hr and mid moutain base depth in inches
        {"state": "california", "ski_areas":[{"domain_name":"https://www.kirkwood.com/", "snow_data_url": "the-mountain/mountain-conditions/snow-and-weather-report.aspx"}]}, # have inches/cm for 24hr and base mid mountain totals
        {"state": "washington", "ski_areas":[{"domain_name":"https://www.mtbaker.us/","snow_data_url":"snow-report"}]}, # have inches of 24hr totals and base totals
        {"state": "british_columbia", "ski_areas": [{"domain_name":"https://ski.powderking.com/", "snow_data_url": "ski-report"}]}, # have cm of 24hr and base totals
        {"state":"alaska", "ski_areas":[{"domain_name":"http://www.alyeskaresort.com/", "snow_data_url": "snow-report"}]}, # inches of 24hr/base totals
        {"state":"idaho" ,"ski_areas":[{"domain_name":"https://skilookout.com/", "snow_data_url": "snow-report"}]}, # inches total of 24hr and base
        {"state":"oregon",  "ski_areas":[{"domain_name": "https://www.mtbachelor.com/", "snow_data_url": "conditions-report"}]}, # have base and midmoutain totals, both in inches, as well as 24 hr totals
        {"state":"alberta", "ski_areas": [{"domain_name":"https://www.skibanff.com/", "snow_data_url": "conditions"}]}, # have 24 and base totals in inches and cm
        {"state":"montana", "ski_areas":[{"domain_name":"https://www.losttrail.com/", "snow_data_url": "snow-report"}]}, # have 24 base base in inches
        {"state":"nevada", "ski_areas":[{"domain_name": "https://skirose.com/", "snow_data_url": "snow-report"}]}, # have totals in inches with "new snow" and base depth average
        {"state":"arizona", "ski_areas": [{"domain_name":"https://www.snowbowl.ski/", "snow_data_url":"snow-report"}]}, # have totals in inches with 24 totals and base totals
    ]      