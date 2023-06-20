import logging
import re
from enum import Enum
from time import time

import emoji
from fastapi import HTTPException
from setfit import SetFitModel

logger = logging.getLogger(__name__)


def clean_text(text):
    replacements = [
        (r'[\.]+', '.'),
        (r'[\!]+', '!'),
        (r'[\?]+', '!'),
        (r'\s+', ' '),
        (r'@\w+', ''),
        (r'\s[n]+[o]+', ' no'),
        (r'n\'t', 'n not'),
        (r'\'nt', 'n not'),
        (r'\'re', ' are'),
        (r'\'s', ' is'),
        (r'\'d', ' would'),
        (r'\'ll', ' will'),
        (r'\'ve', ' have'),
        (r'\'m', ' am'),
        (r'\s[n]+[o]+[p]+[e]+', ' no'),
        (r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%|\~)*\b', ''),
        (r'(www.)(\w|\.|\/|\?|\=|\&|\%)*\b', ''),
        (r'\w+.com', '')
    ]

    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.MULTILINE).strip()
        logger.info(text)

    text = emoji.demojize(text)
    return text


class Sentiment(Enum):
    POSITIVE = 1
    NEGATIVE = 0
    NEUTRAL = 2


def make_response(value):
    match value:
        case Sentiment.POSITIVE.value:
            return {"sentiment": 'positive', "value": 1}
        case Sentiment.NEGATIVE.value:
            return {"sentiment": 'negative', "value": -1}
        case Sentiment.NEUTRAL.value:
            return {"sentiment": 'neutral', "value": 0}
        case _:
            raise HTTPException(status_code=400, detail="unexpected value")


class SentimentClassifier:
    logger.info('Loading SetFit sentiment classifier ...')
    start = time()
    model: SetFitModel = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval",
                                                     multi_target_strategy="multi-output",
                                                     use_differentiable_head=True)
    logger.info(f'Time taken to load SetFit sentiment classifier = {time() - start}')

    def predict(self, text):
        start = time()
        output = self.model([text])
        logger.info(f'Inference time = {time() - start}')
        return make_response(output.item())
