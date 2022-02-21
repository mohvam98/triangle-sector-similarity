# Triangle Area - Sector Area Similarity
It takes two vectors as an input and can return Cosine Similarity, Eucledian Distance, Triangle Area - Sector Area Similarity.

## Installation
``` pip install triangle_sector_similarity ```

## How to use it?
```
from triangle_sector_similarity import Cosine_Similarity,Euclidean_Distance,TS_SS,Pairwise_TS_SS

vec1 = [1,2,3]
vec2 = [2,4,5]

#Triangle Area Similarity – Sector Area Similarity
ts_ss = TS_SS(vec1,vec2)

#Cosine Similarity
cos_sim = Cosine_Similarity(vec1,vec2)

#Euclidean Distance
euc_dist = Euclidean_Distance(vec1,vec2)

#Pairwise Triangle Area Similarity – Sector Area Similarity
lst1 = [[1,2,3],[2,3,4]]
lst2 = [[2,4,5],[2,8,6]]

pairwise_ts_ss = Pairwise_TS_SS(lst1,lst2)
```

## License
© 2022 mohan98

This repository is licensed under the MIT license. See LICENSE for details.