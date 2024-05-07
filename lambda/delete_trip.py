import boto3

def delete_trip_by_id(user_id, trip_id):
  dynamodb = boto3.resource('dynamodb', endpoint_url="http://127.0.0.1:4566")
  table = dynamodb.Table('Trips')

  response = table.delete_item(
      Key={
          'UserId': user_id,
          'TripId': trip_id
      }
  )

  return response

user_id_to_query = "User2"
trip_id_to_query = "XYZ789"

trip_details = delete_trip_by_id(user_id_to_query, trip_id_to_query)

if trip_details:
  print("Deleted trip details:")
  print(trip_details)
else:
  print("No trip found for user", user_id_to_query, "with trip ID", trip_id_to_query)