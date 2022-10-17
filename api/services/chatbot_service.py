from api.models import models


def processor_response(body: models.Body):
    return f"Your message is: {body.message}"
