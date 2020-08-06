import pandas as pd
import requests as r
import json
import time

base_url = 'https://api.godaddy.com/v1/appraisal/'

inl_domains = ['aeromediadigest.co.uk', 'aeromediadigest.com', 'aerospacepartnership.co.uk', 'aerospacepartnership.com', 'automediadigest.co.uk', 'automotiveclub.co.uk', 'automotiveclub.org.uk', 'automotivecommunication.co.uk', 'automotiveintelligence.co.uk', 'automotivepartnership.co.uk', 'automotivepartnership.com', 'biztroduce.co.uk', 'biztroduce.com', 'biztroduction.co.uk', 'blitheringidiot.co.uk', 'boatandskipper.co.uk', 'busandcoachtechnology.co.uk', 'busandcoachtechnology.com', 'businessmeetingacademy.co.uk', 'businesswritingcademy.co.uk', 'carandvannews.co.uk', 'carandvannews.com', 'coachmakers.co.uk', 'coachmakers.com', 'commercialvehicleengineer-uk.co.uk', 'commercialvehicleengineer-uk.com', 'compare-all-cameras.co.uk', 'compare-all-cars.co.uk', 'compare-all-insurance.co.uk', 'compare-all-vans.co.uk', 'compareallcameras.co.uk', 'compareallcaravans.co.uk', 'compareallcaravans.com', 'compareallcars.co.uk', 'compareallinsurance.co.uk', 'compareallvans.co.uk', 'cvengineer.co.uk', 'cvengineer.com', 'drivendata.co.uk', 'financemediadigest.co.uk', 'financemediadigest.com', 'immediatenetwork.co.uk', 'immediatenetwork.com', 'immediatenetworks.co.uk', 'inl.co.uk', 'inl.uk', 'inlcoaching.co.uk', 'inlcoaching.com', 'inlgroup.co.uk', 'inlserver.com', 'inluk.com', 'iybltd.com', 'livingin.ltd.uk', 'livinginavon.co.uk', 'livinginbedfordshire.co.uk', 'livinginbelfast.co.uk', 'livinginberkshire.co.uk', 'livinginbuckinghamshire.co.uk', 'livinginbucks.co.uk', 'livingincambridgeshire.co.uk', 'livingincentrallondon.co.uk', 'livingincheshire.co.uk', 'livingincleveland.co.uk', 'livingincornwall.co.uk', 'livingincumberland.co.uk', 'livinginderbyshire.co.uk', 'livingindev.co.uk', 'livingindevonshire.co.uk', 'livingindorset.co.uk', 'livingindurham.co.uk', 'livingineastanglia.co.uk', 'livingineastlothian.co.uk', 'livingineastmidlands.co.uk', 'livingineastsussex.co.uk', 'livinginedinburgh.co.uk', 'livinginessex.co.uk', 'livingingloucestershire.co.uk', 'livingingrampians.co.uk', 'livingingreaterlondon.co.uk', 'livingingreatermanchester.co.uk', 'livinginhampshire.co.uk', 'livinginhants.co.uk', 'livinginherefordshire.co.uk', 'livinginhertfordshire.co.uk', 'livinginherts.co.uk', 'livinginhomecounties.co.uk', 'livinginhumberside.co.uk', 'livinginhuntingdonshire.co.uk', 'livinginisleofman.co.uk', 'livinginisleofwight.co.uk', 'livinginkentandeastsussex.co.uk', 'livinginkentandsussex.co.uk', 'livinginlakedistrict.co.uk', 'livinginlanarkshire.co.uk', 'livinginlancashire.co.uk', 'livinginleicestershire.co.uk', 'livinginlincolnshire.co.uk', 'livinginlothian.co.uk', 'livinginmerseyside.co.uk', 'livinginmiddlesex.co.uk', 'livinginmidlothian.co.uk', 'livinginmidwales.co.uk', 'livinginnorfolk.co.uk', 'livinginnorthamptonshire.co.uk', 'livinginnorthants.co.uk', 'livinginnorthernireland.co.uk', 'livinginnorthumberland.co.uk', 'livinginnorthwales.co.uk', 'livinginnottinghamshire.co.uk',
               'livinginnotts.co.uk', 'livinginoxfordshire.co.uk', 'livinginperthshire.co.uk', 'livinginrutland.co.uk', 'livinginscotland.co.uk', 'livinginshropshire.co.uk', 'livinginsidethem25.co.uk', 'livinginsomerset.co.uk', 'livinginstaffordshire.co.uk', 'livinginstaffs.co.uk', 'livinginsuffolk.co.uk', 'livinginsurrey.co.uk', 'livinginsussex.co.uk', 'livingintayside.co.uk', 'livinginteeside.co.uk', 'livinginteesside.co.uk', 'livinginthecotswolds.co.uk', 'livinginthehighlands.co.uk', 'livinginthehighlandsandislands.co.uk', 'livinginthehomecounties.co.uk', 'livingintheisleofwight.co.uk', 'livinginthewestcountry.co.uk', 'livinginthewesternisles.co.uk', 'livinginthewestmidlands.co.uk', 'livingintyneandwear.co.uk', 'livingintyneside.co.uk', 'livinginwales.co.uk', 'livinginwarwickshire.co.uk', 'livinginwestmorland.co.uk', 'livinginwestsussex.co.uk', 'livinginwilts.co.uk', 'livinginwiltshire.co.uk', 'livinginworcestershire.co.uk', 'livinginworcs.co.uk', 'livinginyorks.co.uk', 'livinginyorkshire.co.uk', 'livinginyourtown.co.uk', 'livingonthewirral.co.uk', 'manandtoy.com', 'moneyandmotors.co.uk', 'moneyandmotors.com', 'moneymediadigest.co.uk', 'moneymediadigest.com', 'motorsandmoney.co.uk', 'motorsandmoney.com', 'motorweek.co.uk', 'mybrandtoolkit.co.uk', 'mybrandtoolkit.com', 'navitas-brokers.com', 'navitasbrokers.com', 'newbikeinfo.co.uk', 'newcarinfo.co.uk', 'newtruckinfo.co.uk', 'newvaninfo.co.uk', 'perrenproperties.co.uk', 'perrenproperty.co.uk', 'perrenproperty.com', 'planeandpilot.co.uk', 'poolepowerboats.co.uk', 'poolepowerboats.com', 'rayhutton.co.uk', 'rayhutton.com', 'reviewsandsources.co.uk', 'reviewsandsources.com', 'shipsandshipping.co.uk', 'simplynewsletters.co.uk', 'speechwritingacademy.co.uk', 'speechwritingacademy.com', 'styleinsurrey.co.uk', 'the4wdexpert.co.uk', 'the4wdexpert.com', 'the4x4expert.co.uk', 'the4x4expert.com', 'theaeroexpert.co.uk', 'theaeroexpert.com', 'theaerospaceexpert.co.uk', 'theaerospaceexpert.com', 'theautoexpert.co.uk', 'thebikeexpert.co.uk', 'theboatexpert.co.uk', 'thebusexpert.co.uk', 'thebusexpert.com', 'thecarexpert.co.in', 'thecarexpert.co.uk', 'thecarexpert.com', 'thecarexpert.com.au', 'thecarexpert.in', 'thecarexpert.net', 'thecarexpert.news', 'thecarexpert.org', 'thecarexpert.reviews', 'thecarexpert.uk', 'thecomponentexpert.co.uk', 'thecomponentexpert.com', 'thecycleexpert.co.uk', 'thecycleexpert.com', 'thefamilynetwork.co.uk', 'thelogisticsexpert.co.uk', 'thelogisticsexpert.com', 'thereviewbank.co.uk', 'thereviewbank.com', 'thesupplychainexpert.co.uk', 'thesuvexpert.co.uk', 'thesuvexpert.com', 'thetaxiexpert.co.uk', 'thetaxiexpert.com', 'thetireexpert.com', 'thetransportexpert.co.uk', 'thetransportexpert.com', 'thetruckexpert.co.uk', 'thetruckexpert.com', 'thetyreexpert.co.uk', 'thetyreexpert.com', 'thevanexpert.co.uk', 'thevanexpert.com', 'thevehicleexpert.co.uk', 'tuffkit.co.uk', 'tuffkit.com', 'vanfacts.co.uk']

to_value = inl_domains.copy()

responses = []

while len(to_value) > 0:
    for domain in to_value:
        response = r.get(base_url + domain)
        if response.status_code == 200:
            responses.append(response.json())
            to_value.remove(domain)
        else:
            time.sleep(5)
            continue


r_df = pd.DataFrame(responses)

r_df['status'].value_counts()

r_df.to_csv('valued_domains.csv')

oks = list(ok['domain'])

not_oks = [x for x in inl_domains if x not in oks]

next_pass = r_df[next_run_mask]

len(inl_domains)
