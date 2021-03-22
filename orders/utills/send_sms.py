import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class AfricasTalkingException(Exception):
    pass


def send_sms(recipients_list, message):
    """
    Keyword arguments:
    argument -- recipients_list : Passed a list of 07XXX
    Return: None
    """
    headers = {
        "apiKey": settings.AFRICAS_TALKING_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    body_content = {
        "username":settings.AFRICAS_TALKING_USERNAME,
        "to": ",".join(recipients_list),
        "message": message,
    }
    try:
        sms_send_request = requests.post(
            settings.AFRICAS_TALKING_URL_ENDPOINT, data=body_content, headers=headers
        )
        logger.info(sms_send_request.text)
    except AfricasTalkingException as e:
        logger.debug(e)
