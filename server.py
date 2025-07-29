import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/s.mahmoud97/api/zillow56'

mcp = FastMCP('zillow56')

@mcp.tool()
def search(location: Annotated[str, Field(description='Location can be an address, neighborhood, city, or ZIP code.')],
           page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           output: Annotated[Literal['json', 'csv', 'xlsx', None], Field(description='Output format possible values : json (Default value) :Data in a JSON format csv : URL to the generated CSV file xlsx : URL to the generated XLSX (excel) file')] = None,
           status: Annotated[Literal['forSale', 'forRent', 'recentlySold', None], Field(description='Status type of the properties Default : forSale -forSale -forRent -recentlySold')] = None,
           sortSelection: Annotated[Literal['priorityscore', 'saved', 'listingstatus', 'mostrecentchange', 'globalrelevanceex', 'featured', 'priced', 'pricea', 'paymentd', 'paymenta', 'days', 'beds', 'baths', 'size', 'lot', 'zest', 'zesta', None], Field(description='Sorting possible values : days: Newest (Default value), saved: Date Saved, listingstatus: Listing Status, mostrecentchange: Most Recent Change, globalrelevanceex: Homes for You, featured: Verified Source, priced: Price (High to Low), pricea: Price (Low to High), paymentd: Payment (High to Low), paymenta: Payment (Low to High), beds: Bedrooms, baths: Bathrooms, size: Square Feet, lot: Lot Size, zest: Zestimate (High to Low), zesta: Zestimate (Low to High),')] = None,
           listing_type: Annotated[Literal['by_agent', 'by_owner_other', None], Field(description='Listing Type possible values : by_agent : By agent (Default value) by_owner_other : By owner & other (for off market properties)')] = None,
           isSingleFamily: Annotated[Union[bool, None], Field(description='')] = None,
           isMultiFamily: Annotated[Union[bool, None], Field(description='')] = None,
           isApartment: Annotated[Union[bool, None], Field(description='')] = None,
           isCondo: Annotated[Union[bool, None], Field(description='')] = None,
           isManufactured: Annotated[Union[bool, None], Field(description='')] = None,
           isTownhouse: Annotated[Union[bool, None], Field(description='')] = None,
           isLotLand: Annotated[Union[bool, None], Field(description='')] = None,
           doz: Annotated[Literal['any', '1', '7', '14', '30', '90', '6m', '12m', '24m', '36m', None], Field(description='Days on Zillow (For Sale/Rent listings)/ Sold In Last (Sold listings) Possible values : any: Any, 1: 1 day, 7: 7 days, 14: 14 days, 30: 30 days, 90: 90 days, 6m: 6 months, 12m: 12 months, 24m: 24 months, 36m: 36 months')] = None,
           price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           monthlyPayment_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           monthlyPayment_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           beds_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           hoa_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           hoa_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           hasPool: Annotated[Union[bool, None], Field(description='')] = None,
           hasGarage: Annotated[Union[bool, None], Field(description='')] = None,
           built_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           built_max: Annotated[Union[str, None], Field(description='')] = None,
           isForSaleByOwner: Annotated[Union[bool, None], Field(description='')] = None,
           isForSaleByAgent: Annotated[Union[bool, None], Field(description='')] = None,
           isCityView: Annotated[Union[bool, None], Field(description='')] = None,
           isWaterfront: Annotated[Union[bool, None], Field(description='')] = None,
           isPublicSchool: Annotated[Union[bool, None], Field(description='')] = None,
           isPrivateSchool: Annotated[Union[bool, None], Field(description='')] = None,
           isMountainView: Annotated[Union[bool, None], Field(description='')] = None,
           singleStory: Annotated[Union[bool, None], Field(description='')] = None,
           onlyPriceReduction: Annotated[Union[bool, None], Field(description='')] = None,
           onlyRentalAcceptsApplications: Annotated[Union[bool, None], Field(description='')] = None,
           isZillowOwnedOnly: Annotated[Union[bool, None], Field(description='')] = None,
           hasAirConditioning: Annotated[Union[bool, None], Field(description='')] = None,
           isMiddleSchool: Annotated[Union[bool, None], Field(description='')] = None,
           isWaterView: Annotated[Union[bool, None], Field(description='')] = None,
           onlyRentalIncomeRestricted: Annotated[Union[bool, None], Field(description='')] = None,
           isComingSoon: Annotated[Union[bool, None], Field(description='')] = None,
           isForSaleForeclosure: Annotated[Union[bool, None], Field(description='')] = None,
           onlyWithPhotos: Annotated[Union[bool, None], Field(description='')] = None,
           onlyRentalCatsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
           onlyRentalPetsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
           onlyRentalSmallDogsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
           onlyRentalLargeDogsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
           isAuction: Annotated[Union[bool, None], Field(description='')] = None,
           is3dHome: Annotated[Union[bool, None], Field(description='')] = None,
           isNewConstruction: Annotated[Union[bool, None], Field(description='')] = None,
           parkingSpots_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           greatSchoolsRating_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           isElementarySchool: Annotated[Union[bool, None], Field(description='')] = None,
           isParkView: Annotated[Union[bool, None], Field(description='')] = None,
           enableSchools: Annotated[Union[bool, None], Field(description='')] = None,
           lotSize_min: Annotated[Union[int, float, None], Field(description='in sqft Default: 0')] = None,
           lotSize_max: Annotated[Union[int, float, None], Field(description='in sqft Default: 0')] = None,
           keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for filtered properties by neighborhood, city, or ZIP code. PS : To search for an address of a property, use the "/search_address" endpoint. For a list of properties, you can select the output format (JSON , CSV , XLSX) using the optional "output" parameter.'''
    url = 'https://zillow56.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'page': page,
        'output': output,
        'status': status,
        'sortSelection': sortSelection,
        'listing_type': listing_type,
        'isSingleFamily': isSingleFamily,
        'isMultiFamily': isMultiFamily,
        'isApartment': isApartment,
        'isCondo': isCondo,
        'isManufactured': isManufactured,
        'isTownhouse': isTownhouse,
        'isLotLand': isLotLand,
        'doz': doz,
        'price_min': price_min,
        'price_max': price_max,
        'sqft_min': sqft_min,
        'sqft_max': sqft_max,
        'monthlyPayment_min': monthlyPayment_min,
        'monthlyPayment_max': monthlyPayment_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'hoa_min': hoa_min,
        'hoa_max': hoa_max,
        'hasPool': hasPool,
        'hasGarage': hasGarage,
        'built_min': built_min,
        'built_max': built_max,
        'isForSaleByOwner': isForSaleByOwner,
        'isForSaleByAgent': isForSaleByAgent,
        'isCityView': isCityView,
        'isWaterfront': isWaterfront,
        'isPublicSchool': isPublicSchool,
        'isPrivateSchool': isPrivateSchool,
        'isMountainView': isMountainView,
        'singleStory': singleStory,
        'onlyPriceReduction': onlyPriceReduction,
        'onlyRentalAcceptsApplications': onlyRentalAcceptsApplications,
        'isZillowOwnedOnly': isZillowOwnedOnly,
        'hasAirConditioning': hasAirConditioning,
        'isMiddleSchool': isMiddleSchool,
        'isWaterView': isWaterView,
        'onlyRentalIncomeRestricted': onlyRentalIncomeRestricted,
        'isComingSoon': isComingSoon,
        'isForSaleForeclosure': isForSaleForeclosure,
        'onlyWithPhotos': onlyWithPhotos,
        'onlyRentalCatsAllowed': onlyRentalCatsAllowed,
        'onlyRentalPetsAllowed': onlyRentalPetsAllowed,
        'onlyRentalSmallDogsAllowed': onlyRentalSmallDogsAllowed,
        'onlyRentalLargeDogsAllowed': onlyRentalLargeDogsAllowed,
        'isAuction': isAuction,
        'is3dHome': is3dHome,
        'isNewConstruction': isNewConstruction,
        'parkingSpots_min': parkingSpots_min,
        'greatSchoolsRating_min': greatSchoolsRating_min,
        'isElementarySchool': isElementarySchool,
        'isParkView': isParkView,
        'enableSchools': enableSchools,
        'lotSize_min': lotSize_min,
        'lotSize_max': lotSize_max,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_address(address: Annotated[str, Field(description='')]) -> dict: 
    '''Search for a property by address.'''
    url = 'https://zillow56.p.rapidapi.com/search_address'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'address': address,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_polygon(polygon: Annotated[str, Field(description='It is required if the location is empty. Format: lat lng,lat1 lng1,lat2 lng2 34.03959576441558 -118.50636536779786,34.0418716916327 -118.50276047888184,34.042440663894304 -118.49846894445801,34.04201393505594 -118.49417741003418,34.04087598099002 -118.4897142142334,34.03945351693672 -118.48525101843262,34.03788877892429 -118.48095948400879,34.03618175908096 -118.47683961096192,34.034190192514366 -118.47271973791504,34.031629538228394 -118.46962983312989,34.02835747861639 -118.4677415579834,34.02465847668084 -118.46671158972168,34.02081703478521 -118.46636826696778,34.01697541902413 -118.46636826696778,34.01341821237762 -118.4673982352295,34.011283816847104 -118.47100312414551,34.01057233974687 -118.47563798132325,34.01043004361143 -118.47992951574707,34.01071463564384 -118.48439271154786,34.01156840601794 -118.48868424597168,34.01270675316253 -118.49297578039551,34.01398737545716 -118.49709565344239,34.01555255425154 -118.50104386511231,34.01754455825562 -118.50464875402832,34.02039019717532 -118.50756699743653,34.02352028980117 -118.50962693395996,34.02707707311613 -118.51065690222168,34.03063370735633 -118.50997025671387,34.034190192514366 -118.5091119498291,34.03774652858273 -118.50825364294434,34.03959576441558 -118.50636536779786 Last pair must be equal to first pair.')],
                   page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   output: Annotated[Literal['json', 'csv', 'xlsx', None], Field(description='Output format possible values : json (Default value) :Data in a JSON format csv : URL to the generated CSV file xlsx : URL to the generated XLSX (excel) file')] = None,
                   status: Annotated[Literal['forSale', 'forRent', 'recentlySold', None], Field(description='Status type of the properties Default : forSale -forSale -forRent -recentlySold')] = None,
                   sortSelection: Annotated[Literal['priorityscore', 'saved', 'listingstatus', 'mostrecentchange', 'globalrelevanceex', 'featured', 'priced', 'pricea', 'paymentd', 'paymenta', 'days', 'beds', 'baths', 'size', 'lot', 'zest', 'zesta', None], Field(description='Sorting possible values : days: Newest (Default value), saved: Date Saved, listingstatus: Listing Status, mostrecentchange: Most Recent Change, globalrelevanceex: Homes for You, featured: Verified Source, priced: Price (High to Low), pricea: Price (Low to High), paymentd: Payment (High to Low), paymenta: Payment (Low to High), beds: Bedrooms, baths: Bathrooms, size: Square Feet, lot: Lot Size, zest: Zestimate (High to Low), zesta: Zestimate (Low to High),')] = None,
                   listing_type: Annotated[Literal['by_agent', 'by_owner_other', None], Field(description='Listing Type possible values : by_agent : By agent (Default value) by_owner_other : By owner & other (for off market properties)')] = None,
                   isSingleFamily: Annotated[Union[bool, None], Field(description='')] = None,
                   isMultiFamily: Annotated[Union[bool, None], Field(description='')] = None,
                   isApartment: Annotated[Union[bool, None], Field(description='')] = None,
                   isCondo: Annotated[Union[bool, None], Field(description='')] = None,
                   isManufactured: Annotated[Union[bool, None], Field(description='')] = None,
                   isTownhouse: Annotated[Union[bool, None], Field(description='')] = None,
                   isLotLand: Annotated[Union[bool, None], Field(description='')] = None,
                   doz: Annotated[Literal['any', '1', '7', '14', '30', '90', '6m', '12m', '24m', '36m', None], Field(description='Days on Zillow (For Sale/Rent listings)/ Sold In Last (Sold listings) Possible values : any: Any, 1: 1 day, 7: 7 days, 14: 14 days, 30: 30 days, 90: 90 days, 6m: 6 months, 12m: 12 months, 24m: 24 months, 36m: 36 months')] = None,
                   price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   monthlyPayment_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   monthlyPayment_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   beds_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   hoa_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   hoa_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   hasPool: Annotated[Union[bool, None], Field(description='')] = None,
                   hasGarage: Annotated[Union[bool, None], Field(description='')] = None,
                   built_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   built_max: Annotated[Union[str, None], Field(description='')] = None,
                   isForSaleByOwner: Annotated[Union[bool, None], Field(description='')] = None,
                   isForSaleByAgent: Annotated[Union[bool, None], Field(description='')] = None,
                   isCityView: Annotated[Union[bool, None], Field(description='')] = None,
                   isWaterfront: Annotated[Union[bool, None], Field(description='')] = None,
                   isPublicSchool: Annotated[Union[bool, None], Field(description='')] = None,
                   isPrivateSchool: Annotated[Union[bool, None], Field(description='')] = None,
                   isMountainView: Annotated[Union[bool, None], Field(description='')] = None,
                   singleStory: Annotated[Union[bool, None], Field(description='')] = None,
                   onlyPriceReduction: Annotated[Union[bool, None], Field(description='')] = None,
                   onlyRentalAcceptsApplications: Annotated[Union[bool, None], Field(description='')] = None,
                   isZillowOwnedOnly: Annotated[Union[bool, None], Field(description='')] = None,
                   hasAirConditioning: Annotated[Union[bool, None], Field(description='')] = None,
                   isMiddleSchool: Annotated[Union[bool, None], Field(description='')] = None,
                   isWaterView: Annotated[Union[bool, None], Field(description='')] = None,
                   onlyRentalIncomeRestricted: Annotated[Union[bool, None], Field(description='')] = None,
                   isComingSoon: Annotated[Union[bool, None], Field(description='')] = None,
                   isForSaleForeclosure: Annotated[Union[bool, None], Field(description='')] = None,
                   onlyWithPhotos: Annotated[Union[bool, None], Field(description='')] = None,
                   onlyRentalCatsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
                   onlyRentalPetsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
                   onlyRentalSmallDogsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
                   onlyRentalLargeDogsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
                   isAuction: Annotated[Union[bool, None], Field(description='')] = None,
                   is3dHome: Annotated[Union[bool, None], Field(description='')] = None,
                   isNewConstruction: Annotated[Union[bool, None], Field(description='')] = None,
                   parkingSpots_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   greatSchoolsRating_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   isElementarySchool: Annotated[Union[bool, None], Field(description='')] = None,
                   isParkView: Annotated[Union[bool, None], Field(description='')] = None,
                   enableSchools: Annotated[Union[bool, None], Field(description='')] = None,
                   lotSize_max: Annotated[Union[int, float, None], Field(description='in sqft Default: 0')] = None,
                   keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for filtered properties by polygon coordinates. For a list of properties, you can select the output format (JSON , CSV , XLSX) using the optional "output" parameter.'''
    url = 'https://zillow56.p.rapidapi.com/search_polygon'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'polygon': polygon,
        'page': page,
        'output': output,
        'status': status,
        'sortSelection': sortSelection,
        'listing_type': listing_type,
        'isSingleFamily': isSingleFamily,
        'isMultiFamily': isMultiFamily,
        'isApartment': isApartment,
        'isCondo': isCondo,
        'isManufactured': isManufactured,
        'isTownhouse': isTownhouse,
        'isLotLand': isLotLand,
        'doz': doz,
        'price_min': price_min,
        'price_max': price_max,
        'sqft_min': sqft_min,
        'sqft_max': sqft_max,
        'monthlyPayment_min': monthlyPayment_min,
        'monthlyPayment_max': monthlyPayment_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'hoa_min': hoa_min,
        'hoa_max': hoa_max,
        'hasPool': hasPool,
        'hasGarage': hasGarage,
        'built_min': built_min,
        'built_max': built_max,
        'isForSaleByOwner': isForSaleByOwner,
        'isForSaleByAgent': isForSaleByAgent,
        'isCityView': isCityView,
        'isWaterfront': isWaterfront,
        'isPublicSchool': isPublicSchool,
        'isPrivateSchool': isPrivateSchool,
        'isMountainView': isMountainView,
        'singleStory': singleStory,
        'onlyPriceReduction': onlyPriceReduction,
        'onlyRentalAcceptsApplications': onlyRentalAcceptsApplications,
        'isZillowOwnedOnly': isZillowOwnedOnly,
        'hasAirConditioning': hasAirConditioning,
        'isMiddleSchool': isMiddleSchool,
        'isWaterView': isWaterView,
        'onlyRentalIncomeRestricted': onlyRentalIncomeRestricted,
        'isComingSoon': isComingSoon,
        'isForSaleForeclosure': isForSaleForeclosure,
        'onlyWithPhotos': onlyWithPhotos,
        'onlyRentalCatsAllowed': onlyRentalCatsAllowed,
        'onlyRentalPetsAllowed': onlyRentalPetsAllowed,
        'onlyRentalSmallDogsAllowed': onlyRentalSmallDogsAllowed,
        'onlyRentalLargeDogsAllowed': onlyRentalLargeDogsAllowed,
        'isAuction': isAuction,
        'is3dHome': is3dHome,
        'isNewConstruction': isNewConstruction,
        'parkingSpots_min': parkingSpots_min,
        'greatSchoolsRating_min': greatSchoolsRating_min,
        'isElementarySchool': isElementarySchool,
        'isParkView': isParkView,
        'enableSchools': enableSchools,
        'lotSize_max': lotSize_max,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_mls(mls: Annotated[str, Field(description='')]) -> dict: 
    '''Search for properties by their MLS ID.'''
    url = 'https://zillow56.p.rapidapi.com/search_mls'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'mls': mls,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_coordinates(lat: Annotated[Union[int, float], Field(description='Latitude Default: 34.01822')],
                       long: Annotated[Union[int, float], Field(description='Longitude Default: -118.504744')],
                       d: Annotated[Union[int, float], Field(description='Diameter in miles. Default: 1')],
                       page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       status: Annotated[Literal['forSale', 'forRent', 'recentlySold', None], Field(description='Status type of the properties Default : forSale -forSale -forRent -recentlySold')] = None,
                       output: Annotated[Literal['json', 'csv', 'xlsx', None], Field(description='Output format possible values : json (Default value) :Data in a JSON format csv : URL to the generated CSV file xlsx : URL to the generated XLSX (excel) file')] = None,
                       sort: Annotated[Literal['priorityscore', 'saved', 'listingstatus', 'mostrecentchange', 'globalrelevanceex', 'featured', 'priced', 'pricea', 'paymentd', 'paymenta', 'days', 'beds', 'baths', 'size', 'lot', 'zest', 'zesta', None], Field(description='Sorting possible values : priorityscore: Default, saved: Date Saved, listingstatus: Listing Status, mostrecentchange: Most Recent Change, globalrelevanceex: Homes for You, featured: Verified Source, priced: Price (High to Low), pricea: Price (Low to High), paymentd: Payment (High to Low), paymenta: Payment (Low to High), days: Newest, beds: Bedrooms, baths: Bathrooms, size: Square Feet, lot: Lot Size, zest: Zestimate (High to Low), zesta: Zestimate (Low to High),')] = None,
                       listing_type: Annotated[Literal['by_agent', 'by_owner_other', None], Field(description='Listing Type possible values : By agent (Default value) By owner & other (for off market properties)')] = None,
                       isSingleFamily: Annotated[Union[bool, None], Field(description='')] = None,
                       isMultiFamily: Annotated[Union[bool, None], Field(description='')] = None,
                       isApartment: Annotated[Union[bool, None], Field(description='')] = None,
                       isCondo: Annotated[Union[bool, None], Field(description='')] = None,
                       isManufactured: Annotated[Union[bool, None], Field(description='')] = None,
                       isTownhouse: Annotated[Union[bool, None], Field(description='')] = None,
                       isLotLand: Annotated[Union[bool, None], Field(description='')] = None,
                       doz: Annotated[Literal['any', '1', '7', '14', '30', '90', '6m', '12m', '24m', '36m', None], Field(description='Days on Zillow possible values : any: Any, 1: 1 day, 7: 7 days, 14: 14 days, 30: 30 days, 90: 90 days, 6m: 6 months, 12m: 12 months, 24m: 24 months, 36m: 36 months')] = None,
                       price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       monthlyPayment_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       monthlyPayment_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       beds_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       hoa_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       hoa_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       hasPool: Annotated[Union[bool, None], Field(description='')] = None,
                       hasGarage: Annotated[Union[bool, None], Field(description='')] = None,
                       built_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       built_max: Annotated[Union[str, None], Field(description='')] = None,
                       isForSaleByOwner: Annotated[Union[bool, None], Field(description='')] = None,
                       isForSaleByAgent: Annotated[Union[bool, None], Field(description='')] = None,
                       isCityView: Annotated[Union[bool, None], Field(description='')] = None,
                       isWaterfront: Annotated[Union[bool, None], Field(description='')] = None,
                       isPublicSchool: Annotated[Union[bool, None], Field(description='')] = None,
                       isPrivateSchool: Annotated[Union[bool, None], Field(description='')] = None,
                       isMountainView: Annotated[Union[bool, None], Field(description='')] = None,
                       singleStory: Annotated[Union[bool, None], Field(description='')] = None,
                       onlyPriceReduction: Annotated[Union[bool, None], Field(description='')] = None,
                       onlyRentalAcceptsApplications: Annotated[Union[bool, None], Field(description='')] = None,
                       isZillowOwnedOnly: Annotated[Union[bool, None], Field(description='')] = None,
                       hasAirConditioning: Annotated[Union[bool, None], Field(description='')] = None,
                       isMiddleSchool: Annotated[Union[bool, None], Field(description='')] = None,
                       isWaterView: Annotated[Union[bool, None], Field(description='')] = None,
                       onlyRentalIncomeRestricted: Annotated[Union[bool, None], Field(description='')] = None,
                       isComingSoon: Annotated[Union[bool, None], Field(description='')] = None,
                       isForSaleForeclosure: Annotated[Union[bool, None], Field(description='')] = None,
                       onlyWithPhotos: Annotated[Union[bool, None], Field(description='')] = None,
                       onlyRentalCatsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
                       onlyRentalPetsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
                       onlyRentalSmallDogsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
                       onlyRentalLargeDogsAllowed: Annotated[Union[bool, None], Field(description='')] = None,
                       isAuction: Annotated[Union[bool, None], Field(description='')] = None,
                       is3dHome: Annotated[Union[bool, None], Field(description='')] = None,
                       isNewConstruction: Annotated[Union[bool, None], Field(description='')] = None,
                       greatSchoolsRating_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                       isElementarySchool: Annotated[Union[bool, None], Field(description='')] = None,
                       isParkView: Annotated[Union[bool, None], Field(description='')] = None,
                       enableSchools: Annotated[Union[bool, None], Field(description='')] = None,
                       keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for filtered properties by coordinates. You can select the output format (JSON , CSV , XLSX) using the optional "output" parameter.'''
    url = 'https://zillow56.p.rapidapi.com/search_coordinates'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'long': long,
        'd': d,
        'page': page,
        'status': status,
        'output': output,
        'sort': sort,
        'listing_type': listing_type,
        'isSingleFamily': isSingleFamily,
        'isMultiFamily': isMultiFamily,
        'isApartment': isApartment,
        'isCondo': isCondo,
        'isManufactured': isManufactured,
        'isTownhouse': isTownhouse,
        'isLotLand': isLotLand,
        'doz': doz,
        'price_min': price_min,
        'price_max': price_max,
        'sqft_min': sqft_min,
        'sqft_max': sqft_max,
        'monthlyPayment_min': monthlyPayment_min,
        'monthlyPayment_max': monthlyPayment_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'hoa_min': hoa_min,
        'hoa_max': hoa_max,
        'hasPool': hasPool,
        'hasGarage': hasGarage,
        'built_min': built_min,
        'built_max': built_max,
        'isForSaleByOwner': isForSaleByOwner,
        'isForSaleByAgent': isForSaleByAgent,
        'isCityView': isCityView,
        'isWaterfront': isWaterfront,
        'isPublicSchool': isPublicSchool,
        'isPrivateSchool': isPrivateSchool,
        'isMountainView': isMountainView,
        'singleStory': singleStory,
        'onlyPriceReduction': onlyPriceReduction,
        'onlyRentalAcceptsApplications': onlyRentalAcceptsApplications,
        'isZillowOwnedOnly': isZillowOwnedOnly,
        'hasAirConditioning': hasAirConditioning,
        'isMiddleSchool': isMiddleSchool,
        'isWaterView': isWaterView,
        'onlyRentalIncomeRestricted': onlyRentalIncomeRestricted,
        'isComingSoon': isComingSoon,
        'isForSaleForeclosure': isForSaleForeclosure,
        'onlyWithPhotos': onlyWithPhotos,
        'onlyRentalCatsAllowed': onlyRentalCatsAllowed,
        'onlyRentalPetsAllowed': onlyRentalPetsAllowed,
        'onlyRentalSmallDogsAllowed': onlyRentalSmallDogsAllowed,
        'onlyRentalLargeDogsAllowed': onlyRentalLargeDogsAllowed,
        'isAuction': isAuction,
        'is3dHome': is3dHome,
        'isNewConstruction': isNewConstruction,
        'greatSchoolsRating_min': greatSchoolsRating_min,
        'isElementarySchool': isElementarySchool,
        'isParkView': isParkView,
        'enableSchools': enableSchools,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_url(url: Annotated[str, Field(description='')],
               page: Annotated[Union[int, float, None], Field(description='Default: 3')] = None,
               output: Annotated[Literal['json', 'csv', 'xlsx', None], Field(description='Output format possible values : json (Default value) :Data in a JSON format csv : URL to the generated CSV file xlsx : URL to the generated XLSX (excel) file')] = None,
               listing_type: Annotated[Literal['by_agent', 'by_owner_other', None], Field(description='Listing Type possible values : By agent (Default value) By owner & other (for off market properties)')] = None) -> dict: 
    '''Get a list of properties by providing the zillow search results URL You can select the output format (JSON , CSV , XLSX) using the optional "output" parameter.'''
    url = 'https://zillow56.p.rapidapi.com/search_url'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'page': page,
        'output': output,
        'listing_type': listing_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_v2_property_details_by_zpid(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url…), or from a property's URL.")] = None,
                                         url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None) -> dict: 
    '''Get a property's details by its zpid'''
    url = 'https://zillow56.p.rapidapi.com/propertyV2'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url…), or from a property's URL.")] = None,
             url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None) -> dict: 
    '''Get a property's details by its zpid'''
    url = 'https://zillow56.p.rapidapi.com/property'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def photos(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url…), or from a property's URL.")] = None,
           url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None) -> dict: 
    '''Returns a property's photos with different sizes and types.'''
    url = 'https://zillow56.p.rapidapi.com/photos'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def schools(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url…), or from a property's URL.")] = None,
            url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None) -> dict: 
    '''Nearby schools of a property by ZPID'''
    url = 'https://zillow56.p.rapidapi.com/schools'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def walk_transit_bike_score(zpid: Annotated[Union[int, float, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url…), or from a property's URL. Default: 20485700")] = None,
                            url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None) -> dict: 
    '''Get Walk, Transit and Bike Score of a property by zpid'''
    url = 'https://zillow56.p.rapidapi.com/walk_transit_bike_score'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def zestimate_history(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url…), or from a property's URL.")] = None,
                      url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None) -> dict: 
    '''Zestimate history by zpid'''
    url = 'https://zillow56.p.rapidapi.com/zestimate_history'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def price_tax_history(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url…), or from a property's URL.")] = None,
                      url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None) -> dict: 
    '''Price and Tax history of a property by ZPID'''
    url = 'https://zillow56.p.rapidapi.com/price_tax_history'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def rent_estimate(address: Annotated[str, Field(description='')],
                  activeTypes: Annotated[Union[str, None], Field(description='SimilarFloorPlans filter: Possible values: any (Default) active (Active Rentals) inactive (Inactive Rentals)')] = None,
                  activatedDays: Annotated[Union[str, None], Field(description='[SIMILARFLOORPLANS] Filter for Active Rentals within X days: Possible values: any (Default) 30 (Within 30 days) 15 (Within 15 days) 7 (Within 7 days)')] = None,
                  deactivatedDays: Annotated[Union[str, None], Field(description='[SIMILARFLOORPLANS] Filter for inactive rentals within X days: Possible values: 30 (Within 30 days (max)) 15 (Within 15 days) 7 (Within 7 days)')] = None,
                  distanceInMiles: Annotated[Union[str, None], Field(description='[SIMILARFLOORPLANS] Filter for distance in Miles: Possible values: any 1 2 3 4 5')] = None,
                  propertyTypes: Annotated[Union[str, None], Field(description='[SIMILARFLOORPLANS] Filter for Property Types: (To choose multiple values separate with comma eg : house,condo) Possible values: any (Default) apartment house townhouse condo')] = None,
                  bedrooms: Annotated[Union[str, None], Field(description='[SIMILARFLOORPLANS] Filter for number of bedrooms: (To choose multiple values separate with comma eg : 0,1,2) Possible values: 0 1 2 3 4plus')] = None,
                  pets: Annotated[Union[str, None], Field(description='[SIMILARFLOORPLANS] Filter for Pets: (To choose multiple values separate with comma eg : dogs,cats) Possible values: any (Default) dogs cats')] = None,
                  laundry: Annotated[Union[str, None], Field(description='[SIMILARFLOORPLANS] Filter for Laundry: (To choose multiple values separate with comma eg : inUnit,shared) Possible values: any (Default) inUnit shared')] = None,
                  amenities: Annotated[Union[str, None], Field(description='[SIMILARFLOORPLANS] Filter for amenities: (To choose multiple values separate with comma eg : cooling,parking) Possible values: any (Default) cooling heating parking')] = None) -> dict: 
    '''Returns a property's rent zestimate and it's comparable properties in the same area.'''
    url = 'https://zillow56.p.rapidapi.com/rent_estimate'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'address': address,
        'activeTypes': activeTypes,
        'activatedDays': activatedDays,
        'deactivatedDays': deactivatedDays,
        'distanceInMiles': distanceInMiles,
        'propertyTypes': propertyTypes,
        'bedrooms': bedrooms,
        'pets': pets,
        'laundry': laundry,
        'amenities': amenities,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def similar_properties(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url...), or from a property's URL.")] = None,
                       url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None,
                       address: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''List of similar for sale properties by Zpid or URL or address'''
    url = 'https://zillow56.p.rapidapi.com/similar_properties'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
        'address': address,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def similar_sold_properties(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url...), or from a property's URL.")] = None,
                            url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None,
                            address: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''List of similar sold properties by Zpid or URL or address'''
    url = 'https://zillow56.p.rapidapi.com/similar_sold_properties'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
        'address': address,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def similar_rent_properties(zpid: Annotated[Union[str, None], Field(description="The zpid can be extracted from the searching endpoints (/search , /search_url...), or from a property's URL.")] = None,
                            url: Annotated[Union[str, None], Field(description='Property details URL - eg :https://www.zillow.com/homedetails/15626-Laurel-Heights-Dr-Houston-TX-77084/28253016_zpid/')] = None,
                            address: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''List of similar for rent properties by Zpid or URL or address'''
    url = 'https://zillow56.p.rapidapi.com/similar_rent_properties'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'url': url,
        'address': address,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_sale_overview(location: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint delivers a comprehensive snapshot and historical trends of the housing market in a given region using metrics aligned with the Zillow Home Value Index (ZHVI) framework'''
    url = 'https://zillow56.p.rapidapi.com/market_sale_overview'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def zhvi_range(location: Annotated[str, Field(description='')],
               type: Annotated[Literal['all', 'single_family', 'condo', 'all_unadjusted', None], Field(description='Home type')] = None) -> dict: 
    '''This endpoint provides monthly historical data for the Zillow Home Value Index (ZHVI) for a specified region. The ZHVI is a proprietary metric that captures median home values across a wide variety of geographies and housing types, reflecting trends in the real estate market over time.'''
    url = 'https://zillow56.p.rapidapi.com/zhvi_range'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_data(location: Annotated[str, Field(description='')]) -> dict: 
    '''Get market rental data of a location by city or ZIP'''
    url = 'https://zillow56.p.rapidapi.com/market_data'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_for_agents(location: Annotated[str, Field(description='')],
                      name: Annotated[Union[str, None], Field(description='')] = None,
                      page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                      specialty: Annotated[Literal['Any', 'BuyersAgent', 'ListingAgent', 'Relocation', 'Foreclosure', 'ShortSale', 'Consulting', 'Other', None], Field(description='')] = None,
                      language: Annotated[Literal['English', 'Arabic', 'Bengali', 'Cantonese', 'Farsi', 'French', 'German', 'Greek', 'Hebrew', 'Hindi', 'Hungarian', 'Italian', 'Japanese', 'Korean', 'Mandarin', 'Polish', 'Portuguese', 'Russian', 'Spanish', 'Tagalog', 'Thai', 'Turkish', 'Vietnamese', None], Field(description='')] = None) -> dict: 
    '''Search for agents by location and name'''
    url = 'https://zillow56.p.rapidapi.com/search_agents'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'name': name,
        'page': page,
        'specialty': specialty,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_details_by_username(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get agent's details by username(contact infos, active listings and reviews etc). PS : username is the profile link Example : username : Pardee-Properties for https://www.zillow.com/profile/Pardee-Properties/'''
    url = 'https://zillow56.p.rapidapi.com/agent'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_reviews(zuid: Annotated[str, Field(description='')],
                  page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Get agent reviews by the agent's zuid'''
    url = 'https://zillow56.p.rapidapi.com/agent_reviews'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zuid': zuid,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_spast_sales(zuid: Annotated[str, Field(description='The zuid can be extracted from the agent\'s details \\"/agent\\"')],
                      page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Get agent's past sales by zuid'''
    url = 'https://zillow56.p.rapidapi.com/agent_past_sales'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zuid': zuid,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_sactive_listings(zuid: Annotated[str, Field(description='')],
                           page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Get agent's active listings by zuid'''
    url = 'https://zillow56.p.rapidapi.com/agent_active_listings'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zuid': zuid,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_srental_listings(zuid: Annotated[str, Field(description='')],
                           page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Get agent's rental listings by zuid'''
    url = 'https://zillow56.p.rapidapi.com/agent_rental_listings'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zuid': zuid,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lender_search(location: Annotated[str, Field(description='City, State or Zip. Only lenders licensed in the state will be displayed.')],
                  lenderName: Annotated[Union[str, None], Field(description='')] = None,
                  page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Search for Lenders'''
    url = 'https://zillow56.p.rapidapi.com/lender/search'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'lenderName': lenderName,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lender_details(screenName: Annotated[str, Field(description='')]) -> dict: 
    '''Get lender details'''
    url = 'https://zillow56.p.rapidapi.com/lender/details'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenName': screenName,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lender_reviews(screenName: Annotated[str, Field(description='')],
                   page: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get lender reviews'''
    url = 'https://zillow56.p.rapidapi.com/lender/reviews'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'screenName': screenName,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def other_professionals_reviews(zuid: Annotated[str, Field(description='')],
                                page: Annotated[Union[str, None], Field(description='')] = None,
                                size: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get reviews of a professional by their zuid (found in `/other_professionals/details` result)'''
    url = 'https://zillow56.p.rapidapi.com/other_professionals/reviews'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zuid': zuid,
        'page': page,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def other_professionals_details(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get details of a professional by username (found in `/other_professionals/search` results)'''
    url = 'https://zillow56.p.rapidapi.com/other_professionals/details'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def other_professionals_search(type: Annotated[Literal['property_managers', 'home_improvement', 'inspectors', 'photographers', 'other'], Field(description='')],
                               location: Annotated[Union[str, None], Field(description='')] = None,
                               name: Annotated[Union[str, None], Field(description='')] = None,
                               page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Search for professoinals (property managers, inspectors,photographers,home_improvement,etc) by location or name'''
    url = 'https://zillow56.p.rapidapi.com/other_professionals/search'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'location': location,
        'name': name,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def builders_search(location: Annotated[Union[str, None], Field(description='')] = None,
                    name: Annotated[Union[str, None], Field(description='')] = None,
                    page: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Searchfor builders by location or name'''
    url = 'https://zillow56.p.rapidapi.com/builders/search'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'name': name,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def builders_details(builderId: Annotated[str, Field(description='')]) -> dict: 
    '''Get details of builders by their builderId (found in `builders/search` results)'''
    url = 'https://zillow56.p.rapidapi.com/builders/details'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'builderId': builderId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def builders_community_cards(builderId: Annotated[str, Field(description='')],
                             regionId: Annotated[Union[str, None], Field(description='')] = None,
                             page: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get community cards of a builder by their builderId (found in `builders/search` results)'''
    url = 'https://zillow56.p.rapidapi.com/builders/community_cards'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'builderId': builderId,
        'regionId': regionId,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def builders_reviews(builderId: Annotated[str, Field(description='')],
                     regionId: Annotated[Union[str, None], Field(description='')] = None,
                     page: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get reviews of a builder by their builderId (found in `builders/search` results)'''
    url = 'https://zillow56.p.rapidapi.com/builders/reviews'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'builderId': builderId,
        'regionId': regionId,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def mortgage_rates(program: Annotated[Literal['Fixed30Year', 'Fixed20Year', 'Fixed15Year', 'Fixed10Year', 'ARM3', 'ARM5', 'ARM7', 'HomeEquity30Year', 'HomeEquity30YearDueIn15', 'HomeEquity15Year', 'HELOC20Year', 'HELOC15Year', 'HELOC10Year'], Field(description='The loan program. You can select one or two programs, separated by commas. Available: Fixed30Year, Fixed20Year, Fixed15Year, Fixed10Year, ARM3, ARM5, ARM7, HomeEquity30Year, HomeEquity30YearDueIn15, HomeEquity15Year, HELOC20Year, HELOC15Year, HELOC10Year')],
                   state: Annotated[Union[str, None], Field(description='The state abbreviation. AK,AL,AR,AS,AZ,CA,CO,CT,DC,DE,FL,GA, GU,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,MH, MI,MN,MO,MP,MS,MT,NC,ND,NE, NH,NJ,NM,NV,NY,OH,OK,OR,PA,PR,RI,SC,SD,TN,TX,UT,VA,VI,VT,WA,WI,WV,WY,US')] = None,
                   refinance: Annotated[Union[bool, None], Field(description='')] = None,
                   loanType: Annotated[Literal['Conventional', 'FHA', 'VA', 'USDA', 'Other', 'Jumbo', None], Field(description='')] = None,
                   loanAmount: Annotated[Literal['Conforming', 'SmallConforming', 'SuperConforming', 'Jumbo', 'Micro', None], Field(description='Micro < $100,000 SmallConforming $100,000 - $200,000 Conforming > $200,000 SuperConforming Jumbo')] = None,
                   loanToValue: Annotated[Literal['Normal', 'High', 'VeryHigh', None], Field(description='Normal < 80% High > 80% < 95% VeryHigh >= 95%')] = None,
                   creditScore: Annotated[Literal['Low', 'High', 'VeryHigh', None], Field(description='Low < 680 credit score. High > 680 < 740 VeryHigh > 740')] = None,
                   duration: Annotated[Union[int, float, None], Field(description='From 0 to 4000 Default: 30')] = None) -> dict: 
    '''Get mortgage rates'''
    url = 'https://zillow56.p.rapidapi.com/mortgage/rates'
    headers = {'x-rapidapi-host': 'zillow56.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'program': program,
        'state': state,
        'refinance': refinance,
        'loanType': loanType,
        'loanAmount': loanAmount,
        'loanToValue': loanToValue,
        'creditScore': creditScore,
        'duration': duration,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
