#!/usr/bin/env python

import uuid

from human_id import generate_id

# Simple: "appear-hard-idea-case"
print(f'{generate_id()=}')

# Custom separator: "do,past,job,number"
print(f'{generate_id(separator=",")=}')

# More words: "say-may-ask-traditional-power-week"
print(f'{generate_id(word_count=10)=}')

# Custom seed - the same UUID will produce the same ID.
print(f'{generate_id(seed=uuid.uuid4().int)=}')
