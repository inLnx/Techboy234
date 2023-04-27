# Use the code below to add the session validation to your server application.
# More info: https://docs.descope.com/build/guides/session/#Python
jwt_response =
	descope_client.validate_session(session_token=session_token)
