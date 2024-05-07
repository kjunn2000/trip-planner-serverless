import boto3
import json

new_trip = {
  "TripId": "XYZ789",
  "UserId": "User2",
  "Name": "California Adventure",
  "Destination": "Yosemite National Park",
  "StartDate": "2024-05-10",
  "EndDate": "2024-05-14",
  "Activities": [
    {
      "ActivityName": "Hiking to Half Dome",
      "Location": "Half Dome Trail",
      "Date": "2024-05-11",
      "Time": "8:00 AM",
      "Notes": "Requires permit. Breathtaking views from the summit!"
    },
    {
      "ActivityName": "Yosemite Falls Hike",
      "Location": "Lower Yosemite Fall Trail",
      "Date": "2024-05-12",
      "Time": "10:00 AM",
      "Notes": "Easy trail with beautiful waterfall views."
    }
  ],
  "Accommodations": [
    {
      "HotelName": "Yosemite Valley Lodge",
      "Address": "9001 Village Drive, Yosemite Valley, CA 95389",
      "ConfirmationNumber": "GHI456",
      "CheckInDate": "2024-05-10",
      "CheckOutDate": "2024-05-14",
      "Notes": "Scenic location in the heart of Yosemite Valley."
    }
  ],
  "Transportation": [
    {
      "Type": "Flight",
      "Itinerary": "AA123 Los Angeles (LAX) to Fresno (FAT)",
      "DepartureDate": "2024-05-10",
      "DepartureTime": "9:00 AM",
      "ArrivalDate": "2024-05-10",
      "ArrivalTime": "10:00 AM",
      "ConfirmationNumber": "JKL789",
      "Notes": "Rental car pick-up at Fresno Airport."
    }
  ],
  "Notes": "A weekend getaway to enjoy the beauty of Yosemite National Park. We plan to go hiking, explore waterfalls, and relax in the stunning scenery."
}

def add_trip(trip_data):
  dynamodb = boto3.resource('dynamodb', endpoint_url="http://127.0.0.1:4566")
  table = dynamodb.Table('Trips')

  trip_data['Activities'] = json.dumps(trip_data['Activities'])
  trip_data['Accommodations'] = json.dumps(trip_data['Accommodations'])
  trip_data['Transportation'] = json.dumps(trip_data['Transportation'])

  response = table.put_item(Item=trip_data)
  return response

add_trip_response = add_trip(new_trip)
print(add_trip_response)