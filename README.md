# サーバーサイドのA
## 実行方法
    プロジェクトディレクトリで  
    $docker build -t back_a_image .  
    $docker container run -d -p 8000:8000 back_b_image  
    http://127.0.0.1:8000/items/にアクセスするとapiを送ることができる  