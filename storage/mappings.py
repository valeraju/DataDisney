mapping = '''
{
  "logs": {
    "mappings": {
      "rawdata": {
        "properties": {
          "file_name": {
            "type": "keyword",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "filesize": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "last_updates": {
            "properties": {
              "DisneylandParisMagicKingdom_P1AA00": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1AA01": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1AA02": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1AA03": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1AA04": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1AA05": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1AA08": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1DA03": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1DA04": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1DA06": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1DA07": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1DA08": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1DA09": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1DA10": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1DA14": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1MA01": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1MA04": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1MA05": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1MA06": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA00": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA01": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA02": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA03": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA05": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA06": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA07": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA08": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA09": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA10": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA12": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA13": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA16": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1NA17": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1RA00": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1RA03": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1RA05": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1RA06": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1RA07": {
                "type": "date"
              },
              "DisneylandParisMagicKingdom_P1RA10": {
                "type": "date"
              }
            }
          },
          "lines_numer": {
            "type": "long"
          },
          "parkname": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "ridesnumber": {
            "type": "long"
          },
          "timestamp": {
            "type": "date"
          },
          "url": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          }
        }
      }
    }
  }
}
'''