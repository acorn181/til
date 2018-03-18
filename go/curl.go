package main

import (
    "fmt"
    "net/http"
    "net/url"
    "io/ioutil"
    "./config"
)

func main() {
    appid, _ := config.readConfig()
    // サンプルとしてYOLPの郵便番号検索APIを叩く
    values := url.Values{}
    //values.Add("appid", "dj00aiZpPUZwZFRGZVhSTWdsdyZzPWNvbnN1bWVyc2VjcmV0Jng9NjU-")
    values.Add("appid", string(appid))
    values.Add("query", "332-0005")
    values.Add("output", "json")
    // URL設定
    url := "https://map.yahooapis.jp/search/zip/V1/zipCodeSearch"

    // http.Getでリクエストを作る
    req, err := http.NewRequest("GET",url,nil)

    if err != nil {
        fmt.Println(err)
        return
    }
    req.URL.RawQuery = values.Encode()

    execute(req)
}

/**
 * httpリクエストを実行する
 *
 * @param response *http.Response レスポンスの中身
 */
func execute(request *http.Request) {
    client := new(http.Client)
    resp, _ := client.Do(request)
    defer resp.Body.Close()

    // httpレスポンスを解析
    // 正常レスポンス：body
    // エラーレスポンス：err
    body, err := ioutil.ReadAll(resp.Body)

    // エラーハンドリングを実施
    if err != nil {
        fmt.Println(err)
        return
    }

    fmt.Println(string(body))
}
