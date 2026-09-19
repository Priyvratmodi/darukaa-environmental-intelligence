import requests
import json

session_id = 'test-check-1'

print('=== TURN 1 ===')
r1 = requests.post('http://localhost:8000/analyze', json={
    'session_id': session_id,
    'query': 'Biodiversity is declining on my land'
})
data1 = r1.json()
print('Turn 1 Status:', data1.get('status'))
if data1.get('status') == 'requires_more_info':
    print('Missing metrics:', [m['metric_name'] for m in data1.get('missing_metrics', [])])
else:
    print(json.dumps(data1, indent=2))

print('\n=== TURN 2 ===')
r2 = requests.post('http://localhost:8000/analyze', json={
    'session_id': session_id,
    'query': 'Here is the missing metric data: species richness is 18. Species abundance includes house sparrow (24 per ha), common myna (12 per ha), and red vented bulbul (8 per ha). Habitat diversity Shannon index is 1.42 across urban vegetation, agricultural land, open grassland, and small water body.'
})
data2 = r2.json()
print('Turn 2 Status:', data2.get('status'))
if data2.get('status') == 'complete':
    print('\n--- EVIDENCE CHAIN ---')
    print(json.dumps(data2.get('evidence_chain'), indent=2))
    print('\n--- RECOMMENDATIONS ---')
    print(json.dumps(data2.get('recommendations'), indent=2))
else:
    print(json.dumps(data2, indent=2))
