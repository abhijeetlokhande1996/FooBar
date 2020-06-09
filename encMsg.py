# You probably have python 3

import base64

MESSAGE = '''
GkUbHAkGAAcfSEtSQUkDF1RYTRFNQk8KBQkJEQ0IHg1GTl5FFlxKQgQHBQwOQklUSwoNDg4cEBYW GQMWRgsGChgAAR0OAw5PTU5DBFJRUFMXBwUMBBFCVFZPTB0PAgsGWlxdEU1CTxsLBwcdGBxMSFtO QxZQX1wRTUJPDwUKQlRWT0wfCABFQkw=
'''

KEY = 'abhijeetlokhande1996'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
