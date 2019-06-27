#this file is server file
from config import NOJIMA_MAZE,GAIA_MAZE,SUNAGA_MAZE
from config import X,Y
from config import RIGHT,LEFT,UP,DOWN,ATTACK

##############################################################################################################

#命名規則について by sunaga

# file名　　　　　　　　全て小文字でなるべく短く　       myfile
# クラス名　　　　　　　最初大文字、大文字区切り　　　   ThisIsMyClass
# 関数名、メッソド名　　全小文字、アンダースコア区切り   this_is_my_func
# 変数名　　　　　　　　全小文字、アンダースコア区切り   this_is_my_val
# 定数名                全大文字、アンダースコア区切り　 THIS_IS_MY_CONST

# 自クラス内でのみ使用する内部変数と内部メソッドはアンダースコアで開始


##############################################################################################################


#test
print(RIGHT)

#座標変換はこんな感じにすればミスが減ると思う 右へ移動の場合 by sunaga
posi = [3,6]
print("現在の座標",posi)

posi[X] += RIGHT[X]
posi[Y] += RIGHT[Y]
print("右へ移動後の座標",posi)




##############################################################################################################
