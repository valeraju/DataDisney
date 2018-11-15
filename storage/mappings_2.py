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
        "rides": {
          "properties": {
            "P1AA00": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1AA01": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1AA02": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1AA03": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1AA04": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1AA05": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1AA08": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1DA03": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1DA04": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1DA06": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1DA07": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1DA08": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1DA09": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1DA10": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1DA14": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1MA01": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1MA04": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1MA05": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1MA06": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA00": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA01": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA02": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA03": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA05": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA06": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA07": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA08": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA09": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA10": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA12": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA13": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA16": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1NA17": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1RA00": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1RA03": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1RA05": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1RA06": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1RA07": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P1RA10": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA00": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA01": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA02": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA03": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA05": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA06": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA07": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA08": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2XA09": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2YA01": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2ZA00": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2ZA01": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            },
            "P2ZA02": {
              "properties": {
                "hasSchedule": {
                  "type": "boolean"
                },
                "lastUpdate": {
                  "format": "epoch_millis",
                  "type": "date"
                }
              }
            }
          }
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