# from api_client.user_client import UserClient
# from types import SimpleNamespace

# def test_create_user():
#     # Create an instance of UserClient
#     client = UserClient()

#     # Example user data to create a new user
#     new_user_data = {
#         "username":1234567819,
#         'phone': None,
#         'is_active': True,
#         'language': 'en',
#         'is_special': False
#     }

#     # Create user using the client
#     response = client.create(new_user_data)

#     # Print the response to verify the created user
#     print("Response:", response)
#     if response["status_code"].startswith("2"):
#         # Optional: Perform some assertions based on expected response
#         assert response.get("phone") == new_user_data['phone'], f"Expected {new_user_data['phone']}, got {response.get('phone')}"
#         assert response.get("language") == new_user_data['language'], f"Expected {new_user_data['language']}, got {response.get('language')}"
#         assert response.get("is_active") == new_user_data['is_active'], f"Expected {new_user_data['is_active']}, got {response.get('is_active')}"
#     else:
#         pass
    
# def test_filter():
#     client = UserClient()
#     user = SimpleNamespace(**client.filter(username="1234567819"))
#     if user:
#         user = user[0]
#     print(user.phone)
# # Run the test
# test_create_user()
# test_filter()

# from languages_de import de
# from languages_en import en

# print(en.keys()==de.keys())