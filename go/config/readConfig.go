package config

import (
    "encoding/json"
    "io/ioutil"
    "fmt"
)

type AppConfig struct {
    appid string `json:"appid"`
}

func readConfig() {
    file, err := ioutil.ReadFile("config.json")
    if err != nil {
        return
    }

    var config AppConfig
    json.Unmarshal(file, &config)
    fmt.Println(config.appid)
    return config.appid
}
