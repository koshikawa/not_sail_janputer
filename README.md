# 切り上げしない麻雀点数計算

麻雀の点数計算は符を10点単位で切り上げてかつ点数を100点単位で切り上げるため、
イチサンニーロクゴンニやザンクチッチとの数字を暗記する必要があり悩ましい。
符計算をそのままに点数にすれば切り上げ不要で数学的にも美しい。

```
$ ./not_sail_janputer.py
20	    0	 1280	 2560	 5120	 8000	12000	12000	16000	16000	16000	24000	24000	32000
22	  704	 1408	 2816	 5632	 8000	12000	12000	16000	16000	16000	24000	24000	32000
24	  768	 1536	 3072	 6144	 8000	12000	12000	16000	16000	16000	24000	24000	32000
26	  832	 1664	 3328	 6656	 8000	12000	12000	16000	16000	16000	24000	24000	32000
28	  896	 1792	 3584	 7168	 8000	12000	12000	16000	16000	16000	24000	24000	32000
30	  960	 1920	 3840	 7680	 8000	12000	12000	16000	16000	16000	24000	24000	32000
32	 1024	 2048	 4096	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
34	 1088	 2176	 4352	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
36	 1152	 2304	 4608	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
38	 1216	 2432	 4864	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
40	 1280	 2560	 5120	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
42	 1344	 2688	 5376	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
44	 1408	 2816	 5632	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
46	 1472	 2944	 5888	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
48	 1536	 3072	 6144	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
50	 1600	 3200	 6400	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
52	 1664	 3328	 6656	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
54	 1728	 3456	 6912	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
56	 1792	 3584	 7168	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
58	 1856	 3712	 7424	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
60	 1920	 3840	 7680	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
62	 1984	 3968	 7936	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
64	 2048	 4096	 8000	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
66	 2112	 4224	 8000	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
68	 2176	 4352	 8000	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
70	 2240	 4480	 8000	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
72	 2304	 4608	 8000	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
74	 2368	 4736	 8000	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
76	 2432	 4864	 8000	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
78	 2496	 4992	 8000	 8000	 8000	12000	12000	16000	16000	16000	24000	24000	32000
25	    0	 1600	 3200	 6400	 8000	12000	12000	16000	16000	16000	24000	24000	32000

20	    0	 1920	 3840	 7680	12000	18000	18000	24000	24000	24000	36000	36000	48000
22	 1056	 2112	 4224	 8448	12000	18000	18000	24000	24000	24000	36000	36000	48000
24	 1152	 2304	 4608	 9216	12000	18000	18000	24000	24000	24000	36000	36000	48000
26	 1248	 2496	 4992	 9984	12000	18000	18000	24000	24000	24000	36000	36000	48000
28	 1344	 2688	 5376	10752	12000	18000	18000	24000	24000	24000	36000	36000	48000
30	 1440	 2880	 5760	11520	12000	18000	18000	24000	24000	24000	36000	36000	48000
32	 1536	 3072	 6144	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
34	 1632	 3264	 6528	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
36	 1728	 3456	 6912	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
38	 1824	 3648	 7296	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
40	 1920	 3840	 7680	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
42	 2016	 4032	 8064	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
44	 2112	 4224	 8448	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
46	 2208	 4416	 8832	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
48	 2304	 4608	 9216	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
50	 2400	 4800	 9600	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
52	 2496	 4992	 9984	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
54	 2592	 5184	10368	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
56	 2688	 5376	10752	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
58	 2784	 5568	11136	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
60	 2880	 5760	11520	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
62	 2976	 5952	11904	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
64	 3072	 6144	12000	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
66	 3168	 6336	12000	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
68	 3264	 6528	12000	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
70	 3360	 6720	12000	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
72	 3456	 6912	12000	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
74	 3552	 7104	12000	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
76	 3648	 7296	12000	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
78	 3744	 7488	12000	12000	12000	18000	18000	24000	24000	24000	36000	36000	48000
25	    0	 2400	 4800	 9600	12000	18000	18000	24000	24000	24000	36000	36000	48000
```
