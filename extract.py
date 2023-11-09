import csv
import json

def parseCsvToArray(filename):
  reader = csv.reader(
      open(filename, 'r', encoding='utf-8'))
  data = []
  headers = next(reader)
  nextLine = next(reader)
  while nextLine != None:
    obj = {}
    for i in range(len(headers)):
      obj[headers[i]] = nextLine[i]
    data.append(obj)
    try:
      nextLine = next(reader)
    except StopIteration:
      break
    except Exception:
      continue

  return data

videos = parseCsvToArray('US_youtube_trending_data.csv')

years = []
for i in range(len(videos)):
  year = videos[i]['publishedAt']
  sub = year[0:4]
  if sub not in years:
    years.append(sub)

channels = parseCsvToArray('most_subscribed_youtube_channels.csv')

filteredVideos = []
for i in range(len(channels)):
  channelVideos = list(filter(lambda c: c['channelTitle'] == channels[i]['Youtuber'], videos))
  filteredVideos = filteredVideos + channelVideos

with open('out.json', 'w') as f:
  json.dump(filteredVideos, f)

print('success')
