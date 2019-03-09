% Test function to run the plot_k_NN_RunTimes

% Run times
postgres_v1 = [0.329075 0.307771 0.306216 0.297853 0.297395 0.300822 0.294294 0.316212 0.294033 0.297463 0.300204 0.341735 0.320901 0.302445 0.297262 0.30187 0.297381 0.299262 0.303307 0.299213 0.297744 0.300275 0.299276 0.318241 0.301804 0.296808 0.298237 0.316693 0.299818 0.300706 
0.313239 0.342036 0.305677 0.299845 0.297277 0.298306 0.294244 0.2979 0.300727 0.301428 0.314855 0.296816 0.29824 0.349124 0.296792 0.300302 0.334722 0.303695 0.299795 0.320352 0.299108 0.29923 0.298755 0.333374 0.301179 0.295341 0.296353 0.302026 0.300331 0.297746 
0.298153 0.299269 0.302821 0.298797 0.299023 0.30026 0.311264 0.296399 0.300731 0.296528 0.296341 0.299285 0.296851 0.296279 0.297237 0.299651 0.296374 0.314357 0.319312 0.300807 0.299744 0.297271 0.300331 0.294891 0.302806 0.293924 0.301376 0.303314 0.297213 0.300793 
0.314233 0.30027 0.29907 0.301229 0.298267 0.296182 0.301802 0.309746 0.300346 0.295636 0.314468 0.295558 0.300963 0.299506 0.305202 0.297756 0.300327 0.298775 0.29725 0.301244 0.313234 0.301864 0.295712 0.297629 0.302181 0.302624 0.300831 0.299143 0.297257 0.295481 
0.300949 0.298268 0.318936 0.299788 0.300296 0.302241 0.323558 0.300149 0.307287 0.316157 0.313626 0.296803 0.313701 0.298796 0.299225 0.298839 0.302252 0.307216 0.298361 0.302273 0.299689 0.297513 0.29728 0.320765 0.304583 0.319931 0.355855 0.340532 0.307267 0.299836 
0.298802 0.29838 0.298245 0.299321 0.299815 0.299742 0.326278 0.299895 0.294857 0.300844 0.30095 0.298175 0.298456 0.300398 0.299719 0.31526 0.298188 0.300679 0.297931 0.299802 0.298841 0.301714 0.29996 0.298933 0.300267 0.296692 0.298278 0.304198 0.29791 0.297423  
];

postgres_v2= [0.045589 0.060839 0.066826 0.027954 0.061801 0.071812 0.030615 0.029925 0.030854 0.059872 0.032914 0.05986 0.067932 0.029512 0.027898 0.059923 0.060702 0.030917 0.061028 0.029922 0.027925 0.027967 0.02799 0.028925 0.026992 0.027934 0.071803 0.071144 0.026959 0.028953 
0.060926 0.030006 0.02992 0.026528 0.030924 0.028439 0.071419 0.029043 0.061831 0.029183 0.026928 0.07184 0.029924 0.027893 0.026954 0.060547 0.029922 0.071389 0.03092 0.030921 0.027928 0.061597 0.026932 0.06053 0.027682 0.027926 0.061679 0.027925 0.070871 0.026928 
0.028737 0.027958 0.030917 0.026983 0.030013 0.027926 0.026961 0.027439 0.027925 0.028909 0.026955 0.02802 0.061226 0.027895 0.027926 0.027924 0.027954 0.028956 0.034907 0.030948 0.027686 0.027802 0.026926 0.026984 0.059816 0.027896 0.02995 0.026959 0.027925 0.026987 
0.026993 0.027956 0.027918 0.027924 0.026969 0.026958 0.060947 0.028978 0.070847 0.026959 0.030009 0.059841 0.059689 0.028953 0.028922 0.060902 0.028928 0.062834 0.027956 0.026973 0.026958 0.028959 0.028617 0.026991 0.060582 0.026902 0.028418 0.027955 0.028922 0.027747 
0.029008 0.032881 0.026991 0.027022 0.028917 0.027902 0.034907 0.028924 0.027925 0.028928 0.030918 0.062879 0.02796 0.028923 0.027925 0.028922 0.059934 0.02992 0.027953 0.028586 0.027951 0.026987 0.02898 0.028986 0.06257 0.029991 0.036358 0.032912 0.027555 0.02696 
0.032386 0.026928 0.061563 0.027556 0.027989 0.026925 0.030406 0.058847 0.073894 0.030006 0.060705 0.029736 0.029988 0.028433 0.028924 0.028924 0.060933 0.030549 0.028976 0.061866 0.030002 0.02995 0.028492 0.027924 0.061718 0.060813 0.030242 0.072089 0.06457 0.072121 
];



mongo=[0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.000998 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.000998 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.000998 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.000997 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.000997 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
];

postgres_v1_big=[
    174.981827 216.716977 214.870589 210.539657 203.633903 188.526452 187.945576 184.845347 188.420946 186.822386 186.120567 190.996061 184.466397 182.673859 181.277893 182.94352 184.68022 185.229543 191.230901 186.744523 186.885022 185.505032 181.356147 182.487821 182.548255 185.72053 184.885055 183.365615 186.17804 193.815981 
187.788606 185.655095 185.811814 187.670898 189.274806 188.58844 205.450538 192.793159 201.13128 198.979591 199.061045 196.397088 199.745898 196.576714 195.463425 198.473999 198.367323 199.697631 207.067033 202.691157 204.694337 200.227429 202.522055 200.092303 203.220971 199.046469 201.54068 203.895964 199.984677 200.617101 
201.546955 203.638691 201.101374 208.171649 204.179529 204.934636 207.195446 205.879517 204.160593 206.0369 211.234321 210.306882 212.474391 211.758127 213.571891 211.203042 203.235221 204.944637 204.363965 203.370577 211.929398 208.909551 204.413297 209.656689 208.007192 205.194588 215.741974 206.193894 205.184707 205.041611 
210.629651 207.354779 210.182326 205.430742 205.336573 207.776888 207.186165 203.176759 201.973412 201.845466 201.571549 202.049439 198.459279 196.051666 200.165036 198.112403 198.262582 207.953471 197.858892 200.416957 198.935221 196.580322 194.604211 196.273666 197.377811 199.473957 192.625504 196.274829 196.24947 197.395565 
191.563362 195.182519 199.924663 199.565545 196.795248 192.994986 193.954473 192.707609 195.179111 197.510078 191.038567 197.103082 189.868237 188.79419 194.325301 191.7734 192.760445 191.739838 192.238778 199.81483 192.090007 192.389307 192.45279 187.633494 192.243237 187.185492 185.200189 185.49586 185.269907 190.328382 
782.059134 688.375116 693.265838 689.562359 698.854859 705.943744 731.657202 724.881438 715.850523 730.825482 746.966718 741.746382 731.91398 752.982206 729.300651 739.116586 741.200431 738.624279 752.030503 764.082983 771.812702 811.553498 777.593131 745.36325 661.220479 661.671657 653.765838 627.267134 601.396742 596.666859
];

postgres_v2_big=[
    0.049839 0.024933 0.027594 0.023937 0.013943 0.01895 0.007011 0.025919 0.019946 0.020944 0.023905 0.02191 0.018949 0.007976 0.013936 0.017534 0.01794 0.007982 0.013557 0.019947 0.011941 0.008976 0.020945 0.010975 0.014474 0.016464 0.020943 0.007948 0.008976 0.008977 
0.015958 0.007005 0.012939 0.015012 0.011968 0.006001 0.010477 0.008976 0.005996 0.007984 0.012918 0.007979 0.009944 0.027903 0.009976 0.009973 0.01097 0.134742 0.009972 0.011968 0.018949 0.008976 0.142107 0.011005 0.010002 0.009974 0.008976 0.012966 0.00399 0.008963 
0.06383 0.04847 0.086126 0.076023 0.073566 0.081041 0.076987 0.059564 0.05594 0.22417 0.06344 0.065693 0.04887 0.227327 0.049224 0.056308 0.203405 0.057387 0.058542 0.053937 0.058236 0.064518 0.056361 0.052408 0.05059 0.055442 0.063438 0.058092 0.04159 0.386563 
0.492191 0.426078 0.408022 0.384664 0.469078 0.390912 0.477166 0.346383 0.374071 0.374124 0.447377 0.373727 0.421729 0.372238 0.336656 0.381086 0.452982 0.537186 0.394839 0.383071 0.509897 0.448379 0.460735 0.387337 0.397357 0.490583 0.39375 0.401059 0.476171 0.418978 
3.960151 3.364224 3.673405 3.54686 3.987394 4.026375 3.767406 3.262752 3.859302 3.546979 3.767913 3.727016 3.796676 3.191209 3.750743 3.779404 3.652433 3.596896 3.867423 3.695114 4.308598 3.901015 3.40619 4.480865 4.29678 4.045602 3.893524 4.409099 3.645384 3.733058 
44.951778 42.536802 44.233451 45.161503 44.798132 42.527847 45.200078 41.966772 44.622019 43.830363 45.977104 43.40413 47.365556 46.478043 46.460148 45.896826 46.102134 46.137454 46.39147 45.238086 46.81355 46.622621 44.997025 45.198388 47.094058 46.448108 55.233288 50.91344 48.092273 44.419501
];

mongo_big=[
  0.0 0.0 0.000998 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.001024 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0  
];


kValues = {'1', '5', '10', '20', '50', '100'};
kValues_big = {'1', '10', '100', '1K', '10K', '100K'};

for k=1:size(kValues, 2)
    avg_P1(k) = mean(postgres_v1_big(k,:));
    avg_P2(k) = mean(postgres_v2_big(k,:));
    avg_M(k) = mean(mongo_big(k,:));
end


avgRunTimes = [avg_P1; avg_P2; avg_M];


plot_k_NN_RunTimes(avgRunTimes, kValues_big);

