from requests import Response

def handle_response(response:Response):
    try:
        response.raise_for_status()
        if response.status_code == 204:
            return {"detail": "Deleted successfully"}
        return response.json()
    except Exception as e:
        return {"error": response.content , "status_code": response.status_code}
