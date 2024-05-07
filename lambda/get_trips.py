import boto3

def get_all_trips_by_user_id(user_id):
  dynamodb = boto3.resource('dynamodb', endpoint_url="http://127.0.0.1:4566")
  table = dynamodb.Table('Trips')

  response = table.query(
      IndexName='user-trips-index',
      KeyConditionExpression='UserId = :val',
      ExpressionAttributeValues={':val': user_id}
  )

  trips = response.get('Items', [])
  return trips

user_id_to_query = "User2"
all_trips = get_all_trips_by_user_id(user_id_to_query)

if all_trips:
  print("Found trips for", user_id_to_query)
  for trip in all_trips:
    print(trip)
else:
  print("No trips found for user ID", user_id_to_query)