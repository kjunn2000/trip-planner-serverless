import boto3

def get_trip_by_id(user_id, trip_id):
  dynamodb = boto3.resource('dynamodb', endpoint_url="http://127.0.0.1:4566")
  table = dynamodb.Table('Trips')

  response = table.get_item(
      Key={
          'UserId': user_id,
          'TripId': trip_id
      }
  )

  item = response.get('Item', None)
  return item

user_id_to_query = "User2"
trip_id_to_query = "XYZ789"

trip_details = get_trip_by_id(user_id_to_query, trip_id_to_query)

if trip_details:
  print("Found trip details:")
  print(trip_details)
else:
  print("No trip found for user", user_id_to_query, "with trip ID", trip_id_to_query)