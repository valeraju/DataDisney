mapping = '''
{
  "mappings": {
    "rawdata": {
      "properties": {
        "file_name": {
          "fields": {
            "keyword": {
              "ignore_above": 256,
              "type": "keyword"
            }
          },
          "type": "keyword"
        },
        "filesize": {
          "type": "float"
        },
        "has_schedule_attractions": {
          "type": "boolean"
        },
        "lastUpdates_attractions": {
          "format": "epoch_millis",
          "type": "date"
        },
        "lines_numer": {
          "type": "integer"
        },
        "park_name": {
          "fields": {
            "keyword": {
              "ignore_above": 256,
              "type": "keyword"
            }
          },
          "type": "keyword"
        },
        "rides_number": {
          "type": "integer"
        },
        "timestamp": {
          "format": "epoch_second",
          "type": "date"
        },
        "url": {
          "fields": {
            "keyword": {
              "ignore_above": 256,
              "type": "keyword"
            }
          },
          "type": "text"
        }
      }
    }
  },
  "settings": {
    "index": {
      "number_of_replicas": 1,
      "number_of_shards": 5
    }
  }
}
'''