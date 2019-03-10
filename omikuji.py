#ランダムにおみくじの結果を返すアプリを作ってね
#あからさまなヒント:randomモジュールが使えそう

import random

omikuji = ["大吉", "吉", "凶"]

#print(omikuji[random.randint(0, 2)])

idx = random.randint(0, 2)
#idxはインデックスの略

print(omikuji[idx])


